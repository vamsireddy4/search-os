# Off-site authority: links, PR, mentions, reviews, local entity

Links, digital PR, brand mentions, reviews, GBP and NAP. On-page entity work (entity home, Organization/Person schema, sameAs, Wikidata) lives in `onpage-schema-entity.md`; AI share-of-voice tracking lives in `ai-visibility.md`; the local vertical audit lives in `audits.md`.

## 1. Ground rules

- **Build something worth linking to, then promote it.** Outreach without a reason is spam. Before any link or mention work, ask: which page are you building authority for, and why would someone reference it (tool, unique stat, better guide, comparison)? If there is no reason, say so and fix the page first (`content.md`).
- **Links and mentions both count.** Every outreach should end in a link or a mention. For AI answers, branded mentions matter at least as much as links (section 7).
- **Foundational links = legitimacy, not ranking power.** Social profiles, consistent local citations, GBP, relevant directories prove you exist. They do not move rankings much. Web 2.0 blogs and forum link drops are dropped entirely.
- **Judge the linking PAGE, not the domain.** DR/DA/PA are third-party estimates of a whole site. They are fine for comparing pages that rank (winnability, see `foundations-keywords.md`) and useless for vetting a single link source.
- **Never fabricate**: reviews, testimonials, quotes, journalist names, emails, past articles, data, rankings, test results, authors, AI answers. A fabricated testimonial is a fake review.
- **Drafts only.** Write outreach; never send it, never offer to, never mass-send.
- **Audience wording.** Business owner chasing press: never say "backlink" or "link building" (press is the goal, links a byproduct). Practitioner: plain terms.
- **Leak material** (NavBoost, site-wide quality, entity consistency) describes what Google's systems can store, not confirmed ranking weights. Never quote unpublished thresholds.

## 2. Timeline

| When | Work | Why |
|---|---|---|
| Months 1-2 | Foundational: social profiles, local citations with consistent NAP, relevant directories, GBP, relevant profile listings | Legitimacy and entity confirmation, not ranking power |
| Before serious outreach | Publish your first 10-15 great pages | Nothing to point links at otherwise |
| Month 3+ | Quality: guest posts, niche edits, podcasts, journalist quotes, sparing relevant link exchanges, digital PR | Links are the most expensive lever; good keyword research reduces how many you need |

- **New site:** plan pages that can rank with foundational links only (low-difficulty long tail). Do not make links the foundation, but keep building some.
- **Honest timelines:** NAP fixes 2 to 12 weeks; domain authority compounding 12 to 26 weeks. Prioritize compounding signals over one-off placements.
- **When a competitor with a worse site outranks you**, the gap is usually authority: run competitor prospecting (section 4) and the authority plan (section 5.4).

## 3. Vetting a link source or link offer

Check the specific page the link would sit on.

- [ ] Does the page appear in search for its own distinctive phrases? (indexed and ranking)
- [ ] Is it maintained? (recent dates, comments, named author)
- [ ] Does it have human readers? (shares, replies, page traffic if you have it)
- [ ] Is the site relevant to your topic and market?
- [ ] Editorial standards (would they publish anything for money?), low spam signals
- [ ] Real organic traffic for the domain as a sanity check

**Tier verdict for the linking page:**

| Tier | What it looks like | Worth |
|---|---|---|
| Desk | Ranks and has readers | Real value |
| Shelves | Indexed, no readers | Marginal |
| Basement | No search presence, exists to hold links | Worthless; paying for it violates Google's spam policy |

Google's index uses storage tiers (fast storage for important, updated content), so a link from a page people actually visit is worth more than a link from an unvisited page on the same domain. No link offer to judge? Assess the user's own most-linked page the same way.

`nofollow`, `ugc`, `sponsored` are hints, not hard rules.

**Low value in 2026:** bulk submission, classifieds, bookmarking, article directories, Web 2.0 blogs, PDF/PPT/infographic submission, forum link drops, "500 backlinks/month", daily backlink quotas (SpamBrain risk), press-release wires for links.

**Never:** PBNs, "100 links for $5", vendors who cannot show a client's traffic graph across the engagement, exact-match anchor spam, sockpuppet accounts.

## 4. Link tactics menu

