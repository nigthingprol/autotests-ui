from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    link = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'

    # Захожу по ссылке + дожидаюсь загрузки страницы
    page.goto(link,
              wait_until='networkidle'
              )

    # Нахожу кнопку registration + проверяю что она disabled
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Нахожу поле email + заполняю его + проверяю что оно заполнено
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')
    expect(registration_email_input).to_have_value('user.name@gmail.com')

    # Нахожу поле username + заполняю его + проверяю что оно заполнено
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')
    expect(registration_username_input).to_have_value('username')

    # Нахожу поле password + заполняю его + проверяю что оно заполнено
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')
    expect(registration_password_input).to_have_value('password')

    # Проверяю что кнопка registration disabled
    expect(registration_button).to_be_enabled()
