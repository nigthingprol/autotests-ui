from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    link = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

    page.goto(link)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for char in 'user@gmail.com':
        page.keyboard.type(char)

    page.keyboard.press("ControlOrMeta+A")
    page.keyboard.press("Backspace")

    page.wait_for_timeout(5000)
