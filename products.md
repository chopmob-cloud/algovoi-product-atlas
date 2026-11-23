# Product catalogue (by architectural layer)

All 65 public AlgoVoi product repos, 2026-11-23. Descriptions quoted from GitHub.

Element tags link to the [key elements](README.md#the-key-elements); see [overlap.md](overlap.md) for the full matrix.

## L0 · Substrate & canonicalisation

4 repos.

### [algovoi-keyhygiene-conformance](https://github.com/chopmob-cloud/algovoi-keyhygiene-conformance)
Signed, cross-language conformance battery for RSA/EC public-key hygiene and primality soundness (the L0 key-soundness layer): 12-way byte-for-byte consensus over primality, RSA modulus hygiene, batch common-factor, EC key hygiene, and ROCA fingerprint.
- **Language:** Python · **Last push:** 2026-08-12
- **Elements:** [`conformance`](elements/conformance.md) [`keyid`](elements/keyid.md)

### [algovoi-substrate](https://github.com/chopmob-cloud/algovoi-substrate)
AlgoVoi agentic-payments substrate -- JCS canonicalisation, action_ref, composite trust-query, compliance receipts, audit chain. Python + TypeScript reference implementations.
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`receipts`](elements/receipts.md) [`verify`](elements/verify.md)

### [algovoi-substrate-pqc](https://github.com/chopmob-cloud/algovoi-substrate-pqc)
AlgoVoi substrate-author layer for JCS+PQC integration — signature_algorithm open-enum convention + cross-implementor byte-anchor convergence proof. Wraps PQClean (via pqcrypto), Anders Rundgren's rfc8785, and the Python Cryptographic Authority. AlgoVoi-authored substrate; underlying primitives credited per Apache-2.0 attribution.
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`jcs`](elements/jcs.md) [`pqc`](elements/pqc.md) [`conformance`](elements/conformance.md)

### [substrate-comparisons](https://github.com/chopmob-cloud/substrate-comparisons)
A reproducible comparison of substrate methods for agentic-payment records. Names no implementation; the bytes decide.
- **Language:** Python · **Last push:** 2026-08-04
- **Elements:** [`jcs`](elements/jcs.md) [`conformance`](elements/conformance.md)

## L1 · Signing & key identity

8 repos.

### [algovoi-key-credential-binding](https://github.com/chopmob-cloud/algovoi-key-credential-binding)
RFC 9421 key-to-credential binding: reference verifier and conformance vectors (Python + TypeScript)
- **Language:** Python · **Last push:** 2026-08-08
- **Elements:** [`rfc9421`](elements/rfc9421.md) [`conformance`](elements/conformance.md) [`verify`](elements/verify.md) [`keyid`](elements/keyid.md)

### [algovoi-rfc9421-a2a](https://github.com/chopmob-cloud/algovoi-rfc9421-a2a)
A2A per-message signing adapter binding the AlgoVoi RFC 9421 signer/verifier/keyid resolver to the A2A message envelope. Apache-2.0.
- **Language:** Python · **Last push:** 2026-08-08
- **Elements:** [`rfc9421`](elements/rfc9421.md) [`verify`](elements/verify.md) [`keyid`](elements/keyid.md) [`protocols`](elements/protocols.md) [`gateway`](elements/gateway.md)

### [algovoi-rfc9421-ecdsa](https://github.com/chopmob-cloud/algovoi-rfc9421-ecdsa)
Pure ECDSA (P-256/P-384) add-on for the AlgoVoi RFC 9421 verifier. Delegates Ed25519 to the unchanged verifier 0.4.2.
- **Language:** Python · **Last push:** 2026-08-09
- **Elements:** [`rfc9421`](elements/rfc9421.md) [`verify`](elements/verify.md)

### [algovoi-rfc9421-keyid](https://github.com/chopmob-cloud/algovoi-rfc9421-keyid)
SSRF-guarded RFC 9421 keyid resolver (did:key / did:web / HTTPS) to Ed25519 public keys. Apache-2.0.
- **Language:** Python · **Last push:** 2026-08-08
- **Elements:** [`rfc9421`](elements/rfc9421.md) [`keyid`](elements/keyid.md)

### [algovoi-rfc9421-signer](https://github.com/chopmob-cloud/algovoi-rfc9421-signer)
RFC 9421 HTTP Message Signatures + RFC 9530 Content-Digest signer (Ed25519) — Python + TypeScript
- **Language:** Python · **Last push:** 2026-08-02
- **Elements:** [`rfc9421`](elements/rfc9421.md)

