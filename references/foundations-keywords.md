# Foundations and keywords

How search and AI answers work, myths, dated numbers, then the planning chain: keywords → intent → clusters → topical map → priorities → new-site ramp.

Related files: writing the pages (content.md), crawl/index/render (technical.md), on-page, schema, entity and internal linking detail (onpage-schema-entity.md), links and mentions (offsite-authority.md), AI visibility program and measurement (ai-visibility.md), GSC, striking distance, cannibalisation and decay (measure-refresh.md), which audit to run (audits.md).

---

## 1. How search works

**Google is a library, not a live reader.** It crawls, indexes, then ranks. A page that is not indexable cannot rank anywhere, including in AI answers built on the index. Check that first (`python3 ~/.claude/skills/searchos/scripts/check_indexable.py <url>`, details in technical.md).

**Three reliable signals** to plan around:
1. **Backlinks and mentions:** votes of trust from other sites (offsite-authority.md).
2. **Search intent:** the page type and format the live SERP rewards. You cannot optimise your way out of the wrong page type.
3. **User satisfaction:** resolve the query fast. Length does not matter: a 283-word page ranks #1 for "how to turn off iPhone 12".

**SEO is "search everywhere optimisation".** AI assistants search the web before answering (ChatGPT search leans on the Bing index), so ranking in Google and Bing is the foundation of AI visibility. The fundamentals have not changed; distribution has. Google wants searchers back (ads), so the winning page is the one searchers prefer.

**How AI answers pick sources (planning view; the full program is in ai-visibility.md):**
- Almost all AI visibility work acts on what gets **retrieved** at answer time (RAG). Changing what a model learned in training is slow (refresh roughly every ~6 months) and nearly impossible to steer.
- **Query fan-out:** one prompt splits into many sub-queries generated on the fly (typically 9-11, up to 28; AI Mode usually 5-11; Deep Research ~420). 95%+ of fan-out queries have zero search volume, so plan for **whole-topic coverage**, not single keywords.
- Prompts are long (~25 words vs ~6 for a typed search, "the long tail is back"; prompts ~5x longer than keywords) and carry the user's situation and fears.
- AI answers usually name only 2-3 brands, and the brand mentioned most across all retrieved pages tends to win, not the owner of the #1 cited URL. That makes third-party mentions on fan-out pages (best / top / vs / review / alternative) a planning target in their own right.
- Answers vary on purpose and platforms differ: one screenshot proves nothing (ai-visibility.md).

**GEO vs SEO, for explaining to a client.** "SEO gets you ranked. GEO gets you quoted." Both need visibility, quality and intent match, and AI platforms still use search engines, so SEO is the base. Google's own guidance (Search Central "Optimizing for generative AI features", announced 2026-05-15, updated 2026-07-10) says optimising for its generative AI features is SEO: no special markup, no AI text file or llms.txt, no chunking spec, no separate GEO/AEO playbook; the page must be indexed and snippet-eligible.

| | SEO | GEO / AEO |
|---|---|---|
| Target | SERPs | AI answers |
| What moves it | keywords, backlinks, technical health, alt text | structure, authority, citations and mentions |
| Traffic | click-driven | exposure-driven (mentions → branded and direct visits) |
| Unit | whole page or site | each passage |
| Role of your content | a recommendation (a link) | a resource (quoted) |

**What Google's systems can store (leak and patent material, not confirmed weights).** The May 2024 Search API leak (Content Warehouse API: 14,014 attributes, 2,596 modules; Google confirmed authenticity on 29 May 2024 while cautioning on context) and Google patents show fields Google's systems can store. They are not a confirmed list of ranking factors and they carry no published thresholds; never quote dwell-time seconds or "average" scores.
- People: NavBoost click fields (goodClicks, badClicks, lastLongestClicks; patent US 8,595,225). Read as: post-click satisfaction is stored; analytics bounce rate and dwell time are only UX proxies.
- Content: siteFocusScore (topical focus), originalContentScore (a 0 to 127 field documented as set only on pages with little content), Information Gain (patent US 11,354,342, "Contextual estimation of link information gain").
- Site: a site-wide quality modifier alongside Q* and siteAuthority, a domain-level lift on every page ("why some sites seem to rank no matter what").
- Entity: name, address and phone consistency across the web helps confirm who you are (NAP audit in offsite-authority.md).

Honest timelines when these are the lever: engagement and NAP fixes 2 to 12 weeks; content focus 8 to 16 weeks; domain authority 12 to 26 weeks.

---

## 2. Myths to stop repeating

Never recommend anything in the left column.