| Tactic | How | Notes |
|---|---|---|
| Be the source | Publish original data (section 5) | Compounds; journalists cite it |
| Outdated-statistic play | Find a stale stat cited by pages linking to a top result, publish a fresh number, email those linkers | Ahrefs reported 27 links and #1 for "SEO statistics" this way (Ahrefs course, 2025-2026; directional) |
| Journalist queries | Source of Sources (free), Featured.com, Qwoted; 15 min/day | Roughly 1 hit per 100 pitches; budget for volume |
| Linkable assets | Calculators, checkers, templates (can be vibe-coded) | Example: "coffee to water ratio calculator" 500/mo, KD 8. Asset pages: `content.md` |
| Broken link building | Find dead pages others link to, offer your live equivalent | Only claim "broken" when verified |
| Guest posts | Find via `"<niche>" "write for us"`; short pitch, 1,000-3,000 words, 1 contextual link to a deep page, real-name bio | One link to a deep page, not the homepage |
| Fan-out pages | Get included on `best`, `top`, `vs`, `review`, `alternative` pages | Section 7.2 |
| Competitor backlink mining | Section 4.1 | Only page-qualified prospects |
| Paid placements | Reputable sites only, `rel="sponsored"` | Disclosed paid, never hidden |
| Community answers | Under a real expert profile | Section 7.3 |
| Press releases | Real news only | Wire links are ignored; the value is pickup and mentions (section 7.6) |
| YouTube | Your own channel and creator collaborations | #2 discovery surface and a top AI Overview source (section 7.4) |
| Unlinked mentions | Ask sites that mention you to link | Every mention is a candidate |

**Tracking sheet** (keep removed rows, they show attrition):

```
Platform | Live URL | Target page | Anchor/keyword | Date | Status (active/pending/removed)
```

Anchors: descriptive and varied. Exact-match anchor repetition is spam.

### 4.1 Competitor backlink prospecting

Goal: turn a competitor's backlink export into a short list of winnable, page-qualified prospects with one angle each and outreach drafts. "Small and real beats long and plausible. Twenty genuine prospects is a better deliverable than two hundred rows."

