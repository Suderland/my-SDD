#!/usr/bin/env python3
"""Generate .agents/specs/INDEX.md from feature STATE.json files using stdlib only."""
from __future__ import annotations
import json
import sys
from pathlib import Path

TERMINAL = {"verified", "cancelled"}
VALID = {"not_started", "in_progress", "implemented", "verified", "blocked", "deferred", "cancelled"}

def load_states(root: Path):
    specs = root / ".agents" / "specs"
    features = specs / "features"
    rows = []
    errors = []
    if not features.exists():
        return rows, errors
    for state_path in sorted(features.glob("*/STATE.json")):
        try:
            data = json.loads(state_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{state_path}: invalid JSON: {exc}")
            continue
        fid = data.get("feature") or state_path.parent.name
        name = data.get("name", "")
        stage = data.get("stage", "unknown")
        reqs = data.get("requirements", {})
        total = len(reqs)
        verified = 0
        next_items = []
        for rid, info in reqs.items():
            status = info.get("status")
            if status not in VALID:
                errors.append(f"{state_path}: {rid} has invalid status {status!r}")
            if status == "verified":
                verified += 1
            elif status not in TERMINAL and len(next_items) < 3:
                next_items.append(rid)
            if status == "verified" and not info.get("evidence"):
                errors.append(f"{state_path}: {rid} is verified without evidence")
        progress = "0/0" if total == 0 else f"{verified}/{total} ({verified/total:.0%})"
        rows.append((fid, name, stage, progress, ", ".join(next_items) or "—"))
    return rows, errors

def render(rows):
    lines = [
        "# Project Specs", "", "Generated from feature `STATE.json` files. Do not hand-edit progress values.", "",
        "| Feature | Name | Stage | Verified | Next |",
        "|---|---|---|---:|---|",
    ]
    for fid, name, stage, progress, nxt in rows:
        lines.append(f"| {fid} | {name} | {stage} | {progress} | {nxt} |")
    if not rows:
        lines += ["", "No feature Specs exist yet."]
    return "\n".join(lines) + "\n"

def main(argv):
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    specs = root / ".agents" / "specs"
    specs.mkdir(parents=True, exist_ok=True)
    rows, errors = load_states(root)
    (specs / "INDEX.md").write_text(render(rows), encoding="utf-8")
    for err in errors:
        print(f"ERROR: {err}", file=sys.stderr)
    print(f"Generated {specs / 'INDEX.md'} from {len(rows)} feature(s).")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
