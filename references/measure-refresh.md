# Measure and refresh

How to get trustworthy search data, read it, find the cheapest wins, track movement, catch decay and cannibalization, diagnose core-update drops, measure local and AI traffic, and report to owners and boards. Writing titles, meta descriptions and links lives in `onpage-schema-entity.md`; AI prompt rounds and citation share live in `ai-visibility.md`; crawl, index and Core Web Vitals live in `technical.md`.

## Ground rules for every measurement task

- **Search Console is the source of truth.** You cannot see live SERPs; scraped rankings are noise. GSC average position comes from real impressions.
- **Own data beats industry averages.** Clicks fall off steeply by position and AI Overviews take clicks even on page 1, so generic CTR curves mislead. Benchmark against the site's own CTR at similar positions. Placeholder numbers are allowed only when data is thin, always labelled "placeholder, not a benchmark".
- **Use only numbers in the data you were given.** Unknown date range: ask, or say "for the period you exported". Missing sections are marked `SKIPPED` or `Not checked`, never estimated.
- **A trend needs two points.** One export = where you stand. Two equal periods = heading. Never fake a trend from one export.
- **Equal periods, same filters.** Flag periods that differ by more than a day or two; unequal periods corrupt every comparison.
- **Weight by impact, not count** (impressions or absolute clicks). Ignore noise: position 12 with 3 impressions, or 5 clicks falling to 3.
- **Every change gets a re-check date** (calendar in section 13). "A baseline without a re-check date is a screenshot, never a tracker."
- **Directions, not forecasts.** Never promise a position or a recovery timeline. End every report with `WHAT THIS DID NOT CHECK`.

## 1. Set up Search Console

If the user has no GSC, walk them through this. If they paste data, skip to section 3. If the request is vague, ask two questions:

```
1. Do you have Google Search Console set up for your website? (Yes / No / Not sure)
2. Can you paste any data from it, or would you like me to explain what to look at?
```

| Step | Action | Time |
|---|---|---|
| 1 | Go to search.google.com/search-console, sign in with the business Google account | 30 sec |
| 2 | Add property: "URL prefix" + full URL. (A Domain property covers every version but needs a DNS record.) | 30 sec |
| 3 | Verify. One-click via Google Analytics (needs Edit access on the GA property, tag in head) or Google Tag Manager (Publish/Admin on the container, the `<noscript>` part right after the opening body tag). Otherwise paste the HTML tag into the head. Wix, Squarespace and WordPress SEO plugins have a box for it. Shopify: Online Store > Themes > Edit code > theme.liquid, new line just below `<head>`. | 2-3 min |
| 4 | Click Verify | 10 sec |
| 5 | Wait 2-3 days for data | |

Also set up Bing Webmaster Tools: the same two-export methods in this file work there, and Bing feeds ChatGPT and Copilot answers. Bing's AI Performance report (citation share by grounding query) is read in `ai-visibility.md`.

## 2. Export recipes and data pitfalls

### Which export for which job

| Job | Export | Range |
|---|---|---|
| First look / weekly habit | Performance (Search results) > Queries table, plus Pages if possible | Last 3 months |
| Striking distance, cannibalization | Query AND page on the same row (see below) | Last 28 days or 3 months |
| Low-CTR pages | Pages tab, with a Query filter "not containing [brand name]" added before export | Last 3 months |
| Rank tracking | Queries tab, two equal periods (current + prior) or the Compare export | 7 days each for fast-moving sites, 28 days each for most |
| Content decay | Pages tab, two equal periods: recent (e.g. last 3 months) vs same period a year ago (or at least 6 months back) | |
| Core update | Date > Compare: pre-rollout window vs post-completion window, Pages then Queries | 3 weeks each side |
| Internal links baseline | Pages tab with Average position ticked | Last 3 months |

**Query and page on the same row.** The standard UI export splits them. Options: the free Search Analytics for Sheets add-on (group by query and page), Looker Studio with the Search Console connector (URL impression table, dimensions Query + Landing Page), SEOGets or any GSC-API tool, or by hand: filter Performance to one page and export its Queries tab (repeat per top page), or filter by one query and open the Pages tab. Minimum columns: query, page, clicks, impressions, position (CTR optional; compute clicks / impressions).

**Third-party exports** (Ahrefs, SEOtesting CSV): map the columns. No position column: the analysis cannot run, ask for a re-export. Relative paths: ask for the domain.

### Pitfalls to state in every report they touch

