import pytest 
from typing import Generator
from playwright.sync_api import sync_playwright, Page, Playwright, expect


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        yield browser.new_page(), context
        browser.close()


# Фикстура, регистрирующая нового юзера + сохраняющая состояние браузера
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(
          'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration',
          wait_until="networkidle"
          )

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('email@mail.ru')

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Забираем состояние браузера и помещаем в JSON
    context.storage_state(path='browser-state.json')

    page.close()
    context.close()
    browser.close()


# Фикстура, открывающая новую страницу браузера, используя сохраненное состояние браузера
@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # Используем ранее сохраненное состояние браузера
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
      