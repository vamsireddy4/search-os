#!/usr/bin/env python3
"""Shortlist quick-win keywords from an Ahrefs (or similar) CSV export.

Usage: pick_keywords.py keywords.csv --my-dr 29 [--max-kd 20] [--dr-margin 10] [--top 25]
       pick_keywords.py --selftest

Needs columns for keyword, volume and KD (Ahrefs names: Keyword, Volume, Difficulty;
case-insensitive, "KD"/"SV" also accepted). Optional column "SERP DRs" with the
ranking pages' DRs separated by ; or spaces, e.g. "24;37;13".

Keeps keywords that contain a buying modifier (best, top, vs, alternative(s), review,
cheap, affordable, compare) and have KD <= --max-kd. If SERP DRs are given, also
requires at least 3 ranking pages with DR <= your DR + margin. Sorted by volume.
Stdlib only.
"""
import argparse
import csv
import re
import sys

MODIFIERS = re.compile(r"\b(best|top|vs|versus|alternatives?|reviews?|cheap|affordable|compare|comparison)\b", re.I)
ALIASES = {"keyword": ["keyword", "query"], "volume": ["volume", "sv", "search volume"],
           "kd": ["difficulty", "kd", "keyword difficulty"], "drs": ["serp drs", "drs", "serp dr"]}


def col(fieldnames, key):
    low = {f.strip().lower(): f for f in fieldnames}
    return next((low[a] for a in ALIASES[key] if a in low), None)


def num(s):
    s = (s or "").replace(",", "").strip()
    return float(s) if re.fullmatch(r"\d+(\.\d+)?", s) else None


def winnable(drs, my_dr, margin):
    # ponytail: "3+ beatable pages in the SERP" is a heuristic for the video's
    # "competitors with DR near yours" rule; tune --dr-margin per niche
    return sum(d <= my_dr + margin for d in drs) >= 3


def pick(rows, my_dr, max_kd, margin):
    out = []
    for kw, vol, kd, drs in rows:
        if not MODIFIERS.search(kw) or kd is None or kd > max_kd:
            continue
        if drs and not winnable(drs, my_dr, margin):
            continue
        out.append((kw, vol or 0, kd, drs))
    return sorted(out, key=lambda r: -r[1])


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(4096)
        f.seek(0)
        reader = csv.DictReader(f, dialect=csv.Sniffer().sniff(sample, delimiters=",\t;"))
        c = {k: col(reader.fieldnames, k) for k in ALIASES}
        if not (c["keyword"] and c["kd"]):
            raise SystemExit(f"need keyword and KD columns; found {reader.fieldnames}")
        for r in reader:
            drs = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", r.get(c["drs"], "") or "")] if c["drs"] else []
            yield r[c["keyword"]].strip(), num(r.get(c["volume"]) if c["volume"] else None), num(r[c["kd"]]), drs


def selftest():
    rows = [("crm software", 617000, 71, []),
            ("top-rated crm platforms for small business", 21000, 0, [24, 37, 13, 40]),
            ("best crm for contact management", 4000, 12, [85, 90, 88, 80]),
            ("hubspot alternatives", 9000, 18, []),
            ("what is a crm", 50000, 5, [])]
    got = [r[0] for r in pick(rows, my_dr=29, max_kd=20, margin=10)]
    assert got == ["top-rated crm platforms for small business", "hubspot alternatives"], got
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
        sys.exit()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv")
    ap.add_argument("--my-dr", type=float, required=True)
    ap.add_argument("--max-kd", type=float, default=20)
    ap.add_argument("--dr-margin", type=float, default=10)
    ap.add_argument("--top", type=int, default=25)
    a = ap.parse_args()
    res = pick(load(a.csv), a.my_dr, a.max_kd, a.dr_margin)
    for kw, vol, kd, drs in res[:a.top]:
        print(f"{vol:>9,.0f}  KD {kd:>3.0f}  {kw}" + (f"  (SERP DRs: {', '.join(f'{d:.0f}' for d in drs)})" if drs else ""))
    print(f"{len(res)} quick-win keyword(s)")
