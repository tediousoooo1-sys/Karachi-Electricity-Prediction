#!/usr/bin/env python3
"""Execute the ordered notebook workflow without changing the source notebooks."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


NOTEBOOKS = [
    "00_grid_resolution_selection.ipynb",
    "01_feature_engineering_eda.ipynb",
    "02_model_screening_and_tuning.ipynb",
    "03_tabular_and_cnn_evaluation.ipynb",
    "04_data_source_ablation.ipynb",
    "05_prediction_and_spatial_analysis.ipynb",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0, choices=range(len(NOTEBOOKS)))
    parser.add_argument("--stop", type=int, default=len(NOTEBOOKS) - 1, choices=range(len(NOTEBOOKS)))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.start > args.stop:
        raise SystemExit("--start must be less than or equal to --stop")

    root = Path(__file__).resolve().parents[1]
    executed = root / "build" / "executed-notebooks"
    executed.mkdir(parents=True, exist_ok=True)

    subprocess.run(["python", str(root / "scripts" / "validate_inputs.py")], check=True)

    for name in NOTEBOOKS[args.start : args.stop + 1]:
        source = root / "notebooks" / name
        print(f"Running {name}", flush=True)
        subprocess.run(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--ExecutePreprocessor.timeout=-1",
                "--output-dir",
                str(executed),
                str(source),
            ],
            cwd=root,
            check=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

