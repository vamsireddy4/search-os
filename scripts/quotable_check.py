#!/usr/bin/env python3
"""Lint a Markdown page for AI-quotability (AEO formatting rules).

Usage: quotable_check.py page.md
       quotable_check.py --selftest

Flags: headings that are not questions, vague words, paragraphs that open with a
pronoun (can't stand alone), sections whose first 2 sentences have no number/fact,
and table cells that are bare or vague. Exit 1 if anything is flagged. Stdlib only.
"""
import re
import sys

VAGUE = ["affordable", "great", "powerful", "best-in-class", "seamless", "robust",
         "cutting-edge", "world-class", "innovative", "easy to use", "game-changer",
         "synergy", "leverage", "many", "various", "a lot of"]
PRONOUN_START = re.compile(r"^(it|this|that|these|those|they|he|she)\b", re.I)
QUESTION_WORDS = re.compile(r"^(how|what|which|why|when|where|who|is|are|can|does|do|should|will)\b", re.I)
# ponytail: heuristic lint, not NLP; it misses vague claims without these words


def check(md):
    issues, section = [], None
    lines = md.splitlines()
    for n, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line:
            continue
        m = re.match(r"^(#{2,6})\s+(.*)", line)
        if m:
            h = m.group(2).strip()
            if not (h.endswith("?") or QUESTION_WORDS.match(h)):
                issues.append((n, f"heading is not a question: {h!r}"))
            section = {"line": n, "text": ""}
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            is_header = not lines[n - 2].strip().startswith("|")  # first row of a table
            if is_header or all(re.fullmatch(r":?-+:?", c) for c in cells if c):
                continue
            for c in cells[1:]:  # column 1 is the item name, single words are fine
                if c and len(c.split()) == 1 and not re.search(r"\d", c):
                    issues.append((n, f"table cell too bare to quote alone: {c!r}"))
            continue
        if line.startswith("#"):
            continue
        low = line.lower()
        for w in VAGUE:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                issues.append((n, f"vague phrase {w!r}: replace with a number or fact"))
        if PRONOUN_START.match(line.lstrip("-*> ")):
            issues.append((n, "paragraph opens with a pronoun; won't stand alone"))
        if section is not None and section["text"] == "":
            first_two = " ".join(re.split(r"(?<=[.!?])\s+", line)[:2])
            if not re.search(r"\d", first_two):
                issues.append((n, "first 2 sentences under heading have no number/fact"))
            section["text"] = line
    return issues


def selftest():
    good = ("## How much does Blotato cost?\n\nBlotato starts at $29/mo for solo creators.\n\n"
            "| Tool | Best For | Starting Price |\n|---|---|---|\n"
            "| Blotato | Solo creators posting to 8 platforms | $29/mo |\n")
    bad = ("## Pricing\n\nIt is very affordable and powerful.\n\n"
           "| Tool | Best For |\n|---|---|\n| X | Scheduling |\n")
    assert check(good) == [], check(good)
    msgs = " ".join(m for _, m in check(bad))
    for want in ("not a question", "affordable", "powerful", "pronoun", "no number", "'Scheduling'"):
        assert want in msgs, want
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    elif len(sys.argv) == 2:
        found = check(open(sys.argv[1], encoding="utf-8").read())
        for n, msg in found:
            print(f"line {n}: {msg}")
        print(f"{len(found)} issue(s)" if found else "OK: page looks quotable")
        sys.exit(1 if found else 0)
    else:
        sys.exit(__doc__)
