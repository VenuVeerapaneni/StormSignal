"""Refresh the small Chennai warning snapshot used by the static app.

The source is the public IMD Regional Meteorological Centre Chennai
district-warning page. This script deliberately fails closed: if its HTML
shape changes or the Chennai record is missing, it leaves the existing
snapshot untouched so the app can mark old data as stale.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen


SOURCE_URL = (
    "https://mausam.imd.gov.in/imd_latest/contents/"
    "districtwise-warning_mc.php?id=26&day=Day_1"
)
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = REPOSITORY_ROOT / "data" / "imd-warning.json"
TARGET_DISTRICT = "CHENNAI"


def extract_areas(document: str) -> list[dict[str, object]]:
    marker = re.search(r'"areas"\s*:\s*', document)
    if marker is None:
        raise ValueError("IMD page no longer contains the expected areas field")

    start = document.find("[", marker.end())
    if start < 0:
        raise ValueError("IMD areas field is not a JSON array")

    depth = 0
    in_string = False
    escaped = False
    end = -1
    for index in range(start, len(document)):
        char = document[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                end = index
                break

    if end < 0:
        raise ValueError("IMD areas array is incomplete")

    parsed = json.loads(document[start : end + 1])
    if not isinstance(parsed, list):
        raise ValueError("IMD areas value is not a list")
    return parsed


def clean_text(fragment: str) -> str:
    no_tags = re.sub(r"<[^>]*>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(no_tags)).strip()


def parse_area(area: dict[str, object]) -> dict[str, object]:
    title = str(area.get("title", "")).strip().upper()
    balloon = str(area.get("balloonText", ""))
    paragraphs = [
        clean_text(value)
        for value in re.findall(r"<p\b[^>]*>(.*?)</p>", balloon, flags=re.I | re.S)
    ]

    update_date = None
    warnings: list[str] = []
    no_warning = False
    for paragraph in paragraphs:
        date_match = re.fullmatch(r"Updated on\s*:\s*(\d{4}-\d{2}-\d{2})", paragraph, re.I)
        if date_match:
            update_date = date_match.group(1)
        elif re.fullmatch(r"No warning(?:s)?", paragraph, re.I):
            no_warning = True
        elif paragraph:
            warnings.append(paragraph)

    if update_date is None:
        date_match = re.search(r"Updated on\s*:\s*(\d{4}-\d{2}-\d{2})", clean_text(balloon), re.I)
        if date_match:
            update_date = date_match.group(1)

    if not update_date:
        raise ValueError(f"IMD record for {title} has no source update date")

    if no_warning:
        warnings = []
    elif not warnings:
        raise ValueError(f"IMD record for {title} has neither a warning nor a no-warning status")

    return {
        "district": title,
        "sourceUpdatedOn": update_date,
        "warnings": warnings,
        "noWarning": no_warning,
    }


def main() -> None:
    request = Request(
        SOURCE_URL,
        headers={
            "Accept": "text/html",
            "User-Agent": "StormSignal/1.0 (public IMD district-warning page reader)",
        },
    )
    with urlopen(request, timeout=25) as response:
        if response.status != 200:
            raise RuntimeError(f"IMD returned HTTP {response.status}")
        document = response.read().decode("utf-8", errors="replace")

    areas = extract_areas(document)
    source_area = next(
        (area for area in areas if str(area.get("title", "")).strip().upper() == TARGET_DISTRICT),
        None,
    )
    if source_area is None:
        raise ValueError("IMD page did not include the Chennai district record")

    snapshot = {
        "schemaVersion": 1,
        "sourceName": "India Meteorological Department, RMC Chennai",
        "sourceUrl": SOURCE_URL,
        "forecastDay": "Day 1",
        "districts": [parse_area(source_area)],
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUTPUT_PATH.write_text(serialized, encoding="utf-8")
    print(f"Updated {OUTPUT_PATH.relative_to(REPOSITORY_ROOT)} from {SOURCE_URL}")


if __name__ == "__main__":
    main()
