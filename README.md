# SearchOS

**One Claude Code skill for getting found in Google, Bing and AI answer engines.**

SearchOS covers classic SEO, answer-engine optimization (AEO), generative-engine optimization (GEO) and AI visibility
in a single skill, from keyword research to measurement. It works with Google and Bing search as well as ChatGPT,
Claude, Perplexity, Gemini, Copilot, and Google AI Overviews / AI Mode.

It was built by studying about 80 separate SEO, AEO, GEO and AI-visibility skills, merging the duplicates (about 25
groups of skills doing the same job), resolving their conflicts, and rewriting everything as one workflow with one
set of rules.

---

## The idea in one paragraph

Search engines and AI assistants both pull from pages they can crawl, then pick sources that match the searcher's
intent, add something new, and are backed up by other sites. So the work is: be crawlable and indexed, build one page
per intent, add information nobody else has, and get named on the sites those engines already trust. Classic SEO is the
foundation of AI visibility; AI visibility adds positioning, brand mentions and a different scoreboard.

---

## Install

SearchOS is a [Claude Code](https://docs.claude.com/en/docs/claude-code) skill. Clone it into your skills folder:

```bash
git clone https://github.com/vamsireddy4/search-os.git ~/.claude/skills/searchos
```

That's it. Start a new Claude Code session and the skill is available.

**Requirements:** Claude Code. The helper scripts need Python 3 (standard library only, nothing to install).

---

## How to use it

Type `/searchos` followed by your request, or just ask a search question. Claude loads the skill on its own when you
ask how to rank, why traffic dropped, how to get cited by AI, or paste Search Console, GA4, Bing, crawl, log, backlink,
review or AI-answer data.

Example requests:

```text
/searchos plan SEO for my new bakery website in Pune
/searchos here's my Search Console export, why did clicks drop 40% since June?
/searchos audit https://example.com for technical issues
/searchos write a comparison page: our tool vs Asana for agencies
/searchos how do I get ChatGPT and Perplexity to recommend us?
/searchos run the AI visibility checklist on example.com
/searchos generate Organization and LocalBusiness schema for this page
```

### What happens

1. `SKILL.md` matches your request to a row in its routing table.
2. Only the reference file that row needs is loaded (so the context stays small).
3. It asks for the inputs it needs, in one message, and says what it can do without them.
4. It runs that reference's method and ends with a fixed report:

```text
[REPORT NAME]: [site / page / query], [date], data: [fetched / pasted / export]
HEADLINE: the biggest issue or result
...findings...
DO THIS WEEK: 1-3 actions, smallest effort / biggest impact first
NEXT CHECK: date and what to re-export or re-run
WHAT THIS DID NOT CHECK: gaps, and the export or tool that would answer each
```

---

## The workflow

SearchOS follows the order the work is really done. Each phase feeds the next.

| Phase | What happens |
|---|---|
| 0. Baseline | Goal, business type, market; record clicks, rankings, conversions and AI visibility before changing anything |
| 1. Crawl + index | Remove blockers: robots.txt, noindex, canonicals, soft 404s, redirects, JavaScript-only content, blocked AI search bots |
| 2. Research | Keywords and buyer questions, intent from the live results, "can AI fully answer this?" filter, winnability |
| 3. Plan | One page per intent, money pages first, topical map, publishing order |
| 4. Create | Pages that match intent and add new information; answer first, easy to quote |
| 5. On-page | Titles, headings, schema that matches the page, entity and author pages, internal links |
| 6. Authority | Earned links and mentions, digital PR from your own data, reviews, Google Business Profile |
| 7. AI visibility | Positioning line, "best / vs / alternatives" pages, mentions where each assistant looks, prompt tracking |
| 8. Measure + refresh | Near-page-one queries, CTR, rank movement, decay, cannibalization, update impact, AI citations, conversions |

Audits are entry points into this loop: they diagnose which phase is broken.

---

## What's inside

```text
searchos/
├── SKILL.md                         router, workflow, principles, house rules
├── references/
│   ├── foundations-keywords.md      how search + AI answers work, dated stats, keyword research,
│   │                                intent, clustering, topical maps, master 30-day plan
│   ├── content.md                   briefs, drafts, information gain, listicles, comparison pages,
│   │                                calculators, customer-fit scoring, pre-publish checks
│   ├── technical.md                 technical audits, AI bot policy + robots.txt template, logs,
│   │                                Core Web Vitals, migrations, repo HTML audits
│   ├── onpage-schema-entity.md      titles/meta, schema (JSON-LD), entity / Knowledge Panel,
│   │                                author authority, internal linking
│   ├── offsite-authority.md         link building, digital PR, outreach, Reddit/YouTube/LinkedIn,
│   │                                reviews + Google review policy, NAP, optional grey-hat section
│   ├── ai-visibility.md             AEO/GEO program, AI Visibility Checklist, prompt library,
│   │                                citation share, share-of-voice experiments
│   ├── measure-refresh.md           Search Console, striking distance, rank tracking, decay,
│   │                                cannibalization, core updates, reporting, board slide
│   ├── audits.md                    site and page audits, quality-rater grading, helpful content,
│   │                                B2B / SaaS / ecommerce / local / restaurant, product feeds
│   └── local-international.md       Google Business Profile, local map grids, citations by country,
│                                    hreflang and multilingual sites
└── scripts/                         13 helper scripts (Python, standard library only)
```

### Scripts

All run with `python3 ~/.claude/skills/searchos/scripts/<name>.py`. Each has a `--selftest` (except
`review_proof_sorter.py`).

| Script | What it does |
|---|---|
| `site_audit.py` | Site-level technical + AI-access audit (host, redirects, soft 404, sitemap, canonicals, raw-HTML content, schema) |
| `ai_crawl_check.py` | Which AI bots robots.txt blocks (search vs training bots), llms.txt, text visible without JavaScript |
| `check_indexable.py` | noindex, X-Robots-Tag and robots.txt checks for search bots |
| `keyword_score.py` | Scores keywords by traffic potential, business potential and difficulty, with an AI-answer discount |
| `pick_keywords.py` | Finds winnable buying-intent long-tail keywords by difficulty and ranking-page authority |
| `onpage_check.py` | On-page basics for one page |
| `draft_check.py` | Pre-publish draft check (answer first, keyword placement; structure and length as notes) |
| `ready_check.py` | Placeholders, image alt text, author/reviewer, evidence density |
| `quotable_check.py` | How easily AI can quote each passage (headings, pronoun openers, vague words) |
| `entity_schema.py` | Organization + WebSite JSON-LD with sameAs links |
| `aeo_gaps.py` | AI share of voice per engine and gap queries from pasted AI answers |
| `sov_experiment.py` | Test vs control lift with a permutation p-value |
| `review_proof_sorter.py` | Sorts Google reviews into proof blocks for each service or location page |

---

## Rules it always follows

- **Read or stop.** Never grades a page, site, search result or AI answer it didn't actually read.
- **Never invents data.** No made-up volumes, rankings, reviews, quotes, credentials, citations or AI answers.
  Gaps are marked `[ADD: ...]` or `[VERIFY]`.
- **Leads with the fix.** Exact page, exact issue, exact change; patterns over single pages; short lists.
- **Says what it didn't check.** Every report ends with it.
- **No guarantees.** No promised rankings, citations or timelines; directions and re-check dates instead.
- **Soft numbers stay soft.** Title (~60 characters), meta (~155), word counts and link counts are hints, never
  pass/fail rules.
- **Schema honesty.** Markup must match the visible page. FAQ rich results ended on 7 May 2026: FAQ sections are fine
  for readers, but FAQ markup is never sold as a ranking or AI win. There is no special "AI schema".
- **AI bots.** Blocking bots that power AI search is a problem; blocking training-only bots is the site owner's choice.
- **White-hat by default.** Grey-hat tactics appear only in one optional section, with disclosure and risks stated.
- **Asks before acting.** No paid API calls, sent emails, live-site edits or git commits without permission.

---

## Limits

- It can't query AI assistants by itself: AI visibility is measured from answers you paste or from a tracking tool.
- Third-party statistics (Ahrefs studies and others) are dated and directional; re-check them before quoting.
- Google changes some features often (Business Profile posts and Q&A, rich result types). Re-check those against
  Google's documentation before relying on them.
- Not covered: paid search campaigns and faceted-navigation decision trees beyond ecommerce basics.

---

## Credits

SearchOS distills methods from many public SEO and AI-search teachings (including Google Search Central
documentation and the Search Quality Rater Guidelines, plus community courses and skills on SEO, AEO and GEO),
rewritten in its own words. It is not affiliated with Google, Microsoft, OpenAI, Anthropic, Ahrefs or any other
company mentioned.

Contributions and issues are welcome.
