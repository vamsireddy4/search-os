# Audits: which one to run, how to run it, how to report it

Audits diagnose. Writing pages: content.md. Crawl, render, speed: technical.md. Schema, entity, authors, internal links: onpage-schema-entity.md. Links, reviews, GBP: offsite-authority.md. AI citation tracking: ai-visibility.md. GSC trends and core-update winners/losers: measure-refresh.md.

## 1. Router

Run ONE audit per pass. Asked for everything → run the most urgent fully and list the order for the rest ("Four shallow audits help nobody").

| User situation | Audit / mode | Inputs needed |
|---|---|---|
| "What does Google see on my site?", no customers from Google, quick plain-English check | Trust check, 3.1 | URL, or pasted homepage, About, one service page, page list |
| "Score my site", "Will my site survive AI search?" | Website score /25, 3.2 | URL, or homepage, service pages, content titles, short description |
| "What's my website missing?", absent from Google and AI answers, "Is this link offer worth taking?" | Leak diagnostic (desk / shelves / basement), 3.3 | Website, money page, optional linking-site URL; web search |
| "Why does competitor X outrank me?" | Competitor gap, 3.4 | Your URL, competitor URL, the search(es) they win |
| "What pages should I add?", content gaps | Gap finder, 3.5 | Page list + what / who / where; GSC Queries export optional |
| Local identity inconsistent | Ranking-laws Mode 1 NAP, 3.6 | NAP from footer, GBP, 3 directories |
| Bounce back to search, falling clicks on one page | Ranking-laws Mode 2 First 100 Words, 3.6 | Title, meta description, first 200 words |
| Content never ranks, site unfocused | Ranking-laws Mode 3 Focus + Information Gain, 3.6 | Niche sentence + last 10-20 URLs with summaries |
| Weaker-looking site outranks you sitewide | Ranking-laws Mode 4 Authority Compounding, 3.6 | Name, service, market, 2-3 internal data points |
| Grade a page like a quality rater, E-E-A-T, one page not ranking for a query | Quality rater OUR, 4.1 | URL + exact query; web search |
| "Is this helpful content?", page lost rankings after a core update, numeric grade | Helpful content 32 Q, 4.2 | Pasted page text, topic, site focus, YMYL flag |
| B2B, SaaS, ecommerce, local service or restaurant site audit | Vertical module, 5 | URL (3 pages) or the vertical's paste list |
| One category / collection page, faceted nav | Category audit, 6.1 | URL or paste, head term, platform, optional competitor |
| One product page, Product schema, AI shopping recommendations | Product audit, 6.2 | URL or paste, query or current title, vertical |
| Merchant Center, disapprovals, GTIN, Shopping titles | Feed audit, 6.3 | Feed export, diagnostics, platform, top 10 by revenue |
| Can an AI agent read and buy from my product page? | Agent-readiness 0-100, 6.4 | Accessibility tree or rendered HTML + raw source |
| Affiliate commissions look off, coupon extensions | Affiliate traffic audit, 7 | GA4 Traffic acquisition export (+ network payout report) |
| Site traffic dropped after a core update (GSC data) | Winner-or-loser | measure-refresh.md |
| Reviews: more, sorting into proof, sentiment, removal | Review modules | offsite-authority.md |

Symptom routing: local identity → Mode 1; bounce / falling clicks → Mode 2; never ranks → Mode 3, then a page grader on the worst page; worse site outranks → Mode 4 or competitor gap; "is this a real business to Google" → website score; beginner owner → trust check.

The four whole-site diagnostics overlap: trust check is the beginner subset, website score the most quantified (business model), the leak diagnostic the strictest on evidence, competitor gap the only head-to-head. Don't run two back to back without a reason.

## 2. Audit discipline (every audit)

- **Read or stop.** Unreadable page (paywall, login, bot block, JS empty shell) → stop, ask for a paste, label "rated from pasted content". "A guess dressed as a rating is worse than no rating."
- **Fetch vs paste.** Mode A fetch; Mode B stop and ask for labelled text using the audit's paste list. Fetch failure: "I couldn't fetch the page automatically. Please paste the homepage content here and I'll audit from that."
- **Never fabricate** content, page counts, trust signals, traffic, rankings, backlinks, DA, review counts, prices, GTINs or figures. Thin paste = scored thin, with what to add.
- **Label the unseen:** "not assessed" (unread), "not checked" (no data), UNVERIFIED (site-level fact), "provisional" (fewer than 3 pages read), "uncalibrated" (relevance without the SERP). Not linked from nav → "I couldn't find one", never "it doesn't exist".
- **Text fetches strip scripts:** structured data is "not checked", not "missing", unless you saw source. Raw source has none, rendered unchecked → "not found in the initial HTML; rendered markup not checked".
- **Quote the page; one decisive fix per finding; lead with the fix.** Specific, not generic ("Add a water-usage calculator that estimates monthly bills based on dwelling size and number of occupants", not "Add a calculator").
- **Patterns over pages; cap lists** (top 3 this week, top 5 for feeds). **Don't manufacture problems**; say what works. "Politeness that hides a problem costs them rankings."
- **Tie findings to the business outcome** (leads, trials, revenue, bookings, calls), not SEO metrics.
- **Leak / patent material** = what Google's systems can store, not confirmed weights. Never quote unpublished thresholds.
- **Diagnose vs write:** the leak diagnostic, quality rater and helpful content grade never produce copy; Mode 2 and the ecommerce optimizers rewrite.
- **Plain English**, jargon defined on first use, no em dashes. **Every report ends with WHAT THIS DID NOT CHECK**, then one next-step offer.

Common skeleton when an audit has no template of its own:

```
[AUDIT NAME]: [Business / page]
Site or page: [URL]   Date: [today]   Read as: [Fetched / Pasted]   Pages audited: [list]

VERDICT: [one line, biggest issue in business terms]

FINDINGS (most damaging first)
1. [Page]: [issue, quoted evidence] → [exact fix]

DO THIS WEEK
1.
2.
3.

WHAT THIS DID NOT CHECK
- [unread pages, missing data, out-of-scope layers + which file covers each]

[One next-step offer question]
```

## 3. Site diagnostics

### 3.1 Trust check (4 RAG scores)

Fetch homepage, About, 2-3 key service pages, main nav, /sitemap.xml (page count). Paste list: homepage full visible text, About, one key service or product page, page list / navigation, each under a heading like `### Homepage`.

| Score | GREEN | AMBER | RED |
|---|---|---|---|
| Topic Coverage | 15+ pages covering different aspects | 5-14 with some variety | under 5, or all say the same thing |
| Content Depth | most pages fully cover the visitor need with specifics | some substance, many generic | mostly stock / boilerplate or missing what the visitor needs |
| Site Structure | logical groups + clear hierarchy | some internal links, no clusters | isolated pages |
| Trust Signals | named team, credentials, reviews / testimonials, detailed About with history | generic (stock photos, no names, vague About) | none |

