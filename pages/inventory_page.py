import allure
from pages.base_page import BasePage


class InventoryPage(BasePage):
    @property
    def items(self):
        return self.page.locator(".inventory_item")

    @property
    def cart_badge(self):
        return self.page.locator(".shopping_cart_badge")

    @allure.step("Add product to cart: {slug}")
    def add_to_cart(self, slug: str) -> "InventoryPage":
        self.page.get_by_test_id(f"add-to-cart-{slug}").click()
        return self

    @allure.step("Open cart")
    def open_cart(self):
        from pages.cart_page import CartPage
        self.page.locator(".shopping_cart_link").click()
        return CartPage(self.page, self.base_url)