### [algovoi-rfc9421-verifier](https://github.com/chopmob-cloud/algovoi-rfc9421-verifier)
AlgoVoi RFC 9421 HTTP Message Signatures + RFC 9530 Content-Digest reference verifier (Python + TypeScript)
- **Language:** TypeScript · **Last push:** 2026-11-22
- **Elements:** [`rfc9421`](elements/rfc9421.md) [`verify`](elements/verify.md)

### [algovoi-rfc9421-verifier-go](https://github.com/chopmob-cloud/algovoi-rfc9421-verifier-go)
Go RFC 9421 verifier + independent ECDSA (P-256/P-384) add-on. Byte-parity with the AlgoVoi Python/TypeScript verifier. Apache-2.0.
- **Language:** Go · **Last push:** 2026-08-12
- **Elements:** [`rfc9421`](elements/rfc9421.md) [`conformance`](elements/conformance.md) [`verify`](elements/verify.md)

### [algovoi-rfc9421-verifier-rs](https://github.com/chopmob-cloud/algovoi-rfc9421-verifier-rs)
Rust RFC 9421 verifier + independent ECDSA (P-256/P-384) add-on. Byte-parity with the AlgoVoi Python/TypeScript verifier. Apache-2.0.
- **Language:** Rust · **Last push:** 2026-08-12
- **Elements:** [`rfc9421`](elements/rfc9421.md) [`conformance`](elements/conformance.md) [`verify`](elements/verify.md)

## L2 · References & receipt formats

11 repos.

### [AlgoVoi-A2A-Artifact](https://github.com/chopmob-cloud/AlgoVoi-A2A-Artifact)
artifact_ref: a deterministic, content-addressed reference to an A2A Task output. RFC 8785 JCS + SHA-256, no JWS or JWKS. Apache-2.0.
- **Language:** Python · **Last push:** 2026-07-08
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`protocols`](elements/protocols.md)

### [AlgoVoi-A2A-Card](https://github.com/chopmob-cloud/AlgoVoi-A2A-Card)
card_ref: a deterministic, content-addressed reference to an A2A AgentCard. RFC 8785 JCS + SHA-256, no JWS or JWKS. Apache-2.0.
- **Language:** Python · **Last push:** 2026-07-08
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`protocols`](elements/protocols.md)

### [AlgoVoi-A2A-Task](https://github.com/chopmob-cloud/AlgoVoi-A2A-Task)
task_ref: a deterministic, content-addressed reference to an A2A Task delegation. RFC 8785 JCS + SHA-256, no JWS or JWKS. Apache-2.0.
- **Language:** Python · **Last push:** 2026-07-08
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`protocols`](elements/protocols.md)

### [algovoi-delegation-ref](https://github.com/chopmob-cloud/algovoi-delegation-ref)
Open, content-addressed delegation references for AlgoVoi Keystone: tamper-evident, chainable cross-party hand-offs with conformance vectors. Apache-2.0.
- **Language:** Python · **Last push:** 2026-09-20
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`keystone`](elements/keystone.md) [`conformance`](elements/conformance.md)

### [algovoi-journey-ref](https://github.com/chopmob-cloud/algovoi-journey-ref)
Open, content-addressed journey references for AlgoVoi Keystone: bind a whole multi-agent task (hops + delegations + outcome) into one offline-verifiable reference. Apache-2.0.
- **Language:** Python · **Last push:** 2026-09-20
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`keystone`](elements/keystone.md) [`verify`](elements/verify.md)

### [algovoi-pef](https://github.com/chopmob-cloud/algovoi-pef)
Payment Evidence Frame (PEF) v1 -- AlgoVoi canonical wrapper for payment-lifecycle receipts
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`rfc9421`](elements/rfc9421.md) [`receipts`](elements/receipts.md)

### [algovoi-probityai](https://github.com/chopmob-cloud/algovoi-probityai)
Offline verifier and byte-pinned conformance vectors for the refund and receipt binding case. Apache-2.0.
- **Language:** Python · **Last push:** 2026-11-01
- **Elements:** [`receipts`](elements/receipts.md) [`conformance`](elements/conformance.md) [`verify`](elements/verify.md)

### [algovoi-receipt-sentinel](https://github.com/chopmob-cloud/algovoi-receipt-sentinel)
Tenant-side monitoring layer: sliding-window attack/abuse pattern detection for receipt and webhook verification events
- **Language:** Python · **Last push:** 2026-06-09
- **Elements:** [`receipts`](elements/receipts.md) [`verify`](elements/verify.md)

