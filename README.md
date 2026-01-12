# API Automation — Robot Framework version

Quickstart ✅

Prerequisites

- Python 3.11 or newer
- Git
- (Optional) Docker / `act` if you want to run GitHub Actions locally

Clone the repository

```bash
git clone <repo-url>
cd API_Automation_RobotFramework/robot_framework_project
```

Create a virtual environment (Windows example)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Running tests locally

- Run the full suite (default):

```bash
robot --outputdir reports tests
# or (explicit python runner)
python -m robot.run --pythonpath . --outputdir reports tests
```

- Run a single suite or file:

```bash
robot --outputdir reports tests/posts/posts.robot
```

- Run a single test case by name:

```bash
robot -t "Validate Posts Schema" tests/posts/posts.robot
```

- Increase verbosity / debug logging:

```bash
robot -L DEBUG --outputdir reports tests
```

Where to find local reports

- After a run, reports are placed in the `reports/` directory:
  - `reports/output.xml` (Robot XML)
  - `reports/log.html` (detailed log)
  - `reports/report.html` (summary report)

GitHub Actions (CI)

- Workflow file: `.github/workflows/robot-ci.yml`
- Trigger: `push` and `pull_request` on `main` (you can add `workflow_dispatch` to trigger manually from the Actions UI)
- The workflow installs dependencies and runs `robot --outputdir reports tests`, then uploads the `reports` directory as an artifact named `robot-reports`.

To view CI runs and download reports:

1. Open the repository on GitHub → **Actions** tab.
2. Select the workflow run you want, then open the job and click **Artifacts** → download **robot-reports**.
3. Extract and open `report.html` / `log.html` in a browser to investigate failures.

Run workflow locally (optional)

- Install `act` (https://github.com/nektos/act) and run the workflow locally to reproduce CI: e.g.

```bash
act -j test
# or target the workflow file directly
act -W .github/workflows/robot-ci.yml -j test
```

Linting & formatting

- Robot lint: `robocop` (installed from source) or `robotframework-lint` (rflint)
- Python lint/format: `ruff` / `flake8`, `black`

Troubleshooting

- If Robot cannot import libraries, ensure you run commands from the project root and include `--pythonpath .` when needed (recommended):

  ```bash
  python -m robot.run --pythonpath . --outputdir reports tests
  # or, if you have `robot` installed in the active venv
  robot --pythonpath . --outputdir reports tests
  ```

  Note: the suite also supports relative path imports for libraries (e.g., `Library    ../libraries/api_library.py`) so `robot` can be run without adding the project to PYTHONPATH, but using an isolated venv is recommended to ensure dependencies (requests, jsonschema, etc.) are available.
- If dependencies fail to install, activate the venv and run `pip install -r requirements.txt` again.

What this scaffold provides

- `libraries/posts_library.py` — Python Robot library wrapping `/posts` endpoints
- `tests/` — Robot test suites ported from the original pytest repo
- `config/config.yaml` — base URL and timeouts
- `schema/` — JSON schemas used for contract tests
- `.github/workflows/robot-ci.yml` — CI to run Robot tests and upload reports

Next steps

- Add linters and pre-commit hooks
- Add more keywords and port additional tests
- Add richer reporting (Allure) and cross-platform matrix in CI
