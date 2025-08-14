from playwright.sync_api import sync_playwright, expect

# Создаю тестовую функцию
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Открываю страницу + явно дожидаюсь загрузки
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration',
                  wait_until="networkidle")

        # Локатор кнопки регистрации + ввод текста + проверка текста в инпуте
        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('nalivayko_2018@inbox.ru')
        expect(registration_email_input).to_have_value('nalivayko_2018@inbox.ru')

        # Локатор кнопки username + ввод текста + проверка текста в инпуте
        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill('maxim')
        expect(registration_username_input).to_have_value('maxim')

        # Локатор кнопки password + ввод текста + проверка текста в инпуте
        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill('password')
        expect(registration_password_input).to_have_value('password')

        # Локатор кнопки registration + нажатие на кнопку
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняю состояние браузера + создаю новый JSON файл
        context.storage_state(path='playwright_courses_browser_state.json')

    # Создаю новую сессию браузера
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Подставляю в контекст ранее сохраненное состояние
        context = browser.new_context(storage_state='playwright_courses_browser_state.json')
        page = context.new_page()

        # Перехожу по новой ссылке
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses',
                  wait_until='networkidle')

        # Локатор заголовка + проверка видимости и текста в нем
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        # Локатор иконки "папка" + проверка видимости
        courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_icon).to_be_visible()

        # Локатор элемента + проверка видимости + проверка текста в нем
        courses_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_title_text).to_be_visible()
        expect(courses_title_text).to_have_text('There is no results')

        # Локатор элемента + проверка видимости + проверка текста в нем
        courses_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_description).to_be_visible()
        expect(courses_description).to_have_text('Results from the load test pipeline will be displayed here')