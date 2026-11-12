#!/usr/bin/env python3
"""Rank keywords with the 5-point checklist + AI filter.

CSV columns (header row required):
  keyword, volume, traffic_potential, business_potential (0-3),
  intent_match (yes/no), difficulty_yes (0-4 yeses vs top pages),
  ai_satisfies (yes/no: can an AI Overview answer it with no click?)

Usage: keyword_score.py keywords.csv     |   keyword_score.py --selftest
"""
import csv, sys

def yes(v): return str(v).strip().lower() in ("yes", "y", "true", "1")

def score(row):
    """Return (score, reason). score None = drop."""
    if not yes(row["intent_match"]):
        return None, "can't match SERP intent"
    bp, dy = int(row["business_potential"]), int(row["difficulty_yes"])
    tp = float(row["traffic_potential"] or 0)
    if bp == 0:
        return None, "business potential 0"
    if yes(row["ai_satisfies"]):
        if bp < 2:
            return None, "AI answers it, low business value"
        tp *= 0.65  # ~35% click loss when an AI Overview shows
    # ponytail: naive weighting (traffic x business x odds); tune weights per niche
    return round(tp * bp * (1 + dy) / 4), "brand-mention target" if yes(row["ai_satisfies"]) else "ok"

def main(path):
    keep, drop = [], []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            s, why = score(row)
            (drop if s is None else keep).append((s, row["keyword"], why))
    keep.sort(reverse=True)
    print("RANK  SCORE     KEYWORD  (note)")
    for i, (s, k, why) in enumerate(keep, 1):
        print(f"{i:>4}  {s:>8}  {k}  ({why})")
    for _, k, why in drop:
        print(f"DROP  {k}: {why}")

def selftest():
    r = lambda **kw: {"keyword": "k", "traffic_potential": "1000", "business_potential": "3",
                      "intent_match": "yes", "difficulty_yes": "3", "ai_satisfies": "no", **kw}
    assert score(r())[0] == 3000
    assert score(r(intent_match="no"))[0] is None
    assert score(r(business_potential="0"))[0] is None
    assert score(r(ai_satisfies="yes", business_potential="1"))[0] is None
    assert score(r(ai_satisfies="yes"))[0] == 1950
    print("selftest ok")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    selftest() if sys.argv[1] == "--selftest" else main(sys.argv[1])
