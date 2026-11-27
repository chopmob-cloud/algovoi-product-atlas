# The AlgoVoi overview

One document covering the whole estate: the stack, the products that build it, the subjects it documents, and the surfaces it runs on. Read this first; every other page is a detail of something named here.

*Built 2026-11-27 from live sources — 68 public repos, 172 documented subjects, 7 live platform surfaces. Every number below is read from those artefacts at build time, not typed.*

## At a glance

| | Count | What it is |
|---|---|---|
| Products | 68 | Public, live, non-fork repos in the estate |
| Architectural layers | 10 | L0 substrate → L8 platform, plus meta |
| Shared elements | 12 | The cross-cutting spine every product binds to |
| Documented subjects | 172 | Pages on the documentation site |
| Subject groups | 12 | How those subjects are organised for a reader |
| Platform surfaces | 7 | Hosts probed live, HTTP 200 |

## The one idea

AlgoVoi is **one canonicalisation substrate with several protocol faces**. A JSON object is canonicalised (RFC 8785 JCS), hashed into a content-addressed reference, signed (RFC 9421, optionally post-quantum), and returned as a receipt a third party can verify offline with no AlgoVoi service in the loop.

Everything else is a face of that one chain:

| Face | What it adds |
|---|---|
| **x402** | Per-request payment over HTTP |
| **MPP** | Per-call payment for MCP tools and JSON-RPC methods |
| **AP2** | Human-signed mandates for autonomous agent commerce |
| **A2A** | Agent-to-agent discovery with payment-gated calls |

The overlap is the product: the same canonical bytes, references and receipts serve all four, so a receipt issued over one protocol verifies against another.

## The stack — every layer, and what lives in it

| Layer | Role | Products |
|---|---|---|
| **L0 · Substrate & canonicalisation** | JCS canonicalisation and the PQC author layer — the shared base | 4 |
| **L1 · Signing & key identity** | RFC 9421 / RFC 9530 signing and verification, key identity | 8 |
| **L2 · References & receipt formats** | Content-addressed references and payment-lifecycle receipt formats | 11 |
| **L3 · Keystone composition** | Keystone L2 composition and the fabric spine | 4 |
| **L4 · Verification & audit** | Offline third-party verification and audit bundles | 5 |
| **L5 · Conformance & cross-validation** | Cross-language conformance batteries across independent implementations | 5 |
| **L6 · Settlement & chain rails (AVM)** | Algorand/Voi settlement, state proofs, bridges, wallet auth | 12 |
| **L7 · Protocol adapters & integrations** | AP2 / x402 / MPP / A2A adapters and the MCP tool surface | 9 |
| **L8 · Platform & gateway** | The hosted gateway, pay rail, platform and secure hub | 2 |
| **Meta · profile, hub & docs** | Organisation profile, hub and documentation repos | 8 |

## The shared elements — what every product binds to

These are the cross-cutting concerns. A product's row in the overlap matrix says which it implements or depends on; the count is how many products touch it.

| Element | Products | What it is |
|---|---|---|
| JCS canonicalisation (RFC 8785) | 17 | RFC 8785 JSON Canonicalization Scheme |
| Content-addressed references | 10 | Deterministic SHA-256-over-JCS identifiers (action_ref, card_ref, task_ref, artifact_ref, delegation/journey/revocation refs) |
| RFC 9421 HTTP signatures + RFC 9530 Content-Digest | 12 | HTTP Message Signatures and Content-Digest |
| Post-quantum cryptography | 10 | ML-DSA / ML-KEM (NIST FIPS 203/204) and Falcon-1024 (FIPS 206), classical+PQ hybrid |
| Payment-lifecycle receipt / evidence formats | 20 | payment-mandate, settlement-attestation, refund, cancellation, Payment Evidence Frame (PEF), composite trust-query |
| Keystone composition (L2) / Fabric spine | 11 | The Keystone SDK and the algovoi-fabric composition spine: bind authority -> policy -> decision -> delegation -> outcome into one tamper-evident, fail-closed chain |
| Cross-language conformance / cross-validation | 20 | Signed, byte-for-byte conformance batteries across independent implementations |
| Offline third-party verification / audit | 29 | Standalone verifiers and audit bundles a relying party can run with no AlgoVoi service in the loop: verify.algovoi.co.uk, verify-it-yourself, evidence readers, reseal-verify |
| Key identity / DID / credential binding | 4 | did:key / did:web resolution, key-to-credential binding (RFC 9421), key hygiene / primality soundness, rotation lineage |
| On-chain settlement / state proofs / bridges (AVM) | 14 | Algorand & Voi mesh settlement receipts argued from state proofs, portable proofpacks, mainnet bridges, consensus blocklist, multi-chain wallet auth |
| Agent payment protocols (AP2 / ACP / x402 / MPP / A2A) | 16 | Adapters and reference implementations for the agent-payment protocols: AP2 mandates, ACP checkout, x402 paid HTTP, MPP, A2A message/artifact/task refs, MCP tool surface |
| Hosted gateway / pay rail / platform adapters | 10 | The hosted x402 gateway (api.algovoi.co.uk), the pay rail (pay.algovoi.co.uk), the platform, and the ecommerce / marketplace / AI-agent / no-code adapters |