| Myth | Reality |
|---|---|
| Keyword density 2-3% | No target exists. Cover the topic; repeating a phrase 10-50 times does nothing. Pages rank for terms not on the page. |
| Meta keywords tag | Ignored since 2009. |
| "LSI keywords" | Not a Google concept. Use real subtopics and entities. |
| Keyword prominence/proximity in source | Not mechanical. |
| FAQ / HowTo rich results | HowTo removed 2023; FAQ rich results ended 2026-05-07. FAQ sections are fine for readers; FAQPage markup is optional, harmless only if it matches visible Q&A, never a ranking, rich-result or AI-citation win. No "AI schema" exists. |
| Sitemap priority / changefreq | Ignored; only accurate lastmod matters. |
| robots.txt keeps pages out of the index | It blocks crawling, not indexing. Use noindex or X-Robots-Tag. |
| 302s pass nothing | Both pass signals; use 301 for permanent moves. |
| AMP required | Not required since 2021. |
| FID < 100 ms | Replaced by INP < 200 ms (March 2024). |
| Dwell time / bounce rate are direct ranking factors | Not confirmed. Click-satisfaction data is stored (NavBoost); analytics metrics are UX proxies. |
| Google stopped using PageRank | Still used internally; only the toolbar died (2016). |
| DA / PA / DR determine rankings | Third-party metrics. Fine for comparing ranking pages (winnability); useless for vetting a single link source. |
| Max 100-120 links per page | Dropped. |
| Submit to hundreds of engines | Google and Bing (Bing covers ChatGPT, Copilot, DuckDuckGo, Yahoo); Yandex/Baidu only if targeting those markets. |
| Bulk classifieds, bookmarking, article directories, Web 2.0 blogs, forum link drops | Low value; at scale a link scheme. |
| Daily backlink quotas | SpamBrain risk. |
| Article spinning / mass AI pages | Scaled-content spam. |
| Copy a competitor's schema including ratings | Fake ratings risk a manual action. |
| Sockpuppet Quora/Reddit accounts | Deceptive; communities and AI source filters both punish it. |
| Press-release wires for links | Wire links are ignored; release only real news. |
| Word count or title/meta length targets | Word count is a competitor-relative compass; ~60/~155 chars are display hints (pixel truncation). Front-load what matters. |
| Ranking reports alone prove SEO works | Report conversions, GSC clicks, AI visibility. |

---

## 3. Numbers worth knowing (dated, directional)

Third-party research figures. Quote them with source and date, call them directional, and never turn them into rules (a correlation is not a listicle, freshness or authority rule). Where two figures disagree, quote the range with both dates.

| Figure | Source | Date (as quoted) |
|---|---|---|
| Google sends more traffic than AI chatbots: ~345x (Ahrefs, earlier cut) / 190-210x (Ahrefs, later cut) | Ahrefs | 2025-2026 |
| AI chatbots ~0.25-0.5% of site traffic; AI traffic up 9.7x YoY | Ahrefs | 2025-2026 |
| ChatGPT 900M weekly users, ~12% of Google's search volume | Ahrefs | 2025-2026 |
| AI Overviews cut #1 CTR ~35%, rising to ~58% a year later | Ahrefs | ~2025 → 2026 |
| AIOs show on ~21% of keywords (20.5% of SERPs), ~58% of question queries (57.9% vs 15.5% non-questions), 46% of 7+ word queries; 99.9% informational. Lower estimate: 11.7% of keywords | Ahrefs; McCoy | 2025-2026 |
| AIO keywords: usually 3+ words; 71% have KD < 30; median KD 12 vs 33 for non-AIO; 99.2% informational | Ahrefs 300k-keyword study | 2025 |
| AIOs usually co-occur with ~3 other features: PAA 60%+, featured snippets 50%+ | Ahrefs | 2025 |
| ~76% of AIO citations come from top-10 pages (newer figure ~38%; ~40% from below position 10; 14% not in top 100) | Ahrefs | 2025 → 2026 |
| 86% of top-cited sources are unique to one assistant; 7 of top 50 domains (14%) cited on all of AIO/ChatGPT/Perplexity | Ahrefs | 2025-2026 |
| AIO vs AI Mode: 13.7% citation overlap despite 86% semantic similarity; AI Mode cites Quora 3.5x more | Ahrefs | 2025-2026 |
| Top-10 overlap with search results: Perplexity 28.6%, ChatGPT 8-10% (figures of ~35%/~70% elsewhere unverified) | Ahrefs | 2025-2026 |
| Branded web mentions correlate 0.664 with AIO visibility (75k brands); DR 0.326, referring domains 0.295, branded traffic 0.274, backlinks 0.218 | Ahrefs | 2025 |
| YouTube mentions correlate 0.737 with AI visibility; mention impressions ~0.717 | Ahrefs | 2025-2026 |
| Only 28% of AI mentions are linked (Perplexity 51.6%, AI Mode 36.8%, ChatGPT 26.9%, AIO 10.7%) | Ahrefs | 2025-2026 |
| YouTube 5.6% of AIO citations, most-cited domain in AI Mode and AIO; Reddit most-cited in ChatGPT | Ahrefs | 2025-2026 |
| "70-85% of AI brand mentions come from other sites" | Unsourced; do not rely on it | n/a |
| 43.8% of cited pages are listicles | Ahrefs | 2025-2026 |
| AI-cited pages ~25.7% fresher; cited content ~2.9 vs 3.9 years old; 76.4% of ChatGPT top-cited URLs updated in the last 30 days | Ahrefs (17M citations) | 2025-2026 |
| Word count correlation with citation 0.04; 53.4% of cited pages under 1,000 words; cited average 1,282 words, only 16% over 2,000 | Ahrefs | 2025-2026 |
| 45%+ of AIO citations change on each refresh (~every 2 days) | Ahrefs | 2025-2026 |
| ~60% of Google searches end without a click; Perplexity ~0.5M → 15M monthly users | Hostinger Academy | Jan 2023 → Apr 2024 |
| >96% of pages get zero Google traffic | Ahrefs | as quoted |
| "km to miles" gets ~0.17 clicks per search | Ahrefs | as quoted |
| AI-referred visitors convert better: 23x signups (Ahrefs: 0.5% traffic → 12.1% signups), ~6x (Webflow), "reportedly 4-10x" (the AI Visibility Checklist 2026 (focal)), 10% conversion (Vercel) | each named source | 2025-2026 |

