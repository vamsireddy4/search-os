#!/usr/bin/env python3
"""On-page SEO checklist for one page (stdlib only).

Usage: onpage_check.py <url-or-html-file> "<keyword>" [--base https://site.com]
Exit code 0 when every required check passes, 1 otherwise. Run with --selftest to self-check.
"""
import sys, urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

VIDEO_HOSTS = ("youtube.com", "youtube-nocookie.com", "youtu.be", "vimeo.com", "wistia", "loom.com")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""; self.h2 = []; self.alts = []; self.links = []
        self.meta_desc = None; self.canonical = None; self.schema = False; self.video = False
        self._in = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("title", "h2"):
            self._in = tag
            if tag == "h2": self.h2.append("")
        elif tag == "img": self.alts.append(a.get("alt") or "")
        elif tag == "a" and a.get("href"): self.links.append(a["href"])
        elif tag == "meta" and (a.get("name") or "").lower() == "description": self.meta_desc = a.get("content") or ""
        elif tag == "link" and "canonical" in (a.get("rel") or "").lower(): self.canonical = a.get("href")
        elif tag == "script" and a.get("type") == "application/ld+json": self.schema = True
        elif tag == "video": self.video = True
        elif tag == "iframe" and any(h in (a.get("src") or "") for h in VIDEO_HOSTS): self.video = True

    def handle_endtag(self, tag):
        if tag == self._in: self._in = None

    def handle_data(self, data):
        if self._in == "title": self.title += data
        elif self._in == "h2": self.h2[-1] += data


def check(html, keyword, base):
    p = Page(); p.feed(html)
    kw = keyword.lower().strip()
    host = urlparse(base).netloc if base else ""
    internal = external = 0
    for href in p.links:
        if href.startswith(("#", "mailto:", "tel:", "javascript:")): continue
        h = urlparse(urljoin(base or "", href)).netloc
        if not h or h == host: internal += 1
        else: external += 1
    # (name, passed, detail, required)
    return [
        ("keyword in title", kw in p.title.lower(), p.title.strip()[:80], True),
        ("keyword in an H2", any(kw in h.lower() for h in p.h2), f"{len(p.h2)} H2s, only where it reads naturally", False),
        ("keyword in an image alt", any(kw in a.lower() for a in p.alts), f"{len(p.alts)} images", False),
        ("has a video", p.video, "only if the SERP shows video", False),
        ("has an internal link", internal > 0, f"{internal} internal", True),
        ("has an external link", external > 0, f"{external} external", False),
        ("meta description", bool(p.meta_desc), (p.meta_desc or "")[:80], False),
        ("canonical tag", bool(p.canonical), p.canonical or "", False),
        ("schema (JSON-LD)", p.schema, "", False),
    ]


def main(argv):
    if "--selftest" in argv: return selftest()
    if len(argv) < 2: print(__doc__); return 2
    src, kw = argv[0], argv[1]
    base = argv[argv.index("--base") + 1] if "--base" in argv else (src if src.startswith("http") else "")
    if src.startswith("http"):
        req = urllib.request.Request(src, headers={"User-Agent": "onpage-check/1.0"})
        html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
    else:
        html = open(src, encoding="utf-8", errors="replace").read()
    results = check(html, kw, base)
    for name, ok, detail, req in results:
        print(f"{'PASS' if ok else ('FAIL' if req else 'WARN')}  {name:24} {detail}")
    if not base: print("note: no --base given, so every absolute link counts as external")
    return 0 if all(ok for _, ok, _, req in results if req) else 1


def selftest():
    good = """<html><head><title>Best Gaming Chairs 2026</title>
    <meta name="description" content="x"><link rel="canonical" href="https://a.com/c">
    <script type="application/ld+json">{}</script></head><body>
    <h2>Why gaming chairs matter</h2><img src=a.jpg alt="red gaming chairs">
    <iframe src="https://www.youtube.com/embed/x"></iframe>
    <a href="/desks">desks</a><a href="https://other.com">ref</a></body></html>"""
    assert all(ok for _, ok, _, _ in check(good, "Gaming Chairs", "https://a.com/c"))
    bad = check("<title>Home</title><a href='https://a.com/x'>x</a>", "gaming chairs", "https://a.com/")
    d = {n: ok for n, ok, _, _ in bad}
    assert not d["keyword in title"] and d["has an internal link"] and not d["has an external link"]
    print("selftest ok"); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
