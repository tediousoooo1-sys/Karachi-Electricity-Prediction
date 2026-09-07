#!/usr/bin/env python3
"""Check the raw inputs required by the ordered notebook workflow."""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from project_config import RAW_DATA_DIR  # noqa: E402


REQUIRED = [
    "boundary/karachi_boundary_mask.json",
    "electricity consumption/Electricity_consumption_data.gpkg",
    "road/Karachi_Spatial_Data.gpkg",
    "road/Karachi_Spatial_Data_csv/pois_new.csv",
    "daylight21/processing/B02_k.tif",
    "daylight21/processing/B03_k.tif",
    "daylight21/processing/B04_k.tif",
    "daylight21/processing/B08_k.tif",
    "daylight21/processing/B11_k.tif",
    "daylight21/processing/TCI_k.tif",
    "nightlight/VNL_v21_npp_2021_global_vcmslcfg_c202205302300.median_masked_k.tif.tif",
    "population/pak_ppp_2020.tif",
    "building density/3eb_buildings.csv.gz",
    "building density/395_buildings.csv.gz",
]


def main() -> int:
    missing = [relative for relative in REQUIRED if not (RAW_DATA_DIR / relative).exists()]
    print(f"Raw data directory: {RAW_DATA_DIR}")
    if missing:
        print("Missing required inputs:")
        for relative in missing:
            print(f"  - {relative}")
        return 1
    print(f"All {len(REQUIRED)} required inputs were found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