---

## 4. Keyword research

### 4.1 Intake

Ask once, then work with what you get: goal (leads, sales, signups), URL or repo (read the repo instead of asking), business type (local, SaaS, ecommerce, publisher), USP, locations, site age and authority, tools available (GSC, Ahrefs, Semrush, Surfer, none). Record a baseline before changing anything (rankings, monthly organic clicks, conversions). Fix crawl and index blockers before any keyword work.

### 4.2 Discovery (cheapest sources first)

1. **GSC queries** you already get impressions for.
2. **The live SERP:** incognito autocomplete, People Also Ask (open 2-3 nested levels), People Also Search For, wildcard searches (`cleaning _ services`), autocomplete sweeps `[entity] a..z` and `[entity] for / vs / how / cost / best`.
3. **Customer wording:** sales calls (best source), support tickets, live chats, reviews, Reddit and forum threads in exact phrasing ("my team keeps missing client emails", not "workflow inefficiency").
4. **Competitors:** sitemaps and folder structures (3-5 competitors), their top pages and organic keywords.
5. **Formula roots:** root + modifiers (best, buy, price, cheapest, near me, for sale, professional) + location.
6. **Adjacent up-funnel topics** (plumber → "signs you need a new water heater").
7. **AI seeds** (ideas only, never ship unvalidated): "Give me 30 questions someone asks before buying <category>".
8. **Tools:** Ahrefs Matching terms + Questions, Semrush Keyword Magic, AnswerThePublic, Keyword Planner (ideas only: its ranges are for ads; use a 12-month range and "All locations" for city-named keywords).

**Conversation mining prompt** (paste transcripts, emails, chats or threads into an LLM):

```
Based on these customer conversations:
- What does the customer care about?
- What is the customer afraid of?
- What are their fears, uncertainties and doubts?
- What questions do they ask before buying, in their own words?
List the topics and full questions, and mark the ones a keyword tool would not show.
```

**Buyer-query sort:** turn 10-20 customer quotes into ~20 ready-to-buy queries in three buckets, **competitor terms, problem terms, fit terms**; for the top 5, list the 5 smaller sub-questions an AI would need to answer (that is your fan-out coverage). Skip anything purely educational with no buying intent.

**Seed expansion without paid tools (30-50 phrases):** related searches and PAA; `<seed> guide / tips / tools / examples / vs`, `best <seed>`, `how to <seed>`; `what is / how does / why <seed>`, `<seed> for beginners`; commercial (best, top, review, comparison, pricing), informational (guide, tutorial, explained, examples), transactional (buy, download, tool, software, service); `<seed> <current year>` from the system date. Drop near-duplicates (stop word or plural only). More than 50 variants → narrow the seed; fewer than 5 → broaden it.

**Ahrefs recipes (each has a no-tool fallback):**

| Goal | Recipe | No-tool fallback |
|---|---|---|
| Buying-intent long tail | Keywords Explorer → seed → Matching terms → Include, Any word: `best, top, review, how to, vs, budget, for beginners, cheap, affordable, alternatives` | Google `best <category>`, `<competitor> vs`, `<competitor> alternatives`, `<category> review` |
| Conversational questions that already trigger AIO | Matching terms → Questions → SERP features: AI overview → Word count min 4 | Google the questions, note which show an AI answer |
| Informational with buying signals | AI overview + Intent: Informational, exclude Branded and Local ("natural ozempic alternatives"; teach → trust → CTA) | Filter an export by question words, spot-check SERPs |
| Several features at once | Questions + Featured snippet + AI overview + People also ask | Manual SERP check |
| Competitor's easy AIO keywords | Site Explorer → competitor → Organic keywords → AI overview "Where target ranks" → KD max 30 → Position 1-20 (nike.com: "how to clean suede shoes", KD 12) | Competitor sitemap + manual SERP checks |
| Action queries (AI cannot finish the job) | Include, Any word: `calculator, checker, generator, converter, estimator, tool, template, finder, planner, maker`, or Intents = Transactional | Filter an export for those words + buy / hire / near me / price |
| Reddit / YouTube opportunities | Site Explorer → reddit.com → Organic keywords → Pos 1-5 → Include topic; `www.youtube.com/watch` → Pos 1-3 | Google `<topic> reddit`, `<topic> youtube` |
| Niche gaps vs giants | Brand Radar → Topics, filter Topic contains `<category>` (e.g. `nonprofit crm` 2.2K, `ecommerce crm` 1.9K vs `crm software` 117K) | `aeo_gaps.py` on pasted answers (ai-visibility.md) |

