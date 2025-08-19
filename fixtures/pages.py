import pytest 
from playwright.sync_api import Page

from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# Фикстура инициализации страницы LoginPage
@pytest.fixture(scope='function')
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

# Фикстура инициализации страницы RegistrationPage
@pytest.fixture(scope='function')
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

# Фикстура инициализации страницы DashboardPage
@pytest.fixture(scope='function')
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)