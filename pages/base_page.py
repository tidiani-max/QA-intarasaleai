from playwright.sync_api import Page


class BasePage:
    """Page Object base: locators live in pages, assertions live in tests."""

    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = "/") -> None:
        self.page.goto(f"{self.base_url}{path}")
