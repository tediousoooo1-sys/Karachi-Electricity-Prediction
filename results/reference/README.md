# Reference outputs

These files are aggregate outputs from the final dissertation run. They allow the reported tables and figures to be checked without distributing raw electricity records, grid-level targets, OOF predictions, imagery, or model embeddings.

| Folder | Contents | Produced by |
|---|---|---|
| `grid_resolution/` | Four-resolution data support and model comparisons | Notebook 00 |
| `eda/` | Data audit, target summary, feature inventory, and correlations | Notebook 01 |
| `model_tuning/` | Random Forest and XGBoost nested-CV summaries and fold results | Notebook 02 |
| `multimodal/` | Final tabular/CNN comparison, target sensitivity, PCA selection, and pretraining sensitivity | Notebook 03 |
| `data_source_ablation/` | Remote-sensing, urban spatial, and combined feature comparisons | Notebook 04 |
| `spatial_analysis/` | Final model, spatial-fold, error-decile, SHAP, and Gi* summaries | Notebook 05 |
| `figures/` | Selected non-identifying figures used to inspect the reported analysis | Notebooks 01–05 |

Files with one record per grid are deliberately excluded. A new run writes its complete outputs to `work/`.

