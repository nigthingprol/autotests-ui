import pytest 
from playwright.sync_api import Page

from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

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

# Фикстура инициализации страницы DashboardPage (с сохраненным состоянием браузера)
@pytest.fixture(scope='function')
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)

# Фикстура инициализации страницы CoursesListPage
@pytest.fixture(scope='function')
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)

# Фикстура инициализации страницы CreateCoursePage
@pytest.fixture(scope='function')
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)  