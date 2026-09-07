# Submission checklist

Use this checklist before submitting the additional materials.

- Make the GitHub repository public and open the link in a private browser window.
- Add the final repository URL to the technical appendix or the submission field specified by the course.
- Keep the six notebooks in the numbered order shown in the main README.
- Confirm that the dissertation's model names, validation design, feature counts, and reported values match `results/reference/`.
- Do not upload the electricity GeoPackage, feature matrices, grid-level OOF predictions, CNN embeddings, rasters, or derived spatial layers containing electricity values.
- Keep `data/README.md`, `environment.yml`, `project_config.py`, and the validation scripts in the repository.
- Run `python scripts/validate_repository.py` after any final edit.
- If a source or result changes, regenerate `results/reference/manifest.csv` with `python scripts/build_reference_manifest.py`.
- Record the final commit hash in the submitted technical appendix so the assessed version can be identified.

Suggested appendix sentence:

> The code, environment specification, data-access instructions, and aggregate reference outputs are available in the accompanying public GitHub repository at [repository URL] (commit [full commit hash]). Controlled-access electricity records and large geospatial source files are not redistributed; access and preparation instructions are provided in the repository.
