#!/usr/bin/env python3
"""AEO gap analysis without Ahrefs: where do AI answers name competitors but not you?

Usage: aeo_gaps.py answers.csv --brand nike [--top 30]
       aeo_gaps.py --selftest

answers.csv columns: query,engine,brands   (brands = names in that AI answer, ';'-separated)
Log one row per query per engine (ChatGPT, Perplexity, AI Overview, ...); repeat runs
are fine (each row counts). Prints share of voice per engine and the gap queries,
ranked by how many competitors appear. Stdlib only.
"""
import argparse
import csv
import sys
from collections import defaultdict


def analyze(rows, brand):
    brand = brand.strip().lower()
    seen = defaultdict(lambda: [0, 0])          # engine -> [answers naming you, answers]
    gaps = defaultdict(set)                     # query -> competitors named where you weren't
    for query, engine, brands in rows:
        names = {b.strip().lower() for b in brands.split(";") if b.strip()}
        seen[engine][1] += 1
        if brand in names:
            seen[engine][0] += 1
        elif names:
            gaps[query] |= names
    covered = {q for q, e, b in rows if brand in {x.strip().lower() for x in b.split(";")}}
    # a query is only a gap if you never appeared for it on any engine/run
    gaps = {q: c for q, c in gaps.items() if q not in covered}
    sov = {e: (hit / total if total else 0.0) for e, (hit, total) in seen.items()}
    return sov, sorted(gaps.items(), key=lambda kv: (-len(kv[1]), kv[0]))


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        missing = {"query", "engine", "brands"} - {c.strip().lower() for c in r.fieldnames or []}
        if missing:
            raise SystemExit(f"missing columns: {', '.join(sorted(missing))}")
        norm = {c.strip().lower(): c for c in r.fieldnames}
        return [(row[norm["query"]].strip(), row[norm["engine"]].strip() or "?", row[norm["brands"]] or "")
                for row in r if row[norm["query"]].strip()]


def selftest():
    rows = [("best trail running shoes for beginners", "AIO", "Hoka; Brooks"),
            ("best trail running shoes for beginners", "ChatGPT", "Hoka"),
            ("running shoes for plantar fasciitis", "AIO", "Asics;New Balance;Nike"),
            ("sustainable running shoe brands", "Perplexity", "Allbirds;On;Veja"),
            ("how to clean suede shoes", "AIO", "Nike")]
    sov, gaps = analyze(rows, "Nike")
    assert sov == {"AIO": 2 / 3, "ChatGPT": 0.0, "Perplexity": 0.0}, sov
    assert [q for q, _ in gaps] == ["sustainable running shoe brands", "best trail running shoes for beginners"], gaps
    assert gaps[1][1] == {"hoka", "brooks"}
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
        sys.exit()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv")
    ap.add_argument("--brand", required=True)
    ap.add_argument("--top", type=int, default=30)
    a = ap.parse_args()
    sov, gaps = analyze(load(a.csv), a.brand)
    print("Share of voice (answers naming you):")
    for e, s in sorted(sov.items()):
        print(f"  {e:<14} {s:6.1%}")
    print(f"\n{len(gaps)} gap quer{'y' if len(gaps) == 1 else 'ies'} (competitors named, you never):")
    for q, comps in gaps[:a.top]:
        print(f"  [{len(comps)}] {q}  <- {', '.join(sorted(comps))}")
