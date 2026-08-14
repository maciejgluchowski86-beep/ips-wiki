#!/usr/bin/env python3
"""Mechanical metadata gate for the live wiki.

This script does not judge mathematics or prose. It enforces the curation protocol:
- every new or changed docs/entries/*.md page must carry audit: current;
- changed live entries may not use status: obsolete;
- once legacy migration is complete, every live entry must satisfy those rules.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = ROOT / "docs" / "entries"
STATE = ROOT / "wiki-curation-state.json"
ALLOWED_STATUS = {
    "definition",
    "standard fact",
    "proved here",
    "observation",
    "literature",
    "conditional",
    "conjecture",
    "heuristic",
    "open",
    "obsolete",
}


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("'\"")
    return data


def changed_entries(base: str | None) -> set[Path]:
    if not base:
        return set()
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", f"{base}..HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return set()
    result: set[Path] = set()
    for name in out.splitlines():
        if name.startswith("docs/entries/") and name.endswith(".md"):
            path = ROOT / name
            if path.exists():
                result.add(path)
    return result


def check_page(path: Path) -> list[str]:
    meta = front_matter(path)
    errors: list[str] = []
    status = meta.get("status")
    audit = meta.get("audit")
    rel = path.relative_to(ROOT)
    if status not in ALLOWED_STATUS:
        errors.append(f"{rel}: missing or invalid status: {status!r}")
    if audit != "current":
        errors.append(f"{rel}: live entry is not marked 'audit: current'")
    if status == "obsolete":
        errors.append(f"{rel}: obsolete pages must be deleted from the live wiki")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed-from", default=None)
    args = parser.parse_args()

    state = json.loads(STATE.read_text(encoding="utf-8"))
    migration_complete = bool(state.get("legacy_migration_complete"))
    all_entries = sorted(ENTRIES.glob("*.md"))
    changed = changed_entries(args.changed_from)

    targets = all_entries if migration_complete else sorted(changed)
    errors: list[str] = []
    for path in targets:
        errors.extend(check_page(path))

    if errors:
        print("Wiki quality metadata check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    legacy_missing = 0
    legacy_proved_here = 0
    legacy_obsolete = 0
    if not migration_complete:
        for path in all_entries:
            meta = front_matter(path)
            if meta.get("audit") != "current":
                legacy_missing += 1
            if meta.get("status") == "proved here" and meta.get("audit") != "current":
                legacy_proved_here += 1
            if meta.get("status") == "obsolete":
                legacy_obsolete += 1
        print(
            "Legacy migration is incomplete: "
            f"{legacy_missing} entries lack audit: current; "
            f"{legacy_proved_here} legacy proved-here entries; "
            f"{legacy_obsolete} obsolete entries."
        )
        print("Changed/new live entries passed the current admission gate.")
    else:
        print(f"All {len(all_entries)} live entries passed the metadata gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