### 4.3 Validation: the checklist

1. **Search demand.** Do not trust volume alone ("km to miles" gets ~0.17 clicks per search). Default floor ≥100/mo, lower is fine for high-value B2B; traffic potential and business potential override a hard floor.
2. **Traffic potential:** the traffic the current #1 page gets (it usually ranks for ~1,000 other keywords). Use it as the target number, not the keyword's own volume.
3. **Business potential 0-3:** 3 = product is the solution ("buy used golf clubs"), 2 = product helps ("best golf clubs"), 1 = loose fit ("what is a handicap"), 0 = no fit ("happy gilmore review"). 0 → drop.
4. **Search intent:** read the top results for type (blog, video, product, category), format (how-to, listicle, review) and angle (beginner, fresh, cheap). If you cannot produce the dominant type, drop it.
5. **Ranking difficulty:** against the top pages, do you have (or can you get) more quality backlinks, similar authority, equal topical focus, and something better to say? Count the yeses (0-4).
6. **Fit and durability:** a real conversion path ("a keyword without a conversion path is vanity"); Google Trends 12 months and 5 years, prefer evergreen.

**Drop:** competitor brand names, job-seeker queries, things you do not sell, other brands' navigational queries (one line why), anything with no conversion path.

**BID shorthand** for quick triage: **B**usiness potential, **I**ntent, **D**ifficulty.

### 4.4 Winnability: difficulty bands and SERP authority

KD is a tool estimate. Use it to screen, then confirm on the SERP.

| Site situation | KD band | Volume band |
|---|---|---|
| New or small site | KD < 30, prefer single digits ("KD 8 / 700 searches beats KD 67 / 1.8k") | 100-1,000 |
| Established site | KD 30-50 | 1,000-10,000 |
| Quick-win buying modifiers (script default) | KD ≤ 20 | sort by volume |

- **Competition over volume.** Example: "crm software" 617K, KD 71 vs "top-rated crm platforms for small business" 21K, KD 0. Head terms are unwinnable for a new site; start long tail.
- **SERP authority check:** open the SERP overview and compare the ranking pages' DR with yours. Near yours (yours 29, theirs 13 / 24 / 37) → compete. All in the 80s → skip. DR is fine here because you are comparing ranking pages, not vetting a link source.
- **SERP read:** thin pages ranking "by accident" (50-word pages, off-topic pages) = easy win; government or authority sites = harder; all news = skip unless you are a publisher; the same keyword in competitor titles and URLs = direct competition.
- **Mix per topic folder:** 1-2 high-volume, high-competition keywords plus several easy low-volume ones. Sequence easy first: clicks and a track record come before competitive terms (Avalanche theory, a working theory, not a confirmed mechanism).
- **Pruning to a page:** check relevance, dedupe by word overlap, sort by volume, pick 1 primary (max 2, best volume ÷ difficulty), the rest secondary. Score singular and plural separately.

### 4.5 The AI filter and the three buckets

Ask for every keyword: **"Can AI fully satisfy the user for this query?"** Google it and look at the AI answer.

- **Yes** (definitions, "what is", "how to calculate", simple how-tos): the AIO absorbs most of the click. Do not chase it as a traffic target. Keep it only if it feeds a cluster, if you can go far deeper, or as a **brand-mention target** (aim to be named inside the answer, then convert with a CTA).
- **No** (calculator, checker, generator, converter, template, near me, buy, hire, service, current data): classic SEO still works. Prioritise these, and consider building free tools for them (content.md covers calculator pages).

Plan with three buckets:

1. **Be findable where AI looks.** Find the domains your niche's AI answers actually cite: Brand Radar → brand + competitors + niche → Cited domains, or ask each assistant 10-20 buyer questions and record the cited domains. Tendencies, not rules: AIOs lean on YouTube, Reddit, Quora; ChatGPT on publishers and news; Perplexity on niche and regional sites. Always check your niche's real citations (forum visibility in Google contracted in the May 2026 core update, so do not assume).
2. **Get mentioned on fan-out pages.** Brand Radar → Cited pages → filter Prompt, Contains, Phrase match, any word: `best`, `top`, `vs`, `review`, `alternative` (or Brand Radar → platform → "Others only"); or Google the same patterns. Pitch authors for review or inclusion (offsite-authority.md). A mention on a popular domain is not visibility: AI cites specific pages.
3. **Classic SEO for action queries.** Track this list in GSC.

Pick by goal and hold the plan for months (changing direction every few weeks resets authority): goal = clicks → buying intent + tools; goal = mentions → AIO question keywords with a CTA. Re-check citations against competitors on the timing in ai-visibility.md section 11.

### 4.6 Scripts

**Score a validated list** with the checklist plus the AI discount:

