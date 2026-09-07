# Reproducibility notes

## Scope

The six notebooks reproduce the analyses reported in the dissertation. They do not include unrelated preliminary models. Each notebook has one role and writes named outputs for the next stage.

| Stage | Notebook | Main output |
|---|---|---|
| Grid resolution | `00_grid_resolution_selection.ipynb` | Four grid datasets and grid-size comparison tables |
| Feature audit and EDA | `01_feature_engineering_eda.ipynb` | Final 36-predictor matrix and CNN backbone features |
| Model tuning | `02_model_screening_and_tuning.ipynb` | Nested-CV results and fixed spatial-block assignments |
| CNN evaluation | `03_tabular_and_cnn_evaluation.ipynb` | Tabular and tabular-plus-CNN OOF predictions |
| Source ablation | `04_data_source_ablation.ipynb` | Remote-only, urban-only, and combined comparison |
| Spatial analysis | `05_prediction_and_spatial_analysis.ipynb` | Error, SHAP, map, and Gi* outputs |

## Validation design

Random five-fold cross-validation measures prediction for held-out grids distributed across the study area. Spatial cross-validation withholds complete KMeans blocks and tests prediction in areas absent from training. Hyperparameter search, imputation, and CNN PCA are fitted within the training data for each outer fold.

## Data protection

No raw or row-level electricity records are included. Notebook outputs were cleared because rendered outputs can retain local paths and observations even when input files are excluded. `results/reference/` contains only aggregate tables and selected figures used to verify the reported results.

## Output provenance

`results/reference/manifest.csv` records the original relative path and SHA-256 checksum of every copied reference output. `docs/notebook_manifest.csv` records the checksum of each source notebook and its cleaned repository copy.

## Known interface correction

The completed grid-resolution notebook originally wrote to a folder named `grid_size_screening_42`, while the next notebook read from `grid_size_selection`. Both folders existed in the working project, so this mismatch was hidden during interactive work. The repository copy standardises the handoff as `work/grid_size_selection`. This is a path correction only; it does not alter the analysis or reported values.

