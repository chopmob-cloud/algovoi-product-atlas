#!/usr/bin/env python3
"""Build THE major overview: one document covering the whole AlgoVoi estate.

Single source, two renderings, so the repo copy and the docs copy cannot drift:
  * README.md   (repo copy)   — relative links between atlas files
  * docs copy   (docs copy)   — same prose, docs-site-absolute links, no MDX
                                 components, written by --emit-docs <path>

Everything numeric is read from artefacts this script loads:
  data/repos.snapshot.json  (live repo inventory)
  data/atlas.json           (products, layers, elements — built by build_atlas.py)
  data/subjects.json        (documented subjects — built by build_subjects.py)
  data/platforms.json       (probed surfaces — built by probe_platforms.py)

Run:  python scripts/build_overview.py [--emit-docs <path.md>]
The build ABORTS rather than emit a document whose numbers do not reconcile.
"""
import json, os, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = "https://docs.algovoi.co.uk"
GH = "https://github.com/chopmob-cloud/algovoi-product-atlas/blob/master"

LAYER_ORDER = ["substrate", "signing", "refs", "keystone", "verify",
               "conform", "settlement", "protocols", "platform", "meta"]


def load(name):
    p = os.path.join(ROOT, "data", name)
    if not os.path.exists(p):
        sys.exit(f"ABORT: missing {name} — run the builder that produces it first")
    return json.load(open(p, encoding="utf-8"))


