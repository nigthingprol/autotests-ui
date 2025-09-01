import pytest
from playwright.sync_api import Page, Playwright
import allure
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from tools.playwright.pages import initialize_playwright_page



# Фикстура, возвращающая страницу 
@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)

# Фикстура, регистрирующая нового юзера + сохраняющая состояние браузера
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='email@mail.ru', username='username', password='password')
    registration_page.click_registration_button()

    # Забираем состояние браузера и помещаем в JSON
    context.storage_state(path='browser-state.json')
    browser.close()

# Фикстура, открывающая новую страницу браузера, используя сохраненное состояние браузера
@pytest.fixture(scope='function')
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, storage_state='browser-state.json')
