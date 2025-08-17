from playwright.sync_api import sync_playwright, expect
import pytest

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