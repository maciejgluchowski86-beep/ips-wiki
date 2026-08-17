#!/usr/bin/env python3
"""Mechanical validator for staged ergodicity-method entries.

This checks format only. It does not verify mathematical correctness or whether
an attribution/pinpoint actually supports the claim.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
ENTRIES = ROOT / "entries"

REQUIRED_FIELDS = [
    "method_id",
    "title",
    "category",
    "model_scope",
    "source_status",
    "primary_source",
    "primary_pinpoint",
    "primary_url",
    "wiki_candidate",
]
REQUIRED_HEADINGS = [
    "## Criterion",
    "## Mechanism",
    "## Representative IPS use",
    "## Limitations",
    "## Sources",
]
ALLOWED_CATEGORIES = {
    "coupling",
    "graphical-duality",
    "functional-inequality",
    "spatial-mixing",
    "lyapunov-regeneration",
    "kcsm-model-specific",
    "finite-to-infinite",
    "other",
}
URL_RE = re.compile(r"https?://\S+")
WORD_RE = re.compile(r"\b[\w'-]+\b")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    raw = text[4:end]
    body = text[end + 5 :]
    fields = {}
    current_list = None
    for line in raw.splitlines():
        if line.startswith("  - ") and current_list:
            fields.setdefault(current_list, []).append(line[4:].strip())
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        current_list = key if value == "" else None
        fields[key] = [] if value == "" else value
    return fields, body


def validate(path: Path):
    errors = []
    text = path.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    if fields is None:
        return ["missing or malformed YAML-style front matter"]

    for key in REQUIRED_FIELDS:
        value = fields.get(key)
        if value is None or value == "" or value == []:
            errors.append(f"missing required field: {key}")

    targets = fields.get("targets")
    if not isinstance(targets, list) or not targets:
        errors.append("targets must be a nonempty list")

    category = fields.get("category")
    if category and category not in ALLOWED_CATEGORIES:
        errors.append(f"unknown category: {category}")

    if fields.get("source_status") != "primary-checked":
        errors.append("source_status must be primary-checked")
    if fields.get("wiki_candidate") != "yes":
        errors.append("wiki_candidate must be yes")

    if not URL_RE.search(str(fields.get("primary_url", ""))):
        errors.append("primary_url must contain an http(s) URL")
    pinpoint = str(fields.get("primary_pinpoint", "")).lower()
    if pinpoint in {"", "none", "n/a"}:
        errors.append("primary_pinpoint must be specific")

    for heading in REQUIRED_HEADINGS:
        if heading not in body:
            errors.append(f"missing heading: {heading}")

    words = WORD_RE.findall(body)
    if len(words) > 1200:
        errors.append(f"body too long: {len(words)} words > 1200")
    if len(words) < 250:
        errors.append(f"body suspiciously short: {len(words)} words < 250")

    if "## Criterion" in body:
        criterion = body.split("## Criterion", 1)[1].split("## Mechanism", 1)[0]
        if len(WORD_RE.findall(criterion)) < 35:
            errors.append("Criterion section is too short to be theorem-level")

    return errors


def main():
    files = sorted(ENTRIES.glob("*.md")) if ENTRIES.exists() else []
    if not files:
        print("No staged entries found.")
        return 0

    bad = 0
    seen = set()
    for path in files:
        errors = validate(path)
        fields, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fields:
            method_id = fields.get("method_id")
            if method_id in seen:
                errors.append(f"duplicate method_id: {method_id}")
            seen.add(method_id)
        if errors:
            bad += 1
            print(f"FAIL {path.name}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"PASS {path.name}")

    print(f"\nChecked {len(files)} entries; {bad} failed mechanical validation.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
