#!/usr/bin/env python3
"""AEO technical check: can AI crawlers read these pages?

Usage: ai_crawl_check.py URL [URL ...]
       ai_crawl_check.py --selftest

For each site: which AI bots robots.txt blocks, and whether llms.txt exists.
For each URL: how much visible text the raw HTML has (ChatGPT's crawler does not run JS).
Stdlib only.
"""
import re
import sys
import urllib.error
import urllib.request
import urllib.robotparser
from urllib.parse import urlsplit

AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot",
           "PerplexityBot", "Google-Extended", "Applebot-Extended", "CCBot"]
# training-only crawlers: blocking them is an owner policy choice and does not block the same vendor's search bot
TRAINING_BOTS = {"GPTBot", "ClaudeBot", "Google-Extended", "Applebot-Extended", "CCBot"}
UA = "Mozilla/5.0 (compatible; aeo-check/1.0)"
MIN_WORDS = 150  # ponytail: crude "is there content without JS" threshold, tune per site


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read(3_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""


def blocked_bots(robots_txt, url):
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(robots_txt.splitlines())
    return [b for b in AI_BOTS if not rp.can_fetch(b, url)]


def visible_words(html):
    html = re.sub(r"(?is)<(script|style|noscript|svg|template)\b.*?</\1>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    return len(re.findall(r"\w{2,}", text))


def main(urls):
    bad = False
    seen = set()
    for url in urls:
        p = urlsplit(url)
        base = f"{p.scheme}://{p.netloc}"
        if base not in seen:
            seen.add(base)
            code, robots = fetch(base + "/robots.txt")
            blocked = blocked_bots(robots, url) if code == 200 else []
            print(f"\n{base}\n  robots.txt: HTTP {code}")
            search = [b for b in blocked if b not in TRAINING_BOTS]
            training = [b for b in blocked if b in TRAINING_BOTS]
            print(f"  AI search/user bots blocked: {', '.join(search) if search else 'none'}")
            if training: print(f"  training bots blocked (policy choice, confirm it is deliberate): {', '.join(training)}")
            if search:
                bad = True
                print("  -> remove those Disallow rules; on Cloudflare check "
                      "'Instruct AI bot traffic with robots.txt'")
            print(f"  llms.txt: {'present' if fetch(base + '/llms.txt')[0] == 200 else 'absent (optional)'}")
        code, html = fetch(url)
        words = visible_words(html)
        ok = code == 200 and words >= MIN_WORDS
        bad |= not ok
        print(f"  {url}: HTTP {code}, {words} words in raw HTML "
              f"{'OK' if ok else '-> LOW: content likely needs JS; use SSR/prerender'}")
    return 1 if bad else 0


def selftest():
    robots = "User-agent: GPTBot\nDisallow: /\n\nUser-agent: *\nAllow: /\n"
    assert blocked_bots(robots, "https://x.com/a") == ["GPTBot"]
    assert blocked_bots("User-agent: *\nDisallow: /\n", "https://x.com/") == AI_BOTS
    spa = '<html><body><div id="root"></div><script>' + "word " * 500 + "</script></body></html>"
    assert visible_words(spa) == 0
    assert visible_words("<p>" + "hello world " * 100 + "</p>") == 200
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    elif len(sys.argv) > 1:
        sys.exit(main(sys.argv[1:]))
    else:
        sys.exit(__doc__)
