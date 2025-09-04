import pytest 
from playwright.sync_api import Page

from pages.authentication.registration_page import RegistrationPage
from pages.authentication.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage 

# Фикстура инициализации страницы LoginPage
@pytest.fixture(scope='function')
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)

# Фикстура инициализации страницы RegistrationPage
@pytest.fixture(scope='function')
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page=page)

# Фикстура инициализации страницы DashboardPage
@pytest.fixture(scope='function')
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page=page)

# Фикстура инициализации страницы DashboardPage (с сохраненным состоянием браузера)
@pytest.fixture(scope='function')
def dashboard_page_with_state(page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=page_with_state)

# Фикстура инициализации страницы CoursesListPage
@pytest.fixture(scope='function')
def courses_list_page(page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=page_with_state)

# Фикстура инициализации страницы CreateCoursePage
@pytest.fixture(scope='function')
def create_course_page(page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=page_with_state)  