```
python3 ~/.claude/skills/searchos/scripts/keyword_score.py keywords.csv
python3 ~/.claude/skills/searchos/scripts/keyword_score.py --selftest
```

CSV header: `keyword, volume, traffic_potential, business_potential, intent_match, difficulty_yes, ai_satisfies` (business_potential 0-3; intent_match yes/no; difficulty_yes 0-4 yeses vs top pages; ai_satisfies yes/no).
Logic: drop if intent_match is no ("can't match SERP intent") or business potential is 0; if ai_satisfies is yes and business potential < 2, drop ("AI answers it, low business value"), otherwise traffic potential × 0.65 (~35% click loss) and note "brand-mention target". Score = round(traffic_potential × business_potential × (1 + difficulty_yes) / 4). The weighting is naive; tune per niche.

**Shortlist quick wins** from an Ahrefs (or similar) export:

```
python3 ~/.claude/skills/searchos/scripts/pick_keywords.py keywords.csv --my-dr 29 [--max-kd 20] [--dr-margin 10] [--top 25]
python3 ~/.claude/skills/searchos/scripts/pick_keywords.py --selftest
```

Columns, case-insensitive: keyword/query; volume/sv/search volume; difficulty/kd/keyword difficulty; optional `SERP DRs` (e.g. `24;37;13`). Keeps keywords that contain a buying modifier (`best, top, vs, versus, alternative(s), review(s), cheap, affordable, compare, comparison`) with KD ≤ `--max-kd`. If SERP DRs are present, it also needs at least 3 ranking pages with DR ≤ your DR + `--dr-margin`. Sorted by volume. Run pick_keywords to find candidates, validate them on the SERP, then score the survivors with keyword_score.

---

## 5. Search intent

### 5.1 Taxonomy and modifier lexicon

Always use four intents.

| Intent | Modifiers | Page type | Example |
|---|---|---|---|
| Informational | what, how, why, guide, examples, meaning, tutorial, explained | guide / explainer / how-to | how to train a puppy |
| Commercial investigation | best, top, review, vs, alternative, comparison, for [use case], pricing | comparison, listicle, buyer guide, honest review | best dog training classes |
| Transactional | buy, price, cost, near me, hire, book, quote, discount, product name with buying context | product / service / category / pricing page | dog training class near me sign up |
| Navigational | brand names, login, contact | the exact brand page; rarely worth content | petsmart dog training |

Local: "near me" and suburb queries are transactional even without buy words.

### 5.2 Read the SERP (ground truth)

- **30-second test:** the top 10 results ARE the intent. When your classification disagrees with what ranks, defer to the SERP.
- Note type, format and angle; skip intent outliers (one forum thread in a page of product pages).
- **Ambiguous query:** name both intents and which one the SERP rewards. Ambiguity is itself a finding.
- No live SERP access: say so once at the top and mark ambiguous calls "unverified against the SERP". Never describe what a SERP shows unless you looked.
- Add the **AI layer** per cluster: AI-answered (definitions, how-tos, comparisons → answer-first page built to win the citation) vs click query (local, transactional, tools, current data → page built to convert).

### 5.3 Mismatch detection

Given keyword-URL pairs, judge each page's type from the fetched page, else from the URL pattern (`/blog/`, `/products/`, `/services/`), and say which you used. Flag type fights: a product page on a how-to query, a blog post on a buy query or category-page SERP. Fix options: change the page type, retarget the page, or build the right page and retarget this one.

Rank the work: **mismatches first** (demand already exists, the page is just the wrong shape), then uncovered clusters by size, then covered-and-correct (leave alone).

Intake line:
```
Paste your keyword list, one per line. A Google Search Console query export works perfectly. If you want mismatch detection, also paste the URL each keyword currently targets (keyword, URL per line), and tell me your site type in a word or two: ecommerce, SaaS, local service, content site.
```
Never block on missing data: no URLs → still map, and say mismatch detection needs pairs.

Edge cases: single keyword → add 2-3 sibling queries; 2,000+ queries → top by impressions, say sampled; all branded → defend the brand SERP; all informational → rank by closeness to money terms.

### 5.4 Intent map output

```
INTENT MAP
Total queries: N | Informational n (x%) | Commercial n | Transactional n | Navigational n
Clusters: N | Mismatches: N

MISMATCHES
QUERY CLUSTER: ... | CURRENT PAGE: url (type) | THE PROBLEM: ... | THE FIX: change page type / retarget / build right page and retarget this one

UNCOVERED CLUSTERS
CLUSTER: name - queries - intent - AI-answer or click
BUILD: content type + working title

COVERED AND CORRECT
...

DO THIS WEEK (top 3)

WHAT THIS DID NOT CHECK
SERP layouts, volumes, difficulty. Check the live SERP for the top 3 clusters before building.
```
Quantify ("31 queries, 9 clusters, 4 mismatches, 3 uncovered clusters") and be decisive ("Build a comparison page titled X"). Always give content type plus working title, never a label alone.

---

## 6. Clustering keywords into pages

### 6.1 Rules