Depth = does the page do its job, not length (Google has no preferred word count; a portfolio or quick-answer page can pass). Never GREEN on assumption. One page only → score what's visible. Missing About → defer Trust. Cite named people and places found.

```
GOOGLE TRUST CHECK: [Business Name]
Website: [URL]
Date: [Today's date]
Analysis mode: [Fetched / Pasted]

WHAT GOOGLE SEES: [2-3 sentences]
WHAT'S MISSING: [2-3 sentences, gap between what the owner thinks the site says and what it reads as]

SCORES:
Topic Coverage:    [GREEN/AMBER/RED]: [...]
Content Depth:     [GREEN/AMBER/RED]: [...]
Site Structure:    [GREEN/AMBER/RED]: [...]
Trust Signals:     [GREEN/AMBER/RED]: [...]

BIGGEST GAP: [...]
FIX THIS WEEK: 1. 2. 3.
BOTTOM LINE: [one sentence]
WHAT THIS DID NOT CHECK: [...]
```

Owner voice, analogies welcome ("Think of your website like a shop front..."), fixes doable today.

### 3.2 Website score /25

Five factors winning sites share, from Cyrus Shepard's analysis of 400+ sites (Zyppy Signal, April 2026; Spearman correlations, directional). Cite it on first run; the scale, brackets and fixes are this card's own.

Read homepage, product / service / pricing, About, any tools / calculators / quizzes / configurators, 2-3 content pieces. Scale: 1 absent or hurting, 2 weak, 3 partial, 4 strong, 5 elite, a defensible moat. "Most real sites land at 2 or 3"; a 5 needs overwhelming evidence.

| Factor (correlation) | 5 | 3 | 1 |
|---|---|---|---|
| Offers a Product or Service (0.391) | clear offering, visible pricing, obvious path | buried or loosely tied | pure content / affiliate / display ads |
| Allows Task Completion On-Site (0.381) | calculators, configurators, booking, filters, interactive databases, downloadable tools, applicable original research | one basic interactive element, or a walkthrough without completion | read-only |
| Proprietary Assets (0.357) | original research, first-party data, UGC, exclusive interviews, proprietary databases, named-outcome case studies | some original perspective | anything an LLM could write from training data |
| Tight Topical Focus (0.250) | one subject "treated like an obsession" | core + 2-3 tangents | five+ unrelated subjects |
| Strong Brand (0.206) | recognized | interchangeable | nobody searches by name |

Brand signals: branded naming, social proof, press, founder visibility, cited research, community, merch. Estimate unless GSC branded clicks are pasted, and say so.

```
WINNING GOOGLE SCORE CARD
Site: [URL]
Date: [today's date]
OVERALL SCORE: XX / 25
Bracket: [At Risk 5-10 / Vulnerable 11-15 / Competitive 16-20 / Winning 21-25]

FACTOR-BY-FACTOR
[Factor]: X/5, [Verdict], Evidence: [2-3 things]

WHERE YOU'RE LOSING
[each factor ≤3: one specific 30-day fix: productize the offering / name the specific tool / the exact research or dataset / which 2-3 subjects to drop and which to triple down on / one brand move, e.g. founder LinkedIn, quarterly report, branded free tool]

YOUR TOP 3 ACTIONS THIS WEEK
THE BOTTOM LINE: [one brutal sentence]
WHAT THIS DID NOT CHECK: [...]
```

### 3.3 Leak diagnostic (desk / shelves / basement)

Built on the May 2024 Content Warehouse API leak; what it is and how to read it: `foundations-keywords.md` section 1. Say "Google and AI search" as one problem. **Desk** = the librarian hands you to everyone who asks; **Shelves** = findable if someone looks; **Basement** = in the building, nobody hears about you.

Diagnose only, never write copy, never promise rankings. Every verdict names its check. Checks 1, 4 and the depth of 2 need web search; without it, give the exact searches (`"Business Name" -site:theirdomain.com`) and mark unrated. Read the money page or stop.

1. **Links and tier.** Judge the linking PAGE, not domain metrics, with the checklist and Desk / Shelves / Basement tiers in `offsite-authority.md` section 3. No offer → assess their most-linked page.
2. **Effort.** `contentEffort` is documented as "LLM-based effort estimation for article pages"; Andrew Ansley (Search Engine Land) reads it as tools, images, video, unique information, depth (present as his reading). Test: "Could a competitor reproduce this page in five minutes with Claude open?" Score /5: tool / calculator / template / interactive; images made for the page; video; information found nowhere else; deeper than the ranking pages.
3. **Engagement, never AI detection.** Finish (a reason to read to the end, vs everything in paragraph one), Interact (tool, checklist, calculator, download), Share (a line, number or idea worth sending a colleague). All no → a problem rewriting can't fix.
4. **Mentions with own marketing stripped.** Search the name excluding the domain. What does the web say they do? Does it match the homepage? How many independent sources? Quote the sources. First fix is always real directories and publications (offsite-authority.md).
5. **Fan-out.** Expand the money page's main question to 8-12 sub-questions (price, comparison, risk, timing, what happens next); mark which are answered. Gaps are why AI cites someone else.

Report, exact shape, no preamble:

```
THE FIVE LINE VERDICT
1. Links: [Desk / Shelves / Basement / Unrated]: [reason]
2. Effort ([X]/5): [Desk / Shelves / Basement]: [reason]
3. Engagement: [Desk / Shelves / Basement]: [reason]
4. Mentions: [Desk / Shelves / Basement / Unrated]: [reason]
5. Fan-out ([X] of [Y] answered): [Desk / Shelves / Basement]: [reason]

THE GRADE: [Desk / Shelves / Basement]
[2 sentences, library metaphor]

THE ONE THING: [one fix. "If you name three, they will do none."]

WHAT I COULD NOT CHECK: [...]
```

Re-run mode: re-run only the check they worked on.

### 3.4 Competitor gap (5 dimensions)

Every conclusion ties to the search they beat you on. Mode A: fetch both sites (homepage, competing page, About, sitemap or menu / footer). Mode B paste request:

```
YOUR SITE: page list, homepage, key service page, About
COMPETITOR SITE: page list, homepage, key service page, About
Label each block, e.g. ### YOUR HOMEPAGE, ### COMPETITOR HOMEPAGE
```

1. **Topic coverage:** page count with source (sitemap / menu + footer / user list) + distinct topics.
2. **Content quality** on pages read: specifics, original data, worked examples, case studies, first-hand detail vs filler. Word count is context, not a verdict.
3. **Site structure:** nav, related links, clusters.
4. **Trust signals /5:** named people; reviews / testimonials; case studies / real work; credentials / awards / memberships; complete About + contact (address or service area, phone or email).
5. **Presence across the web:** only if searchable or the user says; else "not checked" + `brandname -site:theirdomain.com`.

Links aren't visible from content: use pasted tool numbers naming the tool, else "links were not compared". Never estimate traffic, rankings, backlinks or DA. Partial data → defer that dimension.

