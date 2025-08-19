from pages.base_page import BasePage
from playwright.sync_api import Page, expect

# Создаю класс страницы регистрации
class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Передаю локаторы на странице регистрации
        self.registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_page_link = page.get_by_test_id('registration-page-login-link')

    # Метод, заполняющий все поля на странице регистрации
    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_email_input.fill(email)
        expect(self.registration_email_input).to_have_value(email)

        self.registration_username_input.fill(username)
        expect(self.registration_username_input).to_have_value(username)

        self.registration_password_input.fill(password)
        expect(self.registration_password_input).to_have_value(password)

    # Метод, кликающий по кнопке Registration
    def click_registration_button(self):
        self.registration_button.click()

    # Метод, кликающий по кнопке Login
    def click_login_page_link(self):
        self.login_page_link.click()


