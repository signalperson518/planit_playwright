import re
from playwright.sync_api import Page, expect


def test_shopping_total(page: Page):
    page.goto("https://jupiter.cloud.planittesting.com")
    page.get_by_role("link", name="Shop", exact=True).click()

    # buy Stuffed Frog x2
    page.locator("#product-2").get_by_role("link", name="Buy").click()
    page.locator("#product-2").get_by_role("link", name="Buy").click()

    # buy Fluffy Bunny x5
    page.locator("#product-4").get_by_role("link", name="Buy").click()
    page.locator("#product-4").get_by_role("link", name="Buy").click()
    page.locator("#product-4").get_by_role("link", name="Buy").click()
    page.locator("#product-4").get_by_role("link", name="Buy").click()
    page.locator("#product-4").get_by_role("link", name="Buy").click()

    # buy Valentine Bear x3
    page.locator("#product-7").get_by_role("link", name="Buy").click()
    page.locator("#product-7").get_by_role("link", name="Buy").click()
    page.locator("#product-7").get_by_role("link", name="Buy").click()

    page.get_by_role("link", name="Cart (10)").click()

    # verify order line stuffed frog
    expect(page.get_by_role("row", name="Stuffed Frog").locator("td:nth-child(2)")).to_contain_text("$10.99")
    expect(page.get_by_role("row", name="Stuffed Frog").get_by_role("spinbutton")).to_have_value("2")
    # verity the subtotal of 2 items
    expect(page.get_by_role("row", name="Stuffed Frog").locator("td:nth-child(4)")).to_contain_text("$21.98")

    # verify order line fluffy bunny
    expect(page.get_by_role("row", name="Fluffy Bunny").locator("td:nth-child(2)")).to_contain_text("$9.99")
    expect(page.get_by_role("row", name="Fluffy Bunny").get_by_role("spinbutton")).to_have_value("5")
    # verith the subtotal of 5 items
    expect(page.get_by_role("row", name="Fluffy Bunny").locator("td:nth-child(4)")).to_contain_text("$49.95")

    # verify order line valentine bear
    expect(page.get_by_role("row", name="Valentine Bear").locator("td:nth-child(2)")).to_contain_text("$14.99")
    expect(page.get_by_role("row", name="Valentine Bear").get_by_role("spinbutton")).to_have_value("3")
    # verify the subtotal of 3 items
    expect(page.get_by_role("row", name="Valentine Bear").locator("td:nth-child(4)")).to_contain_text("$44.97")

    # verify order total
    expect(page.get_by_text("Total: 116.9")).to_be_visible()