- **1,000-row UI cap.** "Total keywords" means keywords in the export. A URL present in only one of two capped exports is **unknown, never zero**: exclude it from loss totals, list it separately, ask for a page-filtered check or API pull. Report how many URLs matched.
- **16-month retention.** "Last 6 months vs the same 6 months a year ago" does not fit. Data exists only from when the property was added.
- **Lag.** Final data ~2-3 days behind.
- **Average position is an average** across all impressions, delayed, Google-only, and shows no competitor positions.
- **Average-position artifact.** Position "drops" while impressions jump = shown on more, lower results. Say so explicitly.
- **Branded vs non-branded.** Pages exports mix both. Use the Query filter "not containing [brand]", GSC's built-in **Branded** filter (top-level properties with enough impressions only; Google's classification is AI-based), or a regex (the API supports `excludingRegex`). Mostly-branded data needs a different fix (knowledge panel, brand entity, sameAs; see `onpage-schema-entity.md`).
- **AI features.** AI Overviews and AI Mode clicks and impressions are counted inside the normal Performance report, and cannot be isolated there. The separate Generative AI performance reports (Search: AI Overviews + AI Mode; and Discover) show impressions, pages, countries, devices and dates only, no queries or clicks, and have no API. Point to the UI.
- **Known data anomalies.** Check Google's data-anomalies page before blaming an update. Logged: a logging error affected impressions, CTR and average position (not clicks) from **13 May 2025 to 27 April 2026**; the `&num=100` parameter was dropped **mid-September 2025**, so impressions fell and average position improved while clicks held steady; Aug 13 (2026) Discover logging defect; Aug 13-17 (2026) gen-AI Search report impressions, restored Aug 21. Judge any decline that spans those dates on **clicks**.
- **URL variants.** http/https, www/bare, trailing slash, case and query strings can make one page look "dropped" in one export and "new" in the other. Normalize copies before comparing.
- **API row limit.** The Search Analytics API returns at most **50,000 rows per day per search type**, sorted by clicks. A page missing from an API pull is `needs_validation`, not `dropped_out`, unless filters, row limits and dimensions are identical and URL Inspection confirms it.
- **Huge exports** (over 5,000 rows for striking, 10,000 for cannibalization): sample the top 2,000 by impressions and say so.

## 3. Read the data and run the weekly habit

**First read of a pasted export:** a 2-3 sentence overview, then:

| Metric | What it means | Your number | Verdict |
|---|---|---|---|
| Total keywords | Rows in the export | | |
| Top keyword clicks | | | |
| Average position | 1 = top, 50 = page 5. Use GSC's figure or "simple average of the listed keywords" | | |
| Keywords in top 10 | Count of position ≤ 10 | | |

**The weekly 10-minute habit (every Monday morning):**

1. **Performance > Queries.** Are the top 5 by clicks relevant to the business? High impressions + low clicks = title/description problem (section 5). Unexpected new keywords = opportunities.
2. **Performance > Pages.** Top 5 = money pages, keep them updated. High impressions + low clicks = rewrite the title. Drops vs last week: Date filter > Compare tab.
3. **Performance > Countries.** Is traffic coming from the country you serve? Odd countries = wrong audience.

End each section for a beginner with a "What to do right now" line. Explain jargon on first use.

## 4. Striking distance

Queries just below the top 3 with real impressions are the cheapest gains.

### The band

| Range | Tier | What it is | Typical lever |
|---|---|---|---|
| 4-10 | Tier 1 | Page-one CTR quick wins | Title/meta, then on-page |
| 11-15 | Tier 2 | Page-two rank pushes | On-page depth + internal links |
| 16-20 | Watchlist (separate, unscored) | Trend list for rank tracking | Watch; promote rows into the band as they move |

The canonical band is **4-15**. Positions 16-20 never get scored; they go on the watchlist. Some scripts use a narrower 4-10 cut with impressions > 50 (top 200 rows by impressions, max 20 rows, labelled "Position 4-10 with high impressions - small ranking improvement yields significant traffic gain"); treat that as the Tier 1 view only. Impression thresholds depend on site size: prefer relative scoring with a noise floor (reject impressions < 5) over a fixed cut.

### Intake

```
To score these properly I need query AND page on the same row. The standard Search Console
export splits them, so use the Search Analytics for Sheets add-on, Looker Studio (Query +
Landing Page dimensions), any Search Console API tool, or filter Performance to one page and
export its Queries tab for each top page. Last 28 days or 3 months. Minimum columns: query,
page, clicks, impressions, position (CTR optional, I will calculate it).
```

A plain Queries export is accepted: score the queries, then ask which page owns each top one. Push back if columns are missing.

### Full method (query + page data): lift score

1. Parse. CTR given as "3.2%": convert. Missing CTR = clicks / impressions. Reject rows with position > 100 or impressions < 5.
2. Compute `target_ctr` from the **full** export first (the band filter removes positions 1-3), then keep `4 ≤ position ≤ 15`.
3. Score:

```
Lift Score = impressions × (target_ctr - current_ctr) × position_weight

target_ctr: site's own median CTR for non-branded rows at positions 1-3 (full export),
            if ≥20 such rows; else placeholder defaults 11% non-branded informational,
            7% commercial ("ranking weights, not measured benchmarks").
current_ctr: row CTR or clicks/impressions. Only if there is no clicks column:
            pos 4 ≈6%, 5 ≈5%, 6 ≈4%, 7 ≈3%, 8-10 ≈2.5%, 11-15 ≈1.5%.
current_ctr ≥ target_ctr → score 0 (the gain is rank, not CTR).
position_weight: 4=1.0, 5=0.95, 6=0.90, 7=0.85, 8=0.80, 9=0.75, 10=0.70, 11-15=0.55
```

State which `target_ctr` was used in the header.

4. Group by landing page, sum lift scores, sort descending, keep the top 10 pages.
5. Before scoring a page, check the query is not ranking with two of the site's pages (section 8). A split query corrupts both pages' scores.

### Quick method (no page column, or a beginner): terciles

Table `| Keyword | Position | Impressions | Clicks | CTR | Opportunity |`, sorted by impressions descending, scored relative to the site's own striking list:

- **HIGH:** position 4-10 AND impressions in the top third of the striking list.
- **MEDIUM:** position 4-10 with lower impressions, OR position 11-15 with top-third impressions.
- **LOW:** position 11-15 with low impressions, OR an off-business keyword.

