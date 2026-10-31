"""Reproducible STRUCTURAL comparator, not observed competitor accuracy.

Run: python3 research/structural_benchmark.py
No external data, no API, no nursery documents; all scenarios invented.
"""
from dataclasses import dataclass
from decimal import Decimal
from itertools import product
import json

@dataclass(frozen=True)
class Tariff:
    rate: Decimal
    min_days: int
    extra_rate: Decimal
    extra_mandatory: bool
    weeks: int | None
    source_rate: bool = True
    source_min: bool = True
    source_extras: bool = True

def baseline(rate, days, breakfast):
    """Rate-only calculator given rate, days and selected extras. No clauses."""
    return rate * days + (Decimal("5") * days if breakfast else Decimal("0"))

def verified(t,days,breakfast):
    """Toy source-supported rule procedure; not a document-extraction model."""
    if not all((t.source_rate,t.source_min,t.source_extras)):
        return None,"missing_source_rule"
    if days < t.min_days:
        return None,"booking_below_minimum"
    if t.extra_mandatory and not breakfast:
        return None,"mandatory_extra_not_selected"
    return (t.rate + (t.extra_rate if breakfast else Decimal(0))) * days,"supported"

def run():
    scenarios=[]
    for rate,days,min_days,breakfast,mandatory,complete in product(
        [Decimal("60"),Decimal("72")],range(1,6),[1,2,3],[False,True],[False,True],[False,True]):
        t=Tariff(rate,min_days,Decimal("5"),mandatory,52,source_min=complete)
        quote,reason=verified(t,days,breakfast)
        simple=baseline(rate,days,breakfast)
        scenarios.append({"days":days,"min_days":min_days,"breakfast":breakfast,
            "mandatory":mandatory,"complete_source":complete,
            "rate":str(rate),"baseline":str(simple),
            "verifier_result":None if quote is None else str(quote),"reason":reason})
    assert len(scenarios)==240
    assert any(x["reason"]=="booking_below_minimum" for x in scenarios)
    assert any(x["reason"]=="missing_source_rule" for x in scenarios)
    assert all(x["verifier_result"] is None for x in scenarios if not x["complete_source"])
    assert all(x["reason"]=="supported" or x["verifier_result"] is None for x in scenarios)
    counts={r:sum(x["reason"]==r for x in scenarios) for r in
        ["supported","missing_source_rule","booking_below_minimum","mandatory_extra_not_selected"]}
    print(json.dumps({"scope":"invented structured-rule comparison only",
        "cases":len(scenarios),"counts":counts,"baseline_limitation":
        "The baseline is deliberately rate-only, not an actual named competitor",
        "competitive_superiority_proved":False,"document_extraction_tested":False},indent=2))
if __name__=="__main__":
    run()
