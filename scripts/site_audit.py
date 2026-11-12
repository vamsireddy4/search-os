#!/usr/bin/env python3
"""AI-friendly SEO technical audit of a live site (the checks that found real bugs in the source video).

Usage: site_audit.py https://example.com [--sample 10]
       site_audit.py --selftest

Checks: robots.txt AI bots (blocked / named explicitly), llms.txt, canonical host (www vs non-www),
temporary (302/307) vs permanent redirects on sitemap URLs, soft 404s, sitemap size and lastmod,
raw-HTML text (JS-only pages), duplicate titles / meta descriptions, canonical tags pointing at
another host, and schema logo/image URLs that do not resolve. Stdlib only; read-only GETs.
"""
import json, re, sys, uuid
import urllib.error, urllib.request
from collections import Counter
from urllib.parse import urlsplit, urljoin

sys.path.insert(0, __import__("os").path.dirname(__file__))
from ai_crawl_check import AI_BOTS, TRAINING_BOTS, blocked_bots, visible_words, MIN_WORDS  # reuse, don't rewrite

UA = "Mozilla/5.0 (compatible; ai-seo-audit/1.0)"


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch(url, follow=True):
    """-> (status, final_url, location_header, body)."""
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with opener.open(req, timeout=20) as r:
            return r.status, r.geturl(), r.headers.get("Location", ""), r.read(3_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, url, e.headers.get("Location", ""), ""
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return 0, url, "", str(e)


def sitemap_entries(xml):
    """-> (page_urls, child_sitemaps, n_with_lastmod)."""
    locs = lambda tag: re.findall(rf"<{tag}\b[^>]*>.*?<loc>\s*([^<\s]+)\s*</loc>", xml, re.S | re.I)
    return locs("url"), locs("sitemap"), len(re.findall(r"<lastmod>", xml, re.I))


def page_meta(html):
    def first(pat):
        m = re.search(pat, html, re.I | re.S)
        return m.group(1).strip() if m else ""
    return {
        "title": first(r"<title[^>]*>(.*?)</title>"),
        "description": first(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)')
                       or first(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description'),
        "canonical": first(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)')
                     or first(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical'),
    }


def schema_asset_urls(html, base):
    """Logo/image URLs declared in JSON-LD blocks."""
    out = []
    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ("logo", "image"):
                    for item in v if isinstance(v, list) else [v]:
                        u = item.get("url") if isinstance(item, dict) else item
                        if isinstance(u, str): out.append(urljoin(base, u))
                walk(v)
        elif isinstance(node, list):
            for x in node: walk(x)
    for block in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S | re.I):
        try: walk(json.loads(block))
        except ValueError: out.append("!invalid JSON-LD block")
    return sorted(set(out))


def audit(site, sample=10):
    f = []  # (severity, message)
    add = lambda sev, msg: f.append((sev, msg))
    status, home, _, home_html = fetch(site)
    if status != 200:
        return [("HIGH", f"homepage returned HTTP {status} ({home_html[:120]})")]
    host = urlsplit(home).netloc
    base = f"{urlsplit(home).scheme}://{host}"
    print(f"Site resolves to {base}")

    other = host[4:] if host.startswith("www.") else "www." + host
    s, _, loc, _ = fetch(f"{urlsplit(home).scheme}://{other}/", follow=False)
    if s in (302, 303, 307): add("HIGH", f"{other} -> {host} uses a temporary {s} redirect; make it 301")
    elif s == 200: add("HIGH", f"both {host} and {other} serve 200; pick one and 301 the other")

    code, _, _, robots = fetch(base + "/robots.txt")
    if code != 200: add("MEDIUM", f"robots.txt returned HTTP {code}")
    else:
        blocked = blocked_bots(robots, base + "/")
        if search := [b for b in blocked if b not in TRAINING_BOTS]: add("HIGH", f"robots.txt blocks AI search/user bots: {', '.join(search)}")
        if training := [b for b in blocked if b in TRAINING_BOTS]: add("LOW", f"robots.txt blocks training bots {', '.join(training)}: fine if deliberate (does not block search bots)")
        named = [b for b in ("OAI-SearchBot", "GPTBot", "ClaudeBot", "PerplexityBot") if b.lower() in robots.lower()]
        if len(named) < 4: add("LOW", f"robots.txt does not name {', '.join(sorted(set(['OAI-SearchBot','GPTBot','ClaudeBot','PerplexityBot']) - set(named)))} explicitly (OpenAI recommends allowing OAI-SearchBot by name)")
        if "sitemap:" not in robots.lower(): add("LOW", "robots.txt has no Sitemap: line")
    if fetch(base + "/llms.txt")[0] != 200: add("LOW", "no /llms.txt (optional, a small AI-discovery signal)")

    rnd = f"{base}/this-page-should-not-exist-{uuid.uuid4().hex[:8]}"
    if fetch(rnd)[0] == 200: add("HIGH", "soft 404: a nonexistent URL returns HTTP 200; return a real 404")

    m = re.search(r"(?im)^sitemap:\s*(\S+)", robots or "")
    sm_url = m.group(1) if m else base + "/sitemap.xml"
    s, _, _, xml = fetch(sm_url)
    urls, children, lastmods = sitemap_entries(xml) if s == 200 else ([], [], 0)
    for child in children[:5]:
        u, _, lm = sitemap_entries(fetch(child)[3]); urls += u; lastmods += lm
    if not urls: add("HIGH", f"no sitemap URLs found at {sm_url} (HTTP {s})")
    else:
        print(f"Sitemap: {len(urls)} URLs, {lastmods} with <lastmod>")
        if lastmods < len(urls): add("LOW", f"{len(urls) - lastmods} sitemap URLs lack <lastmod>")
        wrong = [u for u in urls if urlsplit(u).netloc != host]
        if wrong: add("HIGH", f"{len(wrong)}/{len(urls)} sitemap URLs use another host (e.g. {wrong[0]}); list only {host}")

    pages = [home] + [u for u in urls if u.rstrip("/") != home.rstrip("/")][:sample]
    metas, thin = {}, []
    for u in pages:
        s, final, loc, html = fetch(u, follow=False)
        if s in (301, 302, 303, 307, 308):
            add("HIGH" if s != 301 and s != 308 else "MEDIUM", f"sitemap URL {u} redirects ({s}) to {loc}; list the final URL")
            s, final, _, html = fetch(u)
        if s != 200: add("HIGH", f"{u} returns HTTP {s}"); continue
        meta = metas[final] = page_meta(html)
        if meta["canonical"] and urlsplit(urljoin(final, meta["canonical"])).netloc != host:
            add("HIGH", f"{final} canonical points to another host: {meta['canonical']}")
        if visible_words(html) < MIN_WORDS: thin.append(final)
    if thin: add("HIGH", f"{len(thin)}/{len(metas)} pages have under {MIN_WORDS} words in raw HTML (rendering test: content likely needs JS, add SSR/prerender; not a thin-content verdict): {', '.join(thin[:3])}")
    for field in ("title", "description"):
        dup = [v for v, n in Counter(m[field] for m in metas.values() if m[field]).items() if n > 1]
        missing = sum(1 for m in metas.values() if not m[field])
        if dup: add("MEDIUM", f"duplicate {field} on several pages: {dup[0][:70]!r}")
        if missing: add("MEDIUM", f"{missing} pages have no {field}")

    for u in schema_asset_urls(home_html, home):
        if u.startswith("!"): add("MEDIUM", "homepage has an invalid JSON-LD block")
        elif fetch(u)[0] != 200: add("MEDIUM", f"schema logo/image URL does not load: {u}")
    if "application/ld+json" not in home_html: add("MEDIUM", "no JSON-LD schema in the homepage raw HTML")
    return f


def selftest():
    xml = "<urlset><url><loc>https://a.com/</loc><lastmod>2026-01-01</lastmod></url><url><loc> https://a.com/b </loc></url></urlset>"
    assert sitemap_entries(xml) == (["https://a.com/", "https://a.com/b"], [], 1)
    idx = "<sitemapindex><sitemap><loc>https://a.com/s1.xml</loc></sitemap></sitemapindex>"
    assert sitemap_entries(idx) == ([], ["https://a.com/s1.xml"], 0)
    html = ('<title>Home</title><meta content="Desc" name="description"><link rel="canonical" href="https://www.a.com/">'
            '<script type="application/ld+json">{"@type":"Organization","logo":"/logo.png","founder":{"image":{"url":"https://a.com/f.jpg"}}}</script>')
    assert page_meta(html) == {"title": "Home", "description": "Desc", "canonical": "https://www.a.com/"}
    assert schema_asset_urls(html, "https://a.com/") == ["https://a.com/f.jpg", "https://a.com/logo.png"]
    assert schema_asset_urls('<script type="application/ld+json">{bad</script>', "https://a.com/") == ["!invalid JSON-LD block"]
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args or not args[0].startswith(("http://", "https://")):
        sys.exit(__doc__)
    n = int(sys.argv[sys.argv.index("--sample") + 1]) if "--sample" in sys.argv else 10
    found = audit(args[0], n)
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    for sev, msg in sorted(found, key=lambda x: order[x[0]]):
        print(f"[{sev}] {msg}")
    print(f"\n{len(found)} finding(s); fix HIGH first (domain consistency, real 404s, SSR).")
    sys.exit(1 if any(s == "HIGH" for s, _ in found) else 0)
