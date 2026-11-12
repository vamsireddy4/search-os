#!/usr/bin/env python3
"""Check the two things that quietly kill search traffic: noindex and robots.txt blocks.

Usage: check_indexable.py <url> [<url> ...]
Exit code 1 if any URL is blocked.
"""
import re, sys, urllib.request, urllib.robotparser
from urllib.parse import urlsplit

BOTS = ["Googlebot", "Bingbot", "OAI-SearchBot", "Claude-SearchBot", "PerplexityBot"]  # search bots only; training-bot blocks are a policy choice (see ai_crawl_check.py)
UA = "Mozilla/5.0 (compatible; seo-fundamentals-check)"

def noindex_in(html, header):
    if "noindex" in (header or "").lower():
        return "X-Robots-Tag header"
    for tag in re.findall(r"<meta[^>]+>", html, re.I):
        if re.search(r'name=["\']?(robots|googlebot)', tag, re.I) and "noindex" in tag.lower():
            return "meta robots tag"
    return None

def check(url):
    problems = []
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        html = r.read(2_000_000).decode("utf-8", "ignore")
        where = noindex_in(html, r.headers.get("X-Robots-Tag"))
    if where:
        problems.append(f"noindex via {where}")
    p = urlsplit(url)
    rp = urllib.robotparser.RobotFileParser(f"{p.scheme}://{p.netloc}/robots.txt")
    try:
        rp.read()
        blocked = [b for b in BOTS if not rp.can_fetch(b, url)]
        if blocked:
            problems.append("robots.txt disallows " + ", ".join(blocked))
    except Exception as e:
        problems.append(f"robots.txt unreadable ({e})")
    return problems

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--selftest":
        assert noindex_in('<meta name="robots" content="noindex,follow">', None)
        assert noindex_in("", "noindex")
        assert not noindex_in('<meta name="description" content="noindex tips">', None)
        sys.exit(print("selftest ok"))
    bad = False
    for u in sys.argv[1:]:
        try:
            probs = check(u)
        except Exception as e:
            probs = [f"fetch failed ({e})"]
        bad |= bool(probs)
        print(f"{'BLOCKED' if probs else 'INDEXABLE'}  {u}" + "".join(f"\n  - {x}" for x in probs))
    sys.exit(1 if bad else 0)
