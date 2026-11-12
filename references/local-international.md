# Local and international search

Covers what the merged source skills did not: Google Business Profile (GBP) optimization in depth, local pack and
map rank grids, local citations by country, and hreflang / international setup. Written from standard practice and
Google's own documentation, not from the source skills; re-check any feature that Google changes often (posts, Q&A,
verification methods) against the live GBP help center before promising it.

Related: reviews, NAP audit and profile claiming live in offsite-authority.md; LocalBusiness schema in
onpage-schema-entity.md; local site audits (service pages, location pages, map embed) in audits.md; GBP metrics in
GA4 in measure-refresh.md.

## 1. How local ranking works

Google documents three local ranking factors: **relevance** (how well the profile matches the search), **distance**
(how far the business is from the searcher or the location in the query) and **prominence** (how well known the
business is: reviews, links, mentions, organic rankings). Distance can't be optimized; you can't rank everywhere in a
city from one address. Work on relevance (categories, services, on-site pages) and prominence (reviews, citations,
mentions, links). Organic rankings of the website feed prominence, so local SEO is still site SEO.

The local pack (map + 3 results) and Google Maps rank differently from the blue links: results depend heavily on
where the searcher stands. One "rank" number for a local business is misleading; measure across a grid (section 4).

## 2. Google Business Profile optimization

Work top to bottom; the first three items do most of the work.

| Field | What to do | Why / risk |
|---|---|---|
| **Primary category** | Pick the most specific category that describes the core business ("Bakery", not "Food"; "Emergency plumber" only if that category exists and fits). Check which primary categories the top 3 map results use for the main query. | Strongest controllable relevance signal. |
| Secondary categories | Add only categories for things the business really does. | Each extra category adds relevance for its queries; irrelevant ones dilute and can trigger edits. |
| **Business name** | The real-world name exactly as on signage, invoices and the website. No added keywords or cities. | Keyword-stuffed names break GBP guidelines and lead to suspension or competitor edit reports. |
| **Address vs service area** | Customers visit the location: show the address. Business travels to customers and has no storefront: service-area business, hide the address, list real service areas. | Wrong type is a common suspension cause. |
| Hours | Regular hours plus special hours (holidays, festivals). Keep them right. | Wrong hours generate bad reviews and "closed" signals. |
| Phone + website | Local number if possible; website link to the matching location page (multi-location) or homepage. Add UTM tags (`utm_source=google&utm_medium=organic&utm_campaign=gbp`) so GA4 separates GBP clicks. | Tracking and relevance between profile and page. |
| Services / products | List every service or product with a plain description; menus for food businesses. | Extra relevance text; shows in the profile. |
| Description | Plain description of what, who, where (up to 750 characters). No links, prices, promos or ALL CAPS. | Guideline compliance; minor relevance. |
| Attributes | Set every true attribute (e.g. wheelchair accessible, delivery, dine-in, women-owned). | Filters and AI answers use them. |
| Photos and video | Real photos: exterior (helps people find the door), interior, team, products/work, recent jobs. Add new ones regularly. No stock images. | Engagement and trust; photo EXIF/geotags are not a ranking factor (a common myth). |
| Posts / updates | Post real updates, offers and events (new product, seasonal menu, project done) on a steady cadence; link to the relevant page. | Freshness and conversion on the profile; not a big ranking lever. |
| Booking / messaging / menu links | Connect the booking provider or menu URL if the business takes bookings or orders. | Conversion; shows as an action button. |
| Reviews | Ask every eligible customer, reply to all (see offsite-authority.md review ladder and policy). | Prominence, conversion, and what AI assistants read. |

**Verification and suspensions.** Verification method is chosen by Google (video, postcard, phone, email). A
suspension usually follows a guideline breach (keyword name, wrong address type, virtual office, duplicate listing).
Fix the cause first, then request reinstatement with proof (business registration, utility bill, signage photo,
storefront video). Don't create a new listing to dodge a suspension.

**Duplicates and spam.** Merge or remove duplicate listings (same business, old address). Competitors with keyword-
stuffed names or fake listings can be reported through "Suggest an edit" or Google's Business Redressal Complaint
Form; report with evidence, never retaliate with fake reviews.

**Multi-location.** One profile per real staffed location, each linked to its own location page with unique content
(audits.md, local module), consistent naming pattern ("Brand, Area" only if that is the real signage).

## 3. Local citations and listings

A citation is any listing of the business name, address and phone (NAP). Citations confirm the entity; they are
legitimacy, not ranking power (offsite-authority.md). Priority order:

1. Data sources Google and AI assistants read directly: Google Business Profile, Bing Places, Apple Business Connect,
   Facebook, the industry's dominant platform.
2. Country aggregators and big directories, for example:
   - India: Justdial, Sulekha, IndiaMART (B2B), plus vertical platforms (Zomato and Swiggy for food, Practo for
     clinics, Urban Company for home services, MagicBricks / 99acres for property).
   - US: Yelp, BBB, Data Axle, Foursquare, Nextdoor, Angi / Thumbtack (services).
   - UK: Yell, Thomson Local, Checkatrade / TrustATrader (trades).
3. Local and niche: chamber of commerce, trade associations, local news sites, city directories.

Rules: identical NAP everywhere (run the NAP audit in offsite-authority.md first), same categories and description
line, real photos, no fake addresses. Fix the inconsistent old listings before building new ones. Verify a directory
still exists and is indexed before spending time on it.