### [algovoi-receipt-verifier](https://github.com/chopmob-cloud/algovoi-receipt-verifier)
Cryptographic verifier for AlgoVoi JWS compliance receipts. Python + TypeScript. 13 cross-validation vectors (5 valid, 8 invalid). Apache-2.0.
- **Language:** Python · **Last push:** 2026-07-01
- **Elements:** [`receipts`](elements/receipts.md) [`conformance`](elements/conformance.md) [`verify`](elements/verify.md)

### [algovoi-revocation-ref](https://github.com/chopmob-cloud/algovoi-revocation-ref)
Open, content-addressed revocation references for AlgoVoi Keystone: tamper-evident, chainable revocation envelopes verified offline. Apache-2.0.
- **Language:** Python · **Last push:** 2026-09-20
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`keystone`](elements/keystone.md)

### [algovoi-webhook-verifier](https://github.com/chopmob-cloud/algovoi-webhook-verifier)
Cryptographic verifier for AlgoVoi webhook signatures (v1 HMAC-SHA256 + v2 HKDF-SHA256/HMAC-SHA384)
- **Language:** Python · **Last push:** 2026-06-09
- **Elements:** [`verify`](elements/verify.md)

## L3 · Keystone composition (flagship)

4 repos.

### [algovoi-fabric](https://github.com/chopmob-cloud/algovoi-fabric)
Security composition core for agentic commerce: tamper-evident, fail-closed, offline-verifiable keystone chains binding authority, policy, decision, execution and settlement. Apache-2.0.
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`rfc9421`](elements/rfc9421.md) [`pqc`](elements/pqc.md) [`receipts`](elements/receipts.md) [`keystone`](elements/keystone.md) [`conformance`](elements/conformance.md) [`verify`](elements/verify.md) [`protocols`](elements/protocols.md)

### [algovoi-keystone](https://github.com/chopmob-cloud/algovoi-keystone)
The Keystone SDK (L2) on the AlgoVoi substrate (L1): build, govern, run and verify agent actions. Apache-2.0.
- **Language:** Python · **Last push:** 2026-10-29
- **Elements:** [`jcs`](elements/jcs.md) [`refs`](elements/refs.md) [`keystone`](elements/keystone.md) [`verify`](elements/verify.md)

### [algovoi-keystone-alias](https://github.com/chopmob-cloud/algovoi-keystone-alias)
Keystone L2 alias layering over the RFC 8785 JCS substrate: resolve @aliases to concrete refs, then canonicalize. Offline-verifiable conformance twins (Python + Node).
- **Language:** Python · **Last push:** 2026-08-04
- **Elements:** [`jcs`](elements/jcs.md) [`keystone`](elements/keystone.md) [`conformance`](elements/conformance.md) [`verify`](elements/verify.md)

### [AlgoVoi-Keystone-Connectors](https://github.com/chopmob-cloud/AlgoVoi-Keystone-Connectors)
AlgoVoi Keystone connectors: bind third-party SDK sends to a keystone decision (Apache-2.0)
- **Language:** Python · **Last push:** 2026-11-21
- **Elements:** [`keystone`](elements/keystone.md)

## L4 · Verification & audit

5 repos.

### [algovoi-audit-verifier](https://github.com/chopmob-cloud/algovoi-audit-verifier)
Standalone reference verifier for AlgoVoi selective-disclosure audit bundles. Hosted at verify.algovoi.co.uk, or git-clone for offline auditor use. No AlgoVoi infrastructure trust required.
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`jcs`](elements/jcs.md) [`receipts`](elements/receipts.md) [`verify`](elements/verify.md)

### [algovoi-evidence-readers](https://github.com/chopmob-cloud/algovoi-evidence-readers)
Two outside readers for Probity AI's evidence corpora: uncertain-effect (54/54) and request-effect-join (11/11), with the gates that show each check bites. Apache-2.0.
- **Language:** Python · **Last push:** 2026-11-20
- **Elements:** [`conformance`](elements/conformance.md) [`verify`](elements/verify.md)

### [algovoi-reseal-verify](https://github.com/chopmob-cloud/algovoi-reseal-verify)
Open, offline verifier for AlgoVoi Reseal: check post-quantum attestations and triage classical signatures. Don't trust the sealer, verify the bytes. Apache-2.0.
- **Language:** Python · **Last push:** 2026-08-10
- **Elements:** [`pqc`](elements/pqc.md) [`receipts`](elements/receipts.md) [`verify`](elements/verify.md)

