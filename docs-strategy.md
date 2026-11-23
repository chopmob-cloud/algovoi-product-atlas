# AlgoVoi consolidated documentation approach — GitHub × docs.algovoi.co.uk (AEO/SEO)

> Status: strategy, 2026-11-23. Grounded in live probes of docs.algovoi.co.uk, algovoi.co.uk and
> chopmob-cloud.github.io on 2026-11-23 (see [Live evidence](#live-evidence)). Governs how the whole
> estate's documentation fits together so search engines and answer engines see **one coherent entity,
> one canonical URL per topic, no duplicate content**.

## The principle

**Author once · canonicalise everywhere · link, don't duplicate.**

Every topic has exactly one canonical URL. Every other surface (a GitHub README, the atlas, the hub,
an apex landing page) is a *thin entry point* that links to that canonical URL — or 301/canonicals to
it. This is what stops the five surfaces cannibalising each other in search, consolidates link equity,
and gives answer engines a single, consistent thing to cite.

## The surfaces today (live, 2026-11-23)

| Surface | Role | AEO/SEO state (verified) |
|---|---|---|
| **docs.algovoi.co.uk** | Reference/concept/protocol/compliance docs. **Mintlify**, source = private GitHub `docs` repo. | `llms.txt` (40 KB, answer-first) + `llms-full.txt` live; self-canonical; meta description + OG; JSON-LD Organization/WebSite/BreadcrumbList/WebPage; FAQPage on the VCS pages; sitemap live. |
| **algovoi.co.uk** (apex) | Marketing/commercial/pricing/product landing + store. | `llms.txt` live; same robots Content-Signal; sitemap live; 4-protocol/11-chain consolidation page live. |
| **chopmob-cloud.github.io** | Substrate micro-hub. | `rel=canonical` → `https://algovoi.co.uk/substrate.html` (already points at apex). |
| **GitHub READMEs** (65 public product repos) | Developer entry points: install, quickstart, API. | Mixed; a "Related links" cross-link block was added to some (graph 4551). |
| **algovoi-product-atlas** (this repo) | Product × key-element map / estate navigation. | New; generated from live inventory; needs an `llms.txt` + canonical links out. |

**robots Content-Signal (both canonical hosts):** `search=yes, ai-input=yes, ai-train=no`.
This is a **deliberate** split, not a defect: searchable and usable as an answer-engine *input*
(citable), but not licensed for model *training*. Keep it; the trade-off is conscious (answer-engine
presence preserved, training-corpus inclusion declined). Do not "fix" `ai-train=no`.

## Canonical-home matrix (single source of truth per content type)

| Content type | Canonical home | Every other surface… |
|---|---|---|
| Concepts, protocols (x402/MPP/AP2/A2A), compliance duties, receipt formats, verification how-tos | `docs.algovoi.co.uk/<page>` | README + atlas + apex **link** to the docs page; never copy its body. |
| Product marketing, pricing, buy/self-host, trial | `algovoi.co.uk/<page>` (+ store) | docs `buy-or-self-host` links to the store; README badge links to apex. |
| Per-repo install / quickstart / API surface | the repo's **README** | links to the canonical docs page for depth. |
| Estate navigation / product×element map | **algovoi-product-atlas** | org profile + every README footer link in. |
| Substrate micro-hub | **retire → 301** to `algovoi.co.uk/substrate.html` | it already canonicals there; a 301 finishes the job. |

Rule of thumb: **reference depth lives on docs; commercial intent lives on apex; code entry lives on
GitHub; the map lives in the atlas.** A page that mixes two of these is a cannibalisation risk — split
it and canonicalise.

## AEO layer (answer-engine optimisation)

1. **`llms.txt` + `llms-full.txt` on every canonical host.** docs ✓, apex ✓. **Add to the atlas**
   (generated from `data/atlas.json`, served via GitHub raw) so answer engines can ingest the product
   map. Keep entries answer-first: one line that *answers* "what is this / what does it do", then the link.
2. **Structured data that answers questions.** `FAQPage` / `HowTo` JSON-LD on question-shaped pages
   (already on the VCS pages). Extend to the protocol and concept pages. Every block must parse; count
   them after editing (a malformed block fails silently).
3. **Answer-first page structure.** One H1; a definition lead sentence; H2s that mirror the buyer's
   actual questions; a regulation spine for compliance content (`compliance-duties` already maps each
   duty to the mechanism that discharges it — that is the pattern to copy).
4. **One entity, everywhere.** A single `Organization` JSON-LD `@id` shared across apex + docs, with
   consistent `name` ("AlgoVoi"), `url`, `logo`, and `sameAs` → the GitHub org (and Wikidata/Wikipedia
   if/when present). This is what lets an answer engine resolve "AlgoVoi" to one thing across surfaces.
5. **Keep the Content-Signal split** (`ai-input=yes`, `ai-train=no`) and document it as policy.

## SEO layer

1. **One sitemap per canonical host** (docs ✓, apex ✓); submit to Google Search Console + Bing;
   **IndexNow** on publish (already in use). Submit the *destination* URL, never a redirecting slug.
2. **`rel=canonical` on every canonical page** (docs ✓, hub ✓). Non-canonical surfaces either 301 or
   carry a canonical to the home. No indexable duplicate of a docs page on apex/hub/README.
3. **Meta description + Open Graph** on all canonical pages (docs ✓). Title/description within budget.
4. **Internal-link mesh:** docs ↔ apex ↔ atlas ↔ repos, with descriptive anchors. Each README carries a
   "Related" block (canonical docs page + apex + atlas). This distributes link equity and tells crawlers
   the surfaces are one estate.
5. **READMEs are summaries, not copies.** A README that duplicates a docs page splits ranking signals;
   a README that summarises and links consolidates them.

## GitHub discipline

- **README standard** (apply across the 65 public repos, gated per repo): answer-first one-liner →
  badges → install/quickstart → a **Docs** link to the canonical docs page → a "Part of the AlgoVoi
  substrate" footer linking apex + docs + atlas.
- **Org profile** (`.github`): links to docs, apex, atlas and the flagship repos; consistent entity name.
- **Repo descriptions + topics:** keyword-rich, consistent (mostly already done); add GitHub topics for
  GitHub-search discoverability (`x402`, `ap2`, `a2a`, `algorand`, `post-quantum`, …).
- **The atlas is the GitHub-side canonical map** — link it from the org profile and every README footer.

## Governance / workflow (keep it consolidated)

1. **Author docs once** in the private `docs` repo (Mintlify) → docs.algovoi.co.uk. That is the source of
   truth for reference content; nothing else re-authors it.
2. **Canonical URL registry** (`data/canonical-urls.json` in the atlas): topic → canonical URL. READMEs,
   atlas and apex footers all link from this one registry, so links never drift.
3. **Atlas is generated** from the live inventory (`scripts/build_atlas.py`) — re-run, never hand-edit.
4. **Periodic consistency audit** (`documentation-accuracy-audit` skill) + **SEO/AEO posture sweep**
   (`seo-aeo-measurement-sweep`, existing `aeo_status.py`). Catch drift before it compounds.

## Measurement (prove it, don't assume it)

- **Posture:** `aeo_status.py` (llms.txt/robots/JSON-LD/canonical presence per host).
- **Answer-engine referrals:** `ai_referrals.py` parses apex logs for answer-engine traffic.
- **Search:** GSC + Bing impressions/clicks — **split brand from market**, normalise **per day**, respect
  the **3–4 day GSC lag**, and never call a change "recovered" from impressions alone (check clicks/CTR).
- **Share-of-answer:** the scheduled answer-engine poll (use the scheduled run, not an ad-hoc second
  record under the same date).
- A layout/IA change does **not** create demand — report it as reachability for existing readers, and
  gate any keep/merge/prune decision on page-level impressions + clicks.

## Phased rollout

| Phase | Scope | Gate |
|---|---|---|
| **0 — now (GitHub-side, safe)** | atlas `llms.txt` + this strategy + canonical-URL registry + org-profile/README cross-link standard | docs-only, no production marketing touched |
| **1 — docs repo** | extend FAQPage JSON-LD to protocol/concept pages; every docs page links its repo + atlas; add atlas to docs nav | founder approval + Mintlify build/deploy proof |
| **2 — apex / hub** | retire github.io hub (301 → apex); unify Organization `@id`; apex↔docs↔atlas footer mesh | founder approval + live readback |
| **3 — READMEs** | apply the README standard across the 65 public repos | batched, per-repo `ship-with-proof` |
| **ongoing** | monthly posture sweep + consistency audit | scheduled |

## Decisions for the founder

1. **Canonical split** — keep docs = reference, apex = marketing (recommended), or merge?
2. **`ai-train=no`** — confirm keep (deliberate answer-input/training split).
3. **Retire the github.io hub** (301 → apex/substrate.html)?
4. **README standard rollout** across 65 repos — approve batched, gated?
5. **FAQ JSON-LD extension** in the docs repo — approve?

## Live evidence (probed 2026-11-23)

- `https://docs.algovoi.co.uk/robots.txt` → `Content-Signal: search=yes, ai-input=yes, ai-train=no` + Sitemap.
- `https://docs.algovoi.co.uk/llms.txt` → HTTP 200, 40,163 bytes, answer-first entries linking `.md` versions; `llms-full.txt` → 200.
- `https://docs.algovoi.co.uk/introduction` → self-canonical, meta description, og:title/url/type, JSON-LD (Organization×3, WebSite×2, BreadcrumbList, WebPage, ImageObject). No FAQPage on this page (FAQ lives on the VCS pages).
- `https://docs.algovoi.co.uk/sitemap.xml` → live urlset with lastmod.
- `https://algovoi.co.uk/llms.txt` → 200; `https://algovoi.co.uk/robots.txt` → same Content-Signal + Sitemap.
- `https://chopmob-cloud.github.io/` → `rel=canonical` = `https://algovoi.co.uk/substrate.html`.
- Docs source = private GitHub `docs` repo (Mintlify; `data-mint-head` attributes, `.md` endpoints). `C:/algo/docs` locally is an audits/design workspace, **not** the Mintlify source.
- Prior work cross-checked against the claims graph: 10916 (docs FAQ retrofit + github.io→apex canonical), 10956 (AEO full pass apex+store+docs), 11055/11056 (4-protocol consolidation page), 10767 (Content-Signal policy), 4551 (repo cross-links), 10773 (measurement tooling). These are leads re-proved live above where load-bearing.