**Intake**
- Export from Ahrefs, Semrush, Moz or Majestic (Site Explorer or Backlink Analytics > Backlinks > Export), or pasted rows. Needed: source URL, target URL. Decisive extras: linking-page traffic (Ahrefs "Page traffic") and page keyword count. Helpful: anchor, first seen, do-follow, page-level score (UR / Semrush Page ascore).
- Ahrefs quick view: Site Explorer > Backlinks > "One link per domain" > sort New / first seen > then DR.
- Which of your pages are you building links to, and why would someone reference it? "If there is no reason, outreach is spam and I will say so."
- Never invent demo rows. Domain only? You cannot pull backlinks yourself (indexes are proprietary). Offer the search-results path instead (finds resource pages and listicles, not the competitor's profile).

**Method**
1. **Parse and normalize** to: source URL, source domain, target URL, anchor, first seen, do-follow, domain score. Report row count and missing columns.
2. **Dedupe** to one row per linking domain (sitewide links swamp exports); keep the strongest page, record link count.
3. **Drop the unwinnable**, counting per reason:
   - directories, aggregators, listings
   - syndicated press releases and their copies
   - footer, sidebar, blogroll, author-bio links
   - scraped or mirrored copies
   - the competitor's own properties and subdomains
   - forums, comments, UGC profiles
   - paid/sponsored (`rel="sponsored"`, "paid post", "advertorial", ad-heavy template)
   - wrong language or market
   Flag (do not silently drop) direct competitors and paid placements: the user may want to know a rival buys links.
4. **Qualify on page-level performance**, not domain authority (DA only a coarse tiebreak). Use the highest rung available and state it:
   1. page traffic + page keyword count from the export
   2. page-level score (UR / Page ascore)
   3. search a distinctive title phrase (shortlist only, a handful)
   4. mark "unqualified"
   Then check the page is maintained and unchanged since first seen. A high-DA domain with a zero-traffic page is the single most common trap.
5. **One angle per prospect, or drop it:**
   - Broken/dead target (only if status/lost-link columns or a live check show it)
   - Out of date (only after reading the page)
   - Resource page fit
   - Better or fresher data
   - Missing alternative
   - Expert reference
   Unopened pages get "to confirm".
6. **Contact path** (top prospects only): byline, contact or editorial-guidelines page, about/team, masthead, public profile, with the URL where you found it. Never guess emails from name + domain.
7. **One draft per angle** (not per prospect), personalization in [brackets].

**Output**
```
SUMMARY: rows in, after dedupe, dropped per reason, shortlisted; best angle overall; what could not be checked
| Prospect page | Domain | Why it survived | Angle | Ranks for | Contact path | Priority (High/Medium/Low + driver) |
THROWN AWAY: table with counts per reason (evidence the list is small on purpose)
DRAFTS: per angle: subject, body under 120 words, single ask, [variables]
GAPS: missing columns, unchecked items
```

**Edge cases:** under 50 rows → the competitor may have few links; every row survives → export likely pre-filtered, ask; nothing survives → the market is winnable with ordinary editorial links (good news); no target page given → weak relevance, ask before assigning priority; Semrush export without page traffic → fall back to page score and recommend a re-export.

## 5. Digital PR from your own data

Goal: mine a business's own data for newsworthy findings, package a study, write tiered journalist pitches. "You already had the story, it was just sitting in a spreadsheet."

### 5.1 Intake
Raw data (CSV, table or description), industry, target audience, geography (local / national / international), optional wished-for outlets.

### 5.2 Analysis and statistical honesty
Look for: surprising comparisons (regional vs metro, age groups, periods, categories), counterintuitive trends, record or extreme points, seasonal or year-over-year shifts, percentages, averages, rankings. Flag headline material.

- Every number comes from the user's data, with the calculation and sample size shown.
- Description-only data → no numbers. Give angles as questions to test plus the exact data cuts to pull.
- A descriptive one-period or one-group finding may be stated as fact with date range and n: "[X]% of [N] orders, [date range]".
- Mark **Needs more data** for: trends from one period, small-group gaps that may be chance, figures a few records would swing.
- Never generalize customers to a population ("our customers" is not "Americans").
- One-pager uses aggregated, de-identified figures only; remind the user to confirm they may publish and that no customer is identifiable.

### 5.3 Package, target, pitch
1. Study concept: working headline, 2-3 sentence summary, why it matters to the publication's readers, extra data that would strengthen it, quotable study title.
2. Publications: 5-10 types, why each fits, in 3 tiers: industry trades, national press, local/niche.
3. Emails: 3 templates, one per tier (rules in section 6). Follow-up 50 words or fewer.
4. One-pager: shareable, cited data, methodology note, quotable stats.

**Output template**
```
DATA PR + OUTREACH
Business: | Data source: | Records: | Date:

KEY FINDINGS
Finding 1: [headline]
  The data: [numbers, calculation, n, date range]
  Why it's newsworthy:
  Strength: Strong / Moderate / Needs more data
(repeat)

BEST STORY TO PITCH
STUDY CONCEPT: Title / Summary / Key stat / Methodology note
TARGET PUBLICATIONS
  Tier 1 Industry trades
  Tier 2 National/major press
  Tier 3 Local press / niche
OUTREACH EMAIL x3 (Subject + body under 150 words)
FOLLOW-UP (Subject: Re: ..., under 50 words)
DATA STORY ONE-PAGER
OTHER ANGLES IN THE DATA (2-3)
BOTTOM LINE (one sentence)
```

### 5.4 Authority compounding plan (competitor with a worse site outranks you)
Input: business name, primary service, target market, 2 to 3 internal data points. Output:
1. 5 original research ideas from their data
2. 3 highest-leverage digital PR angles
3. Linkable asset structure
4. 90-day roadmap with named target publications (publication names from research, never invented contacts)

Original research standard: method, sample size, charts, limitations, named author, downloadable summary. Two such pieces in a quarter is a solid pace.

## 6. Outreach style guide (all outreach: links, PR, listicles, podcasts)

- Lead with the finding or the value, not the business. "Regional customers spend 38% more per order than metro customers", not "We're an ecommerce business...".
- Key data point in the first two sentences. Frame it for the journalist's or author's audience.
- Reference something specific from the recipient's own work or the outlet's content type.
- One ask per email. The first email starts a conversation; it is not a link demand.
- Length: link and listicle outreach under 120 words; journalist pitches under 150 words; follow-ups 50 words or fewer.
- Banned openers: "I hope this email finds you well", "I thought you might be interested in".
- Human, not PR agency. No hype. Never oversell thin data.
- Honest differentiator in one sentence, and admit real weaknesses (authors ignore hype and trust candor).
- Offer something: the full study or data set, free access, samples, commentary.
- Personalization variables in [brackets]; never invent journalist names, emails or past articles.

**Listicle author prompt** (run after collecting the cited articles):
> "...write a short personalized outreach email to the author. Mention something specific from their piece, state my honest differentiator in 1 sentence, and offer free access plus my real weaknesses. No hype, under 120 words each."

## 7. Brand mentions (the AI-answer layer)

**Why it matters.** AI answers name only 2-3 brands and usually hide their sources, so the goal is to be a named brand, not a ranked link. The brand mentioned most across all retrieved sources tends to win, not the single #1 cited URL. Branded web mentions correlate 0.664 with AI Overview visibility vs DR 0.326 (Ahrefs, 75k brands, 2025), and only 28% of AI mentions are linked (Ahrefs, 2025-2026). The full dated table, including YouTube mentions (0.737 correlation with AI visibility, Ahrefs), is in `foundations-keywords.md` §3.

A mention on a popular domain is not visibility: AI cites specific pages. Pick targets from the niche's actual citations (the source URLs in your AI tracking, `ai-visibility.md`), because every niche differs.

**First-move rule:** if AI tracking shows competitors recommended and you are not, it is a mentions problem (this file). Topics missing = content problem (`content.md`). Formats missing = format problem (usually YouTube).

### 7.1 Mention tiers

| Tier | Target | How to find (Ahrefs) | No-Ahrefs fallback |
|---|---|---|---|
| 1 | Listicles and comparison pages | Content Explorer `<topic> title:best OR title:vs -<YourBrand>`, sort by referring domains | Google `best <category>`, `<competitor> vs`, `<competitor> alternatives`, `<category> review` |
| 2 | Reddit threads that rank | Site Explorer → reddit.com → Organic keywords → Position 1-5 → Include topic | Search `site:reddit.com <topic>` |
| 3 | YouTube, podcasts, LinkedIn | Site Explorer → `www.youtube.com/watch` → Position 1-3 | Search YouTube and podcast directories |

Brand Radar alternative for tier 1: **Cited pages** → filter by Prompt, Contains, Phrase match, any word (OR): `best`, `top`, `vs`, `review`, `alternative`. Or platform → "Others only" for mention opportunities.

### 7.2 Listicles and comparison pages

- Outreach to authors for review or inclusion; offer free samples or access; admit weaknesses.
- **Close each gap two ways:** better content on your site (definitive guide or the comparison page itself) plus outreach to publications already cited, offering commentary or data and asking for inclusion in their next update.
- **ICP-specific and three-way comparisons** ("Giant A vs Giant B vs You") win where giants own the head term; how to build them: `content.md` Step 7, Decision pages. Hand-built pages for real, distinct ICP segments or real competitors, each with its own evidence, are fine; mass templated variants are not.
- "Best X in <niche>" articles on reputable third-party sites.
- **Sense check first: "Do you deserve to show up?"** If a "best CRM" list omits HubSpot, that is strange; if you are not genuinely among the best for a niche, pick a narrower niche. AI answers reflect the real world; tactics only go so far, so building a better business is the durable lever.
- Writing your own listicles: template in `content.md`.
- Buying onto existing sponsored lists: grey-hat section 10.

### 7.3 Reddit and community

- Pick 5-10 relevant subreddits; set alerts (f5bot.com).
- Build genuine presence BEFORE any brand mention.
- Post as yourself: name, where you work, one useful answer. Five good comments can be enough.
- Honest participation beats scale: communities and AI source selection both filter spam.
- "Average Reddit post cited by AI is over a year old" (the AI Visibility Checklist 2026 (focal), directional): target threads that already rank.
- Forum visibility contracted in the May 2026 core update (Reddit, Quora, StackExchange declined); check what your niche's AI answers actually cite before investing.
- Never sockpuppet accounts.

### 7.4 YouTube

- Most cited domain in AI Mode and AI Overviews, ChatGPT's 6th (Ahrefs, 2025-2026, directional). Audit your brand on YouTube; sponsorships and creator collabs count (a creator's "Best X" video is a quick win).
- Own channel answering category questions. Video checklist:
  - [ ] Keyword in title and first description lines
  - [ ] Keyword in video file name and thumbnail file name
  - [ ] Keyword said aloud in the first and last 10 seconds (Google reads audio)
  - [ ] Chapter timestamps with descriptive titles
  - [ ] Retention (no slow intros)
  - [ ] Companion blog post per video, video embedded on the page
  - [ ] Channel URL in Organization `sameAs` (`onpage-schema-entity.md`)