### [algovoi-vcs](https://github.com/chopmob-cloud/algovoi-vcs)
AlgoVoi Verifiable Compliance Suite — public documentation and addon interfaces (StorageBackend, Signer) for the Verifiable Archive engine
- **Language:** Python · **Last push:** 2026-11-17
- **Elements:** [`pqc`](elements/pqc.md) [`receipts`](elements/receipts.md) [`verify`](elements/verify.md)

### [algovoi-verify-it-yourself](https://github.com/chopmob-cloud/algovoi-verify-it-yourself)
Don't trust AlgoVoi, verify us: 5-minute offline, post-quantum proof that AlgoVoi evidence is genuine and tamper-evident, with no AlgoVoi code in your trust base.
- **Language:** Python · **Last push:** 2026-07-24
- **Elements:** [`pqc`](elements/pqc.md) [`verify`](elements/verify.md)

## L5 · Conformance & cross-validation

5 repos.

### [algovoi-crest-joint-harness](https://github.com/chopmob-cloud/algovoi-crest-joint-harness)
AlgoVoi x Crest joint conformance harness (joint-harness-v0). AlgoVoi-authored; Crest contributed a service-trust conformance vector.
- **Language:** Python · **Last push:** 2026-06-01
- **Elements:** [`conformance`](elements/conformance.md)

### [algovoi-jcs-conformance-vectors](https://github.com/chopmob-cloud/algovoi-jcs-conformance-vectors)
Conformance vector sets for JCS RFC 8785 canonicalisation across x402, AP2, A2A, MPP receipt anchor sets. Cross-validated across ten independent JCS implementations in ten languages.
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`jcs`](elements/jcs.md) [`conformance`](elements/conformance.md) [`protocols`](elements/protocols.md)

### [algovoi-rfc9421-conformance](https://github.com/chopmob-cloud/algovoi-rfc9421-conformance)
Signed, cross-language conformance battery for RFC 9421 HTTP Message Signatures (Python, TypeScript, Rust, Go), byte-for-byte.
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`rfc9421`](elements/rfc9421.md) [`conformance`](elements/conformance.md)

### [algovoi-ube](https://github.com/chopmob-cloud/algovoi-ube)
Independent Apache-2.0 conformance harness for NTI-1, plus a Keystone coverage map
- **Language:** Python · **Last push:** 2026-11-03
- **Elements:** [`keystone`](elements/keystone.md) [`conformance`](elements/conformance.md)

### [ap2-pq-conformance](https://github.com/chopmob-cloud/ap2-pq-conformance)
Joint canonical home for AP2 Post-Quantum cross-scheme conformance fixtures (AlgoVoi + PQSafe). One AP2 PaymentMandate canonical byte sequence, multiple signature primitives — ES256 + Ed25519 + Falcon-1024 (AlgoVoi) + ML-DSA-65 (PQSafe pending). Per AP2#250 lock-in.
- **Language:** Python · **Last push:** 2026-06-01
- **Elements:** [`pqc`](elements/pqc.md) [`receipts`](elements/receipts.md) [`conformance`](elements/conformance.md) [`protocols`](elements/protocols.md)

## L6 · Settlement & chain rails (AVM)

12 repos.

### [algovoi-consensus-blocklist](https://github.com/chopmob-cloud/algovoi-consensus-blocklist)
4-of-N on-chain consensus wallet blocklist for Algorand and VOI (algopy ARC-4)
- **Language:** Python · **Last push:** 2026-06-03
- **Elements:** [`settlement`](elements/settlement.md)

### [algovoi-multi-chain-wallet-auth](https://github.com/chopmob-cloud/algovoi-multi-chain-wallet-auth)
Multi-chain wallet authentication primitives (EVM/Algorand/VOI/Solana/Stellar/Hedera/Tempo/ARC) — extracted from AlgoVoi production gateway in support of A2A #1737
- **Language:** Python · **Last push:** 2026-06-01
- **Elements:** [`settlement`](elements/settlement.md) [`protocols`](elements/protocols.md) [`gateway`](elements/gateway.md)

