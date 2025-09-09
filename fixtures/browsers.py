import pytest
from playwright.sync_api import Page, Playwright
import allure
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from tools.playwright.pages import initialize_playwright_page 
from config import settings
from tools.routes import AppRoute



# Фикстура, возвращающая страницу 
@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)

# Фикстура, регистрирующая нового юзера + сохраняющая состояние браузера
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email, 
        username=settings.test_user.username, 
        password=settings.test_user.password
        )
    registration_page.click_registration_button()

    # Забираем состояние браузера и помещаем в JSON
    context.storage_state(path=settings.browser_state_file)
    browser.close()

# Фикстура, открывающая новую страницу браузера, используя сохраненное состояние браузера
@pytest.fixture(params=settings.browsers)
def page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright, test_name=request.node.name, 
        storage_state=settings.browser_state_file, 
        browser_type=request.param
        )
