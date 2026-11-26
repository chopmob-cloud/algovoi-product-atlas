# Subject index — every documented AlgoVoi subject

Derived from the live docs corpus at [docs.algovoi.co.uk](https://docs.algovoi.co.uk) on 2026-11-26: **172 subjects** across **12 groups**.

Each row is a documented subject and where to read it. For *which products implement a subject*, use [`overlap.md`](overlap.md); for *products by layer*, see [`products.md`](products.md).

| | |
|---|---|
| Subjects documented | 172 |
| Groups | 12 |
| Reachable from site navigation | 172 |
| Live product repos (public) | see [`products.md`](products.md) |

## Start here

9 subjects.

| Subject | What it covers |
|---|---|
| [Compliance-aware agentic payments](https://docs.algovoi.co.uk/introduction) | AlgoVoi settles agent and merchant payments on-chain with sanctions screening, an audit chain and offline-verifiable receipts. Hosted or self-hosted. |
| [Application matrix](https://docs.algovoi.co.uk/application-matrix) | How every AlgoVoi package, platform service and integration interacts: dependency graph, data flow diagram, and a full cross reference table. |
| [Free licence](https://docs.algovoi.co.uk/free-licence) | Every AlgoVoi application is free to use in production. A free licence key is issued at the suite store, verifies offline, and the source is public. |
| [Quickstart: your first payment](https://docs.algovoi.co.uk/quickstart) | Take your first AlgoVoi USDC payment in five minutes: sign up, add a testnet payout address, create a hosted checkout link, confirm settlement on c… |
| [Take a payment](https://docs.algovoi.co.uk/take-a-payment) | Accept USDC on eight chains with hosted checkout, x402, MPP, AP2 or A2A, or use the tenant-free pay rail with twelve mainnet lanes and no account. |
| [Compliance duties](https://docs.algovoi.co.uk/compliance-duties) | UK MLRs, SAMLA, OFAC, OFSI, EU consolidated, travel rule, AI Act and DORA record keeping, each mapped to the AlgoVoi mechanism that discharges it. |
| [Verify a receipt](https://docs.algovoi.co.uk/verify-a-receipt) | Recompute an AlgoVoi receipt yourself: identify the format, get the bytes, check the digest or signature offline. No AlgoVoi service in the loop. |
| [Get it or self-host](https://docs.algovoi.co.uk/buy-or-self-host) | Run AlgoVoi hosted at 0.50% with a $1,000 mainnet trial, or self-host under a free perpetual licence. Current prices live in the store. |
| [Trial and pricing](https://docs.algovoi.co.uk/trial-and-pricing) | 60 days free on testnet, then KYC unlocks $1,000 of free mainnet USDC across seven chains, then a flat 0.50% per confirmed payment with volume tiers. |

## Protocols

5 subjects.

| Subject | What it covers |
|---|---|
| [x402 (HTTP 402 Payment Required)](https://docs.algovoi.co.uk/protocols/x402) | x402 charges per HTTP request and settles on chain. AlgoVoi is a multi-chain x402 facilitator issuing offline verifiable receipts and attestations. |
| [MPP (Method Payment Protocol)](https://docs.algovoi.co.uk/protocols/mpp) | MPP charges per call for MCP tools and JSON-RPC methods. AlgoVoi is a registered multi-chain MPP service issuing per method, offline verifiable rec… |
| [AP2 (Agent Payments Protocol)](https://docs.algovoi.co.uk/protocols/ap2) | AP2 is Google's mandate based protocol for autonomous agent commerce. AlgoVoi settles AP2 mandates on chain and issues mandate bound verifiable rec… |
| [A2A (Agent2Agent Protocol)](https://docs.algovoi.co.uk/protocols/a2a) | Google's open protocol for AI agents to discover and call each other. AlgoVoi runs a live, payment gated A2A agent issuing offline verifiable attes… |
| [Solana Actions and Blinks](https://docs.algovoi.co.uk/protocols/solana-actions) | AlgoVoi exposes hosted USDC checkouts as Solana Actions, rendered by any Blink aware client through dial.to, X and Discord, with reference binding. |

## Chains

8 subjects.

| Subject | What it covers |
|---|---|
| [Algorand USDC payments](https://docs.algovoi.co.uk/chains/algorand) | Accept USDC (ASA 31566704) on Algorand: memo bound checkouts, roughly five second confirmation, sub cent fees, plus xChain MetaMask pay via Allbridge. |
| [VOI aUSDC payments](https://docs.algovoi.co.uk/chains/voi) | Accept aUSDC (ASA 302190) on VOI: Algorand fork architecture, memo bound checkouts, opt in required, and sub cent transfer fees. |
| [Hedera USDC payments](https://docs.algovoi.co.uk/chains/hedera) | Accept USDC (HTS token 0.0.456858) on Hedera: memo bound checkouts, token association payouts, and Mirror Node verification on mainnet and testnet. |
| [Stellar USDC payments](https://docs.algovoi.co.uk/chains/stellar) | Accept USDC on Stellar: short 28 byte MEMO_TEXT binding, trustline payouts, Horizon API verification, and xChain MetaMask pay through Allbridge Core. |
| [Base USDC payments](https://docs.algovoi.co.uk/chains/base) | Accept USDC (ERC-20) on Base: EVM native settlement, amount only binding, and x402 payment facilitation on both Base mainnet and Base Sepolia testnet. |
| [Solana USDC payments](https://docs.algovoi.co.uk/chains/solana) | Accept USDC (SPL) on Solana: Solana Pay reference pubkey binding, associated token accounts, and xChain MetaMask payments routed through Circle CCT… |
| [Tempo USDCe payments](https://docs.algovoi.co.uk/chains/tempo) | Accept USDCe (TIP-20) on Tempo: EVM style settlement, amount only binding, and x402, MPP, AP2 and AgentCash on Tempo mainnet and Moderato testnet. |
| [ARC Network RPC and Chain ID](https://docs.algovoi.co.uk/chains/arc) | ARC Network testnet RPC (rpc.testnet.arc.io, formerly rpc.testnet.arc.network), chain ID 5042002, native-USDC gas, and EVM wallet setup for MetaMas… |

## Platform and API

24 subjects.

| Subject | What it covers |
|---|---|
| [AlgoVoi Pay](https://docs.algovoi.co.uk/algovoi-pay) | AlgoVoi Pay (pay.algovoi.co.uk) is a tenant-free, cross-protocol payment rail that charges USDC per call and returns an offline-verifiable signed r… |
| [Payment links](https://docs.algovoi.co.uk/concepts/payment-links) | Payment links create short lived hosted checkout URLs so customers pay in USDC by wallet or QR, for humans where x402 agent payment is too low level. |
| [Recurring payments](https://docs.algovoi.co.uk/concepts/recurring) | Three recurring payment models on AlgoVoi: invoice subscriptions (Recurr), agent native standing authority (MPP), and fiat funded agent mandates (A… |
| [Agentic Payment Mandates (APM)](https://docs.algovoi.co.uk/concepts/mandates) | Fiat funded JWT spending authority (in development): a human authorises a GBP cap once, the agent pays autonomously, AlgoVoi settles merchants in c… |
| [xChain payments](https://docs.algovoi.co.uk/concepts/xchain) | Let MetaMask users pay AlgoVoi checkouts with no destination chain wallet. Algorand, Solana and Stellar live, routed via Circle CCTP V2 or Allbridg… |
| [Notifications](https://docs.algovoi.co.uk/concepts/notifications) | Slack, Discord, Teams, Telegram, Mattermost, Rocket.Chat, Google Chat, Zulip, generic webhook. Same retry stack behind every destination. |
| [Chains overview](https://docs.algovoi.co.uk/concepts/chains-overview) | AlgoVoi's supported chains compared: stablecoins, confirmation times, fees, and the memo, reference pubkey and amount only binding mechanisms. Seve… |
| [Platform and API](https://docs.algovoi.co.uk/platform-and-api) | The hosted platform: gateway, control plane, facilitator, compliance engine and audit chain, plus the REST API reference and the concepts behind them. |
| [Platform schema reference](https://docs.algovoi.co.uk/platform-schema) | The canonical platform objects: payment links, payment events, receipts, attestations, mandates and references, and the page defining each schema. |
| [Agent Payment Module (APM)](https://docs.algovoi.co.uk/platform/apm) | The AlgoVoi production agentic payment platform: non custodial live rails and Recurr, plus a separate in development custodial mandate runtime. |
| [Payment Gateway](https://docs.algovoi.co.uk/platform/gateway) | The gateway at api.algovoi.co.uk: entry point for x402, MPP, AP2 and A2A traffic, handling auth, idempotency and routing to the facilitator. |
| [Facilitator](https://docs.algovoi.co.uk/platform/facilitator) | The stateless on-chain verifier: given a transaction and a checkout, it answers whether that exact amount of that asset reached that address. |
| [Control Plane](https://docs.algovoi.co.uk/platform/control-plane) | Tenant onboarding, KYC and KYB state, API key rotation, webhook registration and mandate state: the management backend behind the gateway. |
| [Compliance Engine](https://docs.algovoi.co.uk/platform/compliance-engine) | Sanctions screening against OFSI, OFAC SDN and the EU consolidated list with daily refresh, risk-tiered due diligence, and generic SAMLA-safe verdi… |
| [Audit Chain](https://docs.algovoi.co.uk/platform/audit-chain) | Every audit, screening and compliance event hash-linked at insert over RFC 8785 canonical JSON, so alteration is detectable rather than survivable. |
| [Recurring Payment Engine](https://docs.algovoi.co.uk/platform/recurr-engine) | Two tier recurring payment execution: MPP subscription invoicing and standing authority pull payments, with a customer self serve portal. All seven… |
| [Merchant Dashboard](https://docs.algovoi.co.uk/platform/dashboard) | The AlgoVoi operator and merchant dashboard: payment analytics, tenant management, risk monitoring, subscription tracking and compliance controls. |
| [Architecture](https://docs.algovoi.co.uk/concepts/architecture) | AlgoVoi's four tier topology: Cloudflare, the cloud edge, gateway and stateless facilitator, plus chain RPCs, price oracle and encryption at rest d… |
| [KYC and mainnet](https://docs.algovoi.co.uk/concepts/kyc-and-mainnet) | KYC and mainnet: identity verification gates live USDC payments, runs sanctions screening, and unlocks the $1,000 free mainnet allowance on seven c… |
| [x402 Facilitator: Build vs Buy](https://docs.algovoi.co.uk/x402-build-vs-buy) | Honest cost breakdown of building your own x402 facilitator versus buying a self hosted gateway: seven chains, post quantum receipts, AP2, A2A and… |
| [API introduction](https://docs.algovoi.co.uk/api-reference/introduction) | AlgoVoi REST API at api.algovoi.co.uk: base URL, JSON content type, Bearer authentication, idempotency keys, request IDs, versioning, and rate limits. |
| [Authentication](https://docs.algovoi.co.uk/api-reference/authentication) | Authenticate to the AlgoVoi API with a Bearer key plus X-Tenant-Id header: key prefixes (algv_, algvc_, algvw_), scopes, test versus live, and rota… |
| [API errors and status codes](https://docs.algovoi.co.uk/api-reference/errors) | AlgoVoi API errors: the JSON error envelope, HTTP status mapping (400/401/402/403/409/422/429), common error codes, and 4xx vs 5xx retry behaviour. |
| [Rate limits](https://docs.algovoi.co.uk/api-reference/rate-limits) | AlgoVoi API rate limits: per tenant (300/min) and per IP (120/min) caps, X-RateLimit headers, 429 Retry-After, and exponential back off with jitter. |

## Receipt and evidence formats

12 subjects.

| Subject | What it covers |
|---|---|
| [Settlement Attestation Format](https://docs.algovoi.co.uk/settlement-attestation) | AlgoVoi authored multi-chain settlement attestation format: a categorical SETTLED, PENDING_FINALITY, REVERSED enumeration under JCS RFC 8785. |
| [Refund Receipt Format](https://docs.algovoi.co.uk/refund-receipt) | AlgoVoi authored refund receipt format: a categorical FULL, PARTIAL, REJECTED enumeration under JCS RFC 8785 that composes with compliance receipts. |
| [Mandate Cancellation Receipt Format](https://docs.algovoi.co.uk/cancellation-receipt) | AlgoVoi authored mandate cancellation receipt format: a closed four element reason enumeration under JCS RFC 8785, with a companion IETF Internet-D… |
| [Payment Evidence Frame (PEF)](https://docs.algovoi.co.uk/payment-evidence-frame) | AlgoVoi authored canonical wrapper format for payment lifecycle receipts: a byte deterministic frame_id via JCS RFC 8785 plus optional RFC 9421 sig… |
| [Agentic Payment Receipts](https://docs.algovoi.co.uk/agentic-payment-receipts) | Verifiable agentic payment receipts across x402, AP2, A2A and MPP. Offline recomputable, no PII, on one shared JCS (RFC 8785) canonicalisation subs… |
| [Verifiable x402 Receipts](https://docs.algovoi.co.uk/verifiable-x402-receipt) | Issue and verify an x402 receipt any party can recompute offline. AlgoVoi pins RFC 8785 and SHA-256, so verification needs no issuer call and no ac… |
| [Offline-Verifiable Agent Payment Receipts](https://docs.algovoi.co.uk/offline-verifiable-receipts) | An offline verifiable agent payment receipt recomputes from its own preimage with RFC 8785 and SHA-256: no network, no issuer call, no service depe… |
| [x402 receipt adapter](https://docs.algovoi.co.uk/x402-receipt-adapter) | algovoi-x402-receipt-adapter turns an x402 payment into an offline verifiable settlement attestation, facilitator or origin side, bound into Keystone. |
| [Receipt sentinel](https://docs.algovoi.co.uk/receipt-sentinel) | Tenant side sliding window monitor for AlgoVoi verification failures. Detects tamper attempts, replay patterns and scanning bursts. Zero dependencies. |
| [.epi Evidence Export](https://docs.algovoi.co.uk/epi-evidence-export) | Export Records Vault evidence as a portable, post quantum sealed .epi artifact an auditor verifies offline with a bundled verifier, no AlgoVoi acco… |
| [Cancellation Receipt (lite)](https://docs.algovoi.co.uk/cancellation-receipt-lite) | Content addressed cancellation references for the AlgoVoi substrate: bind a mandate_ref and a cancellation reason into a deterministic cancellation… |
| [Refund Receipt (lite)](https://docs.algovoi.co.uk/refund-receipt-lite) | Content addressed refund references for the AlgoVoi substrate: bind a subject_ref, a result and an amount into a deterministic refund_ref. Apache 2.0. |

## Verification and audit

9 subjects.

| Subject | What it covers |
|---|---|
| [Settlement Verification](https://docs.algovoi.co.uk/settlement-verify) | Confirm a stablecoin payment settled and finalised on chain across seven live networks (Arc from 16 Sep 2026) with one call. The verification that… |
| [Audit verifier](https://docs.algovoi.co.uk/audit-verifier) | Standalone reference verifier for AlgoVoi selective disclosure audit bundles. Hosted, pip installable and npm installable, no infrastructure trust… |
| [Webhook verifier](https://docs.algovoi.co.uk/webhook-verifier) | Cryptographic verifier for AlgoVoi webhook signatures: v1 HMAC-SHA256 and v2 HKDF-SHA256 with HMAC-SHA384, offline capable, Python and TypeScript. |
| [action_ref (legacy / interop)](https://docs.algovoi.co.uk/action-ref-verifier) | action_ref is the legacy interop primitive, unchanged for existing adopters alongside its hosted verifier. New builds should use execution_ref. Apa… |
| [AVM Proofpack: Algorand State Proof Verification in Python](https://docs.algovoi.co.uk/avm-proofpack) | Verify an Algorand or Voi transaction offline in pure Python: avm-proofpack recomputes every hash and Merkle link from raw bytes up to the chain's… |
| [Verify it yourself](https://docs.algovoi.co.uk/verify-it-yourself) | Do not trust, verify. Clone the AlgoVoi conformance corpus and reproduce every vector byte for byte from raw preimages, offline, in Python or Node. |
| [AlgoVoi Reseal: quantum-seal the documents you already have](https://docs.algovoi.co.uk/reseal) | Re-anchor documents already signed with RSA or ECDSA into post-quantum, RFC-3161 timestamped, offline-verifiable attestations, before a quantum adv… |
| [AlgoVoi Evidence Auditor: prove your signed documents are valid, at scale](https://docs.algovoi.co.uk/evidence-auditor) | Batch-verify a whole archive of signed documents (classical RSA/ECDSA and post-quantum), flag the weak, expired and quantum-exposed ones, and produ… |
| [Verifiable Archive](https://docs.algovoi.co.uk/verifiable-archive) | Tamper evident, post quantum document archiving: every document is content addressed, encrypted at rest, and recorded in an append only chain you v… |

## Keystone and agent trust

29 subjects.

| Subject | What it covers |
|---|---|
| [Composite Trust Query Response Format](https://docs.algovoi.co.uk/composite-trust-query) | AlgoVoi authored verifier side response format for agentic payment audit chains: a closed four element trust verdict enumeration under JCS RFC 8785. |
| [Agent Session Authentication](https://docs.algovoi.co.uk/agent-session-auth) | Exchange an ATB ZKP certificate or a federation token for a short lived HMAC session JWT with an embedded spend cap, used across all payment routes. |
| [Agent Trust Bench](https://docs.algovoi.co.uk/agent-trust-bench) | Open agentic payment security test suite: run 187 adversarial x402 profiles against your AI agent. Free, provider neutral, no AlgoVoi account requi… |
| [Operator Control Panel](https://docs.algovoi.co.uk/operator-control-panel) | The operator console for a self hosted AlgoVoi Payment Rails deployment: merchants, payments, refunds, invoices, API keys, compliance and an audit… |
| [Plug a product into the Command Center](https://docs.algovoi.co.uk/command-center-products) | Any product with a health endpoint joins the Command Center live service bridge with one set of environment variables, and self registers on boot. |
| [Crypto-Agility](https://docs.algovoi.co.uk/crypto-agility) | Migrate a signing and encryption estate from classical to post quantum with provable continuity: classify keys, hybrid sign, re-attest evidence for… |
| [Agent Passport](https://docs.algovoi.co.uk/agent-passport) | Issue post quantum trust credentials to AI agents, verify them offline before granting spend authority, and revoke them instantly. Commercial OEM SDK. |
| [Agent Passport (lite)](https://docs.algovoi.co.uk/agent-passport-lite) | Content addressed agent identity references for the AlgoVoi substrate: bind agent_id, issuer, scope and validity window into a deterministic passpo… |
| [Spend Guardrail](https://docs.algovoi.co.uk/spend-guardrail) | The decision point for agentic payments: verify the passport, enforce the mandate, apply your policy, and get a signed ALLOW, DENY or REFER in one… |
| [Spend Guardrail (lite)](https://docs.algovoi.co.uk/spend-guardrail-lite) | Content addressed pre-payment decisions for the AlgoVoi substrate: bind a categorical ALLOW or DENY to the agent, the spend authority and the policy. |
| [Agent Guard](https://docs.algovoi.co.uk/agent-guard) | A spend budget an AI agent cannot raise itself: a human-signed mandate, fail-closed pre-execution checks, and receipts anyone can recompute offline… |
| [Decision chain (composition keystone)](https://docs.algovoi.co.uk/spend-decision-chain) | The open agentic payment lifecycle proven end to end: identity, authority, policy and the guardrail_ref decision compose into one recomputable chain. |
| [Payment Mandate](https://docs.algovoi.co.uk/payment-mandate) | The verifiable authorisation behind recurring and agentic crypto payments: a payer signs a capped, revocable mandate once and every pull is checked… |
| [Payment Mandate (lite)](https://docs.algovoi.co.uk/payment-mandate-lite) | Content addressed spend authority references for the AlgoVoi substrate: bind payer, cap, period and revocation state into a deterministic mandate_ref. |
| [Delegation Ref](https://docs.algovoi.co.uk/delegation-ref) | Content addressed delegation references for the AlgoVoi substrate: bind delegator, delegate, scope and validity into a tamper evident delegation_ref. |
| [Composite Trust Query (lite)](https://docs.algovoi.co.uk/composite-trust-query-lite) | Content addressed trust verdict references for the AlgoVoi substrate: bind a categorical verdict over an ordered set of pinned refs into a trust_qu… |
| [The Keystone](https://docs.algovoi.co.uk/keystone) | The AlgoVoi Keystone is the agentic payment trust chain, byte verifiable end to end: identity, authority, policy, decision, execution and verdict. |
| [The Keystone SDK](https://docs.algovoi.co.uk/keystone-sdk) | algovoi-keystone is the umbrella install: the connector builder, the agentic behaviour layer and the keystone command line in one place. Apache 2.0. |
| [The Keystone, proven on-chain](https://docs.algovoi.co.uk/keystone-proof) | The Keystone trust chain bound to real settlements on seven public testnets across x402, MPP, AP2 and A2A, every reference recomputable offline. |
| [Keystone Connectors](https://docs.algovoi.co.uk/keystone-connectors) | Keystone connectors bind a real data layer operation, such as a database write or an HTTP request, to the keystone decision that authorised it. |
| [Build and test a Keystone bolt-on](https://docs.algovoi.co.uk/keystone-connect) | algovoi-keystone-connect is an open toolkit for Keystone bolt-ons: build a data layer connector in about twelve lines, and verify any bolt-on offline. |
| [Rules, behaviours and triggers](https://docs.algovoi.co.uk/keystone-agent) | algovoi-keystone-agent is the behaviour layer for Keystone: declare rules and triggers as small specs, and gate any keystone-connect write before c… |
| [Runtime and journal](https://docs.algovoi.co.uk/keystone-runtime) | algovoi-keystone-runtime runs a Keystone chain and persists every emitted reference to a queryable, tamper evident SQLite journal that recomputes o… |
| [Publishing a Keystone bolt-on](https://docs.algovoi.co.uk/publishing-bolt-ons) | Take a Keystone bolt-on from scaffold to a published, installable package: build the wheel, publish to PyPI or a private index, confirm auto discov… |
| [Bring Your Own Keys](https://docs.algovoi.co.uk/bring-your-own-keys) | Hold your AlgoVoi signing and encryption keys in your own HSM, KMS or Vault. Custody is pluggable and signed output is byte identical, so verify is… |
| [ATB Pass Certificate: Reputation Pricing](https://docs.algovoi.co.uk/atb-reputation-credential) | Falcon-1024 signed reputation credential from the Agent Trust Bench: prove a refusal rate score to x402 gateways for variable pricing, JCS canonical. |
| [ATB Pass Certificate: Agent Guide](https://docs.algovoi.co.uk/atb-reputation-credential-agent-guide) | Integrate the ATB Pass Certificate into your agent payment flow: run the bench, fetch a certificate, present it on x402 requests for pricing discou… |
| [ATB Hub Conformance: Approval Guide](https://docs.algovoi.co.uk/atb-hub-conformance) | Conformance specification for running your own ATB Pass Certificate issuer hub: requirements, application process, and registry inclusion criteria. |
| [ATB vNext: verifiable agent evaluation](https://docs.algovoi.co.uk/atb-vnext) | Verifiable offline evaluation harness for payment agents: six test modes, seven OWASP LLM Top 10 scenario packs, five scores, a signed reproducible… |

## Substrate and canonicalisation

16 subjects.

| Subject | What it covers |
|---|---|
| [CAIP Chain-Agnostic Identifiers](https://docs.algovoi.co.uk/caip-identifiers) | Byte canonical validation of CAIP-2 chain ids, CAIP-10 account ids and CAIP-19 asset ids in the AlgoVoi substrate. Three opt in tiers, two languages. |
| [RFC 9421 HTTP Signatures Verifier](https://docs.algovoi.co.uk/rfc9421-verifier) | AlgoVoi authored reference verifier for RFC 9421 HTTP Message Signatures and RFC 9530 Digest Fields. Python and TypeScript at byte parity, Ed25519. |
| [RFC 9421 HTTP Signatures Signer](https://docs.algovoi.co.uk/rfc9421-signer) | AlgoVoi authored reference signer for RFC 9421 HTTP Message Signatures and RFC 9530 Digest Fields. Python and TypeScript, byte for byte parity, Ed2… |
| [Key-Credential Binding for RFC 9421 Agent Requests](https://docs.algovoi.co.uk/key-credential-binding) | Bind an RFC 9421 HTTP message signature to an issued agent credential: conformance vectors and reference verifiers (Python and TypeScript) for key… |
| [JCS Canonicalisation Substrate](https://docs.algovoi.co.uk/canonicalisation-substrate) | AlgoVoi authored JCS RFC 8785 canonicalisation discipline for agentic payment receipts, cross validated byte for byte across ten language implement… |
| [jcs-rfc8785-v2: PQC aware discipline](https://docs.algovoi.co.uk/canonicalisation-substrate-v2) | jcs-rfc8785-v2 is the PQC aware revision of the JCS RFC 8785 discipline: strictly additive, adding a signature algorithm registry and fail closed v… |
| [PQC Substrate Layer](https://docs.algovoi.co.uk/pqc-substrate) | AlgoVoi authored JCS and PQC integration layer: a signature_algorithm open enum, a fail closed verifier discipline, and a cross implementor anchor… |
| [Substrate Guard (lite)](https://docs.algovoi.co.uk/substrate-guard) | Deterministic input bounds and DoS hardening for the JCS substrate: runs before canonicalization and fails closed on resource hostile payloads. Apa… |
| [Substrate comparison](https://docs.algovoi.co.uk/substrate-comparison) | A layered comparison of methods for building tamper evident agentic payment records, decided by reproducible bytes at L1 and by capability above it. |
| [Conformance vector sets](https://docs.algovoi.co.uk/conformance-vectors) | 45 JCS conformance anchor sets covering the full receipt lifecycle: 374 vectors and 1226 byte for byte agreements across ten reference implementati… |
| [Substrate Adopters Registry](https://docs.algovoi.co.uk/adopters) | Public registry of parties publishing artefacts under the jcs-rfc8785-v1 canonicalisation discipline: a neutral record of adoption, not an endorsem… |
| [JCS Substrate Authorship and Provenance](https://docs.algovoi.co.uk/substrate-authorship-provenance) | AlgoVoi-authored JCS substrate (RFC 8785 JSON Canonicalization Scheme): what is published, where it runs, and one-command independent verification.… |
| [Substrate Licensing and Attribution](https://docs.algovoi.co.uk/substrate-licensing-and-attribution) | How AlgoVoi's Apache 2.0 substrate may be used, what attribution the licence requires, and how AlgoVoi handles reuse without it. Read before you bu… |
| [Substrate 2](https://docs.algovoi.co.uk/substrate-2) | Commercial AlgoVoi substrate and self hosted payments suite: the agentic payment gateway, post quantum evidence core, Command Center and Records Va… |
| [Substrate 2 Addons](https://docs.algovoi.co.uk/substrate-2-addons) | Bolt additional services onto the Substrate 2 control plane. Any service with a health endpoint joins with two environment variables and self regis… |
| [Ports and interfaces](https://docs.algovoi.co.uk/substrate-2-ports) | Default ports and HTTP interfaces for every service in the AlgoVoi on-prem suite. Every port is overridable and no two defaults collide. |

## Compliance and record keeping

23 subjects.

| Subject | What it covers |
|---|---|
| [Compliance & Security](https://docs.algovoi.co.uk/compliance) | AlgoVoi compliance overview for developers: what we do, what the policy binder contains, and how to request the full documents under NDA. |
| [Compliance Receipt Format](https://docs.algovoi.co.uk/compliance-receipt) | AlgoVoi authored admission time compliance receipt format: a categorical ALLOW, REFER, DENY enumeration under JCS RFC 8785, with a companion IETF d… |
| [No-PII Compliance Receipts](https://docs.algovoi.co.uk/no-pii-compliance-receipt) | A no PII compliance receipt binds an ALLOW, REFER or DENY screening verdict to a content addressed payer reference that is hashed and never emitted. |
| [Compliance Gate Extension v1](https://docs.algovoi.co.uk/compliance-gate-v1) | AlgoVoi authored A2A extension for the admission time sanctions and KYC gate: a closed ALLOW, REFER, DENY verdict enumeration under JCS RFC 8785. |
| [Compliance Gate](https://docs.algovoi.co.uk/compliance-gate-v2) | Turn a screening decision into a signed, no PII compliance receipt: a categorical ALLOW, REFER or DENY verdict that verifies offline. Commercial OE… |
| [Compliance Gate (lite)](https://docs.algovoi.co.uk/compliance-gate-lite) | Content addressed compliance decisions for the AlgoVoi substrate: bind an ALLOW, REFER or DENY verdict and a no PII payer reference to the policy i… |
| [Sanctions Monitor](https://docs.algovoi.co.uk/sanctions-monitor) | Continuous sanctions monitoring as signed, no PII delta evidence: keep a counterparty watchlist, re-screen on every refresh, emit a signed delta re… |
| [Travel Rule](https://docs.algovoi.co.uk/travel-rule) | FATF Travel Rule (Recommendation 16) as signed, no PII, post quantum confidential evidence exchanged between VASPs, with a Falcon-1024 signed receipt. |
| [Zero knowledge compliance proofs](https://docs.algovoi.co.uk/proofs) | Prove a payment was screened and compliant, and that the payer's risk score cleared a threshold, without revealing PII or the score. Commercial OEM… |
| [Compliance receipt verifier](https://docs.algovoi.co.uk/receipt-verifier) | Standalone reference verifier for AlgoVoi JWS compliance receipts: offline capable, no infrastructure trust, Python and TypeScript with shared vect… |
| [Retention Chain Substrate](https://docs.algovoi.co.uk/retention-chain-substrate) | Self verifiable audit chain linking payment receipts with no external infrastructure. Cross validated in eight languages. Satisfies MiCA 80 and DOR… |
| [Self Hosted Compliance Evidence Platform](https://docs.algovoi.co.uk/verifiable-compliance-suite) | Self hosted, air gap capable evidence estate for HIPAA, GDPR and eIDAS: post quantum signatures, a tamper evident audit log, RFC 3161 trusted times… |
| [Compliance Suite: Setup and Deployment](https://docs.algovoi.co.uk/vcs-deployment-guide) | Install and operate the AlgoVoi Verifiable Compliance Suite: extract the bundle, run the Command Center, set up accounts, roles and two factor sign… |
| [EU AI Act Article 12 Record Keeping](https://docs.algovoi.co.uk/eu-ai-act-recordkeeping) | EU AI Act Article 12 record keeping obligations apply from 2 December 2027 (Annex III) and 2 August 2028 (Annex I) under Regulation (EU) 2026/1744.… |
| [MiCA and DORA Record Keeping Evidence](https://docs.algovoi.co.uk/mica-dora-evidence) | MiCA Article 68(9) and DORA logging evidence: self hosted, tamper evident, offline verifiable records under your own keys, with RFC 3161 timestamps. |
| [Self Host Regulated Records Preservation](https://docs.algovoi.co.uk/regulated-records-self-hosting-guide) | Run a self hosted, air gap capable evidence estate for HIPAA, GDPR and eIDAS records: RFC 3161 timestamping, a tamper evident audit log, and legal… |
| [SCIM 2.0 Provisioning](https://docs.algovoi.co.uk/scim-provisioning) | Auto provision and deprovision Compliance Command Center accounts from Okta, Azure AD or OneLogin over SCIM 2.0, mapping directory groups onto RBAC… |
| [Self Hosted Arkivum Alternative](https://docs.algovoi.co.uk/arkivum-alternative) | Arkivum alternative you host yourself: air gap capable records preservation, one perpetual licence, post quantum signatures, offline verification. |
| [Self Hosted Preservica Alternative](https://docs.algovoi.co.uk/preservica-alternative) | Preservica alternative you host yourself: records preservation on your own infrastructure, one perpetual licence, post quantum signed, air gap capa… |
| [Records Vault](https://docs.algovoi.co.uk/records-vault) | Regulated records preservation for health and legal: RFC 3161 trusted timestamping, a tamper evident read access log, and legal and e-discovery holds. |
| [Retention App](https://docs.algovoi.co.uk/retention-app) | Signed, offline verifiable payment receipt retention: auto maintained per issuer hash linked chains and Falcon-1024 signed evidence exports for aud… |
| [Verifiable Audit Log](https://docs.algovoi.co.uk/audit-log) | Append any business event to a tamper evident, post quantum chain. Entries are content addressed, append only and verifiable offline. Commercial OE… |
| [Compliance Command Center](https://docs.algovoi.co.uk/compliance-command-center) | Self hosted management console over your AlgoVoi estate: ingests exported evidence, re-verifies every signed chain offline, and exports an auditor… |

## Integrations

12 subjects.

| Subject | What it covers |
|---|---|
| [Integrations overview](https://docs.algovoi.co.uk/integrations/overview) | Drop-in adapters for e-commerce, chat bots, AI frameworks, accounting, and more. One-line install, then point at your tenant. |
| [E-commerce adapters](https://docs.algovoi.co.uk/integrations/ecommerce) | Drop in USDC payment modules for Shopify, WooCommerce, Magento, Wix and Squarespace, plus settlement links for Amazon, eBay, Etsy and Walmart. |
| [Chat bot payments](https://docs.algovoi.co.uk/integrations/chat-bots) | Take USDC payments inside Discord, Telegram, X, Viber, and WhatsApp with AlgoVoi chat bots. Type 'pay £5' to mint a hosted checkout across seven ch… |
| [AI agent frameworks](https://docs.algovoi.co.uk/integrations/ai-frameworks) | Payment-gate AI agents in LangChain, LangGraph, CrewAI, AutoGen, LlamaIndex, Vercel AI SDK, and ElizaOS. AlgoVoi adds x402, MPP, and AP2 USDC paywa… |
| [AI model APIs](https://docs.algovoi.co.uk/integrations/ai-models) | Paywall OpenAI, Claude, Gemini, Cohere, Mistral, Bedrock, and xAI Grok per call in USDC. AlgoVoi model adapters add x402, MPP, or AP2 payment to ea… |
| [AlgoVoi MCP server](https://docs.algovoi.co.uk/integrations/mcp-server) | Expose AlgoVoi as MCP tools to Claude Desktop, Claude Code, Cursor, and Windsurf. Create USDC payment links and verify x402, MPP, AP2, and A2A on-c… |
| [Native SDKs](https://docs.algovoi.co.uk/integrations/native-sdks) | Zero-dependency AlgoVoi SDKs for Go, PHP, Python, and Rust. One standard-library file creates USDC checkouts, verifies webhooks, and checks payment… |
| [No-code platforms](https://docs.algovoi.co.uk/integrations/no-code) | Wire AlgoVoi USDC payments into Pabbly Connect, Activepieces, GiveWP, and Gravity Forms. Build crypto-payment checkout and triggers with no code. |
| [Accounting and invoicing](https://docs.algovoi.co.uk/integrations/accounting) | Attach AlgoVoi USDC payment links to invoices in Xero, QuickBooks, FreshBooks, MYOB, Sage, Wave and Zoho Books, with writeback on payment confirmat… |
| [Open banking](https://docs.algovoi.co.uk/integrations/banking) | Accept UK Faster Payments and SEPA Instant via TrueLayer or Yapily, then settle automatically as USDC on-chain through AlgoVoi's open-banking adapt… |
| [Chrome extension](https://docs.algovoi.co.uk/integrations/chrome-extension) | AlgoVoi's in house browser wallet: native x402, MPP and AP2 payment protocol support across six chains in one Manifest V3 Chrome extension. |
| [Outbound webhooks](https://docs.algovoi.co.uk/integrations/outbound-webhooks) | Stripe-shaped events delivered to your endpoint with HMAC-SHA256 signing, exponential-backoff retry, and a per-tenant audit log. |

## Self-host and operations

9 subjects.

| Subject | What it covers |
|---|---|
| [On-Premise Deployment](https://docs.algovoi.co.uk/on-premise) | Run the full AlgoVoi payment stack on your own infrastructure: a self contained Docker Compose stack with no dependency on AlgoVoi hosted services. |
| [Self Hosted x402 Agentic Payment Gateway](https://docs.algovoi.co.uk/payment-rails-sqlite) | Self hosted x402 facilitator and agentic payment gateway: settle x402, MPP and AP2 on seven chains (Arc from 16 Sep 2026) with post quantum receipt… |
| [Payment Rails: Setup and Deployment](https://docs.algovoi.co.uk/payment-rails-deployment-guide) | Install and go live with the AlgoVoi Payment Rails bundle: one command brings the stack up under systemd behind TLS, white labelled to your own dom… |
| [Agent Payment Rails Security](https://docs.algovoi.co.uk/payment-rails-security) | The three layer defence built into AV-RAILS. Every block across x402, MPP, AP2 and A2A is a Falcon-1024 signed, offline verifiable decision. |
| [Run Your Own x402 Facilitator](https://docs.algovoi.co.uk/x402-self-host-guide) | Step by step guide to self hosting an x402 facilitator: install the AlgoVoi payment rails, wire your domain, accept x402 payments in five minutes. |
| [Security Suite](https://docs.algovoi.co.uk/security-suite) | Layered, verifiable defence for agentic payment infrastructure: input integrity hardening before canonicalization, plus IP, geo and rate limit at t… |
| [Disaster Recovery and Key Ceremony](https://docs.algovoi.co.uk/disaster-recovery) | HA and DR runbook for the self hosted Verifiable Compliance Suite: recovery objectives, backup scope, restore and verify, and witnessed key ceremon… |
| [Security posture](https://docs.algovoi.co.uk/security) | How AlgoVoi protects merchants, payers, regulators and the audit trail: concrete, independently verifiable claims with no marketing fluff. |
| [Incident protocol](https://docs.algovoi.co.uk/incident-protocol) | How AlgoVoi detects, communicates and recovers from chain or gateway incidents, including degraded versus down handling and the post mortem cadence. |

## Corpus and provenance

16 subjects.

| Subject | What it covers |
|---|---|
| [Protocols and chains](https://docs.algovoi.co.uk/protocols-and-chains) | The agent payment protocols AlgoVoi implements, x402, MPP, AP2, A2A and Solana Actions, and every chain it settles on with asset IDs and binding. |
| [Chain-agnostic agent payment negotiation](https://docs.algovoi.co.uk/chain-agnostic-negotiation) | Agents that speak different chains negotiate a shared settlement lane, then pay from their own wallet. No account. Twelve mainnet chains across x40… |
| [Signed-Token Anchoring](https://docs.algovoi.co.uk/signed-token-anchoring) | Which bytes you hash when anchoring a signed receipt: anchor the raw signed JWS or SD-JWT bytes, never a re-canonicalised decoded payload. |
| [execution_ref](https://docs.algovoi.co.uk/execution-ref) | Decision bound execution evidence over the AlgoVoi substrate: binds an executed agent action to the exact decision that authorised it. RFC 8785, SH… |
| [Policy Binding](https://docs.algovoi.co.uk/policy-binding) | Additive policy snapshot binding over a frozen subject reference: proves which ruleset version was in force when a record was sealed. Apache 2.0. |
| [Cell and KAF](https://docs.algovoi.co.uk/cell-kaf) | The Keystone Assurance Framework: hermetic cells that reproduce every JCS conformance vector byte for byte, and sealed, hash-chained receipts you v… |
| [Ecosystem Adoption Evidence](https://docs.algovoi.co.uk/adoption-evidence) | Reproducible evidence that the AlgoVoi canonicalisation substrate reached ecosystem infrastructure. Every datum recomputes against public APIs. |
| [Ecosystem contributions](https://docs.algovoi.co.uk/ecosystem-contributions) | Public pull requests and IETF Internet-Drafts AlgoVoi filed upstream to x402, AP2, A2A, MPP and the JCS substrate. Verifiable proof of work. |
| [x402 Document Index](https://docs.algovoi.co.uk/x402-document-index) | Neutral index of IETF Internet-Drafts, published specifications and URN registrations in the x402 receipt format ecosystem, by author and by anchor. |
| [Package Suite](https://docs.algovoi.co.uk/package-suite) | 25 AlgoVoi open source packages on PyPI and 25 on npm under Apache 2.0, three commercial packages, and the 29 tool MCP server on three registries. |
| [Post Quantum Evidence Longevity](https://docs.algovoi.co.uk/post-quantum-evidence-longevity) | How Falcon-1024 and ML-DSA-65 signatures keep compliance evidence verifiable for decades: long term key custody in HSM, KMS or Vault, and 21 CFR Pa… |
| [Build a passport bolt-on](https://docs.algovoi.co.uk/passport-bolt-ons) | Map any identity or KYC source into a content addressed AlgoVoi agent passport_ref: a deterministic, no PII reference for the pre-payment decision… |
| [Recovery Vault](https://docs.algovoi.co.uk/recovery-vault) | Threshold (Shamir k-of-n) post quantum key recovery for any Substrate 2 key: data loss protection and identity continuity with no third party key use. |
| [Product Key Registry](https://docs.algovoi.co.uk/product-key-registry) | A Falcon-1024 signed registry of AlgoVoi signing keys with per product custody and did:web identities. Authenticate any signature and follow key ro… |
| [Support and contact](https://docs.algovoi.co.uk/support) | How to get help with AlgoVoi by email, GitHub and security disclosure, what to include in a request, and response targets for tickets and incidents. |
| [AlgoVoi changelog](https://docs.algovoi.co.uk/changelog) | AlgoVoi releases, new chain support and breaking changes: MCP server tools, Agent Trust Bench certificates, xChain settlement and protocol adapters. |
