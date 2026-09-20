import allure
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self) -> "LoginPage":
        self.goto("/")
        return self

    @allure.step("Login as {username}")
    def login(self, username: str, password: str):
        from pages.inventory_page import InventoryPage
        self.page.get_by_test_id("username").fill(username)
        self.page.get_by_test_id("password").fill(password)
        self.page.get_by_test_id("login-button").click()
        return InventoryPage(self.page, self.base_url)

    @property
    def error(self):
        return self.page.get_by_test_id("error")
