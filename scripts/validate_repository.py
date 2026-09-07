#!/usr/bin/env python3
"""Run fast checks on the cleaned notebooks and repository contents."""

from __future__ import annotations

import ast
import json
from pathlib import Path


LOCAL_HOME_MARKER = "/" + "Users" + "/"

FORBIDDEN = [
    LOCAL_HOME_MARKER,
    "grid_size_screening_42",
    "ResNet34 handoff",
    "ResNet34 downstream file",
]

FORBIDDEN_REFERENCE_NAMES = [
    "oof_predictions",
    "feature_matrix",
    "spatial_block_assignments",
    "cnn_features",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures: list[str] = []
    notebooks = sorted((root / "notebooks").glob("*.ipynb"))

    if len(notebooks) != 6:
        failures.append(f"Expected six notebooks; found {len(notebooks)}")

    for path in notebooks:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        text = json.dumps(notebook, ensure_ascii=False)
        for token in FORBIDDEN:
            if token in text:
                failures.append(f"{path.name}: contains forbidden token {token!r}")

        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            if cell.get("outputs"):
                failures.append(f"{path.name}: cell {index} still has outputs")
            if cell.get("execution_count") is not None:
                failures.append(f"{path.name}: cell {index} still has an execution count")
            source = "".join(cell.get("source", []))
            try:
                ast.parse(source)
            except SyntaxError as exc:
                failures.append(f"{path.name}: cell {index} syntax error: {exc}")

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.stat().st_size > 100 * 1024 * 1024:
            failures.append(f"{path.relative_to(root)} exceeds GitHub's 100 MB limit")
        if path.is_relative_to(root / "results" / "reference"):
            lowered = path.name.lower()
            for token in FORBIDDEN_REFERENCE_NAMES:
                if token in lowered:
                    failures.append(
                        f"{path.relative_to(root)} appears to contain row-level or intermediate data"
                    )
        if path.suffix.lower() in {".md", ".py", ".json", ".yml", ".yaml", ".csv"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if LOCAL_HOME_MARKER in text:
                failures.append(f"{path.relative_to(root)} contains a local absolute path")

    if failures:
        print("Repository checks failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(f"Repository checks passed for {len(notebooks)} notebooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
