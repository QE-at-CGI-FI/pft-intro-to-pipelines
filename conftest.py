import pytest
from playwright.sync_api import Page
import allure

@allure.title("Config: Navigate to the base URL before each test")
@pytest.fixture(scope="function")
def page_to_url(pytestconfig, page: Page) -> Page:
    page.goto(pytestconfig.getoption("base_url"))
    yield page