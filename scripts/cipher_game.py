#!/usr/bin/env python3
"""
Judge a `solve: <answer>` issue against the gate.

The plaintext answer is never stored in the repo — only its SHA-256. Change
the puzzle by hashing a new word (see SETUP.md) and swapping ANSWER_HASH plus
the runes shown in the README.

Correct  -> congratulatory comment, issue closed, solver added to Hall of Fame.
Wrong    -> hint comment, issue closed.
"""

import hashlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

# sha256("obsidian") — swap this to change the answer
ANSWER_HASH = "4e2295dd929e424aa1afde7049924cb231f451c9884d7915ae33690b73b227ec"

README = Path("README.md")
START, END = "<!-- HOF-START -->", "<!-- HOF-END -->"
PLACEHOLDER = "no one has passed yet."

API = "https://api.github.com"
TOKEN = os.environ.get("GH_TOKEN", "")
REPO = os.environ.get("REPO", "")
ISSUE = os.environ.get("ISSUE_NUMBER", "")
TITLE = os.environ.get("ISSUE_TITLE", "")
USER = os.environ.get("ISSUE_USER", "")


def api(method, path, payload=None):
    url = f"{API}/repos/{REPO}{path}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "vuav-cipher-gate")
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r) if r.status < 300 and r.length != 0 else {}


def comment(text):
    try:
        api("POST", f"/issues/{ISSUE}/comments", {"body": text})
    except Exception as e:  # noqa: BLE001
        print(f"comment failed: {e}", file=sys.stderr)


def close():
    try:
        api("PATCH", f"/issues/{ISSUE}", {"state": "closed"})
    except Exception as e:  # noqa: BLE001
        print(f"close failed: {e}", file=sys.stderr)


def extract_answer(title):
    # strip the "solve:" prefix, keep only letters, lowercase
    body = re.sub(r"^\s*solve:\s*", "", title, flags=re.I)
    return re.sub(r"[^a-z]", "", body.lower())


def add_to_hof(user):
    if not README.exists():
        return False
    text = README.read_text(encoding="utf-8")
    m = re.search(re.escape(START) + r"(.*?)" + re.escape(END), text, flags=re.S)
    if not m:
        return False
    block = m.group(1)
    if f"@{user}" in block:  # already etched — don't duplicate
        return False

    from datetime import datetime, timezone
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    line = f"- @{user}  ·  {date}"

    inner = block.strip()
    if PLACEHOLDER in inner or inner == "":
        new_block = f"\n{line}\n"
    else:
        new_block = f"{block.rstrip()}\n{line}\n"

    new = text.replace(m.group(0), f"{START}{new_block}{END}")
    README.write_text(new, encoding="utf-8")
    return True


def main():
    if not TITLE.lower().startswith("solve:"):
        print("not a gate submission; ignoring.")
        return 0

    guess = extract_answer(TITLE)
    if not guess:
        comment("The gate saw no answer. Format: `solve: <your decoded word>`.")
        close()
        return 0

    correct = hashlib.sha256(guess.encode()).hexdigest() == ANSWER_HASH
    if correct:
        etched = add_to_hof(USER)
        note = "You're etched into the Hall of Fame." if etched else "You'd already passed — the gate remembers you."
        comment(f"🗝️ **The gate opens.** Well decoded, @{USER}. {note}")
    else:
        comment(
            f"The runes reject `{guess}`, @{USER}. "
            "Re-check the legend, then open a fresh `solve:` issue — the gate never tires."
        )
    close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