- Keep videos fresh; B2B often has a video gap.

### 7.5 LinkedIn and syndication

- Long-form LinkedIn **articles** (Pulse, not posts) get indexed and cited in AI Overviews for B2B; they sometimes rank within an hour. Rewrite, never copy-paste; publish on the company page and reshare from a personal profile. If an AI Overview cites a LinkedIn article, write a better one.
- Repurpose each strong post: blog → podcast (Spotify, Apple, SoundCloud) → image/carousel (Instagram, Pinterest) → republished article (Medium, LinkedIn Pulse).
- Two expert articles per quarter on third-party sites; pursue mentions from partners, associations, conferences, podcasts, universities, client case studies, publications.
- Use one identical positioning line everywhere you have a profile (homepage, about, LinkedIn/X/Instagram/TikTok, G2, Capterra, Trustpilot, SourceForge, directories, marketplaces, email signature, podcast guest bios). AI builds identity from repeated consistent claims; how to write the line: `ai-visibility.md` section 5.

### 7.6 Press releases

Only for one specific real thing: launch, feature, hire, customer milestone, partnership. Value is pickup and mentions (republished on news sites, Google News), not wire links. Link to pricing or comparison pages, not the homepage.

Prompt:
> "Write a 400 word press release ... third person like a reporter ... first paragraph must answer who, what, and why anyone should care, in under 50 words. Include 1 quote from me that says something substantive, not "we're excited." ... do not add any [facts] I haven't given you ... suggest 3 anchor phrases to link, and which page each should point to, choosing pages I want cited rather than my homepage."

### 7.7 Podcasts

Find shows on listennotes.com. Prompt:
> "...Find me 10 episode angles ... 100 word pitch email with a specific episode title, 3 talking points, and 1 surprising thing ... Rank them from easiest to hardest show to get booked on. Then tell me which 3 of those angles I could film as my own YouTube videos this week..."

### 7.8 Off-site consensus checklist

- [ ] GBP, directories, review platforms claimed; NAP identical (section 8)
- [ ] Listed in industry directories and "best of" roundups
- [ ] Listing descriptions written to AI's stated criteria: ask AI "what do you look for when recommending <product/offer>?" and use the answer to shape descriptions (truthfully)
- [ ] Mentioned in 3+ industry publications
- [ ] Podcast appearances
- [ ] YouTube creator coverage
- [ ] Detailed, outcome-specific reviews (section 9)
- [ ] Ask AIs "what do you know about <brand>?"; trace wrong facts to their source pages and get them corrected at the source

