#!/usr/bin/env python3
"""Build the AlgoVoi subject index (docs.algovoi.co.uk) into the product atlas.

Grounding: every row is derived from the LIVE docs corpus at build time, not
hand-written. Sources:
  * https://docs.algovoi.co.uk/llms.txt          -> page list, titles, descriptions
  * https://docs.algovoi.co.uk/docs.json (nav)   -> nav group membership/order
The subject index answers "what does AlgoVoi cover, and where do I read it"
for every documented subject; the atlas answers "which products implement it".

Run:  python scripts/build_subjects.py
Emits: subjects.md, data/subjects.json
Asserts before writing; exits non-zero rather than publishing a bad index.
"""
import json, os, re, sys, urllib.request, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://docs.algovoi.co.uk"
# docs.json is site config, not served at the domain root, and the docs repo is
# PRIVATE — fetch it through authenticated `gh api` (a raw URL 404s either way).
NAV_REPO_FILE = ("chopmob-cloud/docs", "docs.json")
UA = {"User-Agent": "Mozilla/5.0 (compatible; algovoi-atlas-builder)"}


def fetch(path):
    url = path if path.startswith("http") else BASE + path
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


def fetch_nav():
    """docs.json via authenticated gh (works on a private repo)."""
    import base64, subprocess
    repo, path = NAV_REPO_FILE
    out = subprocess.run(["gh", "api", f"repos/{repo}/contents/{path}", "--jq", ".content"],
                         capture_output=True, text=True, timeout=90)
    if out.returncode != 0:
        sys.exit(f"ABORT: cannot read {repo}/{path}: {out.stderr.strip()[:200]}")
    return base64.b64decode(out.stdout).decode("utf-8", "replace")


def parse_llms(text):
    """-> {slug: {title, desc}} from the llms.txt index."""
    rows = {}
    for m in re.finditer(r"^\s*-\s*\[([^\]]+)\]\((https://docs\.algovoi\.co\.uk/[^)]*?)\.md\)\s*:?\s*(.*)$",
                         text, re.M):
        title, url, desc = m.group(1).strip(), m.group(2), m.group(3).strip()
        slug = url.replace("https://docs.algovoi.co.uk/", "").strip("/")
        if slug:
            rows[slug] = {"title": title, "desc": desc}
    return rows


def parse_nav(text):
    """-> {slug: (group_name, order_index)} from the docs.json navigation."""
    cfg = json.loads(text)
    out, order = {}, 0
    def walk(node, group):
        nonlocal order
        if isinstance(node, dict):
            g = node.get("group")
            if g:
                group = g
            for k, v in node.items():
                if k in ("pages", "groups", "tabs", "anchors"):
                    walk(v, group)
        elif isinstance(node, list):
            for item in node:
                if isinstance(item, str):
                    out.setdefault(item.strip("/"), (group or "", order)); order += 1
                else:
                    walk(item, group)
    walk(cfg.get("navigation", {}), None)
    return out


# Subject grouping: the reader's job, not the org chart. Ordered, first match wins.
GROUPS = [
    ("Start here",            {"introduction","application-matrix","free-licence","quickstart",
                               "take-a-payment","compliance-duties","verify-a-receipt",
                               "buy-or-self-host","trial-and-pricing"}),
    ("Protocols",             None),   # prefixes set below
    ("Chains",                None),
    ("Platform and API",      None),
    ("Receipt and evidence formats", None),
    ("Verification and audit", None),
    ("Keystone and agent trust", None),
    ("Substrate and canonicalisation", None),
    ("Compliance and record keeping", None),
    ("Integrations",          None),
    ("Self-host and operations", None),
    ("Corpus and provenance", None),
]
PREFIX_GROUP = {
    "protocols/": "Protocols",
    "chains/": "Chains",
    "platform/": "Platform and API",
    "api-reference/": "Platform and API",
    "integrations/": "Integrations",
    "concepts/": "Platform and API",
}
KEYWORD_GROUP = [
    ("Compliance and record keeping", ("compliance","record-keeping","eu-ai-act","mica","dora",
                                       "travel-rule","sanctions","retention","records-vault",
                                       "arkivum","preservica","regulated","audit-log","scim")),
    ("Keystone and agent trust", ("keystone","agent-guard","agent-passport","spend-guardrail",
                                  "payment-mandate","delegation-ref","spend-decision","atb",
                                  "agent-trust","agent-session","crypto-agility","composite-trust",
                                  "command-center","operator-control","bring-your-own-keys")),
    ("Substrate and canonicalisation", ("substrate","jcs","canonicalis","pqc","rfc9421","keyid",
                                        "key-credential","conformance","caip")),
    ("Receipt and evidence formats", ("receipt","attestation","evidence-frame","pef","refund",
                                      "cancellation","settlement-attestation","evidence-export",
                                      "verifiable-x402","agentic-payment-receipts","offline-verifiable")),
    ("Verification and audit", ("verif","audit-verifier","verify-it-yourself","evidence-auditor",
                                "reseal","settlement-verify","proofs","keystone-proof")),
    ("Self-host and operations", ("self-host","on-premise","deployment","disaster-recovery",
                                  "incident","security","payment-rails-sqlite","-guide")),
    ("Corpus and provenance", ("adopters","adoption-evidence","ecosystem-contributions",
                               "x402-document-index","package-suite","authorship","licensing",
                               "changelog","support","product-key-registry")),
    ("Platform and API", ("gateway","facilitator","platform","pay-rail","algovoi-pay","recurr",
                          "dashboard","control-plane","apm","xchain","payment-links","recurring",
                          "kyc","notifications","chains-overview","architecture","x402-build-vs-buy",
                          "x402-self-host","payment-rails")),
]