## What is documented — every subject, by group

The documentation site carries **172 subjects** in **12 groups**. Each group below is a reader's job, not an org chart; the full index with every page and its description is in the subject index.

| Group | Subjects | Start with |
|---|---|---|
| **Start here** | 9 | [Compliance-aware agentic payments](https://docs.algovoi.co.uk/introduction) |
| **Protocols** | 5 | [x402 (HTTP 402 Payment Required)](https://docs.algovoi.co.uk/protocols/x402) |
| **Chains** | 8 | [Algorand USDC payments](https://docs.algovoi.co.uk/chains/algorand) |
| **Platform and API** | 24 | [AlgoVoi Pay](https://docs.algovoi.co.uk/algovoi-pay) |
| **Receipt and evidence formats** | 12 | [Settlement Attestation Format](https://docs.algovoi.co.uk/settlement-attestation) |
| **Verification and audit** | 9 | [Settlement Verification](https://docs.algovoi.co.uk/settlement-verify) |
| **Keystone and agent trust** | 29 | [Composite Trust Query Response Format](https://docs.algovoi.co.uk/composite-trust-query) |
| **Substrate and canonicalisation** | 16 | [CAIP Chain-Agnostic Identifiers](https://docs.algovoi.co.uk/caip-identifiers) |
| **Compliance and record keeping** | 23 | [Compliance & Security](https://docs.algovoi.co.uk/compliance) |
| **Integrations** | 12 | [Integrations overview](https://docs.algovoi.co.uk/integrations/overview) |
| **Self-host and operations** | 9 | [On-Premise Deployment](https://docs.algovoi.co.uk/on-premise) |
| **Corpus and provenance** | 16 | [Protocols and chains](https://docs.algovoi.co.uk/protocols-and-chains) |

## Where it runs — the platform surfaces

All 7 surfaces below answered HTTP 200 when probed on 2026-11-26. A host that did not resolve is omitted rather than listed as unavailable.

| Surface | Host | What it is |
|---|---|---|
| Documentation | [docs.algovoi.co.uk/introduction](https://docs.algovoi.co.uk/introduction) | The canonical documentation site; every subject in the subject index lives here. |
| Hosted gateway | [api.algovoi.co.uk/health](https://api.algovoi.co.uk/health) | Multi-chain x402 facilitator: tenants, API keys, KYB. Liveness at /health. |
| Suite store | [api.algovoi.co.uk/suite-store](https://api.algovoi.co.uk/suite-store) | Where a free licence key is issued per deployment. |
| x402 discovery | [api.algovoi.co.uk/.well-known/x402](https://api.algovoi.co.uk/.well-known/x402) | Machine-readable statement of the paid routes the gateway serves. |
| Pay rail | [pay.algovoi.co.uk/](https://pay.algovoi.co.uk/) | Tenant-free rail: no account, settlement is the credential. |
| Verification | [verify.algovoi.co.uk/](https://verify.algovoi.co.uk/) | Browser verification of a receipt with no AlgoVoi service in the loop. |
| Marketing site | [algovoi.co.uk/](https://algovoi.co.uk/) | The public marketing apex. |

Two access models sit behind those hosts, and almost every page assumes one: **governed** (a tenant, an API key, KYB — the operator carries the compliance duty) and **tenant-free** (no account, settlement is the credential and the receipt is the evidence). Self-hosting is the third path and is not a host at all.

## The products

Every public product, grouped by the layer it sits in. Descriptions are quoted from GitHub, not rewritten here.

### L0 · Substrate & canonicalisation — 4

- **[algovoi-keyhygiene-conformance](https://github.com/chopmob-cloud/algovoi-keyhygiene-conformance)** — Signed, cross-language conformance battery for RSA/EC public-key hygiene and primality soundness (the L0 key-soundness layer): 12-way byte-for-byte consensus over primality, RSA modulus hygiene, batch common-factor, EC key hygiene, and ROCA fingerprint.
  - Elements: `conformance` `keyid` · Python · last push 2026-11-24
- **[algovoi-substrate](https://github.com/chopmob-cloud/algovoi-substrate)** — AlgoVoi agentic-payments substrate -- JCS canonicalisation, action_ref, composite trust-query, compliance receipts, audit chain. Python + TypeScript reference implementations.
  - Elements: `jcs` `refs` `receipts` `verify` · Python · last push 2026-11-24
- **[algovoi-substrate-pqc](https://github.com/chopmob-cloud/algovoi-substrate-pqc)** — AlgoVoi substrate-author layer for JCS+PQC integration — signature_algorithm open-enum convention + cross-implementor byte-anchor convergence proof. Wraps PQClean (via pqcrypto), Anders Rundgren's rfc8785, and the Python Cryptographic Authority. AlgoVoi-authored substrate; underlying primitives credited per Apache-2.0 attribution.
  - Elements: `jcs` `pqc` `conformance` · Python · last push 2026-11-24
- **[substrate-comparisons](https://github.com/chopmob-cloud/substrate-comparisons)** — A reproducible comparison of substrate methods for agentic-payment records. Names no implementation; the bytes decide.
  - Elements: `jcs` `conformance` · Python · last push 2026-11-24

### L1 · Signing & key identity — 8

- **[algovoi-key-credential-binding](https://github.com/chopmob-cloud/algovoi-key-credential-binding)** — RFC 9421 key-to-credential binding: reference verifier and conformance vectors (Python + TypeScript)
  - Elements: `rfc9421` `conformance` `verify` `keyid` · Python · last push 2026-11-24
- **[algovoi-rfc9421-a2a](https://github.com/chopmob-cloud/algovoi-rfc9421-a2a)** — A2A per-message signing adapter binding the AlgoVoi RFC 9421 signer/verifier/keyid resolver to the A2A message envelope. Apache-2.0.
  - Elements: `rfc9421` `verify` `keyid` `protocols` `gateway` · Python · last push 2026-11-24
- **[algovoi-rfc9421-ecdsa](https://github.com/chopmob-cloud/algovoi-rfc9421-ecdsa)** — Pure ECDSA (P-256/P-384) add-on for the AlgoVoi RFC 9421 verifier. Delegates Ed25519 to the unchanged verifier 0.4.2.
  - Elements: `rfc9421` `verify` · Python · last push 2026-11-24
- **[algovoi-rfc9421-keyid](https://github.com/chopmob-cloud/algovoi-rfc9421-keyid)** — SSRF-guarded RFC 9421 keyid resolver (did:key / did:web / HTTPS) to Ed25519 public keys. Apache-2.0.
  - Elements: `rfc9421` `keyid` · Python · last push 2026-11-24
- **[algovoi-rfc9421-signer](https://github.com/chopmob-cloud/algovoi-rfc9421-signer)** — RFC 9421 HTTP Message Signatures + RFC 9530 Content-Digest signer (Ed25519) — Python + TypeScript
  - Elements: `rfc9421` · Python · last push 2026-11-24
- **[algovoi-rfc9421-verifier](https://github.com/chopmob-cloud/algovoi-rfc9421-verifier)** — AlgoVoi RFC 9421 HTTP Message Signatures + RFC 9530 Content-Digest reference verifier (Python + TypeScript)
  - Elements: `rfc9421` `verify` · TypeScript · last push 2026-11-24
- **[algovoi-rfc9421-verifier-go](https://github.com/chopmob-cloud/algovoi-rfc9421-verifier-go)** — Go RFC 9421 verifier + independent ECDSA (P-256/P-384) add-on. Byte-parity with the AlgoVoi Python/TypeScript verifier. Apache-2.0.
  - Elements: `rfc9421` `conformance` `verify` · Go · last push 2026-11-24
- **[algovoi-rfc9421-verifier-rs](https://github.com/chopmob-cloud/algovoi-rfc9421-verifier-rs)** — Rust RFC 9421 verifier + independent ECDSA (P-256/P-384) add-on. Byte-parity with the AlgoVoi Python/TypeScript verifier. Apache-2.0.
  - Elements: `rfc9421` `conformance` `verify` · Rust · last push 2026-11-24

### L2 · References & receipt formats — 11

- **[AlgoVoi-A2A-Artifact](https://github.com/chopmob-cloud/AlgoVoi-A2A-Artifact)** — artifact_ref: a deterministic, content-addressed reference to an A2A Task output. RFC 8785 JCS + SHA-256, no JWS or JWKS. Apache-2.0.
  - Elements: `jcs` `refs` `protocols` · Python · last push 2026-11-24
- **[AlgoVoi-A2A-Card](https://github.com/chopmob-cloud/AlgoVoi-A2A-Card)** — card_ref: a deterministic, content-addressed reference to an A2A AgentCard. RFC 8785 JCS + SHA-256, no JWS or JWKS. Apache-2.0.
  - Elements: `jcs` `refs` `protocols` · Python · last push 2026-11-24
- **[AlgoVoi-A2A-Task](https://github.com/chopmob-cloud/AlgoVoi-A2A-Task)** — task_ref: a deterministic, content-addressed reference to an A2A Task delegation. RFC 8785 JCS + SHA-256, no JWS or JWKS. Apache-2.0.
  - Elements: `jcs` `refs` `protocols` · Python · last push 2026-11-24
- **[algovoi-delegation-ref](https://github.com/chopmob-cloud/algovoi-delegation-ref)** — Open, content-addressed delegation references for AlgoVoi Keystone: tamper-evident, chainable cross-party hand-offs with conformance vectors. Apache-2.0.
  - Elements: `jcs` `refs` `keystone` `conformance` · Python · last push 2026-11-24
- **[algovoi-journey-ref](https://github.com/chopmob-cloud/algovoi-journey-ref)** — Open, content-addressed journey references for AlgoVoi Keystone: bind a whole multi-agent task (hops + delegations + outcome) into one offline-verifiable reference. Apache-2.0.
  - Elements: `jcs` `refs` `keystone` `verify` · Python · last push 2026-11-24
- **[algovoi-pef](https://github.com/chopmob-cloud/algovoi-pef)** — Payment Evidence Frame (PEF) v1 -- AlgoVoi canonical wrapper for payment-lifecycle receipts
  - Elements: `jcs` `refs` `rfc9421` `receipts` · Python · last push 2026-11-24
- **[algovoi-probityai](https://github.com/chopmob-cloud/algovoi-probityai)** — Offline verifier and byte-pinned conformance vectors for the refund and receipt binding case. Apache-2.0.
  - Elements: `receipts` `conformance` `verify` · Python · last push 2026-11-24
- **[algovoi-receipt-sentinel](https://github.com/chopmob-cloud/algovoi-receipt-sentinel)** — Tenant-side monitoring layer: sliding-window attack/abuse pattern detection for receipt and webhook verification events
  - Elements: `receipts` `verify` · Python · last push 2026-11-24
- **[algovoi-receipt-verifier](https://github.com/chopmob-cloud/algovoi-receipt-verifier)** — Cryptographic verifier for AlgoVoi JWS compliance receipts. Python + TypeScript. 13 cross-validation vectors (5 valid, 8 invalid). Apache-2.0.
  - Elements: `receipts` `conformance` `verify` · Python · last push 2026-11-24
- **[algovoi-revocation-ref](https://github.com/chopmob-cloud/algovoi-revocation-ref)** — Open, content-addressed revocation references for AlgoVoi Keystone: tamper-evident, chainable revocation envelopes verified offline. Apache-2.0.
  - Elements: `jcs` `refs` `keystone` · Python · last push 2026-11-24
- **[algovoi-webhook-verifier](https://github.com/chopmob-cloud/algovoi-webhook-verifier)** — Cryptographic verifier for AlgoVoi webhook signatures (v1 HMAC-SHA256 + v2 HKDF-SHA256/HMAC-SHA384)
  - Elements: `verify` · Python · last push 2026-06-09

### L3 · Keystone composition — 4

- **[algovoi-fabric](https://github.com/chopmob-cloud/algovoi-fabric)** — Security composition core for agentic commerce: tamper-evident, fail-closed, offline-verifiable keystone chains binding authority, policy, decision, execution and settlement. Apache-2.0.
  - Elements: `jcs` `refs` `rfc9421` `pqc` `receipts` `keystone` `conformance` `verify` `protocols` · Python · last push 2026-11-24
- **[algovoi-keystone](https://github.com/chopmob-cloud/algovoi-keystone)** — The Keystone SDK (L2) on the AlgoVoi substrate (L1): build, govern, run and verify agent actions. Apache-2.0.
  - Elements: `jcs` `refs` `keystone` `verify` · Python · last push 2026-11-24
- **[algovoi-keystone-alias](https://github.com/chopmob-cloud/algovoi-keystone-alias)** — Keystone L2 alias layering over the RFC 8785 JCS substrate: resolve @aliases to concrete refs, then canonicalize. Offline-verifiable conformance twins (Python + Node).
  - Elements: `jcs` `keystone` `conformance` `verify` · Python · last push 2026-11-24
- **[AlgoVoi-Keystone-Connectors](https://github.com/chopmob-cloud/AlgoVoi-Keystone-Connectors)** — AlgoVoi Keystone connectors: bind third-party SDK sends to a keystone decision (Apache-2.0)
  - Elements: `keystone` · Python · last push 2026-11-24

### L4 · Verification & audit — 5

- **[algovoi-audit-verifier](https://github.com/chopmob-cloud/algovoi-audit-verifier)** — Standalone reference verifier for AlgoVoi selective-disclosure audit bundles. Hosted at verify.algovoi.co.uk, or git-clone for offline auditor use. No AlgoVoi infrastructure trust required.
  - Elements: `jcs` `receipts` `verify` · Python · last push 2026-11-22
- **[algovoi-evidence-readers](https://github.com/chopmob-cloud/algovoi-evidence-readers)** — Two outside readers for Probity AI's evidence corpora: uncertain-effect (54/54) and request-effect-join (11/11), with the gates that show each check bites. Apache-2.0.
  - Elements: `conformance` `verify` · Python · last push 2026-11-24
- **[algovoi-reseal-verify](https://github.com/chopmob-cloud/algovoi-reseal-verify)** — Open, offline verifier for AlgoVoi Reseal: check post-quantum attestations and triage classical signatures. Don't trust the sealer, verify the bytes. Apache-2.0.
  - Elements: `pqc` `receipts` `verify` · Python · last push 2026-11-24
- **[algovoi-vcs](https://github.com/chopmob-cloud/algovoi-vcs)** — AlgoVoi Verifiable Compliance Suite — public documentation and addon interfaces (StorageBackend, Signer) for the Verifiable Archive engine
  - Elements: `pqc` `receipts` `verify` · Python · last push 2026-11-24
- **[algovoi-verify-it-yourself](https://github.com/chopmob-cloud/algovoi-verify-it-yourself)** — Don't trust AlgoVoi, verify us: 5-minute offline, post-quantum proof that AlgoVoi evidence is genuine and tamper-evident, with no AlgoVoi code in your trust base.
  - Elements: `pqc` `verify` · Python · last push 2026-11-24

### L5 · Conformance & cross-validation — 5

- **[algovoi-crest-joint-harness](https://github.com/chopmob-cloud/algovoi-crest-joint-harness)** — AlgoVoi x Crest joint conformance harness (joint-harness-v0). AlgoVoi-authored; Crest contributed a service-trust conformance vector.
  - Elements: `conformance` · Python · last push 2026-11-24
- **[algovoi-jcs-conformance-vectors](https://github.com/chopmob-cloud/algovoi-jcs-conformance-vectors)** — Conformance vector sets for JCS RFC 8785 canonicalisation across x402, AP2, A2A, MPP receipt anchor sets. Cross-validated across ten independent JCS implementations in ten languages.
  - Elements: `jcs` `conformance` `protocols` · Python · last push 2026-11-24
- **[algovoi-rfc9421-conformance](https://github.com/chopmob-cloud/algovoi-rfc9421-conformance)** — Signed, cross-language conformance battery for RFC 9421 HTTP Message Signatures (Python, TypeScript, Rust, Go), byte-for-byte.
  - Elements: `rfc9421` `conformance` · Python · last push 2026-11-24
- **[algovoi-ube](https://github.com/chopmob-cloud/algovoi-ube)** — Independent Apache-2.0 conformance harness for NTI-1, plus a Keystone coverage map
  - Elements: `keystone` `conformance` · Python · last push 2026-11-24
- **[ap2-pq-conformance](https://github.com/chopmob-cloud/ap2-pq-conformance)** — Joint canonical home for AP2 Post-Quantum cross-scheme conformance fixtures (AlgoVoi + PQSafe). One AP2 PaymentMandate canonical byte sequence, multiple signature primitives — ES256 + Ed25519 + Falcon-1024 (AlgoVoi) + ML-DSA-65 (PQSafe pending). Per AP2#250 lock-in.
  - Elements: `pqc` `receipts` `conformance` `protocols` · Python · last push 2026-11-24

### L6 · Settlement & chain rails (AVM) — 12

- **[algovoi-consensus-blocklist](https://github.com/chopmob-cloud/algovoi-consensus-blocklist)** — 4-of-N on-chain consensus wallet blocklist for Algorand and VOI (algopy ARC-4)
  - Elements: `settlement` · Python · last push 2026-11-24
- **[algovoi-multi-chain-wallet-auth](https://github.com/chopmob-cloud/algovoi-multi-chain-wallet-auth)** — Multi-chain wallet authentication primitives (EVM/Algorand/VOI/Solana/Stellar/Hedera/Tempo/ARC) — extracted from AlgoVoi production gateway in support of A2A #1737
  - Elements: `settlement` `protocols` `gateway` · Python · last push 2026-11-24
- **[avm-ac2](https://github.com/chopmob-cloud/avm-ac2)** — AC2 consent bound to an avm-mesh settlement: proof of who authorised a transaction, on Algorand and Voi
  - Elements: `receipts` `keystone` `settlement` · Python · last push 2026-11-24
- **[avm-algo-voi-bridge](https://github.com/chopmob-cloud/avm-algo-voi-bridge)** — Algorand to VOI Mainnet Bridge
  - Elements: `settlement` · — · last push 2026-11-24
- **[avm-algovoi-falcon](https://github.com/chopmob-cloud/avm-algovoi-falcon)** — Falcon-1024 (FIPS 206) keys and Algorand post-quantum accounts: keygen, deterministic sign/verify, falcon_verify LogicSig address derivation. Standalone, reproducible build from MIT sources.
  - Elements: `pqc` `verify` `settlement` · C · last push 2026-11-24
- **[avm-effectproof](https://github.com/chopmob-cloud/avm-effectproof)** — Application-effect proofs for Algorand and Voi: read what a transaction actually did (inner transactions, logs, global and local state) from a proven SignedTxnInBlock. One implementation, both chains.
  - Elements: `verify` `settlement` · Python · last push 2026-11-24
- **[avm-hbar-bridge-relayer](https://github.com/chopmob-cloud/avm-hbar-bridge-relayer)** — Algorand ↔ Hedera treasury-model bridge relayer
  - Elements: `settlement` · Python · last push 2026-11-24
- **[avm-mesh](https://github.com/chopmob-cloud/avm-mesh)** — Settlement receipts for the Algorand and Voi mesh: third-party-checkable proof that an on-chain transfer happened, argued from state proofs against an anchor you pin yourself. Two chains, zero third-party runtime dependencies.
  - Elements: `receipts` `verify` `settlement` · Python · last push 2026-11-24
- **[avm-proofpack](https://github.com/chopmob-cloud/avm-proofpack)** — Portable, offline-verifiable transaction evidence for Algorand and Voi, anchored in state proofs
  - Elements: `verify` `settlement` · Python · last push 2026-11-24
- **[avm-proofpack-ts](https://github.com/chopmob-cloud/avm-proofpack-ts)** — Offline Algorand and Voi consensus verification primitives in TypeScript. Zero dependencies, no build step; byte-for-byte compatible with avm-proofpack (Python) on mainnet data from both chains.
  - Elements: `conformance` `verify` `settlement` · TypeScript · last push 2026-11-24
- **[avm-voi-algo-bridge](https://github.com/chopmob-cloud/avm-voi-algo-bridge)** — VOI to Algorand Mainnet Bridge
  - Elements: `settlement` · Python · last push 2026-11-24
- **[avm-wormhole-ntt-relayer](https://github.com/chopmob-cloud/avm-wormhole-ntt-relayer)** — Wormhole NTT relayer — Algorand ↔ Base
  - Elements: `settlement` · Python · last push 2026-11-24

### L7 · Protocol adapters & integrations — 9

- **[algovoi-a2a-glink](https://github.com/chopmob-cloud/algovoi-a2a-glink)** — AlgoVoi gibberlink + A2A reference
  - Elements: `protocols` · Python · last push 2026-11-24
- **[algovoi-atb](https://github.com/chopmob-cloud/algovoi-atb)** — AlgoVoi Agent Trust Bench client — run your AI agent through 166 adversarial x402 payment profiles and earn a Falcon-1024 signed reputation certificate.
  - Elements: `pqc` `protocols` · Python · last push 2026-11-23
- **[algovoi-compliance-gate-a2a](https://github.com/chopmob-cloud/algovoi-compliance-gate-a2a)** — Open, A2A-interoperable AlgoVoi Compliance Gate: a no-PII, geo-bound seven-field Compliance Receipt mapped to A2A Payment and Cart Mandate primitives. Receipt format and method, Apache-2.0.
  - Elements: `receipts` `protocols` · Python · last push 2026-11-24
- **[AlgoVoi-MCP-Server](https://github.com/chopmob-cloud/AlgoVoi-MCP-Server)** — MCP server exposing AlgoVoi payment tools to Claude Desktop, Claude Code, Cursor and Windsurf — npm + PyPI
  - Elements: `receipts` `protocols` `gateway` · Python · last push 2026-11-22
- **[AlgoVoi-Platform-Adapters](https://github.com/chopmob-cloud/AlgoVoi-Platform-Adapters)** — AlgoVoi apps & adapters — ecommerce, marketplace, AI-agent, and no-code integrations for the AlgoVoi x402 multi-chain payment gateway. Apache-2.0.
  - Elements: `protocols` `gateway` · Python · last push 2026-11-22
- **[algovoi-recurr](https://github.com/chopmob-cloud/algovoi-recurr)** — Open format and method for AlgoVoi Recurr Tier 2 standing authorities: a recurring, capped, revocable on-chain payment authorisation, signed, disclosed and revoked. Apache-2.0, Python and Node.
  - Elements: `receipts` `gateway` · Python · last push 2026-11-24
- **[algovoi-reference-agent](https://github.com/chopmob-cloud/algovoi-reference-agent)** — Apache 2.0 reference implementation of an agent that emits an AlgoVoi settlement-attestation-v1 receipt for a Base chain transaction. Composes algovoi-substrate + algovoi-settlement-attestation. Byte-deterministic against algovoi-jcs-conformance-vectors.
  - Elements: `receipts` `settlement` `protocols` · Python · last push 2026-11-24
- **[elizaos-plugin-algovoi](https://github.com/chopmob-cloud/elizaos-plugin-algovoi)** — Multi-chain agent-to-agent (A2A) crypto payments for ElizaOS — Algorand, VOI, Hedera, Stellar, Base, Solana, Tempo via the AlgoVoi A2A gateway.
  - Elements: `protocols` `gateway` · TypeScript · last push 2026-11-24
- **[use-wallet-algovoi](https://github.com/chopmob-cloud/use-wallet-algovoi)** — AlgoVoi wallet adapter for @txnlab/use-wallet v5
  - Elements: `gateway` · TypeScript · last push 2026-11-24

### L8 · Platform & gateway — 2

- **[algovoi-platform](https://github.com/chopmob-cloud/algovoi-platform)** — AlgoVoi Platform: payment rails, verifiable compliance estate and the post-quantum substrate they share. Free production use under BUSL-1.1; licence keys issued free.
  - Elements: `pqc` `receipts` `settlement` `protocols` `gateway` · Python · last push 2026-11-24
- **[algovoi-secure-hub](https://github.com/chopmob-cloud/algovoi-secure-hub)** — Universal substrate-neutral AlgoVoi security and trust hub
  - Elements: `gateway` · Python · last push 2026-11-24

### Meta · profile, hub & docs — 8

- **[.github](https://github.com/chopmob-cloud/.github)** — AlgoVoi organization profile
- **[algovoi-advisories](https://github.com/chopmob-cloud/algovoi-advisories)** — Public security advisories for AlgoVoi software and services
- **[algovoi-agent-guard](https://github.com/chopmob-cloud/algovoi-agent-guard)** — The budget your agent can't raise: human-signed spend mandates with offline-verifiable receipts, plus a pluggable AI/human/file/fuzz red team.
  - Elements: `receipts` `verify` · Python · last push 2026-11-26
- **[algovoi-agent-guard-ts](https://github.com/chopmob-cloud/algovoi-agent-guard-ts)** — The budget your agent can't raise - human-signed spend mandates with offline-verifiable receipts. TypeScript port, byte-conformant with the frozen L1 conformance vectors and the Python reference.
  - Elements: `receipts` `conformance` `verify` · TypeScript · last push 2026-11-26
- **[algovoi-keystone-sdk](https://github.com/chopmob-cloud/algovoi-keystone-sdk)** — Documentation for the AlgoVoi keystone: verifying agentic-action keystone chains and agent passports offline (RFC 8785 JCS + SHA-256).
  - Elements: `jcs` `keystone` `verify` · — · last push 2026-11-24
- **[algovoi-product-atlas](https://github.com/chopmob-cloud/algovoi-product-atlas)** — Documentation-only atlas of every public AlgoVoi product and how each overlaps the key architectural elements (JCS, RFC 9421, PQC, receipts, Keystone/Fabric, conformance, verification, settlement, protocols, gateway).
  - Elements: `jcs` `rfc9421` `pqc` `receipts` `keystone` `conformance` `verify` `gateway` · Python · last push 2026-11-24
- **[chopmob-cloud](https://github.com/chopmob-cloud/chopmob-cloud)** — The open substrate for agentic payments. Built so others could use it.
- **[chopmob-cloud.github.io](https://github.com/chopmob-cloud/chopmob-cloud.github.io)** — AlgoVoi substrate hub

## Conflicting sources

Where two live sources disagree about the same figure, this document does not pick a winner. The discrepancy is recorded, with each reading attributed, so a reader knows the number is unsettled rather than trusting whichever page they opened first.

**Agent Trust Bench (ATB) adversarial x402 profile count** — six sources give five different figures; four of those sources were probed and all returned HTTP 200 (three distinct hosts), and no artefact proves any single count

| Source | Says |
|---|---|
| Bench site https://agent-trust-bench.algovoi.co.uk/ (probed: HTTP 200, 2026-11-26) | 187 adversarial x402 profiles across 42 threat categories |
| Docs page https://docs.algovoi.co.uk/agent-trust-bench (live, HTTP 200) | 187 adversarial x402 profiles |
| PyPI algovoi-atb 0.1.6 summary (https://pypi.org/pypi/algovoi-atb/json, HTTP 200) | 178 adversarial x402 payment profiles |
| algovoi-atb README and GitHub repo description (gh api repos/chopmob-cloud/algovoi-atb) | 166 adversarial x402 payment profiles |
| agent-trust-bench GitHub repo description (gh api repos/chopmob-cloud/agent-trust-bench) | 138 adversarial x402 profiles across 30 threat categories |
| Bench API https://agent-trust-bench.algovoi.co.uk/profiles (probed: HTTP 200, returns a JSON object with an 'available' list) | 205 concrete profile ids after expanding two templates, of which 204 are adversarial (one 'honest' baseline) |

*Resolution: Unresolved. The live API is the only machine-checkable enumeration and it does not match any published headline. No number is asserted in the atlas; the upstream figure is quoted with its source and this table states the discrepancy.*

Upstream fix: agent-trust-bench (single source of truth for the profile count, surfaced through its API), then docs.algovoi.co.uk/agent-trust-bench, the algovoi-atb README, its PyPI summary and its GitHub description. Once those agree, delete this entry and let the atlas quote the reconciled figure.

## How to navigate this

| You want | Read |
|---|---|
| The stack and how layers depend on each other | [Application matrix](https://docs.algovoi.co.uk/application-matrix) |
| Every documented subject, with descriptions | [Subject index](https://github.com/chopmob-cloud/algovoi-product-atlas/blob/master/subjects.md) · [live site](https://docs.algovoi.co.uk/introduction) |
| Which products implement a given element | [Overlap matrix](https://github.com/chopmob-cloud/algovoi-product-atlas/blob/master/overlap.md) |
| Every product with its GitHub description | [Product catalogue](https://github.com/chopmob-cloud/algovoi-product-atlas/blob/master/products.md) |
| The live hosts and what runs there | [Platforms](https://github.com/chopmob-cloud/algovoi-product-atlas/blob/master/platforms.md) |
| How to take a payment | [Take a payment](https://docs.algovoi.co.uk/take-a-payment) |
| How to verify a receipt yourself | [Verify a receipt](https://docs.algovoi.co.uk/verify-a-receipt) |
| What it costs, and the free licence | [Trial and pricing](https://docs.algovoi.co.uk/trial-and-pricing) · [Free licence](https://docs.algovoi.co.uk/free-licence) |

## Provenance

- Repo inventory: `gh repo list chopmob-cloud`, snapshot refreshed 2026-11-27 (`data/repos.snapshot.json`).
- Product and element counts: `scripts/build_atlas.py` over that snapshot (2026-11-27).
- Subject list and group coverage: `scripts/build_subjects.py` against the live `https://docs.algovoi.co.uk/llms.txt` and the site's `docs.json` navigation (2026-11-27).
- Platform statuses: `scripts/probe_platforms.py`, HTTP probed 2026-11-26 (`data/platforms.json`).
- The product→element overlap is **derived** from each repo's name and GitHub description by transparent keyword rules plus curated overrides. It is a map, not a conformance claim: verify the specific repo before relying on a cell.
- Counts of chains, protocols and tools are **not** restated here. The documentation pages that own those numbers state them, and this document links to those pages, because a number restated in two places drifts.

## Regenerate

```bash
gh repo list chopmob-cloud --limit 400 --json name,description,url,isArchived,\
  isFork,visibility,pushedAt,primaryLanguage > data/repos.snapshot.json
python scripts/build_atlas.py
python scripts/build_subjects.py
python scripts/probe_platforms.py
python scripts/build_overview.py
```

## Licence

Apache-2.0 for this documentation. The products carry their own licences — Apache-2.0 across the open estate, BUSL-1.1 for licensed engines; see each repo.
