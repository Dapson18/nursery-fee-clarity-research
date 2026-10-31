# Separate fixed-choice feedback collector — NOT DEPLOYED

This Flask API accepts nine multiple-choice answers and stores only counts for each choice plus an overall submission count. No individual rows, names, documents, free text, emails, IP addresses or profile identifiers are stored in PostgreSQL. Hosting/network logs may still process technical IP information, and the in-memory per-IP rate limit temporarily processes IP addresses.

## Activation gates
1. Obtain a dedicated durable PostgreSQL database for this project; never use another project's database, a Render ephemeral SQLite file, or time-limited free Render PostgreSQL for long-term study evidence.
2. Publish a proper privacy notice with identified controller/contact, purposes and lawful basis, processor details, retention plan, data-subject rights and log handling, before real public collection. Confirm whether ICO registration/fee is applicable.
3. Configure environment variables: CCEV_PUBLIC_COLLECTION_ENABLED=1, CCEV_PRIVACY_READY=1, CCEV_AGGREGATE_STORAGE_APPROVED=1, CCEV_CONTROLLER_CONTACT, CCEV_NOTICE_VERSION and secret CCEV_METRICS_DATABASE_URL; use CCEV_ALLOWED_ORIGIN for the exact trusted origin.
4. Create a separate Render Python web service rooted at collector, build command pip install -r requirements.txt, start command gunicorn app:app --bind 0.0.0.0:$PORT --workers 1.
5. Set the public static site's feedback-config.js endpoint URL, update the website privacy notice, and complete genuine write/read-back and negative security tests before inviting participants. Do not count local copies as submissions.

## Limits and data quality
No server endpoint is live solely because these files exist. The IP throttle (6/hour per process) is not distributed bot prevention or an identity check. A malicious person can submit repeat answers. Counts cannot prove unique parents, retention, conversion or the accuracy of real nursery costs.
Aggregate read-back (private SQL): SELECT question, answer, n FROM ccev_feedback_counts ORDER BY question, answer; SELECT n FROM ccev_feedback_total WHERE key=1;
Arrange secure backups, records management and end-of-study deletion, even though no per-person response rows are stored.

## Tests
pip install -r collector/requirements.txt
PYTHONPATH=collector python -m unittest discover -s collector -p 'test_*.py' -v
