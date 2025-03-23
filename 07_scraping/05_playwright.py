import re # Regular expression module for pattern matching.
from playwright.sync_api import Page, expect # Import Page and expect from playwright.

def test_has_title(page: Page): # Define a test function that receives a Page object.
    page.goto("https://playwright.dev/") # Navigate to the Playwright website.

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright")) # Use a regular expression to match the title.

def test_get_started_link(page: Page): #
    page.goto("https://playwright.dev/") # Navigate to the Playwright website.

    # Click the get started link.
    page.get_by_role("link", name="Get started").click() #

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible() # Check if the heading is visible.