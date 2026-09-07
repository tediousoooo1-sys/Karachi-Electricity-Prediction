#!/usr/bin/env python3
"""Write checksums for the reviewed aggregate reference outputs."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    reference = root / "results" / "reference"
    manifest = reference / "manifest.csv"
    files = sorted(
        path for path in reference.rglob("*")
        if path.is_file() and path not in {manifest, reference / "README.md"}
    )

    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["repository_path", "stage", "bytes", "sha256"])
        for path in files:
            relative = path.relative_to(root)
            writer.writerow([
                relative.as_posix(),
                path.parent.name,
                path.stat().st_size,
                hashlib.sha256(path.read_bytes()).hexdigest(),
            ])

    print(f"Wrote {manifest.relative_to(root)} for {len(files)} files.")


if __name__ == "__main__":
    main()