### [avm-ac2](https://github.com/chopmob-cloud/avm-ac2)
AC2 consent bound to an avm-mesh settlement: proof of who authorised a transaction, on Algorand and Voi
- **Language:** Python · **Last push:** 2026-11-17
- **Elements:** [`receipts`](elements/receipts.md) [`keystone`](elements/keystone.md) [`settlement`](elements/settlement.md)

### [avm-algo-voi-bridge](https://github.com/chopmob-cloud/avm-algo-voi-bridge)
Algorand to VOI Mainnet Bridge
- **Language:** — · **Last push:** 2026-10-29
- **Elements:** [`settlement`](elements/settlement.md)

### [avm-algovoi-falcon](https://github.com/chopmob-cloud/avm-algovoi-falcon)
Falcon-1024 (FIPS 206) keys and Algorand post-quantum accounts: keygen, deterministic sign/verify, falcon_verify LogicSig address derivation. Standalone, reproducible build from MIT sources.
- **Language:** C · **Last push:** 2026-10-29
- **Elements:** [`pqc`](elements/pqc.md) [`verify`](elements/verify.md) [`settlement`](elements/settlement.md)

### [avm-effectproof](https://github.com/chopmob-cloud/avm-effectproof)
_(no description on GitHub)_
- **Language:** Python · **Last push:** 2026-10-30
- **Elements:** [`verify`](elements/verify.md) [`settlement`](elements/settlement.md)

### [avm-hbar-bridge-relayer](https://github.com/chopmob-cloud/avm-hbar-bridge-relayer)
Algorand ↔ Hedera treasury-model bridge relayer
- **Language:** Python · **Last push:** 2026-10-29
- **Elements:** [`settlement`](elements/settlement.md)

### [avm-mesh](https://github.com/chopmob-cloud/avm-mesh)
Settlement receipts for the Algorand and Voi mesh: third-party-checkable proof that an on-chain transfer happened, argued from state proofs against an anchor you pin yourself. Two chains, zero third-party runtime dependencies.
- **Language:** Python · **Last push:** 2026-11-17
- **Elements:** [`receipts`](elements/receipts.md) [`verify`](elements/verify.md) [`settlement`](elements/settlement.md)

### [avm-proofpack](https://github.com/chopmob-cloud/avm-proofpack)
Portable, offline-verifiable transaction evidence for Algorand and Voi, anchored in state proofs
- **Language:** Python · **Last push:** 2026-10-30
- **Elements:** [`verify`](elements/verify.md) [`settlement`](elements/settlement.md)

### [avm-proofpack-ts](https://github.com/chopmob-cloud/avm-proofpack-ts)
_(no description on GitHub)_
- **Language:** TypeScript · **Last push:** 2026-10-30
- **Elements:** [`settlement`](elements/settlement.md)

### [avm-voi-algo-bridge](https://github.com/chopmob-cloud/avm-voi-algo-bridge)
VOI to Algorand Mainnet Bridge
- **Language:** Python · **Last push:** 2026-10-29
- **Elements:** [`settlement`](elements/settlement.md)

### [avm-wormhole-ntt-relayer](https://github.com/chopmob-cloud/avm-wormhole-ntt-relayer)
Wormhole NTT relayer — Algorand ↔ Base
- **Language:** Python · **Last push:** 2026-10-29
- **Elements:** [`settlement`](elements/settlement.md)

## L7 · Protocol adapters & integrations

9 repos.

### [algovoi-a2a-glink](https://github.com/chopmob-cloud/algovoi-a2a-glink)
AlgoVoi gibberlink + A2A reference
- **Language:** Python · **Last push:** 2026-10-27
- **Elements:** [`protocols`](elements/protocols.md)

### [algovoi-atb](https://github.com/chopmob-cloud/algovoi-atb)
AlgoVoi Agent Trust Bench client — run your AI agent through 166 adversarial x402 payment profiles and earn a Falcon-1024 signed reputation certificate.
- **Language:** Python · **Last push:** 2026-06-09
- **Elements:** [`pqc`](elements/pqc.md) [`protocols`](elements/protocols.md)

### [algovoi-compliance-gate-a2a](https://github.com/chopmob-cloud/algovoi-compliance-gate-a2a)
_(no description on GitHub)_
- **Language:** Python · **Last push:** 2026-09-21
- **Elements:** [`protocols`](elements/protocols.md)

### [AlgoVoi-MCP-Server](https://github.com/chopmob-cloud/AlgoVoi-MCP-Server)
MCP server exposing AlgoVoi payment tools to Claude Desktop, Claude Code, Cursor and Windsurf — npm + PyPI
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`receipts`](elements/receipts.md) [`protocols`](elements/protocols.md) [`gateway`](elements/gateway.md)

