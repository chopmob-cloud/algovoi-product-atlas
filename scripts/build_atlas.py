#!/usr/bin/env python3
"""Build the AlgoVoi Product Atlas from a live repo-inventory snapshot.

Grounding: data/repos.snapshot.json is `gh repo list chopmob-cloud --limit 200
--json name,description,url,isArchived,isFork,visibility,pushedAt,primaryLanguage`
captured 2026-11-23. Product descriptions are quoted from GitHub, not invented.
The product->element overlap is DERIVED from each description/name by the
transparent keyword rules below, plus a small curated override map for the
active core. Re-run after refreshing the snapshot:

    gh repo list chopmob-cloud --limit 200 --json name,description,url,isArchived,isFork,visibility,pushedAt,primaryLanguage > data/repos.snapshot.json
    python scripts/build_atlas.py

This repo is DOCUMENTATION ONLY. It carries no sellable code.
"""
import json, os, datetime, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(ROOT, "data", "repos.snapshot.json")
STAMP = datetime.date.today().isoformat()

# --- The key architectural elements (the shared spine) -----------------------
ELEMENTS = [
    ("jcs",        "JCS canonicalisation (RFC 8785)",
     "RFC 8785 JSON Canonicalization Scheme. One deterministic byte form for a JSON object, so two parties hash the same thing. The base every reference and receipt binds to."),
    ("refs",       "Content-addressed references",
     "Deterministic SHA-256-over-JCS identifiers (action_ref, card_ref, task_ref, artifact_ref, delegation/journey/revocation refs). Tamper-evident, offline-checkable, no JWS/JWKS required to resolve."),
    ("rfc9421",    "RFC 9421 HTTP signatures + RFC 9530 Content-Digest",
     "HTTP Message Signatures and Content-Digest. Ed25519 (+ECDSA P-256/P-384) signing/verification of requests and responses, with SSRF-guarded keyid resolution."),
    ("pqc",        "Post-quantum cryptography",
     "ML-DSA / ML-KEM (NIST FIPS 203/204) and Falcon-1024 (FIPS 206), classical+PQ hybrid. The substrate-author layer and the licensed AV-VCS engine; classical path stays usable when PQ is absent."),
    ("receipts",   "Payment-lifecycle receipt / evidence formats",
     "payment-mandate, settlement-attestation, refund, cancellation, Payment Evidence Frame (PEF), composite trust-query. Signed, fail-closed, offline-verifiable evidence of a payment decision or outcome."),
    ("keystone",   "Keystone composition (L2) / Fabric spine",
     "The Keystone SDK and the algovoi-fabric composition spine: bind authority -> policy -> decision -> delegation -> outcome into one tamper-evident, fail-closed chain."),
    ("conformance","Cross-language conformance / cross-validation",
     "Signed, byte-for-byte conformance batteries across independent implementations. A planted mutant must fail; the bytes decide, not the prose."),
    ("verify",     "Offline third-party verification / audit",
     "Standalone verifiers and audit bundles a relying party can run with no AlgoVoi service in the loop: verify.algovoi.co.uk, verify-it-yourself, evidence readers, reseal-verify."),
    ("keyid",      "Key identity / DID / credential binding",
     "did:key / did:web resolution, key-to-credential binding (RFC 9421), key hygiene / primality soundness, rotation lineage. Who a key is, and what it is allowed to sign."),
    ("settlement", "On-chain settlement / state proofs / bridges (AVM)",
     "Algorand & Voi mesh settlement receipts argued from state proofs, portable proofpacks, mainnet bridges, consensus blocklist, multi-chain wallet auth."),
    ("protocols",  "Agent payment protocols (AP2 / ACP / x402 / MPP / A2A)",
     "Adapters and reference implementations for the agent-payment protocols: AP2 mandates, ACP checkout, x402 paid HTTP, MPP, A2A message/artifact/task refs, MCP tool surface."),
    ("gateway",    "Hosted gateway / pay rail / platform adapters",
     "The hosted x402 gateway (api.algovoi.co.uk), the pay rail (pay.algovoi.co.uk), the platform, and the ecommerce / marketplace / AI-agent / no-code adapters."),
]
EL_SLUGS = [e[0] for e in ELEMENTS]

