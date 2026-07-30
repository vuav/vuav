#!/usr/bin/env python3
"""
Pull the most recent actively-exploited vulnerabilities from the CISA KEV
catalog and drop them into the README between the KEV markers.

Fail-safe by design: any network/parse error leaves the README untouched
(exit 0) so a bad feed day never blanks your profile.
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
README = Path("README.md")
START, END = "<!-- KEV-START -->", "<!-- KEV-END -->"
N = 6            # how many to show
MAXLEN = 52      # truncate long product/vuln names for alignment


def fetch():
    req = urllib.request.Request(KEV_URL, headers={"User-Agent": "vuav-profile-bot"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)


def clip(s, n=MAXLEN):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1] + "…"


def render(items):
    rows = []
    for v in items:
        cve = v.get("cveID", "CVE-????-????")
        vendor = clip(v.get("vendorProject", "?"), 18)
        name = clip(v.get("vulnerabilityName", v.get("shortDescription", "")), 46)
        added = v.get("dateAdded", "")
        rows.append(f"{cve:<18} {added:<11} {vendor:<18} {name}")

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = f"{'CVE':<18} {'ADDED':<11} {'VENDOR':<18} VULNERABILITY"
    body = "\n".join(rows)
    return (
        "```text\n"
        f"# CISA Known Exploited Vulnerabilities — synced {stamp}\n\n"
        f"{header}\n{body}\n"
        "```"
    )


def main():
    if not README.exists():
        print("README.md not found; skipping.", file=sys.stderr)
        return 0
    try:
        data = fetch()
        vulns = data.get("vulnerabilities", [])
        vulns.sort(key=lambda v: v.get("dateAdded", ""), reverse=True)
        block = render(vulns[:N])
    except Exception as e:  # noqa: BLE001 — deliberately broad, must fail safe
        print(f"feed error ({e}); leaving README untouched.", file=sys.stderr)
        return 0

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print("markers missing; skipping.", file=sys.stderr)
        return 0

    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n{block}\n{END}",
        text,
        flags=re.S,
    )
    if new != text:
        README.write_text(new, encoding="utf-8")
        print("threat feed updated.")
    else:
        print("no change.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