### 7.9 Mention routine

Weekly: check AI answer mentions for target queries → list high-authority sites citing competitors not you → build author/journalist relationships → publish expert content they will reference → work the top 10 mention targets. Monthly: fix wrong information at the source. Staff it with a marketing or community person, not only SEO.

## 8. Local entity, Google Business Profile, NAP

Name/address/phone consistency across the web is how Google confirms a business is one entity; conflicting facts split it. Consistency beats quantity.

### 8.1 Claim and align profiles
Claim: Google Business Profile, Bing Places, Apple Maps (Apple Business Connect), LinkedIn, X, Facebook, Instagram, Pinterest, WhatsApp Business, BBB, and vertical profiles (for agencies/B2B: Clutch, GoodFirms, DesignRush, Trustpilot). Wikipedia only if genuinely notable.

- Identical name, address, phone, description everywhere. Yext (yext.com) pushes one record to hundreds of directories (optional, for scale).
- Drive branded searches (ads, videos, podcasts, offline) to help Google form the entity.
- Link profiles back from the site with `sameAs` (`onpage-schema-entity.md`, `~/.claude/skills/searchos/scripts/entity_schema.py`).

### 8.2 GBP and Bing Places setup (per office)
Categories, services, description, photos, Q&A, tracked links. Collect and answer every review (section 9). GBP performance data and GA4 actions: `measure-refresh.md`.

### 8.3 NAP consistency audit
Ask (verbatim): "Paste your NAPs. Format each one as 'Source: [website / GBP / Yelp / etc]' then the NAP on the next line." Minimum input: website footer, GBP, and 3 directory listings.

Output:
1. Every variant found
2. Every discrepancy that blocks entity confirmation
3. The single canonical version
4. A copy-paste standardized NAP block

"Be ruthless. Even a missing 'Ltd.' or 'Pty Ltd' or a difference in suburb capitalization counts."

```
AUDIT: NAP Consistency (Law 1: how Google measures people)
WHAT I CHECKED: [sources received]
FINDINGS: numbered, most damaging first, each with the evidence from their input
THE FIX THIS WEEK: specific actions, smallest effort first
WHAT THIS DID NOT CHECK: content focus and site-level authority, with one line on when to run those
```

Beyond NAP, keep the same facts everywhere: founding year, offices, services, phone, email, profiles, partnerships, leadership, service areas. Remove or qualify any unproven claim.

## 9. Reviews

### 9.1 Thresholds (different purposes, all valid)

| Situation | Threshold | Consequence |
|---|---|---|
| Per-page proof block | fewer than 3 matching reviews | Page is thin: ask next customers for reviews naming job + place |
| Dedicated reviews page | fewer than 5 reviews total | Premature: "A reviews page with three quotes on it looks worse than no page" |
| Sentiment analysis | under ~10 reviews | Lead with acquisition, not analysis |
| Recency | count the last 90 days | "40 reviews and nothing since March reads as a business that stopped caring" |

### 9.2 Google review policy (applies to every step)
- No buying, no incentives (payment, discounts, free goods), no gating, no discouraging negative reviews, no selective asking.
- Ask every eligible customer (simplest, recommended) or an unbiased selection.
- Never offer anything for removing or changing a review. Fixing the customer's problem is fine; making it conditional on the review is not.
- Negative reviews are data; never hide, delete or suppress them.
- Respect each platform's display and republishing terms.
- Regulated industries (medical, legal, financial, allied health): testimonial rules apply; check before publishing. Australia's Ahpra (Health Practitioner Regulation National Law s133) bans testimonials about clinical care, so use only non-clinical reviews (booking, parking, front desk, wait time).
- Never promise removal, rankings or AI citations.

### 9.3 Review schema (what it will and will not do)
Review snippets are supported for Book, Course, Event, Local business, Movie, Product, Software App, Recipe and creative-work types. A business page about the business itself is not on that list: self-controlled reviews on LocalBusiness/Organization are ineligible for stars, and LocalBusiness review markup is only for sites reviewing OTHER businesses (directories). Never add Review/AggregateRating to your own reviews expecting stars; self-serving review markup is a spam pattern. `aggregateRating` on a product page only when genuine reviews are visible on that page.

### 9.4 The review ladder (order is the product)
Generic "get more reviews" fails because it starts at the ask. Work the rungs in order.

**Intake (verbatim):** "Tell me the business name, the website, and roughly what it sells. Then paste whatever you have: your Google Business Profile reviews, a list of clients, any testimonials sitting in an inbox. If you have nothing to paste that is fine, we start with what I can find and I will tell you what I could not see." Ask for the client list only at rung 2 ("Asking for everything up front is how people abandon").