# --- Architectural layers (for grouping the catalogue) ----------------------
LAYERS = [
    ("substrate",  "L0 · Substrate & canonicalisation"),
    ("signing",    "L1 · Signing & key identity"),
    ("refs",       "L2 · References & receipt formats"),
    ("keystone",   "L3 · Keystone composition (flagship)"),
    ("verify",     "L4 · Verification & audit"),
    ("conform",    "L5 · Conformance & cross-validation"),
    ("settlement", "L6 · Settlement & chain rails (AVM)"),
    ("protocols",  "L7 · Protocol adapters & integrations"),
    ("platform",   "L8 · Platform & gateway"),
    ("meta",       "Meta · profile, hub & docs"),
]
LAYER_MAP = {
    "algovoi-substrate":"substrate", "algovoi-substrate-pqc":"substrate",
    "substrate-comparisons":"substrate", "algovoi-keyhygiene-conformance":"substrate",
    "algovoi-rfc9421-signer":"signing", "algovoi-rfc9421-verifier":"signing",
    "algovoi-rfc9421-verifier-go":"signing", "algovoi-rfc9421-verifier-rs":"signing",
    "algovoi-rfc9421-ecdsa":"signing", "algovoi-rfc9421-keyid":"signing",
    "algovoi-rfc9421-a2a":"signing", "algovoi-key-credential-binding":"signing",
    "AlgoVoi-A2A-Card":"refs", "AlgoVoi-A2A-Task":"refs", "AlgoVoi-A2A-Artifact":"refs",
    "algovoi-delegation-ref":"refs", "algovoi-journey-ref":"refs", "algovoi-revocation-ref":"refs",
    "algovoi-pef":"refs", "algovoi-probityai":"refs", "algovoi-receipt-verifier":"refs",
    "algovoi-webhook-verifier":"refs", "algovoi-receipt-sentinel":"refs",
    "algovoi-keystone":"keystone", "algovoi-keystone-alias":"keystone",
    "AlgoVoi-Keystone-Connectors":"keystone", "algovoi-fabric":"keystone",
    "algovoi-audit-verifier":"verify", "algovoi-verify-it-yourself":"verify",
    "algovoi-evidence-readers":"verify", "algovoi-reseal-verify":"verify", "algovoi-vcs":"verify",
    "algovoi-jcs-conformance-vectors":"conform", "algovoi-rfc9421-conformance":"conform",
    "algovoi-crest-joint-harness":"conform", "algovoi-ube":"conform", "ap2-pq-conformance":"conform",
    "avm-mesh":"settlement", "avm-proofpack":"settlement", "avm-proofpack-ts":"settlement",
    "avm-ac2":"settlement", "avm-algo-voi-bridge":"settlement", "avm-voi-algo-bridge":"settlement",
    "avm-hbar-bridge-relayer":"settlement", "avm-wormhole-ntt-relayer":"settlement",
    "avm-algovoi-falcon":"settlement", "avm-effectproof":"settlement",
    "algovoi-consensus-blocklist":"settlement", "algovoi-multi-chain-wallet-auth":"settlement",
    "AlgoVoi-Platform-Adapters":"protocols", "AlgoVoi-MCP-Server":"protocols",
    "algovoi-a2a-glink":"protocols", "algovoi-compliance-gate-a2a":"protocols",
    "elizaos-plugin-algovoi":"protocols", "use-wallet-algovoi":"protocols",
    "algovoi-reference-agent":"protocols", "algovoi-atb":"protocols", "algovoi-recurr":"protocols",
    "algovoi-platform":"platform", "algovoi-secure-hub":"platform",
    ".github":"meta", "chopmob-cloud":"meta", "chopmob-cloud.github.io":"meta",
    "Content":"meta", "algovoi-keystone-sdk":"meta",
}