```
COMPETITOR GAP ANALYSIS: [Your Business] vs [Competitor]
Your site: [URL]  Competitor: [URL]  Search compared on: [query]  Analysis mode: [Fetched / Pasted]

SIDE-BY-SIDE COMPARISON
| | You | Competitor |
| Pages (source) | | |
| Topics covered | | |
| Content quality | | |
| Avg words, pages read | | |
| Site structure | | |
| Trust signals X/5 | | |
| Presence across the web | | |

WHY THEY RANK ABOVE YOU: [2-3 sentences; if the evidence doesn't explain it, say the gap may be links or reputation not visible from content]

THE 3 BIGGEST GAPS
Gap N: [category]
- What they do: [named pages, quoted phrases, counts]
- What you do:
- The impact:

60-DAY CATCH-UP PLAN
Weeks 1-2: Gap 1 / Weeks 3-4: Gap 2 / Weeks 5-6: Gap 3
Weeks 7-8: remaining, incl. off-site (reviews, listings, mentions)

WHAT YOU DO BETTER: [only with evidence]
BOTTOM LINE:
WHAT THIS DID NOT CHECK:
```

### 3.5 Gap finder (missing pages + 4-week plan)

Mode A: fetch homepage, nav, /sitemap.xml. Mode B: every page by title (e.g. Home / About Us / Services / Contact, from menu + footer or sitemap.xml) + what you do, typical customer, location. Never guess what a vague page covers; fewer than 5 pages → ask if more exist.

1. Audit coverage (overlaps, thin pages).
2. Map 30-50 likely searches by type: questions before buying ("how much does [service] cost", "do I need [service]"); comparison ("X vs Y", "best [service] for [use case]"); problem ("why is my [X] not working", "signs you need [service]"); location ("[service] in [city]", "best [industry] near me"); trust ("are [industry] worth it", "how to choose a [industry]"); each service; niche questions.
3. Gaps: not covered; mentioned but shallow; no dedicated page.
4. Prioritize by buying intent, competition (searched or "unchecked"), business fit. Never recommend pages outside their services; flag assumptions ("I'm assuming your 'Services' page covers X...").
5. 4-week plan: W1 highest impact, W2 next, W3-4 supporting; concrete enough "to start writing Monday morning".

Data honesty: these are likely searches, never with volumes unless tool data exists. GSC impressions are not search volume (label the date range). The Queries export confirms real searches; the Pages export is separate; map query → URL only from same-row data (Search Analytics for Sheets add-on, Looker Studio). Clustering at scale: foundations-keywords.md.

```
WEBSITE GAP ANALYSIS: [Business Name]
Website: / Industry: / Location: / Analysis mode: [Fetched / Pasted]

WHAT YOU CURRENTLY COVER:
WHAT CUSTOMERS LIKELY SEARCH FOR: [top 15-20, marked "likely" unless confirmed]
COVERAGE: Your site covers [X] of the [Y] topics in this map.

YOUR BIGGEST GAPS:
Priority 1 (Build first):
- [Page title]: [why, what to include]
Priority 2:
Priority 3 (Supporting content):

4-WEEK CONTENT PLAN:
Week 1-4: [page + 2-3 bullet outline each]

BOTTOM LINE:
WHAT THIS DID NOT CHECK:
```

### 3.6 Ranking-laws modes

The three laws map to the People / Content / Site groupings of leak and patent material in `foundations-keywords.md` section 1 (fields show what is measured, not the weighting).

Intake, verbatim: "Which audit do you want to run? (1) NAP Consistency Audit, (2) First 100 Words Promise Check, (3) Topical Focus + Information Gain Audit, (4) Domain Authority Compounding Plan. Or describe your ranking problem and I'll pick the right one."

| Mode | Input | Produce |
|---|---|---|
| 1 NAP Consistency (Law 1) | NAPs, asked verbatim as in `offsite-authority.md` 8.3 | the NAP audit output in `offsite-authority.md` 8.3 |
| 2 First 100 Words (Law 1) | title, meta description, first 200 words | what the title promises (one sentence); what the first 100 words deliver; alignment 0-10; the gap that sends people back to search; rewrite landing the promise inside the fold ("If the rewrite needs to drop a paragraph, drop it.") |
| 3 Topical Focus + Information Gain (Law 2) | niche sentence + last 10-20 URLs with summaries or bodies | focus per piece high / medium / low / off-topic, with why; prune / redirect list (high drift, no traffic); per kept piece: adds Information Gain (original data, proprietary insight, contrarian view) or rehashes the top 5; 30-day plan: prune, refresh, original backlog |
| 4 Domain Authority Compounding (Law 3) | name, service, market, 2-3 internal data points | the authority compounding plan in `offsite-authority.md` 5.4 |

Honest timelines: `foundations-keywords.md` section 1. New domain → Modes 1-2 apply fully; 3-4 need a body of work. Wrong-mode input → switch and say so.

```
AUDIT: [mode name] (Law [N]: [law name])
WHAT I CHECKED: [one line on the input received]
FINDINGS: [numbered, most damaging first, each with the evidence from their input]
THE FIX THIS WEEK: [specific actions, smallest effort first]
WHAT THIS DID NOT CHECK: [the other two laws, with one line on when to run those modes]
```

## 4. Single-page graders

Quality rater = ranking diagnosis against the live SERP. Helpful content = numeric checklist. Run one unless asked for both.

### 4.1 Quality rater OUR scorecard

Uses Google's 182-page Search Quality Rater General Guidelines (published 11 September 2025; sections 3.2, 3.3, 3.4, 4.0, 4.5.3, 5.0, 5.3, 12.7, Part 3). Inputs: URL + exact query.

- **Step 0, read** main content, headings, author, tools, who runs the business. Unreadable → stop.
- **Step 1, intent (12.7):** Know (Know Simple), Do, Website, Visit-in-person. State the dominant interpretation in one sentence + any reasonable minor one.
- **Step 2, competitors first:** read the top 3-5 results, one line each. "No competitor pass, no R rating" (value is judged "compared to other pages on the web on the same topic"). No search → rate R anyway, label **uncalibrated**.
- **Step 3, grades:**
  - **O OFFSITE:** "reputation research is required for all PQ rating tasks". Search `[brand] -site:[domain]` and `[brand] reviews -site:[domain]`; name, quote, link sources. Against: credible fraud / scam reports, a pattern of detailed negative reviews, nothing at all on a money / health / safety site. Little info on a small site "is not indicative of high or low quality". No search → hand over the searches, O unrated. PASS / THIN / AT RISK.
  - **U UNIQUENESS:** effort, originality, talent / skill, accuracy; original source? Effort includes functionality (raters use calculators, add products to cart): does the page DO anything? Name what competitors have that it lacks. ORIGINAL SOURCE / SOME UNIQUE INPUT / REWRITE OF WHAT EXISTS.
  - **R RELEVANCE (Needs Met):** Fully Meets (only clear single-result intent; rare), Highly Meets (the realistic target), Moderately, Slightly, Fails to Meet. "Most pages written for a keyword rather than for a person land at Moderately or Slightly."