- **One keyword is not one page.** Engines rank pages for groups of shared-intent queries (a page targeting a 100-search keyword can rank for ~1,300 keywords and ~2,000 visits).
- **One cluster = one page.** Never two pages for one intent (cannibalisation) or one page for two intents (ranks for neither). "A cluster with 30 keywords across three intents is really three clusters."
- Finish ~90-95% of keyword research before building: the map decides structure, prevents duplicate pages and makes on-page work possible.
- Intent-only clustering works; volumes and current ranking URLs sharpen it.

### 6.2 SERP overlap (the grouping test)

Group by intent guess first, then verify within each candidate cluster by counting shared top-10 URLs between two keywords:

| Shared top-10 URLs | Decision |
|---|---|
| 7-10 | Must be the same page |
| 4-6 | Should be the same page |
| 2-3 | Separate pages, interlink heavily |
| 0-1 | Must be separate pages |

Any pair over 70% overlap on separate pages is a cannibalisation risk. Entity mapping (people, products, concepts, organisations) confirms boundaries.

### 6.3 Own page or merge (volume thresholds)

| Volume/mo | Decision | Condition |
|---|---|---|
| 100+ | Own page | Enough demand |
| 10-99 | Check competitors | 2+ competitors with dedicated pages → own page; 0-1 → merge |
| < 10 | Merge | Section or paragraph on a related page |
| Any | Own page (override) | A core service you actively sell |
| Any | Own page (adjacent depth exception) | Medium/High Knowledge Graph importance adjacent topic the persona expects; cap 1-2 articles, explain in the Depth column |

A "dedicated page" means the slug contains the attribute AND the page is mainly about it; a mention on a broader page does not count; word count is only a cue. Depth calibration: whole page = very important; paragraph = related secondary; sentence = tangential; very distant = skip.

**Volume honesty.** Use volumes only when actually seen (tool, web search, user paste). GSC impressions are not search volume: keep them in their own "GSC impressions" column with the date range, never in Search Volume, never for these thresholds. With no data write "no data", never an estimate. Relative labels from SERP signals are allowed only when labelled as estimates, kept out of the Search Volume column and out of the numeric thresholds: autocomplete or PAA presence → Medium-High; several major-publication articles → High; forum/Reddit only → Low-Medium; niche blogs only → Low.

### 6.4 Clustering output

Intake line:
```
Paste your keyword list. Include monthly search volume and, if you have it, current ranking URL for each keyword. If you only have the keywords, that is fine, I will cluster on intent alone. Tell me the site or topic so I can judge relevance.
```
For more than a few hundred keywords, ask whether to cluster all or a top slice by volume. Clean first (duplicates, near-duplicates, irrelevant terms; list removals).

| Cluster name | Primary keyword | Supporting keywords | Intent | Target page (existing URL or new + slug) | Priority |
|---|---|---|---|---|---|

Primary = highest volume or clearest intent. Two existing URLs on one cluster → consolidate into the stronger with a 301. Order by opportunity (volume vs how well the site already covers it). Close with cannibalisation risks and publishing order. Diagnosing live cannibalisation from GSC data is in measure-refresh.md.

### 6.5 Hub and spoke sizing

- Pillar = the broadest keyword (centrality, intent breadth, volume); one per seed; links to every spoke.
- Normal shape: 2-5 clusters per pillar, 2-4 spokes per cluster, 1 pillar + 5-15 spokes. A pillar with only 2-4 spokes is a small cluster: warn first.
- Every spoke has a unique primary keyword, unique H1 and title, a meta that does not repeat the same phrase, and 3+ relevant incoming internal links (the floor in onpage-schema-entity.md section 6.3). Spoke → pillar link in the first 3 paragraphs and again in the conclusion.
- Word estimates (pillar ~2,500-4,000, spoke ~1,200-1,800) are optional context only, never a gate.
- Template by intent: how to → how-to guide; what is → FAQ/knowledge page; best/top → listicle; X vs Y → comparison; review → product review; data → research page; code/tools → tutorial; opinion → thought leadership; expert quotes → roundup.
- Name clusters `Cluster <Letter>: <Theme> (<intent>)`. Get explicit approval before writing; a batch stops on the first quality failure (scaled-content-abuse risk).

Link counts, anchor mix and placement rules live in onpage-schema-entity.md.

---

## 7. Topical authority map and site architecture

It is not a keyword list and not a list of topics. It is a site architecture built around one central entity. Run it interactively with five checkpoints; never skip one. **Critical warning:** low-quality content in the map hurts the whole site. "If you cannot write a good article on a topic, leave it out."

Why it tends to work is a working theory (user data accumulates on a focused site, Knowledge Graph alignment, lower cost of retrieval), not a confirmed mechanism.

### Step 1: Central entity (Checkpoint 1)

The ONE thing the site is about, as a keyword. Test: "If Google gave this site a Knowledge Panel, what would the title be?" Format `[service or product] + [location or modifier]` ("family lawyer Sydney"; "online casino" for digital-only). Think in Entity-Attribute-Value (Michael Jordan → height → 1.98m). Confirm: entity, location, modifier (affordable, specialist, emergency, premium).

### Step 2: Source context and persona (Checkpoint 2)