# --- Transparent element classifier (keyword rules on name+description) -----
RULES = {
    "jcs":        ["jcs", "rfc 8785", "canonicaliz", "canonicalis"],
    "refs":       ["content-addressed", "action_ref", "card_ref", "task_ref", "artifact_ref"],
    "rfc9421":    ["rfc 9421", "rfc9421", "content-digest", "rfc 9530", "message signature"],
    "pqc":        ["post-quantum", "falcon", "ml-dsa", "ml-kem", "pqc", "dilithium", "hybrid", "pq-safe", "pqsafe"],
    "receipts":   ["receipt", "attestation", "refund", "cancellation", "payment evidence", "payment-lifecycle", "mandate", "pef"],
    "keystone":   ["keystone", "fabric", "composition"],
    "conformance":["conformance", "cross-validat", "cross-language", "byte-parity", "byte-for-byte",
                   "byte-anchor", "cross-implementor", "byte-f", "12-way", "ten independent", "10 language"],
    "verify":     ["verifier", "verify", "verification", "audit", "offline-verifiable", "don't trust", "verify us"],
    "keyid":      ["keyid", "did:key", "did:web", "key-to-credential", "credential binding",
                   "key hygiene", "keyhygiene", "primality", "key registry", "rotation", "key-soundness"],
    "settlement": ["bridge", "mesh", "state proof", "relayer", "wormhole", "ntt", "blocklist",
                   "wallet auth", "treasury", "logicsig", "proofpack", "settlement receipt",
                   "on-chain transfer", "settlement-attestation"],
    "protocols":  ["a2a", "ap2", "x402", "mpp", "acp", "mcp", "agent-to-agent", "elizaos", "gibberlink", "agent payment"],
    "gateway":    ["gateway", "platform", "adapter", "ecommerce", "marketplace", "no-code", "pay rail", "secure-hub", "payment tools"],
}
# Curated overrides for the active core (add elements the keywords miss).
OVERRIDES = {
    "algovoi-fabric": ["jcs","refs","rfc9421","pqc","receipts","keystone","conformance","verify","protocols"],
    "algovoi-substrate": ["jcs","refs","receipts","verify"],
    "algovoi-substrate-pqc": ["jcs","pqc","conformance"],
    "algovoi-pef": ["jcs","refs","receipts","rfc9421"],
    "algovoi-jcs-conformance-vectors": ["jcs","conformance","protocols"],
    "algovoi-rfc9421-conformance": ["rfc9421","conformance"],
    "AlgoVoi-MCP-Server": ["protocols","gateway","receipts"],
    "algovoi-platform": ["gateway","settlement","pqc","receipts","protocols"],
    "algovoi-keystone": ["keystone","jcs","refs","verify"],
    "algovoi-audit-verifier": ["verify","receipts","jcs"],
    "avm-mesh": ["settlement","receipts","verify"],
    "avm-ac2": ["settlement","receipts","keystone"],
    "algovoi-reference-agent": ["settlement","receipts","protocols"],
    "algovoi-evidence-readers": ["verify","conformance"],
    "algovoi-vcs": ["verify","receipts","pqc"],
    "substrate-comparisons": ["conformance","jcs"],
    "algovoi-recurr": ["receipts","gateway"],
    "avm-effectproof": ["settlement","verify"],
}

def classify(name, desc):
    hay = (name + " " + desc).lower()
    hits = [slug for slug, kws in RULES.items() if any(k in hay for k in kws)]
    # name-based ref detection for the *-ref / A2A reference family
    if name.lower().endswith("-ref") or name in ("AlgoVoi-A2A-Card","AlgoVoi-A2A-Task","AlgoVoi-A2A-Artifact"):
        hits.append("refs"); hits.append("jcs")
    if name in OVERRIDES:
        hits = list(OVERRIDES[name])
    # de-dup, keep canonical order
    return [s for s in EL_SLUGS if s in set(hits)]

