1. Create the `.jules/bolt.md` journal file.
   - Run `run_in_bash_session` to create `.jules/bolt.md` and log the critical learning about globally caching ML models to prevent expensive disk I/O and deserialization per request in Flask applications.
2. Verify `.jules/bolt.md` creation.
   - Run `run_in_bash_session` with `cat .jules/bolt.md` to verify its contents.
3. Create the `.gitignore` file.
   - Run `run_in_bash_session` to create `.gitignore` and add `__pycache__/` to prevent committing compiled bytecode.
4. Verify `.gitignore` creation.
   - Run `run_in_bash_session` with `cat .gitignore` to verify its contents.
5. Create the `environment.yml` file.
   - Run `run_in_bash_session` to create `environment.yml` containing the dependencies explicitly imported in `app.py`: `flask`, `joblib`, and `numpy`.
6. Verify `environment.yml` creation.
   - Run `run_in_bash_session` with `cat environment.yml` to verify its contents.
7. Modify `app.py` to globally cache machine learning models.
   - Run `replace_with_git_merge_diff` on `app.py` to replace hardcoded absolute paths with relative paths (e.g., using `os.path.join(os.path.dirname(os.path.abspath(__file__)), ...)`), move `joblib.load` to module level global scope outside the request handler, add the required `# ⚡ Bolt:` comment, and change `app.run(debug=True)` to `debug=False`.
8. Verify `app.py` modifications.
   - Run `run_in_bash_session` with `git diff app.py` to ensure all changes across the file are completely verified without truncation.
9. Execute `flake8` to verify no linting regressions were introduced.
   - Run `run_in_bash_session` with `python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics` and `python -m flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics` to verify linting.
10. Execute `pytest` to verify testing.
    - Run `run_in_bash_session` with `python -m pytest || [ $? -eq 5 ]` to test the codebase and ensure it accepts exit code 5 as success since there are no test files.
11. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
12. Submit the PR.
    - Run `submit` to submit the PR with branch name `bolt-optimization`, PR title `⚡ Bolt: Cache ML models globally`, and a description containing the `💡 What`, `🎯 Why`, `📊 Impact`, and `🔬 Measurement` sections.