Five questions: business type; location/market (note state or jurisdiction); unique angle; customer language (not business language); a 2-sentence Knowledge Panel description. The same niche gets different maps (casino affiliate vs operator vs tech provider).
**Persona** = a real author or reviewer with checkable credentials (public register, membership directory, licence number, profile). Never invent one; if nobody qualifies, recommend a real reviewer. The persona bounds what is credible (a scooter site needs 1-2 battery chemistry articles, not 100). This author persona is different from the reader/ICP persona (content.md).

### Step 3: Research (Checkpoint 3)

- **Knowledge Graph:** Wikipedia (section headings = attributes, related articles = adjacent entities, "See also" = close topics), Wikipedia graph visualiser `blinpete.github.io/wiki-graph`, `wikidata.org`, `dbpedia.org`. Topic distance: car accidents ~ car maintenance is CLOSE; car accidents ~ racing helmets is TOO FAR. Node importance (degree, eigenvector centrality, betweenness, closeness): the size of a topic on the site should roughly match its importance in the graph.
- **Competitors:** 3-5 sitemaps and folder structures, gaps (gaps = information gain), thin pages (easy to beat), About pages.
- **Client-situation map:** Persona | Situation | Services Needed | Related Topics. It drives both content and linking.
- **Six attribute sources, do them all:** (1) top 5 Google results (attributes on 3+ of 5 are mandatory); (2) PAA including 2-3 nested levels; (3) Wikipedia, plus legislation for regulated niches; (4) autocomplete sweeps; (5) the business's service list (each service = mandatory core page regardless of volume); (6) laws, regulations, standards (must be in the map). If a source is unreachable, say so and ask the user to paste it.
- Master list: # | Attribute | Source(s) Found | Intent Type | KG Distance | Notes.

### Step 4: Core vs AOR and merge/split (Checkpoint 4)

- **Core pages** = commercial/transactional: buy, hire, cost, near me, best, [service] + [location], [product] review.
- **AOR (area of relevance) pages** = informational: how to, what is, guide to, tips for, history of, vs, types of, examples of.
- Apply the thresholds in 6.3. Decision table: Attribute | Volume | Competitors w/ Page | KG Importance | Decision | If Merge, Into Which Page | Depth.

### Step 5: Folders

One folder per major topic; folder name = the root keyword only (`/divorce/`, not `/divorce-lawyer-sydney/`). Pick the root with a keyword tool, else customer/competitor language (say it is unchecked). Nest subtopics (WordPress: Pages with parent/child). Google learns structure mostly from links, not URLs; folders help organisation, analytics and, on sites over a few thousand URLs, change-frequency learning. Image URLs follow folders (`/family-lawyer-sydney/john-bale-family-lawyer.jpg`), alt text varies by page context.

### Step 6: Buyer journey (Checkpoint 5)

| Stage | Content |
|---|---|
| TOFU | problem, symptom, "what is" (most AOR pages) |
| MOFU | "best [service]", "[A] vs [B]", "[service] cost", "near me", how to choose, case studies. Where most sites have the biggest gap. |
| BOFU | "[brand] reviews", "[service] [location]", pricing, buy, book |
| Retention (optional) | existing-customer help |

Table: Page | Stage | Content Type | Target Keyword. Any stage with zero pages → flag.

### Step 7: Query expansion

PAA plus seven query types: definition ("what is"), instruction ("how to"), comparison ("vs"), reason ("why"), short fact ("cost/price"), boolean ("is it worth it"), consequence ("what happens if"), plus competitor H2s. Competitors have dedicated pages → own page; competitors use it as an H2 → H2; nobody covers it → H2 (information gain). New pages → re-run Step 4.

**Cost of retrieval score /10** (editorial heuristic): 10 = every heading maps to a query, every paragraph answers a question, every image could rank, title/H1/URL/meta reinforce one keyword, a snippet-liftable answer exists; 1 = generic headings ("Our Services"). Concise answers deep in an article can still rank (passage ranking).

### Step 8: Linking architecture

Topical-map linking rules (AOR/Core table) and the reader-relevance test: `onpage-schema-entity.md` section 6.3. Output table: Source Page | Target Page | Anchor Text | Placement | Link Type | Reader Relevance Check. Anchor mix and placement detail: onpage-schema-entity.md.

### Step 9: Central entity sitewide

Sitewide central-entity template: `onpage-schema-entity.md` section 4.2.

**Optional NLP category check** (diagnostic only, not a ranking test): Google Cloud Natural Language API `classifyText`; V2 categories need `"classificationModelOptions": {"v2Model": {"contentCategoriesVersion": "V2"}}` (e.g. `/Law & Government/Legal` in V1, `/Law & Government/Legal/Family Law` in V2). Investigate category drift before rewriting.

### Step 10: Briefs