### [AlgoVoi-Platform-Adapters](https://github.com/chopmob-cloud/AlgoVoi-Platform-Adapters)
AlgoVoi apps & adapters — ecommerce, marketplace, AI-agent, and no-code integrations for the AlgoVoi x402 multi-chain payment gateway. Apache-2.0.
- **Language:** Python · **Last push:** 2026-11-22
- **Elements:** [`protocols`](elements/protocols.md) [`gateway`](elements/gateway.md)

### [algovoi-recurr](https://github.com/chopmob-cloud/algovoi-recurr)
_(no description on GitHub)_
- **Language:** Python · **Last push:** 2026-11-01
- **Elements:** [`receipts`](elements/receipts.md) [`gateway`](elements/gateway.md)

### [algovoi-reference-agent](https://github.com/chopmob-cloud/algovoi-reference-agent)
Apache 2.0 reference implementation of an agent that emits an AlgoVoi settlement-attestation-v1 receipt for a Base chain transaction. Composes algovoi-substrate + algovoi-settlement-attestation. Byte-deterministic against algovoi-jcs-conformance-vectors.
- **Language:** Python · **Last push:** 2026-06-09
- **Elements:** [`receipts`](elements/receipts.md) [`settlement`](elements/settlement.md) [`protocols`](elements/protocols.md)

### [elizaos-plugin-algovoi](https://github.com/chopmob-cloud/elizaos-plugin-algovoi)
Multi-chain agent-to-agent (A2A) crypto payments for ElizaOS — Algorand, VOI, Hedera, Stellar, Base, Solana, Tempo via the AlgoVoi A2A gateway.
- **Language:** TypeScript · **Last push:** 2026-06-02
- **Elements:** [`protocols`](elements/protocols.md) [`gateway`](elements/gateway.md)

### [use-wallet-algovoi](https://github.com/chopmob-cloud/use-wallet-algovoi)
AlgoVoi wallet adapter for @txnlab/use-wallet v5
- **Language:** TypeScript · **Last push:** 2026-08-07
- **Elements:** [`gateway`](elements/gateway.md)

## L8 · Platform & gateway

2 repos.

### [algovoi-platform](https://github.com/chopmob-cloud/algovoi-platform)
AlgoVoi Platform: payment rails, verifiable compliance estate and the post-quantum substrate they share. Free production use under BUSL-1.1; licence keys issued free.
- **Language:** Python · **Last push:** 2026-11-18
- **Elements:** [`pqc`](elements/pqc.md) [`receipts`](elements/receipts.md) [`settlement`](elements/settlement.md) [`protocols`](elements/protocols.md) [`gateway`](elements/gateway.md)

### [algovoi-secure-hub](https://github.com/chopmob-cloud/algovoi-secure-hub)
Universal substrate-neutral AlgoVoi security and trust hub
- **Language:** Python · **Last push:** 2026-10-29
- **Elements:** [`gateway`](elements/gateway.md)

## Meta · profile, hub & docs

5 repos.

### [.github](https://github.com/chopmob-cloud/.github)
AlgoVoi organization profile
- **Language:** — · **Last push:** 2026-08-26
- **Elements:** _(no element tags derived)_

### [algovoi-keystone-sdk](https://github.com/chopmob-cloud/algovoi-keystone-sdk)
Documentation for the AlgoVoi keystone: verifying agentic-action keystone chains and agent passports offline (RFC 8785 JCS + SHA-256).
- **Language:** — · **Last push:** 2026-08-15
- **Elements:** [`jcs`](elements/jcs.md) [`keystone`](elements/keystone.md) [`verify`](elements/verify.md)

### [chopmob-cloud](https://github.com/chopmob-cloud/chopmob-cloud)
The open substrate for agentic payments. Built so others could use it.
- **Language:** HTML · **Last push:** 2026-11-15
- **Elements:** _(no element tags derived)_

### [chopmob-cloud.github.io](https://github.com/chopmob-cloud/chopmob-cloud.github.io)
AlgoVoi substrate hub
- **Language:** HTML · **Last push:** 2026-08-20
- **Elements:** _(no element tags derived)_

### [Content](https://github.com/chopmob-cloud/Content)
_(no description on GitHub)_
- **Language:** — · **Last push:** 2026-04-04
- **Elements:** _(no element tags derived)_
