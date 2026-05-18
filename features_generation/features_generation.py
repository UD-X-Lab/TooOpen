#!/usr/bin/env python3
"""Generate selected DNS query features from CSV logs.

The script appends three features to each row:
  - Dvs: unique requested domains in the recent N-request window for the same source IP
  - Str: unique source IPs in the recent M-request window for the same domain
  - Fth: occurrences of the current domain in the recent K-request window for the same source IP

Window state is preserved across files processed in filename order.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict, deque
from pathlib import Path
from typing import DefaultDict, Deque, Dict, Iterable


# Change this to "source IP" if your input CSV uses the non-anonymized header.
SOURCE_IP_COLUMN = "source IP (anonymized)"
DOMAIN_COLUMN = "domain/URL/name"

FEATURE_COLUMNS = ("Dvs", "Str", "Fth")
LEGACY_FEATURE_COLUMNS = {
    "Unique Request Count",
    "Domain Length",
    "Domain Levels",
    "Domain Entropy",
    "Unique Src IP",
    "Domain Query Count",
    "Dvs.",
    "Str.",
    "Fth.",
    *FEATURE_COLUMNS,
}


class SlidingWindowCounter:
    """Track item frequencies in a fixed-size sliding window."""

    def __init__(self, maxlen: int) -> None:
        self.maxlen = maxlen
        self.buffer: Deque[str] = deque()
        self.counts: DefaultDict[str, int] = defaultdict(int)

    def append(self, item: str) -> None:
        if len(self.buffer) >= self.maxlen:
            oldest = self.buffer.popleft()
            self.counts[oldest] -= 1
            if self.counts[oldest] == 0:
                del self.counts[oldest]

        self.buffer.append(item)
        self.counts[item] += 1

    def unique_count(self) -> int:
        return len(self.counts)

    def count_of(self, item: str) -> int:
        return self.counts.get(item, 0)


def require_columns(fieldnames: Iterable[str] | None, input_file: Path) -> list[str]:
    """Validate required columns and return the original field order."""

    if fieldnames is None:
        raise ValueError(f"{input_file} does not contain a header row.")

    original_columns = list(fieldnames)
    missing_columns = [
        column
        for column in (SOURCE_IP_COLUMN, DOMAIN_COLUMN)
        if column not in original_columns
    ]
    if missing_columns:
        missing = ", ".join(missing_columns)
        raise ValueError(f"{input_file} is missing required column(s): {missing}")

    return original_columns


def get_counter(
    counters: Dict[str, SlidingWindowCounter],
    key: str,
    window_size: int,
) -> SlidingWindowCounter:
    """Return the counter for a key, creating it on first use."""

    if key not in counters:
        counters[key] = SlidingWindowCounter(window_size)
    return counters[key]


def process_file(
    input_file: Path,
    output_file: Path,
    n: int,
    m: int,
    k: int,
    ip_domain_history: Dict[str, SlidingWindowCounter],
    domain_ip_history: Dict[str, SlidingWindowCounter],
    ip_query_history: Dict[str, SlidingWindowCounter],
) -> None:
    """Process one CSV file while reusing sliding-window state."""

    with input_file.open("r", encoding="utf-8", newline="") as fin, output_file.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as fout:
        reader = csv.DictReader(fin)
        original_columns = require_columns(reader.fieldnames, input_file)
        base_columns = [
            column for column in original_columns if column not in LEGACY_FEATURE_COLUMNS
        ]
        writer = csv.DictWriter(
            fout,
            fieldnames=base_columns + list(FEATURE_COLUMNS),
            extrasaction="ignore",
        )
        writer.writeheader()

        for row in reader:
            source_ip = row[SOURCE_IP_COLUMN].strip()
            domain = row[DOMAIN_COLUMN].strip()

            dvs_counter = get_counter(ip_domain_history, source_ip, n)
            dvs = dvs_counter.unique_count() + int(dvs_counter.count_of(domain) == 0)
            dvs_counter.append(domain)

            str_counter = get_counter(domain_ip_history, domain, m)
            strength = str_counter.unique_count() + int(
                str_counter.count_of(source_ip) == 0
            )
            str_counter.append(source_ip)

            fth_counter = get_counter(ip_query_history, source_ip, k)
            frequency = fth_counter.count_of(domain) + 1
            fth_counter.append(domain)

            output_row = {column: row.get(column, "") for column in base_columns}
            output_row.update(
                {
                    "Dvs": str(dvs),
                    "Str": str(strength),
                    "Fth": str(frequency),
                }
            )
            writer.writerow(output_row)


def process_all(
    input_folder: Path,
    output_folder: Path,
    n: int,
    m: int,
    k: int,
    overwrite: bool,
) -> None:
    """Process all CSV files in filename order."""

    output_folder.mkdir(parents=True, exist_ok=True)
    ip_domain_history: Dict[str, SlidingWindowCounter] = {}
    domain_ip_history: Dict[str, SlidingWindowCounter] = {}
    ip_query_history: Dict[str, SlidingWindowCounter] = {}

    for input_file in sorted(input_folder.glob("*.csv")):
        output_file = output_folder / input_file.name
        if output_file.exists() and not overwrite:
            print(f"Skipping existing file: {input_file.name}")
            continue

        process_file(
            input_file=input_file,
            output_file=output_file,
            n=n,
            m=m,
            k=k,
            ip_domain_history=ip_domain_history,
            domain_ip_history=domain_ip_history,
            ip_query_history=ip_query_history,
        )
        print(f"Processed: {input_file.name}")


def positive_int(value: str) -> int:
    """Parse a positive integer command-line argument."""

    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("value must be a positive integer")
    return parsed


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Generate Dvs, Str, and Fth features for DNS query CSV files."
    )
    parser.add_argument("input_folder", type=Path, help="Folder containing input CSV files.")
    parser.add_argument("output_folder", type=Path, help="Folder for generated CSV files.")
    parser.add_argument("--n", type=positive_int, default=5000, help="Window size for Dvs.")
    parser.add_argument("--m", type=positive_int, default=5000, help="Window size for Str.")
    parser.add_argument("--k", type=positive_int, default=5000, help="Window size for Fth.")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output files that already exist.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the feature generation workflow."""

    args = parse_args()
    process_all(
        input_folder=args.input_folder,
        output_folder=args.output_folder,
        n=args.n,
        m=args.m,
        k=args.k,
        overwrite=args.overwrite,
    )


if __name__ == "__main__":
    main()