First 30 articles get the full 17-field brief: Page Title, Target Keyword, URL Slug (`/folder/keyword/`), H1, Title Tag (keyword in the first five words, no length target), Meta Description (keyword + reason to click up front, no length target), Buyer Stage, Word Count (rough, competitor-relative), H2 Sections (each an expanded query), Internal Links Out, Internal Links In, Entities to Mention, Information Gain Angles, Image Requirements, CTA, Persona Angle, Client Situation. Articles 31-90 get a light brief: Title, Keyword, Slug, Stage, one-line scope, Links to (Core). Writing the pages: content.md.

### Deliverables

Spreadsheet (no file tools → each tab as a CSV code block):
1. **Core Pages** (12-20 rows): Page Title | URL Slug | Folder | Target Keyword | Search Volume | Buyer Stage | H1 | Title Tag | Meta Description | Competition Level
2. **AOR Pages** (60-80 rows): same + Links To (Core)
3. **Linking Map:** Source | Target | Anchor | Link Type | Placement | Reader Relevance
4. **Buyer Journey:** cell colours light yellow TOFU, light blue MOFU, light green BOFU, light grey Retention
5. **Publishing Order** (90 rows): Week | # | Page Title | Cluster | Target Keyword | Buyer Stage | Brief Link | Notes

Plus a strategy document covering each step above, the off-site plan and quality standards. Hand-off: read Core → AOR → Linking → Buyer Journey → Publishing Order; "treat the 12 weeks as a plan, not a ranking forecast". Review the map quarterly (predicates like "install" or "setup" can split into separate intents after core updates).

---

## 8. Prioritisation

1. **Fix blockers first** (crawl, index, wrong-intent core pages).
2. **Money pages first:** product, service, pricing, feature, location; one per core offer.
3. **Intent mismatches next:** demand already exists.
4. **Update page-2/3 pages** before writing new ones: often the quickest win (striking distance in measure-refresh.md). Refresh with real changes, not date-only edits (date-only changes are detected); refresh anything important older than ~6 months.
5. **One cluster at a time, attached to a money page, built bottom-up:** money ← commercial (best X, X vs Y, alternatives) ← educational. Link down the funnel and sideways. Finish a cluster before starting the next.
6. **TOFU giants** (e.g. "contract template" 300k/mo) only with a free asset → email → nurture → signup path.
7. **Local:** service × city "zipper" pages, tens not thousands, each genuinely local; reuse the best-converting layout ("a 20% conversion page beats more traffic").

Score by impact ÷ effort; every recommendation ends as a concrete action (page, keyword, file, fix).

---

## 9. New-site plan and publishing ramp

### 9.1 Order of work

1. **Crawl, index and technical basics first:** indexable pages, fast hosting, SSL, mobile, sitemap submitted to GSC and Bing (technical.md).
2. **Keyword research and topical map** (sections 4-7), ~90-95% done before building.
3. **Content:** pages that beat the top 3 (content.md).
4. **On-page** per page (onpage-schema-entity.md; `onpage_check.py` FAILs only on keyword in title and a missing internal link; everything else is WARN).
5. **Links last:** plan pages to rank with foundational links only (profiles, citations, GBP, relevant directories = legitimacy, not ranking power); serious outreach after the first 10-15 great pages, from month 3 (offsite-authority.md). Links are the most expensive lever and good research reduces how many you need.

New domains: NAP consistency and first-100-words alignment pay off immediately; topical focus and authority compound from a body of work.

### 9.2 First 30 days

This is the master SEO plan; the AEO track (`ai-visibility.md` section 12) and the technical implementation track (`technical.md` section 12) run alongside it.

| Week | Work |
|---|---|
| 1 | GSC + Bing Webmaster Tools + GA4; 10-15 sweet-spot keywords; intent test on the top 5; list money pages. Local: claim and fill GBP, collect and answer every review. |
| 2 | Ship the #1 money page. |
| 3 | First cluster piece + refresh page-2/3 pages. |
| 4 | Promote (15 min/day on journalist request platforms), check AI visibility, read GSC early signals (impressions up, new queries, position 5 → 3), plan the next cluster. |

### 9.3 Twelve-week publishing order (topical map sites)

| Weeks | Wave | Volume |
|---|---|---|
| 0 | Foundation: homepage with entity, core pages live, About with real author, Contact; fix broken core pages now (wrong intent, thin, not indexed) | core set |
| 1-6 | AOR wave | 30 articles, 5/week |
| 7-10 | MOFU wave (buyer guides, X vs Y, case studies, pricing explainers) | 40 articles, 10/week |
| 11-12 | Core optimisation (big core rewrites, new BOFU, retention) | 20 |

Total 90. Pace 5-10/week, governed by quality, not the calendar.

### 9.4 Cadence rules

- New sites ramp: day 1 → 1 post, day 2 → 1, day 3 → 2, day 5 → 3, day 8 → 4, then steady. Never dump hundreds of pages at once.
- After publishing: GSC URL Inspection → Request indexing (~10/day limit); submit `/sitemap.xml`.
- Track with the publish-and-track fast loop in content.md Step 10 (daily incognito + VPN check, day-3 compare, "out of 5 pages, maybe 3 rank").

---

Not covered here: international/hreflang keyword research, multilingual intent, non-Ahrefs volume sources beyond the fallbacks above, programmatic pages beyond the local zipper.