- **Step 4, demotion check** (any one trigger caps the verdict):
  - Low: content without adequate effort / originality / talent / skill; title slightly misleading, shocking or exaggerated; ads or supplementary content significantly distract; unsatisfying info about the site or creator.
  - Lowest: so little effort it fails its purpose or adds nothing vs similar pages; gibberish / hacked / defaced / spammed; title extremely misleading; content deliberately obstructed by ads, interstitials, download links; deceptive purpose, info or design; no responsibility info on a YMYL or trust page; very negative or malicious reputation; highly untrustworthy.
  - Judge Trust first: "Trust is the most important member of the E-E-A-T family because untrustworthy pages have low E-E-A-T no matter how" experienced or expert. YMYL (health, finance, safety, legal, civic): look for a named accountable human; anonymity is fine with a legitimate reason.
- **Step 5, rendering / ads:** renders without JS? Phone-width layout, readable, tap targets. Can't render → skip, don't estimate. Score ad load only when it meets a Low / Lowest trigger.
- **Step 6:**

```
OUR SCORECARD
Page: [url]
Search: [query]
Intent: [Know / Know Simple / Do / Website / Visit-in-person]
Dominant interpretation: [one sentence]
Read as: [live page / pasted content]

CURRENTLY RANKING
1. [what it is, what it gives the searcher]
2. [...]
3. [...]

O. OFFSITE ......... [PASS / THIN / AT RISK]
   Found: [...] Why: [...] Do this: [...]
U. UNIQUENESS ...... [ORIGINAL SOURCE / SOME UNIQUE INPUT / REWRITE]
   Why: [quote the page] Do this: [the thing only they could add]
R. RELEVANCE ....... [Fully / Highly / Moderately / Slightly / Fails to Meet]
   Why: [interpretation + result set] Do this: [...]
QUALITY CHECK ...... [CLEAR / LOW TRIGGER / LOWEST TRIGGER]

THE ONE THING
AFTER STATE: Fix items X and Y, moves from [current] to [projected]
WHAT THIS DID NOT CHECK
```

**Re-rate mode:** old scorecard + URL → delta card (`O ... [old] -> [new]`), VERDICT, STILL OPEN. "A fix that did not work is the most useful thing you can tell someone."

Calibration: "how to repot a monstera" (Know), named horticulturist with own photos → PASS / ORIGINAL SOURCE / Highly Meets. "best crm for small business" (Do), competent roundup from vendor sites → PASS / REWRITE / Moderately ("ceiling here is Uniqueness"). "emergency plumber brisbane" (Visit-in-person), national blog "10 Tips For Choosing A Plumber", no NAP or author → THIN / REWRITE / Fails to Meet + LOW TRIGGER.

Judge the page, not the brand; quote when criticizing; never call average fine; one specific action per letter ("Add the three photographs you took on the Trelawney job, with the date"); no invented criteria. Optional, unscored, labelled outside the guidelines: AI answers quote plain early standalone claims; original material gets cited (= U); reputation is what AI checks too (= O).

### 4.2 Helpful content 32-question grade

Google's "Creating helpful, reliable, people-first content" self-assessment (developers.google.com/search/docs/fundamentals/creating-helpful-content, refreshed December 2025). Score /100 + letter grade.

Intake, verbatim: "Paste the full text of the page you want graded (pasted text is the most reliable input; include the title, headings, and byline as they appear). Tell me the topic and, if you can, the site's focus in one line. If the topic touches health, money, safety, or legal decisions, say so, or I will detect it and weight expertise harder."

| Mode | Content & Quality | Expertise | People-first | Search-engine-first avoidance |
|---|---|---|---|---|
| SECTION-WEIGHTED (default) | 40 | 30 | 20 | 10 |
| YMYL (auto when clearly YMYL, no mode chosen) | 30 | 40 | 20 | 10 |
| EQUAL | on request only | | | |

All 32 questions always; Google's wording is authoritative.
- **G1 Content & Quality (12):** original info / analysis; substantial, complete coverage; insight beyond the obvious; adds value over sources; descriptive title; non-exaggerated title; bookmark-worthy; printed-magazine / encyclopedia standard; substantial value vs competitors; spelling / style; care vs sloppy; not mass-produced across creators or sites.
- **G2 Expertise (4):** trustworthy presentation (sourcing, author / site background); a site you'd research as an authority; written or reviewed by someone who knows; no easily verified factual errors.
- **G3 People-first (5):** real audience; first-hand expertise and depth; fits the site's primary focus; reader learns enough for their goal; reader leaves satisfied.
- **G4 Search-engine-first warnings (11, REVERSE-scored, never flip):** made primarily for search engines; scattershot topics; extensive automation across topics; mainly summarizing others; trends outside the audience; readers search again; imagined word count; entering a niche without expertise; promising an unanswerable answer; changing dates to fake freshness; adding / removing content to seem fresh.

Verdicts: PASS; PARTIAL (half credit, mixed evidence, never diplomatic); FAIL; N/A (redistribute weight within the group); UNVERIFIED (site-level, scored like N/A, listed with the fact that settles it). No evidence on a positive page-level question = FAIL. Site-level questions: 12, 14, 17, 19, 23, 24, 31, 32. Grade: A 90-100, B 80-89, C 70-79, D 60-69, F < 60. Unscored **Who / How / Why:** WHO is the author self-evident, bylined, linked; HOW is automation / AI disclosed where a reader would want it; WHY does it exist to help people or to attract search visits.

No word-count advice ever (q28 fails pages written to one). AI-assisted is not an auto-fail (q24 fails automation across many topics). Revise a verdict only if the content supports the dispute. Homepage / category → N/A where questions don't fit (the rubric fits articles best); under ~200 words → not an auto-fail; competitor page → fixes read as "what they would need to do"; several pages → one at a time; guaranteed rankings → say once that no score guarantees them.

Fix routing: originality → content.md (information gain); author / trust and entity / About → onpage-schema-entity.md; stale dates and titles → measure-refresh.md.

```
HELPFUL CONTENT SCORECARD
Page: [...]  Topic: [...]  YMYL: [yes/no]
Mode: [SECTION-WEIGHTED / YMYL / EQUAL] because [...]
Score: [X]/100  Grade: [A-F]

GROUP TABLES (G1-G4)
| Question | Verdict | Points earned of possible | Evidence |

GROUP SUBTOTALS
WHO, HOW, WHY
TOP FIXES (3-5, by impact)
THE VERDICT: [paragraph]
WHAT THIS DID NOT CHECK: [UNVERIFIED items; technical, speed, links, rankings → technical.md; graded as pasted, not rendered]

Want me to re-grade in a different mode, or work through the top fixes one at a time?
```

## 5. Vertical module (B2B, SaaS, ecommerce, local, restaurant)

On-page content only: no backlinks / authority, no third-party tool data, no Core Web Vitals, no off-page layer (GBP, LinkedIn, product analytics, review platforms). Hand those to technical.md and offsite-authority.md.