Fewer than 5 keywords in 4-15: say so, do not pad.

### Per-page action block

```
PAGE: [URL]
PAGE TOTAL LIFT SCORE: [number]
TOP STRIKING-DISTANCE QUERIES (up to 5):
1. "[query]" - position [X], imp [Y], score [Z]
THEME: [one sentence]
ACTION 1 - TITLE TAG TWEAK: Current title (or "fetch the page to see") / Proposed title
  [top 1-2 queries, verbatim] / Why
ACTION 2 - META DESCRIPTION (if the title alone won't move it): primary query + reason to
  click in the opening words
ACTION 3 - ON-PAGE ADDITION: concrete, e.g. "Add an H2 'Step-by-step process' with a
  200-word how-to that uses the query naturally." Not "improve content".
ACTION 4 - INTERNAL LINK: a specific same-site page linking TO this one, descriptive anchor
  containing the query
Expected lift if all 4 actions ship: from position [current avg] toward position [3 or top
half of page 1]. (A direction, not a forecast.)
```

Write the title and meta using the formulas in `onpage-schema-entity.md`. Rules that apply here:

- Never invent queries, pages or current titles. Internal links only FROM pages known to exist; otherwise "from the relevant hub page".
- No keyword stuffing. If the query is already in the title, adjust ordering or prominence. Use the query naturally in body copy, not a set number of times.
- Anchors: descriptive, query-containing, varied; not the same exact phrase on every link.
- Title tweaks first: 30 seconds of work, and CTR can show once the page is recrawled, "often within a couple of weeks". Google sometimes rewrites titles, so check the live SERP. On-page changes second.
- A page with 5+ striking queries is a content cluster opportunity: flag it.
- Mostly branded data: flag it (brand queries need entity work, not title tweaks).

### Report

```
STRIKING DISTANCE REPORT
Date range: / Total rows analysed: / Rows in striking distance: /
Total pages with striking-distance queries: / Target CTR used:

TOP 10 OPPORTUNITY PAGES            (per-page blocks above)
ALSO WORTH NOTING                   (pages 11-20: page, score, top query, one-line action)
QUERIES IN STRIKING DISTANCE WITH NO PAGE MATCHED   (ask the owner which page)
WATCHLIST (positions 16-20, unscored)
QUICK WINS THIS WEEK                (top 3, smallest effort for biggest lift, usually title swaps)
WHAT THIS REPORT DID NOT CHECK
- Whether the content deserves top 3 (information gain: see content.md)
- Off-site factors
- Intent mismatch (a no-click query may be intent-mismatched)
- Seasonality (run monthly)
```

**Beginner action plan (pick 3-5):** fix titles on high-impression, low-click pages; answer the query more fully (details, examples, not word-count filler); relevant internal links to each striking page (floor 3+, `onpage-schema-entity.md` 6.3); update slipping content; new pages for impression gaps with no dedicated page.

## 5. Low-CTR pages (detection only)

Find pages earning impressions but not clicks, then hand the rewrite to `onpage-schema-entity.md` (title formulas, rules, CMS steps).

**Intake (one message):** (1) GSC Pages export, last 3 months, clicks/impressions/CTR/position, ideally with a Query filter "not containing [brand name]" added before exporting (Pages mixes branded and non-branded); a per-page Queries export is a bonus. (2) Or URL + target keyword. (3) Brand name, plus location if local.

**Detection rule:**

1. **Best test:** compare each page's CTR with the site's own typical CTR at a similar position in the same export. Flag the outliers.
2. **Thin-data fallback (labelled placeholder):** below 5% at positions 1-3, below 3% at positions 4-10.
3. Unfiltered data: say brand effects were not assessed; treat homepage and About pages with caution.
4. **Cause discipline:** AI Overviews and other SERP features can depress CTR. Name one as the cause only if the user saw it in live results; otherwise write "cause unverified".
5. Fetch each flagged page (title, meta description, H1, first 100 words). Cannot fetch: ask the user to paste. Never guess a current title.

**Show the upside as a scenario on real impressions:** "If your CTR went from 2% to 5% on 4,000 impressions, that would be 200 clicks instead of 80."

Re-check with a GSC Compare of equal periods once the page has been recrawled (couple of weeks), and again at 28 days.

## 6. Rank tracking

**Intake (verbatim):**

```
Paste two Google Search Console query exports covering the same length of period: the
current period and the one before it (7 days each for fast-moving sites, 28 days each for
most sites). In GSC: Performance, set the date range, open the Queries tab, export, then
repeat for the prior range. Columns needed: query, clicks, impressions, position. If you have
priority keywords you care about most, list them and I will report those first.
```

One period only: baseline table, then show how to pull the second export. GSC's Compare export (both periods side by side) works directly. A one-off diagnosis can use 3 months.

**Classes (per matched query):**

| Class | Rule |
|---|---|
| BIG WIN | Improved 3+ positions, or entered top 10 |
| WIN | Improved 1 to under 3 |
| FLAT | Moved under 1 either way |
| SLIP | Dropped 1 to under 3 |
| BIG SLIP | Dropped 3+, or left top 10 |
| NEW | Impressions now, none prior |
| LOST | Impressions prior, none now |

**Diagnose movers:**

- Position moved, impressions steady: genuine rank change, investigate the page.
- Position "dropped" while impressions jumped: average-position artifact. Say so.
- Impressions collapsed at a stable position: demand shift or SERP layout change, not rank.
- NEW at position 40+: discovery noise unless impressions are real.

