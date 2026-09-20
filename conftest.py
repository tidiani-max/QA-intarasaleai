import os
import pytest
from playwright.sync_api import Playwright

from pages.login_page import LoginPage

USERS = {
    "standard": ("standard_user", "secret_sauce"),
    "locked": ("locked_out_user", "secret_sauce"),
}


@pytest.fixture(scope="session", autouse=True)
def _test_id_attribute(playwright: Playwright):
    # SauceDemo uses data-test instead of data-testid
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def api_base_url() -> str:
    return os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture
def login_page(page, base_url) -> LoginPage:
    lp = LoginPage(page, base_url)
    lp.open()
    return lp


@pytest.fixture
def logged_in_inventory(login_page):
    """Fixture-based setup: every test starts isolated, no shared state."""
    user, pwd = USERS["standard"]
    return login_page.login(user, pwd)


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("base_url") or os.getenv("BASE_URL", "https://www.saucedemo.com")
