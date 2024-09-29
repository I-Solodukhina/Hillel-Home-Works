import pytest
from playwright.sync_api import sync_playwright
from lesson_28.registration1 import RegistrationPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def wd(page):
    wd = RegistrationPage(page)
    wd.page.goto('https://guest:welcome2qauto@qauto2.forstudy.space/')
    wd.page.wait_for_load_state('networkidle')
    wd.page.locator(".hero-descriptor_btn.btn.btn-primary").click()
    return wd