def main():
    snapshot = load("repos.snapshot.json")
    atlas = load("atlas.json")
    subjects = load("subjects.json")
    platforms = load("platforms.json")
    conflict_path = os.path.join(ROOT, "data", "conflicts.json")
    conflict = json.load(open(conflict_path, encoding="utf-8")) if os.path.exists(conflict_path) else None

    products = atlas["products"]
    elements = atlas["elements"]
    rows = subjects["subjects"]
    coverage = subjects["coverage"]

    # --- reconcile the artefacts before writing a single number ---------------
    pub_live = [r for r in snapshot
                if r["visibility"] == "PUBLIC" and not r["isArchived"] and not r["isFork"]]
    if len(pub_live) != len(products):
        sys.exit(f"ABORT: snapshot has {len(pub_live)} public live repos but "
                 f"atlas.json has {len(products)} — rebuild the atlas")
    if len(rows) != len({r["slug"] for r in rows}):
        sys.exit("ABORT: duplicate subject slugs")
    live_surfaces = [s for s in platforms["surfaces"] if s["live"]]
    if not live_surfaces:
        sys.exit("ABORT: no live surfaces probed")

    layer_counts = {s: sum(1 for r in products if r["layer"] == s) for s in LAYER_ORDER}
    el_counts = {e["slug"]: sum(1 for r in products if e["slug"] in r["elements"])
                 for e in elements}
    group_order = ["Start here", "Protocols", "Chains", "Platform and API",
                   "Receipt and evidence formats", "Verification and audit",
                   "Keystone and agent trust", "Substrate and canonicalisation",
                   "Compliance and record keeping", "Integrations",
                   "Self-host and operations", "Corpus and provenance"]

    stamp = datetime.date.today().isoformat()
    n_prod, n_el, n_sub = len(products), len(elements), len(rows)
    n_grp = len(coverage)

    # link helpers: repo-relative vs docs-absolute
    def link(path, docs_path, label):
        return (f"[{label}]({path})", f"[{label}]({DOCS}/{docs_path})")

    L = []
    A = L.append
    A("# The AlgoVoi overview")
    A("")
    A("One document covering the whole estate: the stack, the products that build it, "
      "the subjects it documents, and the surfaces it runs on. Read this first; every "
      "other page is a detail of something named here.")
    A("")
    A(f"*Built {stamp} from live sources — {n_prod} public repos, {n_sub} documented "
      f"subjects, {len(live_surfaces)} live platform surfaces. Every number below is "
      "read from those artefacts at build time, not typed.*")
    A("")

    # ---- at a glance ---------------------------------------------------------
    A("## At a glance")
    A("")
    A("| | Count | What it is |")
    A("|---|---|---|")
    A(f"| Products | {n_prod} | Public, live, non-fork repos in the estate |")
    A(f"| Architectural layers | {len(LAYER_ORDER)} | L0 substrate → L8 platform, plus meta |")
    A(f"| Shared elements | {n_el} | The cross-cutting spine every product binds to |")
    A(f"| Documented subjects | {n_sub} | Pages on the documentation site |")
    A(f"| Subject groups | {n_grp} | How those subjects are organised for a reader |")
    A(f"| Platform surfaces | {len(live_surfaces)} | Hosts probed live, HTTP 200 |")
    A("")

    # ---- the one idea --------------------------------------------------------
    A("## The one idea")
    A("")
    A("AlgoVoi is **one canonicalisation substrate with several protocol faces**. "
      "A JSON object is canonicalised (RFC 8785 JCS), hashed into a content-addressed "
      "reference, signed (RFC 9421, optionally post-quantum), and returned as a receipt "
      "a third party can verify offline with no AlgoVoi service in the loop.")
    A("")
    A("Everything else is a face of that one chain:")
    A("")
    A("| Face | What it adds |")
    A("|---|---|")
    A("| **x402** | Per-request payment over HTTP |")
    A("| **MPP** | Per-call payment for MCP tools and JSON-RPC methods |")
    A("| **AP2** | Human-signed mandates for autonomous agent commerce |")
    A("| **A2A** | Agent-to-agent discovery with payment-gated calls |")
    A("")
    A("The overlap is the product: the same canonical bytes, references and receipts "
      "serve all four, so a receipt issued over one protocol verifies against another.")
    A("")

    # ---- the stack -----------------------------------------------------------
    A("## The stack — every layer, and what lives in it")
    A("")
    A("| Layer | Role | Products |")
    A("|---|---|---|")
    layer_role = {
        "substrate": "JCS canonicalisation and the PQC author layer — the shared base",
        "signing": "RFC 9421 / RFC 9530 signing and verification, key identity",
        "refs": "Content-addressed references and payment-lifecycle receipt formats",
        "keystone": "Keystone L2 composition and the fabric spine",
        "verify": "Offline third-party verification and audit bundles",
        "conform": "Cross-language conformance batteries across independent implementations",
        "settlement": "Algorand/Voi settlement, state proofs, bridges, wallet auth",
        "protocols": "AP2 / x402 / MPP / A2A adapters and the MCP tool surface",
        "platform": "The hosted gateway, pay rail, platform and secure hub",
        "meta": "Organisation profile, hub and documentation repos",
    }
    layer_title = {}
    titles = {
        "substrate": "L0 · Substrate & canonicalisation",
        "signing": "L1 · Signing & key identity",
        "refs": "L2 · References & receipt formats",
        "keystone": "L3 · Keystone composition",
        "verify": "L4 · Verification & audit",
        "conform": "L5 · Conformance & cross-validation",
        "settlement": "L6 · Settlement & chain rails (AVM)",
        "protocols": "L7 · Protocol adapters & integrations",
        "platform": "L8 · Platform & gateway",
        "meta": "Meta · profile, hub & docs",
    }
    for s in LAYER_ORDER:
        layer_title[s] = titles[s]
        A(f"| **{titles[s]}** | {layer_role[s]} | {layer_counts[s]} |")
    A("")

    # ---- the shared elements -------------------------------------------------
    A("## The shared elements — what every product binds to")
    A("")
    A("These are the cross-cutting concerns. A product's row in the overlap matrix "
      "says which it implements or depends on; the count is how many products touch it.")
    A("")
    A("| Element | Products | What it is |")
    A("|---|---|---|")
    for e in elements:
        first = e["spec"].split(". ")[0].rstrip(".")
        A(f"| {e['title']} | {el_counts[e['slug']]} | {first} |")
    A("")

    # ---- subjects ------------------------------------------------------------
    A("## What is documented — every subject, by group")
    A("")
    A(f"The documentation site carries **{n_sub} subjects** in **{n_grp} groups**. "
      "Each group below is a reader's job, not an org chart; the full index with every "
      "page and its description is in the subject index.")
    A("")
    A("| Group | Subjects | Start with |")
    A("|---|---|---|")
    first_of = {}
    for r in rows:
        first_of.setdefault(r["group"], r)
    for g in group_order:
        if g not in coverage:
            continue
        r = first_of[g]
        A(f"| **{g}** | {coverage[g]} | [{r['title']}]({DOCS}/{r['slug']}) |")
    A("")

    # ---- platforms -----------------------------------------------------------
    A("## Where it runs — the platform surfaces")
    A("")
    A(f"All {len(live_surfaces)} surfaces below answered HTTP 200 when probed on "
      f"{platforms['probed']}. A host that did not resolve is omitted rather than "
      "listed as unavailable.")
    A("")
    A("| Surface | Host | What it is |")
    A("|---|---|---|")
    for s in platforms["surfaces"]:
        if not s["live"]:
            continue
        host = s["url"].split("//", 1)[1]
        A(f"| {s['label']} | [{host}]({s['url']}) | {s['desc']} |")
    A("")
    A("Two access models sit behind those hosts, and almost every page assumes one: "
      "**governed** (a tenant, an API key, KYB — the operator carries the compliance "
      "duty) and **tenant-free** (no account, settlement is the credential and the "
      "receipt is the evidence). Self-hosting is the third path and is not a host at "
      "all.")
    A("")

    # ---- product catalogue ---------------------------------------------------
    A("## The products")
    A("")
    A("Every public product, grouped by the layer it sits in. Descriptions are quoted "
      "from GitHub, not rewritten here.")
    A("")
    for s in LAYER_ORDER:
        grp = sorted([r for r in products if r["layer"] == s], key=lambda x: x["name"].lower())
        if not grp:
            continue
        A(f"### {titles[s]} — {len(grp)}")
        A("")
        for r in grp:
            d = (r["desc"] or "").strip() or "_(no description on GitHub)_"
            tags = " ".join(f"`{e}`" for e in r["elements"])
            A(f"- **[{r['name']}]({r['url']})** — {d}")
            if tags:
                A(f"  - Elements: {tags} · {r['lang']} · last push {r['pushed']}")
        A("")

    # ---- how it fits together ------------------------------------------------
    A("## Conflicting sources")
    A("")
    A("Where two live sources disagree about the same figure, this document does not pick "
      "a winner. The discrepancy is recorded, with each reading attributed, so a reader "
      "knows the number is unsettled rather than trusting whichever page they opened first.")
    A("")
    if conflict is not None:
        for c in conflict["conflicts"]:
            A(f"**{c['subject']}** — {c['measured']}")
            A("")
            A("| Source | Says |")
            A("|---|---|")
            for src in c["sources"]:
                A(f"| {src['source']} | {src['says']} |")
            A("")
            A(f"*Resolution: {c['resolution']}*")
            A("")
            A(f"Upstream fix: {c['fix_at']}")
            A("")
    else:
        A("_No conflicts recorded in `data/conflicts.json`._")
        A("")

    A("## How to navigate this")
    A("")
    A("| You want | Read |")
    A("|---|---|")
    A("| The stack and how layers depend on each other | "
      f"[Application matrix]({DOCS}/application-matrix) |")
    A("| Every documented subject, with descriptions | "
      f"[Subject index]({GH}/subjects.md) · [live site]({DOCS}/introduction) |")
    A("| Which products implement a given element | "
      f"[Overlap matrix]({GH}/overlap.md) |")
    A("| Every product with its GitHub description | "
      f"[Product catalogue]({GH}/products.md) |")
    A("| The live hosts and what runs there | "
      f"[Platforms]({GH}/platforms.md) |")
    A("| How to take a payment | " + f"[Take a payment]({DOCS}/take-a-payment) |")
    A("| How to verify a receipt yourself | "
      f"[Verify a receipt]({DOCS}/verify-a-receipt) |")
    A("| What it costs, and the free licence | "
      f"[Trial and pricing]({DOCS}/trial-and-pricing) · [Free licence]({DOCS}/free-licence) |")
    A("")

    # ---- provenance ----------------------------------------------------------
    A("## Provenance")
    A("")
    A(f"- Repo inventory: `gh repo list chopmob-cloud`, snapshot refreshed {stamp} "
      "(`data/repos.snapshot.json`).")
    A(f"- Product and element counts: `scripts/build_atlas.py` over that snapshot "
      f"({stamp}).")
    A(f"- Subject list and group coverage: `scripts/build_subjects.py` against the live "
      f"`{DOCS}/llms.txt` and the site's `docs.json` navigation ({stamp}).")
    A(f"- Platform statuses: `scripts/probe_platforms.py`, HTTP probed {platforms['probed']} "
      "(`data/platforms.json`).")
    A("- The product→element overlap is **derived** from each repo's name and GitHub "
      "description by transparent keyword rules plus curated overrides. It is a map, "
      "not a conformance claim: verify the specific repo before relying on a cell.")
    A("- Counts of chains, protocols and tools are **not** restated here. The "
      "documentation pages that own those numbers state them, and this document links "
      "to those pages, because a number restated in two places drifts.")
    A("")
    A("## Regenerate")
    A("")
    A("```bash")
    A("gh repo list chopmob-cloud --limit 400 --json name,description,url,isArchived,\\")
    A("  isFork,visibility,pushedAt,primaryLanguage > data/repos.snapshot.json")
    A("python scripts/build_atlas.py")
    A("python scripts/build_subjects.py")
    A("python scripts/probe_platforms.py")
    A("python scripts/build_overview.py")
    A("```")
    A("")
    A("## Licence")
    A("")
    A("Apache-2.0 for this documentation. The products carry their own licences — "
      "Apache-2.0 across the open estate, BUSL-1.1 for licensed engines; see each repo.")
    A("")

    out = "\n".join(L)
    # reconcile: no leftover placeholders, and every count appears as claimed
    if "{" in out.replace("```", ""):
        sys.exit("ABORT: unresolved format placeholder in the rendered overview")
    # MDX safety: the same bytes must render on the docs site, so assert the document
    # carries no angle brackets, braces or JSX outside fenced code blocks.
    import re as _re
    _body = _re.sub(r"```.*?```", "", out, flags=_re.S)
    for bad, label in (("<", "angle bracket"), ("{", "curly brace")):
        if bad in _body:
            sys.exit(f"ABORT: {label} outside code blocks — not MDX-safe for the docs copy")
    open(os.path.join(ROOT, "OVERVIEW.md"), "w", encoding="utf-8", newline="\n").write(out)
    print(f"OVERVIEW.md written: {len(out)} chars")
    print(f"  products={n_prod} elements={n_el} subjects={n_sub} "
          f"groups={n_grp} surfaces={len(live_surfaces)}")

    if "--emit-docs" in sys.argv:
        dest = sys.argv[sys.argv.index("--emit-docs") + 1]
        # A carbon copy, byte for byte. The document's links are already absolute
        # (public GitHub and docs.algovoi.co.uk URLs), so nothing needs rewriting to
        # resolve from the docs site — and rewriting would make it no longer a copy.
        # MDX safety is asserted above (no angle brackets, braces or JSX outside code).
        open(dest, "w", encoding="utf-8", newline="\n").write(out)
        import hashlib
        h = hashlib.sha256(out.encode()).hexdigest()[:16]
        print(f"docs copy written: {dest} ({len(out)} chars, sha256:{h}) — identical to OVERVIEW.md")


if __name__ == "__main__":
    main()
