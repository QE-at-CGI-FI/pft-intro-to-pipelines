"""
Example Playwright tests to demonstrate the pipeline functionality.
"""
import re
from playwright.sync_api import Page, expect


def test_example_domain(page: Page):
    """Test basic page navigation functionality."""
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
    
    # Check that the page contains expected content
    expect(page.locator("h1")).to_contain_text("Example Domain")
    expect(page.locator("p")).to_contain_text("This domain is for use in illustrative examples")


def test_httpbin_get(page: Page):
    """Test HTTP endpoint with httpbin service."""
    page.goto("https://httpbin.org/get")
    
    # Check that we get a valid JSON response page
    expect(page.locator("pre")).to_contain_text('"url": "https://httpbin.org/get"')


def test_page_title_validation(page: Page):
    """Test page title validation."""
    page.goto("https://httpbin.org")
    expect(page).to_have_title(re.compile("httpbin", re.IGNORECASE))