import allure
import pytest
from playwright.sync_api import expect

BACKPACK = "sauce-labs-backpack"


@allure.feature("Checkout")
@pytest.mark.smoke
def test_end_to_end_purchase(logged_in_inventory):
    inv = logged_in_inventory
    inv.add_to_cart(BACKPACK)
    expect(inv.cart_badge).to_have_text("1")

    cart = inv.open_cart()
    expect(cart.items).to_have_count(1)

    cart.checkout("Cheick", "Diawara", "65145")
    expect(cart.confirmation).to_have_text("Thank you for your order!")


@allure.feature("Cart")
@pytest.mark.regression
def test_cart_badge_tracks_multiple_items(logged_in_inventory):
    inv = logged_in_inventory
    inv.add_to_cart(BACKPACK).add_to_cart("sauce-labs-bike-light")
    expect(inv.cart_badge).to_have_text("2")