1. **Inventory**, three searches:
   - Google reviews: count, rating, last-90-days count, which name a specific service (quotable).
   - Brand mentions with no review attached: the cheapest opportunity, and almost nobody looks.
   - Empty review platforms: industry directory, marketplace, partner page, association profile. "An empty profile on a site that already ranks is a gap."
   No web access → give the exact searches. Cannot read Google reviews → ask for a paste (count, rating, latest date); never estimate.
2. **Rank the ask.** Interview: top clients by revenue, recent win, quiet for a year, said something nice by email. Produce a ranked list with a reason per name ("A list of six names with a reason each gets worked. A list of sixty does not."). Ranking decides who gets the bigger personal asks (case study, video, interview); it never decides who is excluded from Google review requests.
3. **Four outreach asks:**
   - Review: short, at the happiest moment (almost never invoice time), name the specific thing.
   - Case study: state the time cost and what they get, name the number, confirm comfort.
   - Video testimonial: length, questions, who edits, where it goes ("Uncertainty is what makes people say no").
   - Interview: frame as a conversation about their results; it yields three rungs from one booking.
4. **Reviews page** to own "<brand> reviews" (else a competitor or directory takes it); only at 5+ reviews; schema per 9.3.
5. **AI-answer rung:** is the brand named in AI answers? List 3-5 queries for the user to run and paste back (`ai-visibility.md`). "Never report your own guess as what an AI tool says." Rungs 1-4 are inputs; nothing forces a citation.

