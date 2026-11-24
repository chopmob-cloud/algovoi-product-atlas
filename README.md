# AlgoVoi Product Atlas

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)

> Documentation-only map of **every public AlgoVoi product** (65 repos) and how each overlaps the
> key architectural elements. Generated from the live GitHub inventory on 2026-11-23.
> **No sellable code lives here** — this is the documentation layer over the estate.

## How to read this atlas

Two axes:

1. **Products by layer** — [`products.md`](products.md) groups every repo into the architectural stack (L0 substrate → L8 platform).
2. **Products × key elements** — [`overlap.md`](overlap.md) is the matrix: which shared elements each product implements or depends on.

Each key element also has its own page under [`elements/`](elements/) listing the products that touch it.

See also: [`docs-strategy.md`](docs-strategy.md) — the consolidated GitHub × docs.algovoi.co.uk AEO/SEO approach ·
[`llms.txt`](llms.txt) — answer-engine ingest · [`data/canonical-urls.json`](data/canonical-urls.json) — canonical URL registry.

## The stack

| Layer | What it is |
|---|---|
| **L0 · Substrate & canonicalisation** | JCS canonicalisation + the PQC author layer — the shared base. (4) |
| **L1 · Signing & key identity** | RFC 9421 / RFC 9530 signing & verification, keyid resolution, key identity. (8) |
| **L2 · References & receipt formats** | Content-addressed references and payment-lifecycle receipt formats. (11) |
| **L3 · Keystone composition (flagship)** | Keystone L2 composition and the **algovoi-fabric** flagship spine. (4) |
| **L4 · Verification & audit** | Offline, third-party verification and audit bundles. (5) |
| **L5 · Conformance & cross-validation** | Cross-language conformance batteries — the cross-validation moat. (5) |
| **L6 · Settlement & chain rails (AVM)** | Algorand/Voi settlement, state proofs, bridges, wallet auth (AVM). (12) |
| **L7 · Protocol adapters & integrations** | AP2 / ACP / x402 / MPP / A2A adapters and the MCP tool surface. (9) |
| **L8 · Platform & gateway** | The hosted gateway, pay rail, platform and secure hub. (2) |
| **Meta · profile, hub & docs** | Organisation profile, substrate hub and documentation repos. (5) |

## The key elements

- **[JCS canonicalisation (RFC 8785)](elements/jcs.md)** — 16 products. RFC 8785 JSON Canonicalization Scheme.
- **[Content-addressed references](elements/refs.md)** — 10 products. Deterministic SHA-256-over-JCS identifiers (action_ref, card_ref, task_ref, artifact_ref, delegation/journey/revocation refs).
- **[RFC 9421 HTTP signatures + RFC 9530 Content-Digest](elements/rfc9421.md)** — 11 products. HTTP Message Signatures and Content-Digest.
- **[Post-quantum cryptography](elements/pqc.md)** — 9 products. ML-DSA / ML-KEM (NIST FIPS 203/204) and Falcon-1024 (FIPS 206), classical+PQ hybrid.
- **[Payment-lifecycle receipt / evidence formats](elements/receipts.md)** — 16 products. payment-mandate, settlement-attestation, refund, cancellation, Payment Evidence Frame (PEF), composite trust-query.
- **[Keystone composition (L2) / Fabric spine](elements/keystone.md)** — 10 products. The Keystone SDK and the algovoi-fabric composition spine: bind authority -> policy -> decision -> delegation -> outcome into one tamper-evident, fail-closed chain..
- **[Cross-language conformance / cross-validation](elements/conformance.md)** — 17 products. Signed, byte-for-byte conformance batteries across independent implementations (the 10-language moat).
- **[Offline third-party verification / audit](elements/verify.md)** — 25 products. Standalone verifiers and audit bundles a relying party can run with no AlgoVoi service in the loop: verify.algovoi.co.uk, verify-it-yourself, evidence readers, reseal-verify..
- **[Key identity / DID / credential binding](elements/keyid.md)** — 4 products. did:key / did:web resolution, key-to-credential binding (RFC 9421), key hygiene / primality soundness, rotation lineage.
- **[On-chain settlement / state proofs / bridges (AVM)](elements/settlement.md)** — 14 products. Algorand & Voi mesh settlement receipts argued from state proofs, portable proofpacks, mainnet bridges, consensus blocklist, multi-chain wallet auth..
- **[Agent payment protocols (AP2 / ACP / x402 / MPP / A2A)](elements/protocols.md)** — 16 products. Adapters and reference implementations for the agent-payment protocols: AP2 mandates, ACP checkout, x402 paid HTTP, MPP, A2A message/artifact/task refs, MCP tool surface..
- **[Hosted gateway / pay rail / platform adapters](elements/gateway.md)** — 9 products. The hosted x402 gateway (api.algovoi.co.uk), the pay rail (pay.algovoi.co.uk), the platform, and the ecommerce / marketplace / AI-agent / no-code adapters..

## Provenance & method

- Source: `gh repo list chopmob-cloud` snapshot, 2026-11-23 (`data/repos.snapshot.json`).
- Product descriptions are quoted from GitHub; they are not rewritten here.
- The product→element overlap is **derived** from each description/name by transparent keyword rules plus a curated override map for the active core (`scripts/build_atlas.py`). It is a map, not a conformance claim — verify against each repo before relying on a specific cell.
- Active-core facts (Fabric, AP2 v0.2, payment-mandate hardening) are cross-checked against the AlgoVoi claims graph; see the 7-day plan for their trust states.

## Regenerate

```bash
gh repo list chopmob-cloud --limit 200 --json name,description,url,isArchived,isFork,visibility,pushedAt,primaryLanguage > data/repos.snapshot.json
python scripts/build_atlas.py
```

## Licence

Apache-2.0 (documentation). The products themselves carry their own licences — Apache-2.0 for the open estate, BUSL-1.1 / commercial for the licensed engines; see each repo.
