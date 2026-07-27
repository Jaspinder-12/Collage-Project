## 2026-02-26 - CI Workflow Failure
**Learning:** The default GitHub Actions workflow for Python often assumes a Conda environment if not configured otherwise, or looks for `environment.yml`. If a project uses `requirements.txt`, the workflow must be explicitly updated to use `pip`.
**Action:** Always check `.github/workflows` and ensure the dependency installation step matches the project's dependency management file (`requirements.txt` vs `environment.yml`).
