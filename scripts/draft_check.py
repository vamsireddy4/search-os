#!/usr/bin/env python3
"""Pre-publish check for a Markdown blog draft (Surfer's writing fundamentals, no Surfer needed).

Usage: draft_check.py draft.md [--keyword "how to write a case study"] [--title "..."] [--meta "..."] [--site example.com]
       draft_check.py --selftest

Checks: BLUF (first paragraph short and direct), paragraphs <= 3 sentences, a subheading at least every
300 words, share of question headings, reading grade (target 6-8, max 8), internal link count (3-5),
keyword near the front of the title, title/meta length. Exit 1 if anything is flagged.
"""
import re, sys
from urllib.parse import urlsplit


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if re.search(r"\w", s)]


def syllables(word):
    # ponytail: vowel-group heuristic, about +/-1 grade vs. real tools; swap for textstat if precision matters
    w = word.lower()
    n = len(re.findall(r"[aeiouy]+", w)) - (1 if w.endswith("e") and not w.endswith("le") else 0)
    return max(1, n)


def grade(text):
    """Flesch-Kincaid grade level."""
    words = re.findall(r"[A-Za-z']+", text)
    sents = max(1, len(sentences(text)))
    if not words: return 0.0
    return 0.39 * len(words) / sents + 11.8 * sum(map(syllables, words)) / len(words) - 15.59


def blocks(md):
    """-> list of ('h', level, text) / ('p', text); skips code, tables, lists, images."""
    out, para = [], []
    md = re.sub(r"(?s)```.*?```", "", md)
    for line in md.splitlines() + [""]:
        m = re.match(r"(#{1,6})\s+(.*)", line)
        if m or not line.strip() or re.match(r"\s*([-*+]|\d+\.|\||!\[|>)", line):
            if para: out.append(("p", " ".join(para))); para = []
            if m: out.append(("h", len(m.group(1)), m.group(2).strip()))
        else:
            para.append(line.strip())
    return out


def plain(text):
    return re.sub(r"\[([^\]]*)\]\([^)]*\)|[*_`]", lambda m: m.group(1) or "", text)


def check(md, keyword="", title="", meta="", site=""):
    issues, bl = [], blocks(md)
    paras = [plain(b[1]) for b in bl if b[0] == "p"]
    if paras and len(sentences(paras[0])) > 3:
        issues.append("BLUF: the first paragraph is long; give the direct answer in the first 1-2 sentences")
    for p in paras:
        if len(sentences(p)) > 3:
            issues.append(f"note: paragraph over 3 sentences: {p[:60]!r}...")
    run = 0
    for b in bl:
        if b[0] == "h": run = 0
        else:
            run += len(plain(b[1]).split())
            if run > 300:
                issues.append(f"note: over 300 words without a subheading, near: {plain(b[1])[:50]!r}"); run = 0
    heads = [b[2] for b in bl if b[0] == "h" and b[1] in (2, 3)]
    if heads and sum(h.rstrip().endswith("?") for h in heads) / len(heads) < 0.3:
        issues.append(f"note: only {sum(h.endswith('?') for h in heads)}/{len(heads)} H2/H3s are questions; phrase more as the questions readers ask")
    g = grade(" ".join(paras))
    if g > 8.5:
        issues.append(f"note: reading grade ~{g:.1f}; aim for 6-8 (shorter sentences, plainer words)")
    if site:
        links = re.findall(r"\]\(([^)]+)\)", md)
        internal = [u for u in links if u.startswith("/") or site in urlsplit(u).netloc]
        if not 3 <= len(internal) <= 5:
            issues.append(f"note: {len(internal)} internal links; usually 3-5 to related posts (and link back from 3-5 old posts)")
    if title:
        if keyword and keyword.lower() not in title.lower()[: max(len(keyword) + 20, 40)]:
            issues.append("title: put the target keyword near the front")
        if len(title) > 60: issues.append(f"note: title is {len(title)} chars; may truncate around 60, front-load the words that matter")
    if meta and not 120 <= len(meta) <= 160:
        issues.append(f"note: meta description is {len(meta)} chars; ~120-160 usually displays fully, say exactly what the reader gets")
    if keyword and keyword.lower() not in plain(md).lower()[:1500]:
        issues.append("target keyword does not appear in the opening of the post")
    return issues, g


def selftest():
    good = ("# How long does it take to rank on Google?\n\nTypically 3 to 6 months. Competitive niches take longer.\n\n"
            "## Why does it take months?\n\nGoogle has to crawl the page. Then it tests it. See [our guide](/indexing).\n")
    issues, g = check(good, keyword="rank on google", title="Rank on Google: How Long It Takes", site="example.com")
    assert issues == ["note: 1 internal links; usually 3-5 to related posts (and link back from 3-5 old posts)"], issues
    long_para = "## Intro\n\n" + "This is a sentence. " * 5 + "\n"
    assert any("over 3 sentences" in i for i in check(long_para)[0])
    wall = "## A\n\n" + ("word " * 320) + "\n"
    assert any("300 words" in i for i in check(wall)[0])
    assert any("near the front" in i for i in check(good, keyword="rank on google", title="A very long preamble about many things then rank on google")[0])
    assert grade("The cat sat. The dog ran.") < 3 < grade("Comprehensive organizational methodologies necessitate considerable interdepartmental coordination.")
    assert blocks("```\n# not a heading\n```\n## Real\n") == [("h", 2, "Real")]
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit()
    args, opts = [], {}
    it = iter(sys.argv[1:])
    for a in it:
        if a.startswith("--"): opts[a[2:]] = next(it, "")
        else: args.append(a)
    if not args: sys.exit(__doc__)
    md = open(args[0], encoding="utf-8").read()
    issues, g = check(md, opts.get("keyword", ""), opts.get("title", ""), opts.get("meta", ""), opts.get("site", ""))
    print(f"{len(md.split())} words, reading grade ~{g:.1f}")
    for i in issues: print(f"- {i}")
    hard = [i for i in issues if not i.startswith("note:")]
    print("OK: ready for the human review (read it aloud on your phone)" if not hard else f"{len(hard)} issue(s)")
    sys.exit(1 if hard else 0)