Rank movers by current-period impressions; never list a low-impression mover above a high-impression one. Report priority keywords first, including flat ones ("Silence on a priority keyword reads as hiding"). Caveats are never empty on a busy site.

```
RANK TRACKING REPORT: {site}
Periods compared: {prior range} vs {current range}
PRIORITY KEYWORDS (if provided)
| Keyword | Position | Change | Clicks | Impressions | Verdict |
TOP MOVERS UP (by impressions)
| Query | Position | Change | Impressions | Read |
TOP MOVERS DOWN (by impressions)
| Query | Position | Change | Impressions | Read |
NEW AND LOST
WATCHLIST (positions 16-20, unscored, ranked by impressions)
CAVEATS THIS RUN
NEXT CHECK {the date one full period from now, and what to re-export}
```

Watchlist rows that move into 4-15 with real impressions feed the striking-distance run (section 4).

## 7. Content decay

Decay is a trend, never a snapshot. Two stages: **screen** to surface candidates, **diagnose** to prescribe.

**Intake:** two GSC Pages exports of the same length, recent (e.g. last 3 months) vs the same period a year ago (or at least 6 months back), or the Compare tab. Columns: page, clicks, impressions, position; queries for the worst 2-3 pages sharpen the diagnosis. One period only: rank pages by weakness, give no decay verdict. Mind the 16-month and 1,000-row pitfalls (section 2).

**Windows.** Adjacent periods (quarter over quarter) are fine for short-term screening; a year-over-year comparison of the same length, filters, search type, device, country and property is required before calling anything seasonal. Check the Google Search Status Dashboard for overlapping updates.

### Screen

Flag pages whose clicks (default metric; also review impressions, CTR, position, query+page pairs, device, country, search appearance) fell by 20% or more:

| Drop | Severity |
|---|---|
| 20-39.9% | Warning |
| 40-59.9% | High |
| 60%+ | Critical |

"The 20% quarter-over-quarter rule is a screening heuristic, not a Google threshold and not evidence that a page decayed" (seasonality, updates, tracking changes, URL changes and small-baseline noise all trigger it). Ignore tiny baselines.

### Diagnose

Diagnose pages with **clicks down 25%+** and real prior traffic (default floor **20 clicks** in the earlier period; lower it for small sites and say so).

| Diagnosis | Evidence |
|---|---|
| FRESHNESS DECAY | Position slipping slowly, impressions stable-ish; SERP rewards newer pages |
| COMPETITIVE DISPLACEMENT | Position dropped in steps, impressions stable |
| INTENT SHIFT | Position and impressions steady, clicks/CTR collapsing (query meaning changed, or a SERP feature or AI Overview answers it). Hypothesis only: check queries and the live SERP before prescribing |
| DEMAND DECAY | Impressions falling across the query set at a stable position. Not fixable by content. Page-level data cannot separate it from intent shift |
| SEASONAL | The year-ago period was the peak. "A Christmas-guide page in a July comparison is not sick." |

**One treatment per page:**

| Treatment | When |
|---|---|
| REFRESH | Freshness decay on a sound page: facts, dates, screenshots, missing subtopics, re-promote |
| REWRITE | Lost to a better competitor: rebuild against what ranks, keep the URL |
| CONSOLIDATE | Overlaps a stronger sibling: merge + 301 |
| RETARGET | Intent shifted |
| LEAVE | Seasonal or demand decay |

Never prune as the first move. Delete only when the page has no queries, no links and no salvageable overlap, and only after the merge option fails. Before any refresh, consolidate, redirect or prune, check indexation, canonical, query loss, internal links, backlinks, seasonality and business value. Never delete a page still earning impressions without checking consolidation.

**Prioritize by recoverable traffic** (prior minus current clicks), weighted to treatable diagnoses (freshness and displacement recover; demand does not). "Down 80% on a dead topic matters less than one down 30% on a growing one."

**Edge cases:** site under 6 months old: rank by underperformance instead. Everything declining evenly: a site-level event (update, migration, technical); run section 9 and the technical audit in `technical.md` first. Redesign or URL change in the window: unmeasurable. Thousands of pages: sample the top decliners. Brand queries decaying: a brand or reputation issue.

```
DECAY REPORT
Periods: / Pages analysed (matched URLs): / Decaying count: / Clicks lost: /
Recoverable share (estimate, with arithmetic):

THE SICK LIST
PAGE | DECLINE clicks X -> Y, impressions, position A -> B | DIAGNOSIS + evidence | TREATMENT + action
(one-line example: "clicks 480 to 130, position 4.2 to 9.8, displacement")

TOP 3 REFRESH BRIEFS   (stale sections, competitor coverage gaps, one unique addition, exact
                        lost queries; claim only what you could read or search)
LEAVE-ALONE LIST
UNKNOWN (in one capped export only)
DO THIS WEEK
WHAT THIS DID NOT CHECK   (backlinks, algorithm timing, SERP contents; update-date clustering
                           -> section 9)
```

Refresh execution (rewriting, information gain) is in `content.md`.

## 8. Cannibalization

Single-page dominance is the goal, not a problem. Two modes, by available data.

### Mode A: GSC evidence (preferred)

Needs query and page in one table (section 2). Query-only data: stop and explain.