**Output**
1. What you already have (table: source / what's there / missing / worth fixing; ordered by impact, not count: "Ten Google reviews on a dormant profile matter less than one named case study on a page that already gets impressions")
2. The quotable ones (verbatim, first name + date)
3. Who to ask, in order (name, reason, rung, moment)
4. The outreach (4 templates, guesses in brackets)
5. The reviews page (outline + what schema will and will not produce)
6. AI answer check (queries; weakest of rungs 1-4)
7. What I could not check (not optional; name the export or login needed)

**Edge cases:** no website → rungs 1-3; mostly negative → stop the ladder, response strategy + fix the underlying problem; new business, no clients → claim and complete profiles only; existing reviews page → audit it (ranks for brand + "reviews"? quotes real and attributed?).

### 9.5 Review proof on service and location pages
Proof belongs on the page people land on ("People read proof on the page they land on"), and a separate reviews page owns the brand-reviews query. Do both.

**Inputs** (read `./business-context.md` first if it exists):
- Reviews pasted (save as `reviews.txt`, blank line between reviews, name/date/stars on the first line) or CSV/JSON with columns text/review/comment/content/body; name/author/reviewer; date/time/published; rating/stars/score; place/location/profile/branch. Multiple profiles → a `place` column. Never make up, edit or tidy reviews. If the user cannot export: open Business Profile, copy, paste.
- Service page URLs and names (offer to read the menu or sitemap; confirm).
- Optional places and location page URLs.

**Write the keyword lists** in customer words, not jargon. Plumber hot water page: `hot water; hot water system; water heater; no hot water; heat pump; instantaneous`. Avoid keywords that hit general praise ("sales" catches "no sales pitch"; "new" catches everything). Show the table and ask what is missing.

- `services.csv`: `service,url,keywords` (keywords `;`-separated)
- `places.csv`: `place,url,aliases` (e.g. `St Kilda; St Kilda East`)
- Templates: `~/.claude/skills/searchos/scripts/review-proof-assets/services-template.csv` (Hot water systems; Blocked drains `blocked drain;drain;drains;jetter;camera;tree roots;sewer`; Emergency plumbing `emergency;after hours;middle of the night;weekend;same day;burst pipe`; Gas fitting `gas;gas leak;gas fitting;cooktop;gas heater`) and `places-template.csv` (Richmond; St Kilda `st kilda;st kilda east;stkilda`; Brunswick `brunswick;brunswick east;brunswick west`).

**Run** (stdlib, no network, no `--selftest`):
```
python3 ~/.claude/skills/searchos/scripts/review_proof_sorter.py \
  --reviews reviews.csv --services services.csv --places places.csv \
  --business "<Business name>" --out "<workspace>/review-proof-sorter" \
  [--max-quotes 5]
```
Outputs `sorted-reviews.csv`, `proof-blocks.md`, `summary.json`. `--places` is optional; `--out` defaults to `./review-proof-sorter-output`.

**What the script does** (so you can judge its output):
- Term match `(?<![a-z])term(?![a-z])` on lowercased text; place also matches when the review's place field contains an alias (noted "(from the profile it was left on)"). Primary service = most keyword hits.
- Sentence split `(?<=[.!?])\s+(?=[A-Z\"'(])`. Specificity: +2 if a digit, +1 per before/after/since/within/week(s)/month(s)/day(s)/hour(s), +1 if 60-260 chars. Best quote = keyword hits x 3 + specificity (tie → earlier sentence); under 60 chars appends the next sentence.
- Review rank: (rating ≥ 4, hits, specificity, length ≤ 900, rating); missing rating treated as 4.5. Reviews under 4 stars are never used as quotes.
- Customer words: top 8 two-word phrases + 8 single words (count ≥ 2; stopwords, names and business-name tokens removed).
- Block line: `- "<quote>" - <First L.>, Google review, <date>`. Fewer than 3 members → thin note. Empty bucket: "No reviews name this yet. Ask your next few customers for this job to say what you did and where."

**Read and fix the sort (the important part):**
- Move or drop wrong matches. Assign unsorted reviews by meaning; general praise goes to the homepage or About, not a service page.
- Quotes are whole sentences, exact. You may pick a more specific sentence (job, result, timeframe, suburb). Never join across reviews, never cut mid-word, never fix grammar or typos.
- Final: **3-5 quotes per page, most specific first.**

**Hand over per page:** placement near the top, beside or under the main CTA; attribution "first name and last initial, 'Google review', and the month and year", with the block linked to the GBP (no surnames, photos or profile links); customer words to use in headings and copy where true; reviews naming places also go on location pages; thin pages (under 3) → ask the next customers for a review naming job + suburb. Finish with a 3-line summary: pages covered, thin pages, the one page to update first (most traffic or enquiries).

### 9.6 Review sentiment and language mining
Premise: AI tools use review sentiment when describing brands; consistent positives help you get named, unanswered negatives quietly hurt.

**Intake:** reviews from Google, Trustpilot, product reviews, Tripadvisor, Clutch, G2, with star ratings and dates, which already have replies, and the brand's one-line positioning. Few or none → acquisition mode first; never fabricate example reviews.

**Method**
1. **Sentiment map:** positive/neutral/negative by platform and recency; trajectory over 6-12 months (no dates → cannot read trajectory).
2. **Themes:** praise (citable strengths, phrases AI is likely to repeat); complaints split into **fixable operations** (slow shipping) vs **positioning mismatches** (an upstream messaging problem).
3. **Read it as AI does:** write a 2-3 sentence AI-style brand description from the reviews alone, labelled a simulation, then compare to the positioning: aligned / partially aligned / different story. Verify with real AI runs (`ai-visibility.md`).
4. **Response queue:** unanswered negatives ranked by visibility and recency ("fresh unanswered one-star on Google outranks an old one on a quiet platform"); action per item: reply / fix first / follow up after the fix. Drafting per 9.7.
5. **Language mine:** pull-quote bank of 5-10, verbatim, attributed by platform and date; customer-language keywords the site lacks, mapped to pages; objection list → FAQ or product paragraphs.
6. **Acquisition audit:** right moment (post-delivery, post-result), consistent asking, platforms (Google first, then Trustpilot or the vertical platform), low-friction link, reply to every review. Steady requests, not bursts.
7. **Schema:** one line, per 9.3.

**Output:** SENTIMENT MAP (counts/shares, trajectory, reply coverage) → WHAT AI LIKELY SAYS ABOUT YOU → THEMES → RESPONSE PRIORITY QUEUE → THE LANGUAGE MINE → ACQUISITION WORKFLOW GAPS → DO THIS WEEK (top 3). Lead with the AI-description verdict and quote customers constantly.

**Edge cases:** multi-location → per-location map ("one bad location can poison the brand-level story"); review bomb → flag, report, exclude the cluster and say so; service businesses → Google, directories, testimonial emails (permission noted); multi-language → mark untranslated; customers praise something the brand undersells → make it the headline finding and route to positioning.

### 9.7 Handling one negative Google review
Checks Google's policy grounds, drafts a removal request only on a real violation, and always drafts a public response.

**Intake (verbatim first line):** "Paste the full Google review you want me to check. Include the reviewer's name as shown on their Google profile." Paraphrase → ask for exact text; screenshot → ask for typed text; several → one at a time; positive review → a short genuine thank-you; other platforms (Yelp, Facebook, Trustpilot) → the analysis applies, the removal template is Google-only.

**The 11 checks** (Google heading in brackets):
1. Fake engagement / coordinated spam (Fake engagement; Rating manipulation): reviewer rates unrelated businesses nationally, a flood in a narrow window, review-mill profile.
2. Impersonation: naming a real person is not impersonation.
3. Conflict of interest (Rating manipulation or Misrepresentation): employee or ex-employee, competitor, vendor, personal stake. One of the most consistently removable categories when the relationship can be shown.
4. Non-customer (Fake engagement, not a real experience).
5. Misinformation (Misrepresentation): demonstrably false facts (closed dates, prices, services, staff, locations).
6. Off-topic: political, mask/vaccine rants, industry venting, wrong listing.
7. Harassment / offensive / profanity (Harassment; Offensive content; Obscenity and profanity): threats, attacks, unsubstantiated allegations of wrongdoing, profanity. Harsh but respectful criticism is allowed. Defamation is a legal process: a separate legal removal request with legal advice; never call a review "defamatory" in a policy request.
8. Hate speech.
9. Personal information: but names of public-facing professionals working under their own name (doctors, lawyers, real estate agents) and known executives are allowed.
10. Advertising / solicitation.
11. Repetitive / defacement (Unclear and repetitive content; Defacement and mischief).
Other headings (sexually explicit, violent, dangerous/illegal) are flagged under Google's heading when clear.

**Name authenticity** (handle, brand name, initials only like "J.S.", random characters, pseudonym) is a supporting signal only, never a violation, never the lead.

**Workflow:** read → walk the 11 checks using evidence in the text → pick the single strongest category (mention a second briefly, do not stack) → confidence → name flag → removal request only if a violation → public response → no-record response.
- **High:** the text directly evidences it (self-named competitor, declared never visited, slurs, private employee details).
- **Medium:** strong context, no admission.
- **Low:** a single soft signal, or user context missing. A name-only signal is Low at best.

Google rarely removes text-less one-star ratings, honest negative opinions, or disagreement with a service decision: go straight to the public response.

**Output template (verbatim)**
```
REVIEW ANALYSIS
Reviewer name: [name as provided]
Reviewer name assessment: [Realistic identity / Possible authenticity concern (reason)]
POLICY ASSESSMENT
Violation found: Yes / No
Relevant policy category: [one check from the 11, with Google's policy heading, or "None"]
Explanation: [1 to 3 sentences citing the specific text in the review that drove the conclusion]
Confidence: High / Medium / Low
SUGGESTED REMOVAL REQUEST TO GOOGLE (only if Yes)
"Hello Google Support,
We believe this review violates Google's review policies under the category of [policy category].
The review appears to [brief, factual explanation tied to the specific review text]. We respectfully request that this review be re-evaluated and removed if found to be in violation of Google's policies.
Thank you."
HOW TO SUBMIT: Report the review from your Business Profile (open the review, choose Report, pick the reason matching the policy above) or through Google's Reviews Management Tool, where you can also check the report's status. If it is declined, the same tool offers a one-time appeal. Keep the text above for the appeal, or for Business Profile support if you escalate.
PROFESSIONAL REVIEW RESPONSE (public-facing)
[3 sentences maximum. Acknowledge. Give brief context if useful. Invite offline resolution. No arguing, no accusations, no customer-private info.]
ALTERNATIVE RESPONSE (No record of customer)
"Thank you for taking the time to leave feedback. We take every concern seriously, but we have not been able to match your name or the experience described to any record in our system. We would welcome the chance to look into this properly. Please reach out to us at [business contact] so we can understand what happened and put things right."
```

**Rules:** conclusions only from the review text and name; a bad experience is not a violation (no removal request); say "may qualify for removal", never certain; never accuse the reviewer publicly, even when reporting on that basis; response 3 sentences maximum; regulated industries → never confirm the reviewer was a patient or client, no protected information, legal/compliance sign-off.

## 10. Grey-hat tactics (optional, clearly labelled)

Short-term levers that "work for now" and may not last. Use only with these guardrails: disclose your involvement, use a real stated methodology, state the risk to the user, never fabricate reviews, data, rankings, testing or authors.

| Tactic | Guardrail | Risk |
|---|---|---|
| Buying onto existing sponsored listicles. Find them: Site Explorer → competitor → Backlinks → filter **Sponsored** (e.g. "17 Best Accounting Software for Mac Reviewed for 2025"); no Ahrefs: Google `best <category>` / `<competitor> alternatives` and look for "sponsored"/"partner" disclosures | Placement disclosed as sponsored, `rel="sponsored"` | Listicles' weight in AI answers may fade; long game for new players |
| Parasite publishing on Medium, Substack, LinkedIn Articles, Quora | Affiliation disclosed; content genuinely useful | Platform policy and site-reputation-abuse enforcement |
| "Report-style" press release ("<Niche> Industry Report: Top Leaders Ranked 2026") | Only with a real, published, stated methodology; disclose if you are ranked in it | Credibility damage if the method is thin |

Test paid mentions with a test-vs-control experiment (`ai-visibility.md`) before scaling.

## 11. Check that it worked

- New quality third-party mentions: 8-12 in a 90-day program is a solid pace; 2 original research pieces; review workflow active (steady, replies to all).
- Brand appears on the source URLs AI cited for target queries; share of voice up vs baseline (`ai-visibility.md`).
- Branded search rising in Search Console; profile facts correct; NAP identical everywhere; reviews in last 90 days and reply coverage up.

## 12. Report discipline

Read or stop (never grade sources, reviews or AI answers you did not see), never invent data, mark Not checked / UNVERIFIED, one decisive fix per finding, lead with the fix, cap lists, end with **WHAT THIS DID NOT CHECK** (exports or logins needed, platforms not searched, AI answers not run).

Not covered: mention reclamation or broken-link discovery at scale, link velocity / toxic-link assessment; GBP optimization, map rank grids and country directories are in local-international.md; not covered: reply templates for non-Google platforms.
