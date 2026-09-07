# Assessing Open Geospatial Data for Grid-Level Electricity Prediction in Karachi

This repository contains the computational workflow for an MSc dissertation on residential electricity prediction in Karachi. It tests how far open geospatial data can support reliable prediction at a 500 m grid resolution.

The analysis combines household electricity records with Sentinel-2 imagery, VIIRS nighttime lights, WorldPop population estimates, OpenStreetMap roads and points of interest, and Google Open Buildings. It compares grid resolutions and model families, audits the engineered predictors, evaluates remote-sensing and urban spatial feature groups, tests frozen ResNet50 representations, and examines performance under random and spatial cross-validation.

## Repository structure

```text
.
├── notebooks/                  # Ordered analysis notebooks
├── scripts/                    # Input and repository checks, plus a pipeline runner
├── data/
│   ├── README.md               # Data access and required file layout
│   └── metadata/               # Non-sensitive provenance and classification metadata
├── results/reference/          # Aggregate tables and selected figures from the reported run
├── docs/                       # Reproducibility notes and output provenance
├── environment.yml             # Conda environment used for the final analysis
├── project_config.py           # Portable data and output paths
└── .gitignore
```

## Analysis order

Run the notebooks from the repository root in this order:

1. `00_grid_resolution_selection.ipynb`
2. `01_feature_engineering_eda.ipynb`
3. `02_model_screening_and_tuning.ipynb`
4. `03_tabular_and_cnn_evaluation.ipynb`
5. `04_data_source_ablation.ipynb`
6. `05_prediction_and_spatial_analysis.ipynb`

Notebook 04 reuses the final all-engineered-feature results from notebook 03 and fits the two single-source models. This keeps the comparison on the same outer folds and avoids rerunning an identical model. Notebook 05 reads the validated out-of-fold predictions from notebook 03.

## Setup

Create the environment and activate it:

```bash
conda env create -f environment.yml
conda activate karachi-electricity
```

Obtain the data described in [data/README.md](data/README.md), then set the raw-data directory:

```bash
export KARACHI_RAW_DATA_DIR="/absolute/path/to/karachi-electricity-data"
```

Generated files are written to `work/` by default. To use another location:

```bash
export KARACHI_WORK_DIR="/absolute/path/to/output-directory"
```

Check the inputs before running the analysis:

```bash
python scripts/validate_inputs.py
python scripts/validate_repository.py
```

The notebooks can be run interactively or as an ordered batch:

```bash
python scripts/run_pipeline.py
```

The full workflow includes geospatial aggregation, CNN feature extraction, and nested cross-validation. Runtime depends on hardware and can be several hours.

## Reproducing the reported results

The final analysis used Python 3.10.13 and random seed 42. Random validation used five folds. Spatial validation used four KMeans blocks generated from grid centroids, with one block withheld at a time. Hyperparameters were selected inside each outer training fold.

The raw electricity data are controlled-access records and are not included. Other large source files are also omitted. The required sources, versions, filenames, and preparation steps are listed in [data/README.md](data/README.md). Aggregate outputs from the reported run are provided under `results/reference/` so that the reported tables can be checked without exposing row-level electricity records.

## Important implementation notes

- The repository copies use portable paths; the original notebooks are unchanged.
- Notebook outputs and execution counts are cleared to remove local paths and row-level data.
- The handoff between notebooks 00 and 01 has been standardised as `work/grid_size_selection/`.
- The final CNN experiment uses frozen ImageNet ResNet50 features. The older MLP fusion experiment is not part of the final dissertation workflow and is not included.
- The `results/reference/` files are evidence from the completed run. New executions write to `work/` and do not overwrite them.

