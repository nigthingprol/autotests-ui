from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

# Создаю тестовую функцию
@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    # Перехожу по новой ссылке
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses',
                    wait_until='networkidle')

    # Локатор заголовка + проверка видимости и текста в нем
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Локатор иконки "папка" + проверка видимости
    courses_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    # Локатор элемента + проверка видимости + проверка текста в нем
    courses_title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_title_text).to_be_visible()
    expect(courses_title_text).to_have_text('There is no results')

    # Локатор элемента + проверка видимости + проверка текста в нем
    courses_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_description).to_be_visible()
    expect(courses_description).to_have_text('Results from the load test pipeline will be displayed here')


def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(title="", estimated_time="", description="", max_score="0", min_score="0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercises_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form(title="Playwright", estimated_time="2 weeks", description="Playwright", max_score="100", min_score="10")
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks")
