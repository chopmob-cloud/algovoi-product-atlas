#!/usr/bin/env python3
"""Probe the live AlgoVoi platform surfaces and record what actually answered.

Writes data/platforms.json. Every entry carries the URL probed and the HTTP status
returned, so downstream documents can state a *measured* fact instead of a claim.
A surface that does not resolve is recorded as unreachable, never silently dropped
and never described as available.

Run: python scripts/probe_platforms.py
"""
import json, os, datetime, urllib.request, urllib.error, ssl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "platforms.json")
UA = {"User-Agent": "Mozilla/5.0 (compatible; algovoi-atlas-probe)"}
CTX = ssl.create_default_context()

# (key, label, url, what it is). Label/description must stay true of the URL.
SURFACES = [
    ("docs", "Documentation",
     "https://docs.algovoi.co.uk/introduction",
     "The canonical documentation site; every subject in the subject index lives here."),
    ("gateway", "Hosted gateway",
     "https://api.algovoi.co.uk/health",
     "Multi-chain x402 facilitator: tenants, API keys, KYB. Liveness at /health."),
    ("suite_store", "Suite store",
     "https://api.algovoi.co.uk/suite-store",
     "Where a free licence key is issued per deployment."),
    ("x402_discovery", "x402 discovery",
     "https://api.algovoi.co.uk/.well-known/x402",
     "Machine-readable statement of the paid routes the gateway serves."),
    ("pay_rail", "Pay rail",
     "https://pay.algovoi.co.uk/",
     "Tenant-free rail: no account, settlement is the credential."),
    ("verify", "Verification",
     "https://verify.algovoi.co.uk/",
     "Browser verification of a receipt with no AlgoVoi service in the loop."),
    ("apex", "Marketing site",
     "https://algovoi.co.uk/",
     "The public marketing apex."),
]


def probe(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=25, context=CTX) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None


def main():
    rows = []
    for key, label, url, desc in SURFACES:
        code = probe(url)
        rows.append({"key": key, "label": label, "url": url, "desc": desc,
                     "http": code, "live": code == 200})
        print(f"{label:18s} {str(code):>5s}  {url}")
    live = [r for r in rows if r["live"]]
    if not live:
        raise SystemExit("ABORT: no surface answered — refusing to publish platform facts")
    data = {"probed": datetime.date.today().isoformat(),
            "method": "urllib GET, 25s timeout, Mozilla UA; http=None means no response",
            "surfaces": rows,
            "live_count": len(live), "total_count": len(rows)}
    json.dump(data, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    # Render platforms.md from the same data, so the page and the overview cannot
    # disagree about which hosts were probed or what they returned.
    live = [r for r in rows if r["live"]]
    L = ["# Platforms — the AlgoVoi surfaces, and what runs where", "",
         f"Every AlgoVoi product is consumed through one of these surfaces. Each host below "
         f"was probed on **{data['probed']}**; the **HTTP** column is the status the probe "
         "returned, so a reader can tell a live surface from a documented one.", "",
         "| Surface | Host | What it is | HTTP |", "|---|---|---|---|"]
    for r in rows:
        host = r["url"].split("//", 1)[1]
        code = r["http"] if r["http"] is not None else "no response"
        L.append(f"| {r['label']} | [`{host}`]({r['url']}) | {r['desc']} | {code} |")
    L += ["", f"**{len(live)} of {len(rows)} surfaces answered HTTP 200.** A host that "
          "returned anything else is shown with its real status rather than dropped, and "
          "a host that does not resolve is recorded as `no response`.", "",
          "## The two access models", "",
          "The estate is consumed two ways, and almost every page assumes one of them:", "",
          "- **Governed (hosted).** Tenant, API key, KYB. The operator carries the compliance "
          "duty; the platform carries the state.",
          "- **Proof (tenant-free).** No account, no key. Settlement is the credential and "
          "the receipt is the evidence.", "",
          "Self-hosting is the third path and is not a host at all: the same products run "
          "under a free perpetual licence. See the subject index → *Self-host and operations*.", "",
          "## What this file is not", "",
          "Hosts appear here because they are **live and checkable**, not because they are "
          "endorsed capacity claims. Counts of chains, protocols and tools are stated on the "
          "documentation pages that own them; this file links those pages rather than "
          "restating their numbers, because a number restated in two places drifts.", "",
          f"*Provenance: `scripts/probe_platforms.py`, {data['probed']} — "
          f"{data['method']}. This file is regenerated by that script; edit the script, "
          "not the page.*", ""]
    open(os.path.join(ROOT, "platforms.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))
    print(f"platforms.md written: {len(live)}/{len(rows)} live")
    print(f"\nlive={len(live)}/{len(rows)} -> data/platforms.json")


if __name__ == "__main__":
    main()