def main():
    repos = json.load(open(SNAP, encoding="utf-8"))
    prod = [r for r in repos if r["visibility"]=="PUBLIC" and not r["isArchived"] and not r["isFork"]]
    prod.sort(key=lambda r: r["name"].lower())
    records = []
    for r in prod:
        name = r["name"]
        desc = (r.get("description") or "").strip()
        lang = (r.get("primaryLanguage") or {}).get("name") or "—"
        els = classify(name, desc)
        records.append({
            "name": name, "url": r.get("url") or f"https://github.com/chopmob-cloud/{name}", "lang": lang,
            "pushed": r["pushedAt"][:10], "desc": desc,
            "layer": LAYER_MAP.get(name, "meta"), "elements": els,
        })
    os.makedirs(os.path.join(ROOT,"elements"), exist_ok=True)
    write_readme(records)
    write_elements(records)
    write_products(records)
    write_overlap(records)
    write_llms(records)
    write_canonical()
    json.dump({"generated": STAMP, "source": "gh repo list chopmob-cloud",
               "products": records,
               "elements":[{"slug":s,"title":t,"spec":d} for s,t,d in ELEMENTS]},
              open(os.path.join(ROOT,"data","atlas.json"),"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"products={len(records)} elements={len(ELEMENTS)} layers={len(LAYERS)}")
    print("element coverage:", {s:sum(1 for r in records if s in r['elements']) for s in EL_SLUGS})

def el_link(slug):
    t = next(t for s,t,_ in ELEMENTS if s==slug)
    return f"[{t}](elements/{slug}.md)"

def write_readme(records):
    n=len(records)
    lines = [
        "# AlgoVoi Product Atlas",
        "",
        f"> Documentation-only map of **every public AlgoVoi product** ({n} repos) and how each overlaps the",
        "> key architectural elements. Generated from the live GitHub inventory on " + STAMP + ".",
        "> **No sellable code lives here** — this is the documentation layer over the estate.",
        "",
        "## Start here",
        "",
        "**[The AlgoVoi overview](OVERVIEW.md)** — one document covering the whole estate: the stack, the",
        "products, the documented subjects and the live platforms. Every number in it is read from these",
        "artefacts at build time.",
        "",
        "## How to read this atlas",
        "",
        "Three axes:",
        "",
        "0. **The overview** — [`OVERVIEW.md`](OVERVIEW.md) is the single front door; read it first.",
        "1. **Products by layer** — [`products.md`](products.md) groups every repo into the architectural stack (L0 substrate → L8 platform).",
        "2. **Products × key elements** — [`overlap.md`](overlap.md) is the matrix: which shared elements each product implements or depends on.",
        "",
        "And two indexes over the documentation itself:",
        "",
        "- [`subjects.md`](subjects.md) — every documented subject on docs.algovoi.co.uk, grouped by reader's job.",
        "- [`platforms.md`](platforms.md) — the live host surfaces, with the HTTP status each returned when probed.",
        "",
        "Each key element also has its own page under [`elements/`](elements/) listing the products that touch it.",
        "",
        "See also: [`docs-strategy.md`](docs-strategy.md) — the consolidated GitHub × docs.algovoi.co.uk AEO/SEO approach ·",
        "[`llms.txt`](llms.txt) — answer-engine ingest · [`data/canonical-urls.json`](data/canonical-urls.json) — canonical URL registry.",
        "",
        "## The stack",
        "",
        "| Layer | What it is |",
        "|---|---|",
    ]
    layer_desc = {
        "substrate":"JCS canonicalisation + the PQC author layer — the shared base.",
        "signing":"RFC 9421 / RFC 9530 signing & verification, keyid resolution, key identity.",
        "refs":"Content-addressed references and payment-lifecycle receipt formats.",
        "keystone":"Keystone L2 composition and the **algovoi-fabric** flagship spine.",
        "verify":"Offline, third-party verification and audit bundles.",
        "conform":"Cross-language conformance batteries across independent implementations.",
        "settlement":"Algorand/Voi settlement, state proofs, bridges, wallet auth (AVM).",
        "protocols":"AP2 / ACP / x402 / MPP / A2A adapters and the MCP tool surface.",
        "platform":"The hosted gateway, pay rail, platform and secure hub.",
        "meta":"Organisation profile, substrate hub and documentation repos.",
    }
    for slug,title in LAYERS:
        cnt=sum(1 for r in records if r["layer"]==slug)
        lines.append(f"| **{title}** | {layer_desc[slug]} ({cnt}) |")
    lines += ["", "## The key elements", ""]
    for s,t,d in ELEMENTS:
        cnt=sum(1 for r in records if s in r["elements"])
        lines.append(f"- **[{t}](elements/{s}.md)** — {cnt} products. {d.split('. ')[0]}.")
    lines += [
        "", "## Provenance & method", "",
        f"- Source: `gh repo list chopmob-cloud` snapshot, {STAMP} (`data/repos.snapshot.json`).",
        "- Product descriptions are quoted from GitHub; they are not rewritten here.",
        "- The product→element overlap is **derived** from each description/name by transparent keyword rules plus a curated override map for the active core (`scripts/build_atlas.py`). It is a map, not a conformance claim — verify against each repo before relying on a specific cell.",
        "- Active-core facts (Fabric, AP2 v0.2, payment-mandate hardening) are cross-checked against the AlgoVoi claims graph; see the 7-day plan for their trust states.",
        "", "## Regenerate", "",
        "```bash",
        "gh repo list chopmob-cloud --limit 200 --json name,description,url,isArchived,isFork,visibility,pushedAt,primaryLanguage > data/repos.snapshot.json",
        "python scripts/build_atlas.py",
        "```",
        "", "## Licence", "",
        "Apache-2.0 (documentation). The products themselves carry their own licences — Apache-2.0 for the open estate, BUSL-1.1 / commercial for the licensed engines; see each repo.",
        "",
    ]
    open(os.path.join(ROOT,"README.md"),"w",encoding="utf-8").write("\n".join(lines))

def write_elements(records):
    for s,t,d in ELEMENTS:
        users=[r for r in records if s in r["elements"]]
        L=[f"# {t}","",d,"",f"## Products that touch this element ({len(users)})","",
           "| Product | Layer | Language | Last push |","|---|---|---|---|"]
        for r in sorted(users,key=lambda x:x["name"].lower()):
            lt=next(tt for ss,tt in LAYERS if ss==r["layer"])
            L.append(f"| [{r['name']}]({r['url']}) | {lt} | {r['lang']} | {r['pushed']} |")
        L+=["","[← Back to the atlas](../README.md) · [Overlap matrix](../overlap.md)",""]
        open(os.path.join(ROOT,"elements",f"{s}.md"),"w",encoding="utf-8").write("\n".join(L))

def write_products(records):
    L=["# Product catalogue (by architectural layer)","",
       f"All {len(records)} public AlgoVoi product repos, {STAMP}. Descriptions quoted from GitHub.","",
       "Element tags link to the [key elements](README.md#the-key-elements); see [overlap.md](overlap.md) for the full matrix.",""]
    for slug,title in LAYERS:
        grp=[r for r in records if r["layer"]==slug]
        if not grp: continue
        L+=[f"## {title}","",f"{len(grp)} repos.",""]
        for r in sorted(grp,key=lambda x:x["name"].lower()):
            tags=" ".join(f"[`{e}`](elements/{e}.md)" for e in r["elements"]) or "_(no element tags derived)_"
            desc=r["desc"] or "_(no description on GitHub)_"
            L+=[f"### [{r['name']}]({r['url']})",
                f"{desc}",
                f"- **Language:** {r['lang']} · **Last push:** {r['pushed']}",
                f"- **Elements:** {tags}",""]
    open(os.path.join(ROOT,"products.md"),"w",encoding="utf-8").write("\n".join(L))

def write_overlap(records):
    L=["# Product × key-element overlap matrix","",
       f"{len(records)} products × {len(ELEMENTS)} elements, {STAMP}. `●` = the product implements or depends on the element (derived from its description/name; see [method](README.md#provenance--method)).","",
       "Columns: " + " · ".join(f"`{s}`" for s in EL_SLUGS),"",
       "| Product | " + " | ".join(EL_SLUGS) + " |",
       "|---|" + "---|"*len(EL_SLUGS)]
    layer_idx = {s:i for i,(s,_) in enumerate(LAYERS)}
    for r in sorted(records,key=lambda x:(layer_idx.get(x["layer"],99),x["name"].lower())):
        cells=" | ".join("●" if s in r["elements"] else "·" for s in EL_SLUGS)
        L.append(f"| [{r['name']}]({r['url']}) | {cells} |")
    L+=["","## Element coverage","", "| Element | Products |","|---|---|"]
    for s,t,_ in ELEMENTS:
        L.append(f"| [{t}](elements/{s}.md) | {sum(1 for r in records if s in r['elements'])} |")
    L+=["","[← Back to the atlas](README.md)",""]
    open(os.path.join(ROOT,"overlap.md"),"w",encoding="utf-8").write("\n".join(L))

# Canonical URL registry — topic -> the ONE canonical URL (grounded in the live
# docs.algovoi.co.uk/llms.txt and apex, probed 2026-11-23). READMEs/atlas/apex
# footers link from this registry so links never drift. See docs-strategy.md.
CANONICAL = {
    "introduction": "https://docs.algovoi.co.uk/introduction",
    "protocols-and-chains": "https://docs.algovoi.co.uk/protocols-and-chains",
    "x402": "https://docs.algovoi.co.uk/protocols/x402",
    "mpp": "https://docs.algovoi.co.uk/protocols/mpp",
    "ap2": "https://docs.algovoi.co.uk/protocols/ap2",
    "a2a": "https://docs.algovoi.co.uk/protocols/a2a",
    "solana-actions": "https://docs.algovoi.co.uk/protocols/solana-actions",
    "verify-a-receipt": "https://docs.algovoi.co.uk/verify-a-receipt",
    "compliance-duties": "https://docs.algovoi.co.uk/compliance-duties",
    "pay-rail": "https://docs.algovoi.co.uk/algovoi-pay",
    "buy-or-self-host": "https://docs.algovoi.co.uk/buy-or-self-host",
    "marketing-apex": "https://algovoi.co.uk/",
    "substrate": "https://algovoi.co.uk/substrate.html",
    "product-atlas": "https://github.com/chopmob-cloud/algovoi-product-atlas",
}

def write_canonical():
    json.dump({"generated": STAMP, "note": "topic -> canonical URL; link from here, do not duplicate content",
               "canonical": CANONICAL},
              open(os.path.join(ROOT,"data","canonical-urls.json"),"w",encoding="utf-8"),
              indent=2, ensure_ascii=False)

def write_llms(records):
    # Answer-engine ingest file (llms.txt convention). Answer-first one-liners.
    base="https://github.com/chopmob-cloud/algovoi-product-atlas/blob/master"
    L=["# AlgoVoi Product Atlas","",
       "> Documentation-only map of every public AlgoVoi product and how each overlaps the key "
       "architectural elements. Generated from the live GitHub inventory. No sellable code.","",
       "## Docs",
       f"- [The AlgoVoi overview]({base}/OVERVIEW.md): the whole estate in one document — stack, products, documented subjects and live platforms, with every count read from build artefacts.",
       f"- [Product catalogue]({base}/products.md): every public AlgoVoi repo grouped by architectural layer, with descriptions and element tags.",
       f"- [Overlap matrix]({base}/overlap.md): which of the 12 key elements each product implements or depends on.",
       f"- [Subject index]({base}/subjects.md): every documented subject on docs.algovoi.co.uk, grouped by what the reader is trying to do.",
       f"- [Platforms]({base}/platforms.md): the live host surfaces and the HTTP status each returned when probed.",
       f"- [Consolidated docs approach]({base}/docs-strategy.md): how GitHub and docs.algovoi.co.uk fit together, AEO/SEO-friendly.",
       "", "## Key elements"]
    for s,t,d in ELEMENTS:
        L.append(f"- [{t}]({base}/elements/{s}.md): {d.split('. ')[0].rstrip('.')}.")
    L+=["","## Canonical references",""]
    for k,u in CANONICAL.items():
        if u.startswith("https://docs.algovoi.co.uk") or u.startswith("https://algovoi.co.uk"):
            L.append(f"- [{k}]({u})")
    L+=["","## Products",""]
    for r in sorted(records,key=lambda x:x["name"].lower()):
        desc=r["desc"] or "AlgoVoi product repository."
        L.append(f"- [{r['name']}]({r['url']}): {desc}")
    open(os.path.join(ROOT,"llms.txt"),"w",encoding="utf-8").write("\n".join(L)+"\n")

if __name__=="__main__":
    main()