**Workflow:** get the URL → fetch the homepage asking for full text, nav items + URLs, key links, title + meta, H1/H2/H3 (local and restaurant: footer NAP / contact too) → auto-pick 2 more pages and announce "I'll audit these 3 pages: the homepage, [X], and [Y]. Fetching them now." → run the checklist quoting page text → report (5.3) → "Want me to go deeper on any of these? I can dig into [specific area 1], [specific area 2], or [specific area 3]." and wait for the pick. Several URLs → first is the homepage. Paste-only → ask for the vertical's paste list.

The master principle is **one page per intent** (service, use case, location, category): each has its own query and buyer, and one page can't rank for all of them. "Google ranks pages, not websites."

A bakery, cafe or food shop uses the restaurant / venue module if it serves customers on site; otherwise the local service module.

### 5.1 Per-vertical table

| | B2B services | SaaS | Ecommerce | Local service | Restaurant / venue |
|---|---|---|---|---|---|
| **#1 lever** | one page per service | use-case pages | category page content | one page per service (+ location pages) | functional map embed on the visit page |
| **Why** | "Each service has its own search intent and its own buyer. One page can't rank for all of them." | "SaaS prospects search by use-case, not product name. 'Best [tool] for [use-case]' is one of the highest-intent SaaS keyword patterns." | empty category pages are the most common ecommerce failure; categories win broad commercial queries products can't | "One page trying to rank for 12 services ranks for none of them." | same-day visit intent: "Someone searching 'winery near me' is often deciding within the hour, on their phone" |
| **Pages to fetch** | home, services (/services, /how-we-help, /what-we-do), case study or About (whichever shows more trust) | home, pricing (/pricing, /plans), use-case (preferred) or feature page | home, top category (biggest range, highest traffic or first nav item), one product | home, About (where E-E-A-T lives), top service (highest revenue or first in dropdown) | home, menu (wine list / tasting menu; hotels: rooms / rates), visit (/visit-us, /contact, /find-us, /cellar-door, /locations) |
| **Paste list** | homepage, services overview, 2-3 service pages, About / Team, 1-2 case studies, blog index titles (minimum: home + 1 service + case study or About) | homepage, features, 2-3 use-case pages, pricing, integrations list, docs index | homepage, 1-2 categories, 1-2 products, category hierarchy, optional JSON-LD | homepage, Services, 2-3 service pages, location pages, About / Team | homepage, menu as text (not a PDF screenshot), visit page incl. map info, booking page, About / Our Story |
| **Conversion unit** | qualified leads, pipeline | trials, signups, MRR | revenue | calls, leads, bookings | bookings, walk-ins, repeat visits |
| **Homepage title front-loads** | service category + ideal customer | product category + ideal customer | brand + primary category | primary service + location | cuisine / venue type + location |
| **Extra report scores** | `SERVICE PAGE ARCHITECTURE: X/10`, `BUYER JOURNEY COVERAGE` | `FEATURE PAGE ARCHITECTURE: X/10`, `USE-CASE COVERAGE: X/10`, `PRICING TRANSPARENCY [Present / Hidden]` | none | none | `MAP & DIRECTIONS CHECK [Present / Missing]`, `MENU CONTENT CHECK [HTML menu present / PDF only / missing]` |
| **AI SEARCH READINESS /10** | topical depth, AI-parseable case studies (before / after, metrics), named experts with bios: none 0-3, some 4-6, all solid 7-10 | topical depth 0-3 + parseable case studies 0-2 + category clarity 0-3 + review platforms (G2 / Capterra) 0-2 | topical depth /4 + structure /3 + brand and category clarity /3 | topical depth 0-4 + headings and lists 0-3 + authored content 0-3 | topical depth 0-4 + chef / team content 0-3 + cuisine + location clarity 0-3 ("wood-fired Neapolitan pizza in Fitzroy") |
| **Flag hard** | missing trust ("B2B buyers don't enquire without them"); hidden pricing | hidden pricing ("a top-3 conversion killer"); trial friction (long forms, card required) | empty categories | one page for all services; faceless About | missing map; PDF-only menu ("a critical issue every time"); bad photos |

Never score title length; check the front of the title does the work (first ~5 words). Shared thresholds: forms under 5 fields; home → trial / booking under 2 clicks; any product within 3 clicks; CTA above the fold on desktop and mobile; tap-to-call. Every X/10 names the pages it's based on, or says "not assessed".

### 5.2 Checklists

**B2B services**
- [ ] Homepage: H1 says what + who (not just brand); social proof above the fold (logos, years, team size); CTA ("Book a consultation", "Get a quote"); links to each major service.
- [ ] Service pages: one per service; service name in title / H1 / URL; opens naming the pain; who it's for; how it works (process, timeline); pricing context (ranges or "starting from"); FAQs; proof; lead form. Score: 0-3 all services on one page; 4-6 separate but thin; 7-10 dedicated pages with most items.
- [ ] Buyer journey (buyers read several pieces before contacting a vendor): Unaware (thought leadership), Consideration (comparison, how-to-choose, pros / cons), Decision (case studies, pricing, ROI calculators), After-service (customer success, onboarding docs).
- [ ] Trust: About with real team, roles, credentials, photos; client logos; awards; author bios; address + team size.
- [ ] Case studies: a hub (/case-studies, /our-work); numbers, not "significant improvement"; client context (size, industry, challenge, approach, outcome); visuals; linked from service pages.
- [ ] Lead capture: CTA above the fold on every page; multiple paths (demo, discovery call, gated resource, contact).
- [ ] Industry pages ("HR Compliance for Healthcare"): unique, not templated, linked from services.
- Example: split /how-we-help's 15 services into `/services/hr-compliance`, `/services/payroll-services`, `/services/recruitment-outsourcing`. "Start with your highest-revenue service first, roll out the rest over 60-90 days." "10 dedicated service pages mean 10 entry points from Google instead of one."

