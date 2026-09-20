# QA Automation Framework (Playwright + Pytest + Docker + GitHub Actions)

Layered framework covering web UI, API and CI gating, built to be extended with a desktop driver.

## Architecture
| Layer | Tech | Why |
|---|---|---|
| Runner | pytest, xdist | parallel, markers, parametrization |
| Driver | Playwright (Python) | auto-waiting, tracing, multi-browser |
| Page objects | `pages/` | locators isolated from assertions |
| Fixtures | `conftest.py` | isolated setup, no shared state |
| API tests | requests | contract, status, latency budget |
| Reporting | Allure + Playwright trace/video | evidence on failure |
| CI | GitHub Actions | PR smoke, nightly cross-browser matrix |
| Runtime | Docker | identical local/CI environment |

## Run
```bash
pip install -r requirements.txt && playwright install chromium
pytest -m smoke -n auto                # fast gate
pytest                                 # full regression
pytest --browser firefox               # cross-browser
allure serve allure-results            # report
docker build -t qa-demo . && docker run --rm qa-demo
```

## Strategy
- **smoke** runs on every PR (merge gate); **regression** runs on main + nightly across 3 browsers.
- Failures ship trace, screenshot and video as artifacts.
- Flaky tests: root-cause first; `@pytest.mark.flaky` quarantine with a ticket, tracked as a metric.
- Desktop extension: add a `drivers/desktop.py` adapter (TestComplete/TestExecute or pywinauto) behind the same page-object contract; run on a Windows runner.
