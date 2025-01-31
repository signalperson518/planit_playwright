import re
from playwright.sync_api import Page, expect
import pytest


def test_contact_validation(page: Page):
    page.goto("https://jupiter.cloud.planittesting.com")
    page.get_by_role("link", name="Contact").click()
    page.get_by_role("link", name="Submit").click()

    # Verify validation messages are visible for mandatory fields
    expect(page.get_by_text("Forename is required")).to_be_visible()
    expect(page.get_by_text("Email is required")).to_be_visible()
    expect(page.get_by_text("Message is required")).to_be_visible()

    # Fill in Forename, Email and Message
    page.locator("#forename").fill("John")
    page.locator("#email").fill("test@planit.net.au")
    page.locator("#message").fill("Something is wrong")

    # Verify validation messages are hidden
    expect(page.get_by_text("Forename is required")).to_be_hidden()
    expect(page.get_by_text("Email is required")).to_be_hidden()
    expect(page.get_by_text("Message is required")).to_be_hidden()

# run 5 times successful submission
@pytest.mark.parametrize("run", range(5))
def test_contact_message_sent(page: Page, run):
    page.goto("https://jupiter.cloud.planittesting.com")
    page.get_by_role("link", name="Contact").click()

    # Fill in Forename, Email and Message
    page.locator("#forename").fill("John" + str(run))
    page.locator("#email").fill("test@planit.net.au")
    page.locator("#message").fill("Something is wrong")

    page.get_by_role("link", name="Submit").click()

    # Verify validation messages are hidden
    expect(page.get_by_text(f"Thanks John{run}, we appreciate")).to_be_visible(timeout=30000)