**SaaS**
- [ ] Homepage: H1 what + who; hero answers what it does, who it's for, what changes for them; trial / demo CTA; logos; nav to features, use cases, pricing.
- [ ] Feature pages: one per major feature, problem-solution not spec, "How [persona] uses this feature", screenshots, trial CTA.
- [ ] Use-case pages ("CRM for Real Estate Agents"; `/solutions/real-estate-agents`, `/use-cases/marketing-teams`): persona + problem, role-specific screenshots, a customer story from that use case, tailored CTA.
- [ ] "[Brand] vs [Competitor]" pages for 3-5 competitors: feature table, pricing, pros / cons, ideal use cases each, fair (Google's guidance on comparison content asks for evidence and fair trade-offs); linked from features. Writing them: content.md.
- [ ] Integration pages (Zapier, Slack, Salesforce): use cases + setup, more than a logo grid; target "[Your Tool] + [Partner Tool]".
- [ ] Pricing: in main nav; tiers + comparison table; not "contact sales" only; objection FAQs (annual vs monthly, refunds, upgrades, contracts); proof; trial CTA. "[Tool] pricing" is among the highest purchase-intent searches.
- [ ] Trial flow: CTA above the fold everywhere; no-credit-card option.
- [ ] Docs: help center visible and indexed; question-led headings, answer in the first lines, numbered steps; linked from product pages (they rank long-tail "how to" and give AI quotable answers).
- [ ] Proof and category: G2 / Capterra badges, named testimonials, one clear category position.

**Ecommerce (site level; deep dives in 6)**
- [ ] Homepage: unique title; H1 not "Welcome" or brand only; meta with a reason to click; hero says what the store sells; crawlable links to main categories; reviews, delivery / returns.
- [ ] Categories: H1 names the category, not a UI label ("Shop By Category", "Products"); intro, buying guide, FAQ per 6.1; links to related categories and key products.
- [ ] Products: specific H1; unique description (not manufacturer copy); alt with product name; visible reviews; Product data (name, image, offers: price, priceCurrency, availability) judged only from source; review markup only with genuine visible reviews; cross-sell; clear CTA.
- [ ] Structure: category > subcategory > product; breadcrumbs.
- Example: "'Products | StoreName' to 'Wireless Chargers: Fast Charging for iPhone & Samsung | StoreName'"; H1 "Wireless Chargers for iPhone & Samsung"; link to power banks and cables.

**Local service**
- [ ] Homepage: H1 has service AND location; NAP in the footer of every page; suburbs served; trust above the fold (reviews, years, certifications).
- [ ] Service pages: one per service (`/services/cockroach-pest-control`, `/services/termite-inspection`); title / H1 = service + location; what, who, process, pricing context (length is a competitor-relative compass, not a floor); FAQs; suburbs served; links to related services + About; phone / form / booking CTA.
- [ ] About (the E-E-A-T unlock): real team with photos, names, roles; credentials, years; story; author attribution; insurance, licenses, memberships (e.g. Master Plumbers, HIA); community work. "AI search can't recommend a business that looks faceless."
- [ ] Location pages: one per suburb, not a templated "We service [SUBURB]"; landmarks, streets, travel time, local customer examples.
- [ ] Freshness: latest post more than 18 months old → flag hard; stale prices, offers, staff. Never just change the year (Google warns against faking freshness).
- [ ] Contact: tap-to-call on every page; embedded map; opening hours.
- NAP across the web: Mode 1 (3.6). GBP and citations: offsite-authority.md.

**Restaurant / venue**
- [ ] Homepage: H1 not "Welcome"; hero says what, cuisine, where; booking CTA; professional photos; footer address + phone; Restaurant (LocalBusiness) schema with address, phone, opening hours, servesCuisine, menu URL, acceptsReservations matching the page ("not checked" without source).
- [ ] Visit page (non-negotiable; lead with it if missing): functional embedded Google Map ("A screenshot of a map does not count"); one-tap Get Directions; address, hours, parking, public transport; booking link / phone. Fix: embed above the fold beside address, hours, parking; takes about 5 minutes.
- [ ] Menu in HTML: dish names in headings / copy, a description per dish, dietary (vegan, GF, DF), prices, more for signature dishes. Don't call PDFs or images unreadable (Google can index PDF text and often image text); HTML wins on phones, screen readers and clean text for Google and AI.
- [ ] Photos: professional food, interior / exterior, chef / team; alt with dish / venue. A venue with bad photos needs a photo shoot before SEO.
- [ ] Booking: sticky button on every page (e.g. "Add a sticky booking button to the mobile header that links directly to your OpenTable widget"); OpenTable, ResDiary or direct.
- [ ] Multi-location: page per location with unique content, photos, hours, NAP; cross-links.
- [ ] Events (private dining, weddings, wine dinners): Event schema only on real, dated events, never happy hours, standing specials or opening hours (Google's event guidelines).
- Never estimate "lost walk-ins".

### 5.3 Vertical report

```
[VERTICAL] SEO AUDIT: [Business / domain]
[Vertical fields, e.g. Venue type + Location]
Pages audited: [3 URLs]   Read as: [Fetched / Pasted]

OVERALL HEALTH: [STRONG / NEEDS WORK / CRITICAL ISSUES]
[One line: biggest issue in conversion-unit terms]

[Vertical extra scores, each naming its pages]

QUICK WINS (fix this week)
1. [Specific page]: [Specific issue]: [Exact fix]
2.
3.

STRUCTURAL ISSUES (fix this month)
CONTENT GAPS / CONTENT STRATEGY (build over next 90 days)

AI SEARCH READINESS: [X/10] [provisional if <3 pages read]
What's present:
What's missing:
Quickest unlock:

PRIORITY ACTION PLAN (ordered by impact)
1. ... 5.

WHAT THIS DID NOT CHECK:

Want me to go deeper on any of these? I can dig into [area 1], [area 2], or [area 3].
```

For high-effort or counter-intuitive fixes add one "Why this matters" line in business terms. Never cite figures you didn't read this session.

## 6. Ecommerce stack

"Schema, feed, and visible page must say the same thing." Full shopping stack = category + product + feed; add agent-readiness for agentic checkout. Shopify: a Storefront MCP reads live catalog and policies; an admin MCP (Shopify AI toolkit / Admin API) applies rewrites. Without MCP, paste in, paste back. Missing facts → `[ADD: fact needed]`, never invented.

### 6.1 Category / collection page

Intake, verbatim: "Give me: (1) the category page URL, or paste its content (title, heading, any intro copy, the first rows of products, filters shown), (2) the target query (the category head term), (3) your platform (Shopify, WooCommerce, Magento, other), and (4) optional but powerful: one competitor category page outranking you. If you can also tell me your top 3 sellers in this category and the 2 or 3 questions customers ask before buying in it, the copy I write gets much sharper."

1. **Evaluate** (status + fix each):
   - [ ] TITLE / META / H1: unique, head-term-led, no boilerplate shared across categories.
   - [ ] THE INTRO ANSWER: what it is, who it's for, how to choose (the most common gap).
   - [ ] BUYING GUIDANCE: criteria, comparisons, use cases. [ ] FAQ.
   - [ ] PRODUCT VISIBILITY: crawlable HTML, not JS-only; top products + subcategories surfaced.
   - [ ] INTERNAL LINKING: parent / child / sibling, no orphaned subcategories, breadcrumbs, inbound from guides with descriptive anchors.
   - [ ] SCHEMA: ItemList + BreadcrumbList matching the page.
   - [ ] INDEXATION: no accidental noindex, robots.txt blocks or bad canonicals.
2. **Faceted nav:** labels match how buyers filter (material, size, use), never internal codes. Index only the one or two filters with real demand ("leather sofas", "waterproof hiking boots"); the rest out via canonical / noindex per platform. Page 2+ reachable as HTML. Conservative, platform-aware.
3. **AI-answer layer:** the intro answers comparative questions ("what should I look for in X", "which type of X for Y") in liftable standalone sentences; a comparison element (types, price tiers, use cases); copy agrees with product data.
4. **Rewrites:**
   - Title + meta.
   - **Intro ~80-150 words above (or beside) the grid**, answer-first and unique, never pushing the grid below the fold on mobile.
   - **Buying guide below the grid**: criteria + comparison table from supplied facts only.
   - **FAQ below the grid**: 3-8 real questions buyers actually ask (PAA, sales calls; fewer real beats more padded), one-sentence-first answers (markup optional, no rich-result promise).
   - 3-5 internal anchor suggestions.
   Total copy can exceed 150 words because depth sits below the grid. "Unique and meaningful beats long: an 80-word intro that genuinely helps beats 400 words of category boilerplate."
5. **Competitor gap:** what they answer, structure, 2-3 closing moves; never copy.
6. Summary table (element | status | fix), top 3 this week, CSV on request.

Grid contradicts copy → the copy loses. Under ~6 products → merge into parent or sibling; huge category → parent routes, depth on subcategories; seasonal → stable URL year to year; brand category → compare across the brand's lines; already-ranking filter page → optimize, don't de-index; headless / marketplace → copy + placement note.

```
PAGE VERDICT: [intent gap, e.g. "this page ranks for nothing because it answers nothing"]
CATEGORY EVALUATION
FACETED NAVIGATION READ
AI-ANSWER LAYER
REWRITES [gaps as [ADD: ...]; one before/after]
SCHEMA NOTES
COMPETITOR GAP
SUMMARY TABLE + DO THIS WEEK
WHAT THIS DID NOT CHECK: product pages (6.2), feed (6.3), page speed (technical.md). Category, product, feed: run all three.

Want me to run the next category, or turn this into a reusable template for all your collection pages?
```

### 6.2 Product page

AI shopping assistants match products to CONSTRAINTS ("will this fit a 15 inch laptop", "is it safe for sensitive skin", "can I machine wash it"). "A spec bullet says 'water-resistant polyester'; a recommendable sentence says the coating protects your electronics through a rainy bike commute."

Intake: "(1) the product page URL, or paste the page content (title, headings, description, specs, reviews snippet), (2) the target query or the current title tag, (3) optional but powerful: one competitor product page that outranks you, and (4) your vertical in a word (apparel, beauty, electronics, homewares)".

1. **Eight points:** [ ] TITLE + URL (product type + defining attributes; keyword slug, not a code) [ ] META [ ] H1 + headings [ ] DESCRIPTION (usually the biggest gap) [ ] IMAGES (alt, filenames, angles) [ ] STRUCTURED DATA (Product, offers with price + availability, brand, identifiers; missing or partial schema is a top-three finding on most pages) [ ] REVIEWS / UGC (visible, crawlable, not locked in a widget) [ ] INTERNAL LINKS (breadcrumbs, related, parent collection).
2. **AI layer:** 5-8 "can I / will it / does it" constraint questions per vertical. Apparel: fit vs comparable brands, fabric feel, care. Beauty: ingredients, skin-type compatibility, usage. Electronics: compatibility, dimensions, battery, what's in the box. Homewares: dimensions, materials, assembly, care. Plus ideal-buyer clarity (who it's for and, honestly, not for) and variant clarity (same names in copy and schema, "does it come in green").
3. **Rewrites:** front-loaded honest title + meta; description opening sells the outcome and names the buyer, benefit sentences fold in specs, spec list below; FAQ from constraint questions; alt-text patterns.
4. **Schema:** Product JSON-LD with name, image, brand, identifiers, offers (price, priceCurrency, availability), shippingDetails and hasMerchantReturnPolicy where stated, aggregateRating only with real visible reviews (misuse is a documented spam pattern); variants → ProductGroup with hasVariant and variesBy. Validation: onpage-schema-entity.md.
5. Competitor gap. 6. Summary, top 3, CSV on request.

Copy facts exactly (sizes, materials, measurements, prices); no hype or "best seller" without evidence; one page per run + a reusable rule per fix; feed mismatch = priority fix. Thin variant URLs → canonicalize to parent or keep + ProductGroup; no reviews → skip aggregateRating, FAQ as trust substitute, reviews work in offsite-authority.md; bundles → precise contents (feed mismatch causes disapprovals); discontinued → redirect to successor or availability-aware page; marketplace → what the platform allows; already strong → 2-3 marginal wins.

```
PAGE VERDICT: [money gap, e.g. "your description is five spec bullets, so AI has nothing to recommend"]
EIGHT-POINT EVALUATION
AI-RECOMMENDATION LAYER
REWRITES [before/after for title + opening paragraph]
SCHEMA BLOCK
COMPETITOR GAP
SUMMARY + DO THIS WEEK
WHAT THIS DID NOT CHECK: Core Web Vitals, Merchant Center feed (6.3), agent parse / transact (6.4). Run all three for the full shopping stack.

Want me to run the next product, or turn these fixes into a reusable template for this product type?
```

### 6.3 Merchant Center feed

"In Shopping, the product TITLE does the job the keyword does in search": "Sunset Beach Vibes" vs "Scented Candle, Sunset Beach, Soy Wax, 45 Hour Burn". Feed titles may differ from poetic on-site titles.

Intake: "(1) a product feed export (CSV or a paste of rows: title, description, product type, brand, GTIN, price, availability, attributes), (2) the diagnostics summary from Merchant Center (disapprovals and warnings from the needs-attention view, pasted as text), (3) your store platform, and (4) your top 10 products by revenue". Never block on missing data; say which checks needed diagnostics.

1. **Disapprovals first** ("visibility zero times a better title is still zero"), grouped: missing / invalid GTIN; image policy (watermarks, promo text, placeholders); price / availability mismatch; policy flags; missing required attributes. Per group: what it blocks, the fix, where (feed field, landing page, data source, account).
2. **NEVER-TOUCH** (state even unasked): never overwrite ID / SKU (it creates a new product with zero history; whole catalogs have been sunk this way). PRICE, CURRENCY, AVAILABILITY, SALE PRICE, SALE DATES are fixed at the data source, never with Merchant Center overrides (Google re-checks the landing page).
3. **Titles:** product type + narrowing attributes (scent, material, color, size, count, burn time, model). Apparel: gender + category, then brand, attributes, size. Hard goods: brand + type, then attributes. Hard limit 150 characters, roughly 70 shown. No word salad, ALL CAPS or promo ("free shipping", "sale", "best price"). Before / after + a pattern per product type.
4. **Identifiers:** genuine GTIN (UPC / EAN / ISBN) wherever it exists (cross-seller history); else brand + MPN; own manufacture without MPN → a unique stable code labelled "assigned"; one-of-a-kind → identifier_exists. Never fabricate a GTIN.
5. **Attributes:** most specific google_product_category; product_type = own taxonomy. Variants: color, size, gender, age_group, material, pattern + item_group_id (unique per product, identical across its variants); useful beyond apparel (couch: color / size / material / pattern; kids bike: gender / age_group). COLOR: dominant first, up to two more, slashes `red/grey/white`, never commas, "variety" or "N/A"; use the landing page's name even if marketing ("Dusty Ash") and the plain color (grey) in the title. SIZE: standard values (S, M, L; 11.5 shoes); size_type / size_system apparel-only. MULTIPACK = 2+ of one item (enter count); BUNDLE = different items as one. adult is separate from age_group. PRODUCT HIGHLIGHTS: 3-4 short ones (the most underused field in small-store feeds). CUSTOM LABELS: high-margin, best sellers, high-ticket.
6. **Description:** factual, attributes + use cases, no promo (free shipping, BOGO violate policy).
7. **Feed-to-landing consistency** (the silent killer): currency handling, sale price on page but not at source, stale feed schedule; fix refresh frequency.
8. **Free + AI:** free listings on; Product schema agrees with the feed. "A product an agent cannot parse is a product an agent cannot buy."
9. **Cadence:** DAILY (suspension banner, needs-attention; top-seller disapprovals same day); MONTHLY titles + highlights from converting search terms.
10. **Priority:** top-seller disapprovals → top-seller titles → identifiers / attributes → long tail.

Fix at platform level so it survives the next sync. Shopify / Woo auto-feeds → product data, metafields or feed-app mapping (title overrides are the exception); 10,000+ SKUs → top sellers by hand + title pattern + feed rules; multi-country → language / currency / availability per country; services / digital goods → ineligible; suspended account outranks everything → Google's remediation flow; all approved → titles, highlights, labels.

```
FEED HEALTH SUMMARY [lead with the disapproved best-seller]
NEVER-TOUCH CONFIRMATION
DISAPPROVAL TRIAGE
TITLE REWRITES
IDENTIFIER AND ATTRIBUTE FIX LIST
CONSISTENCY CHECKS
FREE AND AI VISIBILITY LAYER
THE CADENCE
DO THIS WEEK (top 5 by revenue: field, product set, change)
WHAT THIS DID NOT CHECK: bidding, negatives, budgets (Google Ads); landing page (6.4)

Want me to run the same pass on the next batch of products, or write the feed rules for your platform?
```

### 6.4 Agent-readiness (0-100)

Agents rebuild a product graph from several code layers; a clean accessibility tree is necessary but not sufficient (JS-injected price, unlabelled add-to-cart or unselectable variant still fail).

Intake: Chrome → Inspect → Accessibility tab, paste the tree; better, the rendered HTML of the product container, or Lighthouse output asked to "analyse the page for a shopping agent"; plus raw source (Ctrl+U / Cmd+Option+U); if JSON-LD is JS-injected, the rendered page (Elements → right click `<html>` → Copy → Copy outerHTML); platform. curl of raw HTML is fine; a summarized text fetch is not. No price / add-to-cart / variant controls in the input → stop and ask. Screenshot only → best effort, flag unverifiable layers.

| Layer | Weight | Checks |
|---|---|---|
| Transactable elements | 25 | press add-to-cart, choose a variant, read price / availability as TEXT (not image or CSS sprite) |
| Structured data | 20 | Product + Offer (price, priceCurrency, availability, SKU or GTIN), Review / AggregateRating; raw + rendered. JS-only markup is not missing but goes under JS-dependency (dynamic markup can make Shopping crawls less frequent and reliable) |
| JS-dependency | 20 | title, price, availability, variants in server HTML |
| Visible-vs-parsed consistency | 15 | what a human sees = markup + tree |
| Accessibility metadata | 10 | alt, ARIA roles / labels, labelled add-to-cart, variant selector, quantity |
| Semantic HTML | 10 | one H1 = product name, sensible H2s |

Pass = full, Weak = half, Fail = 0. Unseen layer → no /100; report "48 of 65 checked" and name what's missing. One TEMPLATE-level fix per Weak / Fail, with the file (Shopify product.liquid; WooCommerce content-single-product.php + template-parts; Magento PDP .phtml; custom PDP component), ranked by what blocks a sale or citation; transaction blockers before headings and alt. Never "fix the accessibility tree and you are done". Be decisive ("Your price is injected by JS, so an agent reads a blank. Output it server-side in product.liquid"). All Pass → off-site signals, brand mentions, digital PR (offsite-authority.md).

```
AGENT-READINESS AUDIT
[Page or URL]
[score]/100. [verdict, e.g. "62/100. An agent can read this product but cannot reliably complete the purchase."]

LAYER SCORES
[Layer]: [Pass / Weak / Fail] - [why]   (x6)

PRIORITISED FIXES (worst first)
ISSUE:
LAYER:
WHY AN AGENT CARES:
TEMPLATE FIX: [e.g. "Add aria-label='Add [Product] to cart' to the add-to-cart <button> in product.liquid"]
PAYOFF: [agent / SEO / accessibility / all]

DO THIS WEEK (top 3)
WHAT THIS DID NOT CHECK: [unseen layers, off-page; feed layer only if selling via Google / Bing Shopping]
```

## 7. Affiliate traffic audit

Cross-checks GA4 referrals against affiliate payouts for last-click hijacking or cookie stuffing. Flags, never accuses: "worth checking", "possible interception", never "this is fraud". GA4 shows traffic; the network attributes commission.

Modes: **A** GA4 only (can flag, can't confirm). **B** GA4 + payout report (Impact, Rakuten Advertising, CJ, Awin, which absorbed ShareASale in 2025), best. **C** no data → export steps, then stop.

Export, verbatim: "GA4 -> Reports -> Acquisition -> Traffic acquisition. Set the date range to your last full month. Change the primary dimension to 'Session source / medium'. Add 'Key events' and 'Total revenue' as columns if not shown. Export to CSV". ("Key events" replaced "conversions" in 2024; same thing.) Payout: last month's transactions with partner / source, order ID or count, commission.

Watchlist: Honey / joinhoney.com / PayPal Honey; Phia / phia.com; Capital One Shopping / Wikibuy; Rakuten / Ebates; Karma / Shoptagr; Coupert, Cently, RetailMeNot, Slickdeals, Klarna, Piggy, CouponCabin; plus unknown converting referrers and implausibly high conversion rates. Presence is not proof; the test is earned vs intercepted.

1. GA4 scan: sessions, conversions, rate, revenue, exactly as given.
2. Hijack signature: last-click credit for journeys that started elsewhere (organic, direct, email, paid), extension only at the final touch. Paths: "GA4 Advertising -> Key events -> Key event attribution paths, with the purchase key event selected", dimension set to Source; or network click vs order timestamps.
3. Cross-reference: commission with little or no GA4 traffic, or far above the source's share of sessions.
4. Verify in the network: click-to-order gap (seconds suggests checkout interception); an earlier affiliate or first-party touch; signed agreement + rate; compliance flags (adware / extension policies).

```
FLAGGED SOURCES
| Source | Sessions | Conversions | Conv. rate | Revenue attributed | Why flagged | What to verify |

THE ONE TO CHECK FIRST
WHAT I COULD NOT SEE
VERIFICATION CHECKLIST (3-5 steps)
```

Explain terms on first use, short paragraphs, end each section with "What to do right now".

Not covered: vertical modules for publishers, marketplaces, real estate, education or international sites; a crawl-scale vertical mode beyond 3 pages; Organization / Service / SoftwareApplication schema for B2B, SaaS and local (see onpage-schema-entity.md); Bing, Meta and Amazon feeds.
