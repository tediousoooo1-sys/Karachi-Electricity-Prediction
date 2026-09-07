# Data access and file layout

The source data are not stored in this repository. The electricity records require controlled access, while the geospatial files are too large for a normal Git repository. Download or request the sources below, prepare them as described, and place them under one raw-data directory.

Set that directory with:

```bash
export KARACHI_RAW_DATA_DIR="/absolute/path/to/karachi-electricity-data"
```

## Sources

| Data | Source and access | Version used | Required local file |
|---|---|---|---|
| Residential electricity | [UK Data Service ReShare record 856294](https://reshare.ukdataservice.ac.uk/856294/), DOI `10.5255/UKDA-SN-856294` | Dataset supplied for the dissertation | `electricity consumption/Electricity_consumption_data.gpkg` |
| Sentinel-2 Level-2A | [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) | Karachi scenes from 28 and 30 October 2021 | Processed bands listed below |
| VIIRS nighttime lights | [EOG VIIRS Nighttime Light annual composites](https://eogdata.mines.edu/products/vnl/) | VNL v2.1, 2021 median masked composite | `nightlight/VNL_v21_npp_2021_global_vcmslcfg_c202205302300.median_masked_k.tif.tif` |
| Population | [WorldPop global archive](https://hub.worldpop.org/Global1_2000-2020) | Pakistan 2020 population raster | `population/pak_ppp_2020.tif` |
| Roads and POIs | [OpenStreetMap](https://www.openstreetmap.org/copyright), extracted through the [ohsome API](https://docs.ohsome.org/ohsome-api/v2-rc/) | Snapshot at 31 March 2020 23:59:59 UTC | Files listed below |
| Buildings | [Google Open Buildings](https://sites.research.google/gr/open-buildings/) | Tiles `3eb` and `395` | Files listed below |
| Administrative boundary | [GADM](https://gadm.org/data.html) | GADM 4.1, Karachi boundary | `boundary/karachi_boundary_mask.json` |

The UK Data Service page explains the registration and permission conditions for the electricity dataset. A repository user must obtain access from the data provider; the file cannot be redistributed here.

## Expected directory tree

```text
karachi-electricity-data/
├── boundary/
│   └── karachi_boundary_mask.json
├── building density/
│   ├── 3eb_buildings.csv.gz
│   ├── 395_buildings.csv.gz
│   └── karachi_buildings.gpkg          # Optional cache; created if absent
├── daylight21/
│   └── processing/
│       ├── B02_k.tif
│       ├── B03_k.tif
│       ├── B04_k.tif
│       ├── B08_k.tif
│       ├── B11_k.tif
│       └── TCI_k.tif
├── electricity consumption/
│   └── Electricity_consumption_data.gpkg
├── nightlight/
│   └── VNL_v21_npp_2021_global_vcmslcfg_c202205302300.median_masked_k.tif.tif
├── population/
│   └── pak_ppp_2020.tif
└── road/
    ├── Karachi_Spatial_Data.gpkg
    └── Karachi_Spatial_Data_csv/
        └── pois_new.csv
```

## Preparation notes

The Sentinel-2 inputs are surface-reflectance bands clipped or mosaicked to Karachi and aligned to the project area. The three dated products used in the completed analysis were:

- `S2A_MSIL2A_20211028T060951_N0500_R134_T42RUP_20230102T051113.SAFE`
- `S2A_MSIL2A_20211028T060951_N0500_R134_T42RTN_20230102T051113.SAFE`
- `S2B_MSIL2A_20211030T055959_N0500_R091_T42RUN_20230115T103358.SAFE`

The OpenStreetMap snapshot was projected to EPSG:32642. The completed extract contained 61,659 road features and 20,358 POIs before and after category reclassification. The POI mapping used in that step is stored in `data/metadata/poi_reclassification_mapping.csv`.

Run `python scripts/validate_inputs.py` after assembling the directory. It reports every missing input before the notebooks start.

