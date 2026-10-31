"""Fixed-choice aggregate feedback collector: OFF until explicit privacy+storage gates."""
import os
import time
from collections import defaultdict, deque
from threading import Lock
from flask import Flask, request, jsonify

FIELDS={
 "relationship":["researching","current_parent","former_parent","other","prefer_not"],
 "prior":["quote","fee_schedule","calculator","invoice","other","none"],
 "topic":["total_extras","funding","comparisons","quote_check","unknowns"],
 "preference":["evidence","questions","compare","funding_rules"],
 "tried":["yes","no"],
 "clarity":["very_clear","clear","neutral","unclear","very_unclear","not_tried"],
 "usefulness":["very_useful","useful","unsure","not_very","not_useful"],
 "comparison":["better","alongside","same","worse","no_method"],
 "future_use":["yes","maybe","no"]
}
ORIGIN=os.getenv("CCEV_ALLOWED_ORIGIN","https://nursery-fee-clarity-research.onrender.com").rstrip("/")
app=Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=4096
_lock=Lock()
_attempts=defaultdict(deque)

def configured():
    return (os.getenv("CCEV_PUBLIC_COLLECTION_ENABLED")=="1"
            and os.getenv("CCEV_PRIVACY_READY")=="1"
            and os.getenv("CCEV_AGGREGATE_STORAGE_APPROVED")=="1"
            and bool(os.getenv("CCEV_CONTROLLER_CONTACT","").strip())
            and bool(os.getenv("CCEV_NOTICE_VERSION","").strip())
            and os.getenv("CCEV_METRICS_DATABASE_URL","").startswith(("postgres://","postgresql://"))
            and ORIGIN.startswith("https://"))

def valid_answers(data):
    return (type(data) is dict and set(data)==set(FIELDS) and
            all(type(data[k]) is str and data[k] in FIELDS[k] for k in FIELDS))

def limited(peer,now=None):
    now=time.monotonic() if now is None else now
    with _lock:
        q=_attempts[peer]
        while q and q[0]<=now-3600:q.popleft()
        if len(q)>=6:return True
        q.append(now)
        if len(_attempts)>10000:_attempts.clear()
        return False

@app.after_request
def response_headers(resp):
    resp.headers["Cache-Control"]="no-store"
    resp.headers["X-Content-Type-Options"]="nosniff"
    resp.headers["Referrer-Policy"]="no-referrer"
    resp.headers["Vary"]="Origin"
    if request.headers.get("Origin")==ORIGIN:
        resp.headers["Access-Control-Allow-Origin"]=ORIGIN
    return resp

@app.get("/healthz")
def health():
    return jsonify(status="ok",collecting=configured())

@app.route("/v1/feedback",methods=["POST","OPTIONS"])
def feedback():
    if request.headers.get("Origin")!=ORIGIN:
        return jsonify(error="origin_not_allowed"),403
    if request.method=="OPTIONS":
        r=app.make_default_options_response()
        r.headers["Access-Control-Allow-Methods"]="POST, OPTIONS"
        r.headers["Access-Control-Allow-Headers"]="Content-Type"
        return r
    if not configured():return jsonify(error="not_enabled"),503
    if request.content_length is None or request.content_length>4096 or not request.is_json:
        return jsonify(error="invalid_request"),400
    data=request.get_json(silent=True)
    if not valid_answers(data):return jsonify(error="invalid_answers"),400
    if (data["tried"]=="no")!=(data["clarity"]=="not_tried"):
        return jsonify(error="inconsistent_answers"),400
    if limited(request.remote_addr or "unknown"):return jsonify(error="rate_limited"),429
    try:
        import psycopg
        with psycopg.connect(os.environ["CCEV_METRICS_DATABASE_URL"],connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute("CREATE TABLE IF NOT EXISTS ccev_feedback_counts (question TEXT NOT NULL, answer TEXT NOT NULL, n BIGINT NOT NULL DEFAULT 0, PRIMARY KEY(question,answer))")
                cur.execute("CREATE TABLE IF NOT EXISTS ccev_feedback_total (key INTEGER PRIMARY KEY CHECK(key=1), n BIGINT NOT NULL DEFAULT 0)")
                for key,value in data.items():
                    cur.execute("INSERT INTO ccev_feedback_counts(question,answer,n) VALUES (%s,%s,1) ON CONFLICT(question,answer) DO UPDATE SET n=ccev_feedback_counts.n+1",(key,value))
                cur.execute("INSERT INTO ccev_feedback_total(key,n) VALUES(1,1) ON CONFLICT(key) DO UPDATE SET n=ccev_feedback_total.n+1")
        return jsonify(status="recorded"),201
    except Exception:
        app.logger.error("Aggregate write failed; payload not logged")
        return jsonify(error="storage_unavailable"),503