## 4. Measuring local rankings: map rank grids

Because results change with the searcher's position, measure each keyword from a grid of points over the service area.

- **Tools**: geogrid rank trackers such as Local Falcon, BrightLocal (Local Search Grid), Local Viking, or similar.
  Set the center on the business, a grid (e.g. 5x5 to 9x9 points) and a radius that matches the real service area
  (a bakery: 1-3 km; a plumber: the whole service region).
- **Read it as**: a heat map of rank per point, plus average rank across points and the share of points where the
  business is in the top 3 (tools name this differently, e.g. ARP, ATRP, SoLV). The top-3 share matters most: only
  the top 3 show in the local pack.
- **Use it to**: see where you are strong (usually close to the address) and weak; compare against the competitors
  who win the weak areas (their category, reviews, proximity); re-run monthly with the same grid, keyword and settings.
- **No-tool fallback**: in Chrome, open DevTools → More tools → Sensors → set a custom location (lat/long), then search
  in an incognito window. Repeat for 5-10 points across the area and record positions. Slow but free; label it a sample.
- Keyword set: 5-15 core "service + area" and "near me" style queries; near-me queries are transactional even without
  buy words.

What the grid can't tell you: why you rank (check categories, reviews count and recency, on-site location page,
proximity), and it measures Google only. For AI assistants, run the local prompts in ai-visibility.md (quick 8-query
check uses city and suburb wording).

## 5. International and multilingual sites (hreflang)

Use hreflang when the same content exists in several languages or for several regions, so Google shows the right
version to each searcher. It is a signal, not a directive.

**URL structure** (pick one, keep it consistent):

| Option | Example | Trade-off |
|---|---|---|
| ccTLD | example.in, example.de | Strongest country signal; separate domains to build and maintain. |
| Subfolder | example.com/hi/, example.com/en-gb/ | Shares the main domain's authority; easiest to run. Usual default. |
| Subdomain | hi.example.com | Works, but treated more like a separate site. |
| Parameters | ?lang=hi | Avoid. |

**hreflang rules**
- Each language/region version lists ALL versions including itself (self-reference), and every version links back
  (return tags). Missing return tags make Google ignore the pair.
- Codes: language in ISO 639-1 (`en`, `hi`, `te`), optional region in ISO 3166-1 alpha-2 (`en-IN`, `en-GB`, not `en-UK`).
  Region alone is invalid.
- Add `x-default` for the fallback page (language selector or global version).
- Each version's canonical points to itself, never to another language version (cross-language canonicals cancel
  hreflang).
- Only point to 200, indexable, canonical URLs (no redirects, noindex or 404s).
- Implement in one place: `<link rel="alternate" hreflang="..." href="...">` in the `<head>`, HTTP headers (for PDFs),
  or the XML sitemap (easiest for large sites). Don't mix methods with conflicting values.

```html
<link rel="alternate" hreflang="en-in" href="https://example.com/en-in/pricing/" />
<link rel="alternate" hreflang="hi-in" href="https://example.com/hi-in/pricing/" />
<link rel="alternate" hreflang="en-gb" href="https://example.com/en-gb/pricing/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/pricing/" />
```

**Content rules**
- Translate fully: titles, meta descriptions, headings, image alt, schema text, navigation. Machine translation is
  fine only if a fluent person reviews it; unreviewed auto-translation at scale is scaled-content risk.
- Localize, not just translate: currency, prices, units, phone formats, addresses, shipping, examples, and the words
  locals actually search (research keywords per language; for India, many people search in Hinglish or English for
  commercial terms and in Hindi/Telugu/Tamil for informational ones, so check the SERP for each).
- Don't auto-redirect by IP or browser language; Googlebot mostly crawls from the US and would only see one version.
  Show a banner suggesting the local version instead.
- Google detects language from visible content, not the `lang` attribute; still set `<html lang>` correctly for
  accessibility and other engines (Bing uses the content-language signal).

**Checks**: crawl with Screaming Frog (hreflang tab: missing return links, non-200 targets, bad codes, missing
self-reference); spot-check with URL Inspection in Search Console; compare GSC performance by country.

**AI search**: AI assistants answer in the user's language and often cite local-language sources. Track prompts in
each target language and market separately (ai-visibility.md prompt library: one series per language/country).

## 6. Local and international audit checklist

- [ ] GBP primary category matches the core service and what top-3 competitors use
- [ ] Real business name, correct address vs service-area setup, correct hours incl. special hours
- [ ] Services/products, description, attributes complete; real photos added in the last 3 months
- [ ] Website link to the matching location page with UTM tags
- [ ] Reviews: steady flow, all replied to (offsite-authority.md)
- [ ] NAP identical on GBP, Bing Places, Apple, Facebook, top country directories
- [ ] Location page per real location with unique content (audits.md local module)
- [ ] LocalBusiness (most specific subtype) schema matching the visible page
- [ ] Grid rank baseline recorded for 5-15 local keywords; re-check monthly
- [ ] International: hreflang complete with return tags, self-reference and x-default; self-canonicals; no IP redirects
- [ ] Each language version fully localized and researched for its own keywords

WHAT THIS DID NOT CHECK applies as usual: say which listings, grids or hreflang sets you actually saw.
