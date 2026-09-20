import allure
import pytest
from playwright.sync_api import expect

from conftest import USERS


@allure.feature("Authentication")
@pytest.mark.smoke
def test_valid_login_shows_inventory(login_page):
    inv = login_page.login(*USERS["standard"])
    expect(inv.items.first).to_be_visible()
    assert inv.items.count() == 6


@allure.feature("Authentication")
@pytest.mark.regression
def test_locked_user_is_rejected(login_page):
    login_page.login(*USERS["locked"])
    expect(login_page.error).to_contain_text("locked out")


@allure.feature("Authentication")
@pytest.mark.regression
@pytest.mark.parametrize(
    "user,pwd",
    [("", ""), ("standard_user", ""), ("", "secret_sauce"), ("standard_user", "wrong")],
    ids=["empty-both", "no-password", "no-username", "bad-password"],
)
def test_invalid_credentials_show_error(login_page, user, pwd):
    login_page.login(user, pwd)
    expect(login_page.error).to_be_visible()