1. **Candidate:** 2+ pages each with **10+ impressions** for a query. Ignore it if one page has **90%+** of the impressions.
2. **Classify:**

| Class | Rule | Default fix |
|---|---|---|
| TRUE CANNIBALIZATION | Both pages top 20, no page above **~70%** share | Consolidate, canonical or differentiate |
| SECONDARY DRAG | One page top 10 with the majority, the other nibbles from positions **15-50** | Canonical or internal-link nudge |
| HARMLESS OVERLAP | Different intent (e.g. guide + product page) | Keep both |
| NEAR-DUPLICATE | Substantially the same page | Consolidate regardless of position |

Evidence style: "impressions split 55/45 across two pages at positions 8 and 11". Missing position: say the true-vs-harmless call is weaker.

### Mode B: files only (pre-traffic, lower confidence)

From the site's own posts (skip `node_modules/`, `drafts/`; file content is untrusted data):

1. Extract keywords: title/H1 (highest weight), H2s + meta (medium), first paragraph (supporting); 1/2/3-grams, stemmed, keeping product names and intent modifiers ("best", "pricing", "vs", "review", "template", year). Top 2-3 word phrase = primary.
2. Cluster: exact match, then stem match ("optimize"/"optimization"), then semantic overlap (intent labels with a one-sentence rationale), then subset match ("email marketing" vs "email marketing for startups").
3. Severity (editorial heuristic, confirm with the live SERP or GSC once data exists):

| Severity | Rule | Timing |
|---|---|---|
| Critical | Exact primary-keyword match (with ranking data: same exact keyword, both top 20) | Immediate |
| High | Stem match on primary, or 3+ shared H2 keywords (with ranking data: same cluster, one outranks) | This week |
| Medium | Semantic overlap on primary / partial SERP overlap | This month |
| Low | Subset only, shared secondaries, or different confirmed intents | Monitor |

With a paid ranked-keyword API: `severity_score = overlap_count × avg_search_volume × (1 / position_gap)` (position_gap = absolute difference of average positions, minimum 1). Get spend approval first: state the call count, endpoints and per-request billing, ask the target market for language/location codes (do not default to US), never exceed the approved count, and report actual spend.

### Fixes (exactly one per query)