def group_for(slug, title, nav_group):
    if slug in ("introduction", "application-matrix", "free-licence", "quickstart",
                "take-a-payment", "compliance-duties", "verify-a-receipt",
                "buy-or-self-host", "trial-and-pricing"):
        return "Start here"
    for pref, g in PREFIX_GROUP.items():
        if slug.startswith(pref):
            return g
    hay = (slug + " " + title).lower()
    for g, kws in KEYWORD_GROUP:
        if any(k in hay for k in kws):
            return g
    return "Corpus and provenance"


def main():
    llms = parse_llms(fetch("/llms.txt"))
    nav = parse_nav(fetch_nav())
    if len(llms) < 100:
        sys.exit(f"ABORT: parsed only {len(llms)} pages from llms.txt — refusing to publish")
    # assertion: every nav page must exist as a document
    missing = [s for s in nav if s not in llms]
    orphans = [s for s in llms if s not in nav]
    rows = []
    for slug, meta in llms.items():
        g = group_for(slug, meta["title"], nav.get(slug, ("", 0))[0])
        rows.append({"slug": slug, "title": meta["title"], "desc": meta["desc"],
                     "group": g, "in_nav": slug in nav,
                     "nav_order": nav.get(slug, ("", 10**6))[1]})
    rows.sort(key=lambda r: (r["group"], r["nav_order"], r["slug"]))
    # assertion: no page may land in zero groups, and coverage must be complete
    grouped = {}
    for r in rows:
        grouped.setdefault(r["group"], []).append(r)
    order = [g for g, _ in GROUPS]
    unknown = [g for g in grouped if g not in order]
    if unknown:
        sys.exit(f"ABORT: ungrouped subject buckets {unknown}")

    stamp = datetime.date.today().isoformat()
    L = ["# Subject index — every documented AlgoVoi subject", "",
         f"Derived from the live docs corpus at [docs.algovoi.co.uk]({BASE}) on {stamp}: "
         f"**{len(rows)} subjects** across **{len(grouped)} groups**.", "",
         "Each row is a documented subject and where to read it. For *which products implement "
         "a subject*, use [`overlap.md`](overlap.md); for *products by layer*, see "
         "[`products.md`](products.md).", "",
         "| | |", "|---|---|",
         f"| Subjects documented | {len(rows)} |",
         f"| Groups | {len(grouped)} |",
         f"| Reachable from site navigation | {sum(1 for r in rows if r['in_nav'])} |",
         f"| Live product repos (public) | see [`products.md`](products.md) |", ""]
    for g in order:
        if g not in grouped:
            continue
        items = grouped[g]
        L += [f"## {g}", "", f"{len(items)} subjects.", "",
              "| Subject | What it covers |", "|---|---|"]
        for r in items:
            d = (r["desc"] or "").replace("|", "\\|").strip()
            if len(d) > 150:
                d = d[:147].rstrip() + "…"
            L.append(f"| [{r['title']}]({BASE}/{r['slug']}) | {d} |")
        L.append("")
    if orphans:
        L += ["## Not in site navigation", "",
              f"{len(orphans)} documented subject(s) exist as pages but are absent from the "
              "`docs.json` navigation — reachable only by direct URL.", "",
              "| Subject | Page |", "|---|---|"]
        for s in sorted(orphans):
            L.append(f"| {llms[s]['title']} | [{s}]({BASE}/{s}) |")
        L.append("")

    open(os.path.join(ROOT, "subjects.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))
    json.dump({"generated": stamp, "source": BASE + "/llms.txt",
               "subjects": rows,
               "coverage": {g: len(v) for g, v in grouped.items()},
               "nav_missing_pages": sorted(missing),
               "pages_not_in_nav": sorted(orphans)},
              open(os.path.join(ROOT, "data", "subjects.json"), "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print(f"subjects={len(rows)} groups={len(grouped)} in_nav={sum(1 for r in rows if r['in_nav'])}")
    print("coverage:", {g: len(v) for g, v in sorted(grouped.items(), key=lambda x: -len(x[1]))})
    if missing:
        print("WARNING nav pages with no document:", missing)
    if orphans:
        print("pages not in nav:", len(orphans))


if __name__ == "__main__":
    main()
