import allure
from pages.base_page import BasePage


class CartPage(BasePage):
    @property
    def items(self):
        return self.page.locator(".cart_item")

    @allure.step("Checkout with {first} {last} {zip_code}")
    def checkout(self, first: str, last: str, zip_code: str) -> None:
        self.page.get_by_test_id("checkout").click()
        self.page.get_by_test_id("firstName").fill(first)
        self.page.get_by_test_id("lastName").fill(last)
        self.page.get_by_test_id("postalCode").fill(zip_code)
        self.page.get_by_test_id("continue").click()
        self.page.get_by_test_id("finish").click()

    @property
    def confirmation(self):
        return self.page.get_by_test_id("complete-header")
