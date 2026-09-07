"""Portable paths shared by the dissertation notebooks."""

from __future__ import annotations

import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
RAW_DATA_DIR = Path(
    os.environ.get("KARACHI_RAW_DATA_DIR", REPO_ROOT / "data" / "raw")
).expanduser().resolve()
WORK_DIR = Path(
    os.environ.get("KARACHI_WORK_DIR", REPO_ROOT / "work")
).expanduser().resolve()