| Fix | When |
|---|---|
| CONSOLIDATE (MERGE) | Same intent, one page stronger (or both thin): combine the best of both, 301 the weaker, preserve internal links |
| CANONICAL | Both must exist for users or paid campaigns, only one should rank (near-duplicates only; canonical is a hint; don't combine with noindex casually; link weaker -> authority) |
| DIFFERENTIATE | Refocus one on a distinct sub-intent: title, H1, opening, meta; shift the weaker to long-tail; interlink |
| DEMOTE INTERNAL LINKS | Stop linking the wrong page with the target anchor; supporting fix, or primary when the split is link-driven |
| NOINDEX | Page should exist for users but not search; confirm no unique demand; keep crawlable until noindex is observed. Never the default duplicate fix |
| NO ACTION | Document, monitor quarterly |

**Keeper** = better position, more clicks, stronger backlinks, best intent match; state why. 3+ pages: one keeper, consolidate or differentiate the rest.

**Edge cases:** branded queries (homepage + product page is legitimate, flag separately); pagination and parameters (`?page=2`, `?sort=`) are a canonical/parameter issue, not cannibalization; an export filtered to one page: ask for the full export.

```
CANNIBALIZATION REPORT
Date range: / Queries analysed: / Multi-page queries: / True cannibalization count:

TRUE CANNIBALIZATION (worst first by combined impressions)
QUERY / COMPETING PAGES (position, clicks, impressions) / WHY IT IS REAL / KEEPER / FIX /
EXPECTED RESULT (direction to check in GSC after 4-8 weeks, never a promised position)
SECONDARY DRAG
NOT CANNIBALIZATION
NEAR-DUPLICATE PAGES
DO THIS WEEK (top 3)
WHAT THIS DID NOT CHECK (content depth, backlinks per page, true intent, 301 equity)
```

Weight by combined impressions, not query count. Prevention for new clusters: `foundations-keywords.md`.

## 9. Core updates: winners, losers and update analysis

### Window hygiene

1. Confirm the rollout start and completion dates on the Google Search Status Dashboard (status.search.google.com). Check for overlapping confirmed updates and say if the window is mixed.
2. Wait at least one full week after completion.
3. Compare equal windows: e.g. for the May 2026 core update (rollout 21 May to 2 June 2026), 3 weeks before (30 April to 20 May) vs 3 weeks after (3 to 23 June), excluding the June 2026 spam update from 24 June. Most recent confirmed update at time of writing: September 2026 spam update (start Sep 24, complete Oct 8, global).
4. Separate Web, Images, Video and News. Separate small from large sustained drops.
5. Check the data-anomalies page (section 2). Dates alone do not prove cause; impact stays `PENDING_OBSERVATION` until data exists.
6. No quick fixes or mass deletion. "Wait for the next update" is not an action. Recoveries typically surface at the next core update; give no timelines.

### Classify pages

Intake: Pages export from the Compare view, then Queries. Minimum columns: page, clicks both periods, impressions both periods; position is a bonus.

1. Drop rows with < 10 impressions in both periods.
2. **WINNER:** clicks up 15%+ AND impressions or position improved. **LOSER:** clicks down 15%+ AND impressions or position declined. **FLAT:** everything else.
3. Rank by absolute click change. "A page that lost 400 clicks matters more than one that lost 80% of 5."
4. **Pattern scan before individual diagnosis:** same folder or page type (template), same intent type, same market mismatch (e.g. a .com.au site losing UK traffic), same format mismatch (text losing to video, tools, marketplaces). Never say "the site was hit" from < 10 affected pages.

### Fit test (top 10 losers by click impact)

The working framework: visibility shifts toward the source type that best fits each query's dominant intent, user market and expected result format. Authority alone no longer explains outcomes. Gains went to canonical reference brands, local-market entities and task-completion destinations; losses to forums, wrong-market domains and derivative layers that summarize instead of completing the task.

| Test | Question | Score |
|---|---|---|
| a. Source-type fit | What type does the SERP reward (canonical reference, official source, marketplace, local result, tool, video, forum)? Cannot search: ask, or mark UNCHECKED. "Never describe a SERP you have not seen." | Y/P/N/U |
| b. Task completion | Does the page complete the task? Derivative layers need a much stronger reason to exist | Y/P/N |
| c. Market fit | Local entity, currency, shipping, spelling, ccTLD/hreflang | Y/P/N |
| d. Format fit | Matches the expected result format | Y/P/N/U |

**Verdicts:** FIXABLE FIT GAP (1-2 NOs, a concrete fix shippable this month); WRONG SOURCE TYPE (stop investing, redirect effort); COLLATERAL FLAT (demand or SERP layout changed: watch, don't rebuild). For winners, name the common pattern: "The strategy is more of that."

**Edge cases:** one range only: ask for the comparison. Branded queries dominate: strip and re-run. All flat: say so. Aggregator or affiliate: be direct about the task-completion bar (marketplaces gained, derivative layers fell). Forum/UGC: forum visibility contracted in May 2026 (Reddit, Quora, StackExchange declined), format-led rather than quality-led.

```
WINNER OR LOSER REPORT
Window: / Totals: / Winners / Losers / Flat: / Net click change:
THE PATTERN (2-3 sentences, lead with this)
TOP WINNERS (≤5)
TOP LOSERS DIAGNOSED (≤10)
  PAGE / CLICKS before to after / TOP LOST QUERY /
  FIT TEST source-type [Y/P/N/U], task completion [Y/P/N], market [Y/P/N], format [Y/P/N/U] /
  VERDICT / ACTION
DO THIS MONTH (top 3)
WHAT THIS DID NOT CHECK (technical, links, seasonality, tracking; a migration or GSC property
change in the window invalidates the comparison: ask)
```

Warn whenever a window overlaps a rollout.

## 10. Local: Google Business Profile in GA4

Ask one question: "Have you already linked your Google Business Profile to Google Analytics? Yes or no." No: setup mode. Yes: report mode.

### Setup mode

1. **Prerequisites:** Editor or Administrator on the GA property AND Owner or Manager on the GBP. Without both the link cannot be created; tell them who to ask (whoever set up GA or verified the profile).
2. GA **Admin > Product links > Google Business Profile links > Link** > select profile(s) > review data sharing > confirm. One GA property can link several profiles. Link from a standard property (subproperties are not supported).
3. **Verify:** a "Google Business Profile" collection appears in Reports (only when a link exists). Missing after refresh = the link did not save. The integration is rolling out progressively: if absent, re-check Admin > Product links in a week or two.
4. **Warn:**
   - **DATA RETENTION 6 MONTHS**, regardless of the GA date range.
   - **MULTI-PROFILE DATA IS AGGREGATED** (summed, no per-location filter; use the native GBP dashboard per profile).
   - **NO CUSTOM EXPLORATIONS** (no explorations, comparisons or filters).
5. Remove a link: Admin > Product links > GBP links > three-dot menu > Delete (needs Editor/Admin).

### Report mode

Paste from Reports > Google Business Profile collection > metric cards (minimum metric + value; ideal: this vs previous period). Parse any of: Interactions, Website clicks, Calls, Directions, Messages, Bookings, Menus.

- Two periods: absolute + % change. One period: baseline, come back next month.
- **Action mix** = each metric / total interactions (a restaurant skews to menus and directions, a trades business to calls). Zero in an irrelevant metric (Menus for a plumber) is normal.
- **Flags:** any metric down 20%+; calls down while website clicks up (site link shown more prominently, or a call CTA lost); directions down with no seasonal reason (address or service area changed?); bookings at zero for a booking business (provider disconnected). Address changes lag: don't diagnose gaps within days of an edit.
- **Cross-check:** GBP website clicks should roughly track GA organic sessions landing on the homepage and location pages. If the profile link has UTM tags, match on those and say which you used.

```
LOCAL ACTIONS REPORT
Period: / Profiles linked: / Data source:
THE NUMBERS        | Metric | This period | Last period | Change |
ACTION MIX
FLAGS              (likely cause + the check to run)
DO THIS MONTH      (top 3, e.g. re-add the booking link, refresh photos, reply to reviews, post the offer)
RECORD THIS        (Google keeps only 6 months: export and log these numbers)
```

Repeat the 6-month warning in every report until they confirm they are logging. Say "across all linked profiles" on aggregated numbers. Plain words ("people asked for directions 240 times"): what changed, why, what to do. GBP optimization: `offsite-authority.md`.

## 11. Live data through Google APIs

Use APIs when credentials exist; otherwise fall back to pasted exports. Only on explicit request.

### Credential tiers (tell the user before running)

| Tier | Needs | Unlocks |
|---|---|---|
| 0 | API key | PageSpeed Insights, CrUX, CrUX History, YouTube, Cloud NLP |
| 1 | + OAuth client or service account | Search Analytics, URL Inspection, Indexing API |
| 2 | + GA4 property id (numeric, from Property Details) | GA4 Data API |
| 3 | + Google Ads developer token + customer id | Keyword Planner |

**Setup:** GCP project; enable the APIs you need (leave the Web Search Indexing API disabled for a blog); API key restricted to those APIs; service account with a JSON key, its `client_email` added in GSC Settings > Users and permissions at the **lowest** role (Restricted for Performance; Full only on a 403 for URL Inspection; never Owner); in GA4, Admin > Property Access Management, service account as Viewer. Keyword Planner volumes come back bucketed ("1K-10K") with no ad spend, and its competition is advertiser competition, not organic difficulty. Read-only scopes by default (`webmasters.readonly`, `analytics.readonly`); credential directory mode 700, files 600.

### Consent and cost gate (mandatory)

- Before the **first** call per session that reads account data (Search Analytics, URL Inspection, GA4, Keyword Planner), spends a small bucket (YouTube search, batch inspection), can bill (Cloud NLP) or writes (Indexing API, credential setup): name the call, the property/URL, the expected call count and the quota or cost basis, then wait for an explicit yes. Free reads (PageSpeed, CrUX on a public URL) only need the call named.
- No uncapped loops; stop on the first quota error. Report each skip in one line ("Google: no credentials, skipped CrUX").
- Never enable billing or make a paid request without explicit approval.
- Some helpers return an `error` field with exit code 0: parse the output and treat any `error` (including per item in batches) as a failure.

### Endpoints and quotas

| API | Endpoint and key facts | Quota |
|---|---|---|
| Search Analytics | `POST https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query`. Dimensions query, page, country (ISO alpha-3), device, date, searchAppearance; filter operators include `includingRegex` / `excludingRegex` (brand splits); rowLimit 1-25000 (default 1000) + startRow; dataState final / all / hourly_all. Default: 28 days ending 3 days ago, dimensions query,page | 1,200 QPM per site and per user; 40,000 QPM / 30M QPD per project |
| URL Inspection | `POST https://searchconsole.googleapis.com/v1/urlInspection/index:inspect` `{inspectionUrl, siteUrl, languageCode}`. Returns verdict, coverageState, indexingState, pageFetchState, lastCrawlTime, googleCanonical. After a correct canonical fix, treat it as pending re-evaluation for 14 days | 600 QPM/site, 2,000 QPD/site |
| GA4 Data API | `https://analyticsdata.googleapis.com/v1beta` runReport; organic filter sessionDefaultChannelGroup EXACT "Organic Search"; send `returnPropertyQuota: true` | 200K core tokens/day; 40,000 tokens/hour/property; simple report ~1-5 tokens |
| PageSpeed / CrUX | Usage and CWV thresholds: `technical.md` | PSI 240 QPM, 25,000 QPD; CrUX 150 QPM |
| Indexing API | Eligible pages only (below) | 200 publish/day |
| Cloud NLP / YouTube | NLP bills after 5,000 free units/month; YouTube search.list has its own 100 calls/day bucket | |

Backoff on 429/5xx: 1, 2, 4, 8, 16 s plus 0-500 ms jitter, give up after 5; honor Retry-After.

**Errors:** 403 Search Console: add the service account or raise it to Full (not Owner). 403 GA4: add it as Viewer. 404 Search Console: wrong property format (`sc-domain:example.com`, or a URL-prefix property's trailing slash). 404 CrUX: insufficient traffic, use lab data.

**Indexing API:** only for `JobPosting` pages or `BroadcastEvent` in `VideoObject` (livestream) pages. Blog posts are ineligible. Ask whether the page is one of those, get a second explicit yes, and never assert eligibility yourself. For everything else: URL Inspection > Request Indexing in the UI (quota-limited, about 10/day; reserve for important URLs).

## 12. Reporting and KPIs

Keep audit reports and progress reports separate.

**Baseline before any work:** GSC clicks and impressions, positions, conversions, indexed pages, Lighthouse/Core Web Vitals, AI visibility snapshot (from `ai-visibility.md`). Record it dated.

**KPIs, in order:**

1. Organic conversions
2. GSC clicks + impressions by page and query
3. Positions, including drops
4. Indexed pages / coverage
5. AI share of target prompts cited or recommended
6. Links and mentions (quality, not count)

Rankings alone are not a report. **Early signals in months 1-3:** impressions rise before clicks, new queries appear, pages move from page 5 toward page 3.

**Monthly report** (weekly for short engagements): baseline vs now, trend chart, what was done (live URLs), what moved and why, what dropped (honestly), next plan.

**Tracking workbook tabs:** Dashboard; Keywords (keyword | target URL | intent | position per month); On-page; Technical/Audit; Off-page; Content (page, cluster, publish date, refresh date).

### AI traffic in GA4

Check first for GA4's built-in **AI Assistant** channel (Reports > Acquisition > Traffic acquisition: Sessions, Key events, Total revenue). If the property lacks it, build a custom channel: Admin > Data display > Channel groups > Default Channel Group > ⋮ > Copy to create new > channel `AI traffic`, Source matches regex `chatgpt\.com|perplexity|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai|deepseek\.com`, placed ABOVE Referral.

AI traffic is always **a floor**: a third to two thirds of AI visits arrive with no source; Copilot lands in Direct; AI Overview and AI Mode clicks sit inside Organic; deep-landing Direct traffic is likely AI. Last-click undersells AI (a January answer can become an April form): show first-touch beside last-click. Full three-signal attribution: `ai-visibility.md`.

### The board slide: four gauges

Inputs: AI visibility round files (`ai-visibility.md`), GA4 Traffic acquisition CSV (skip `#` comment lines), GSC Performance with the Branded filter and totals; optionally Bing AI Performance, a rank tracker and the CRM. Ask for monthly SEO cost, paid spend and paid conversions.

| Gauge | What it shows |
|---|---|
| **Eligible** | Target keywords in the top 10 + share of voice vs the top rival; positions 4-15 = best opportunity list (section 4) |
| **Chosen** | Category citation share per assistant, site citation count, most-chosen competitor; Bing count in brackets. Never mix tracker numbers with manual-round numbers |
| **Arriving** | AI Assistant sessions beside branded clicks and Direct sessions; always labelled "a floor" |
| **Paying off** | Key events + revenue from Organic + AI Assistant, or CRM pipeline. Value per lead = average deal value × lead-to-close rate (labelled estimate). Organic CPA = monthly SEO cost ÷ organic key events; paid CPA = ad spend ÷ paid key events. First-touch beside last-click |

**Reading the gauges together:**

- Rankings up + citation share flat: nothing unique to quote; add information gain (`content.md`).
- Citations up + rankings flat: authority lags; work off-site (`offsite-authority.md`).
- Branded search up + rankings down: AI is building demand.
- Direct + branded rising with no paid brand campaign: possible AI recommendation; check the rounds (Direct also catches email, messaging and broken tracking).
- Traffic not converting: fix landing pages or key events.

**Template (example shape; every number comes from the user's data or is a placeholder):**

```
Search and AI, [Month YYYY]
Eligible: 14 of 40 target keywords in the top 10 (was 11); share of voice 9% vs [rival] 15%.
Chosen: named or cited in 11 of 42 ChatGPT category answers (was 7 of 42); our site linked
in 4; [rival] chosen in 18.
Arriving: 212 AI Assistant sessions (was 180), beside 1,140 branded clicks and 2,300 Direct
sessions. A floor: Copilot lands in Direct, AI Overviews in Organic.
Paying off: 31 organic and AI key events worth $46,500 (estimated value per lead); organic
cost per lead $180 vs paid $410.
```

Then three sentences: **what moved** (counts, e.g. 4 of 18 -> 7 of 18, with rounds held constant), **next quarter's one constraint** (the weakest gauge and the workstream that fixes it), **cost** (from the user, or "estimate, to confirm"). Say "moved after the change", never "because of it".

**Page-level 2x2** (citations × AI sessions, split at the median):

| | High AI sessions | Low AI sessions |
|---|---|---|
| **High citations** | Strategic Priority: use as the template | Evidence Asset: leave it |
| **Low citations** | Hidden Opportunity: tighten structure and credibility (tighter answers, named expert, stronger evidence) | Dead Weight: other workstreams or repurpose |

Single-digit counts make a placement provisional.

Label every number Observed / Inferred / Not checked with its source; never score Not checked as a fail. A fetch is a first look (missing ≠ absent); search is a sample, not a ranking; one before/after is not proof. Destructive advice (delete, merge, redirect, noindex, canonical) needs observed evidence in the same row; otherwise recommend the check.

## 13. Check-in calendar

| Change | Re-check | What to compare |
|---|---|---|
| Title / meta tweak | After recrawl ("often within a couple of weeks"), then 28 days | GSC Compare, equal periods, CTR at that position; check the live SERP for a Google rewrite |
| Internal links added | **14 and 28 days** after go-live | See `onpage-schema-entity.md` 6.2 step 8 |
| Cannibalization fix | **4-8 weeks** | Query's impressions consolidating on the keeper |
| Rank tracking | One full period from now (7 or 28 days) | The same export, same period length |
| Canonical fix | 14 days (pending re-evaluation until then) | URL Inspection googleCanonical |
| Site migration | Launch day, **+7, +14, +28** | Each vs the pre-launch baseline. Normal: movement in the first fortnight. Problem: steady decline past 4 weeks, sharp drop in indexed pages. Full plan in `technical.md` |
| Core update | ≥1 full week after rollout completes | Post-completion window vs equal pre-rollout window |
| GBP / local | Monthly | This vs previous period; log numbers (6-month retention) |
| Content decay | Monthly screen; YoY before calling seasonal | Equal periods |
| Striking distance | Monthly (seasonality) | Fresh export |
| New program | Months 1-3 early signals, then monthly | Impressions, new queries, page 5 -> 3, then clicks and conversions |
| AI visibility rounds | Never edit a prompt mid-series | Timing: `ai-visibility.md` section 11 |

## WHAT THIS FILE DOES NOT COVER

- Writing titles, meta descriptions, anchors and link placements: `onpage-schema-entity.md`.
- Prompt libraries, AI answer scoring, citation share and test-vs-control experiments: `ai-visibility.md`.
- Core Web Vitals thresholds, crawl/index diagnosis, migrations in full: `technical.md`.
- Not covered: GA4 conversion and revenue attribution setup for organic beyond the board-slide math; a statistical noise threshold for month-to-month changes; local rank grids.
