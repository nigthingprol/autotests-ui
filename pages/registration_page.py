from components.authentication.registartion_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from elements.button import Button
from elements.link import Link
from playwright.sync_api import Page, expect

# Создаю класс страницы регистрации
class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        # Передаю локаторы на странице регистрации
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration button')
        self.login_page_link = Link(page, 'registration-page-login-link', 'Login page link')

    # Метод, кликающий по кнопке Registration
    def click_registration_button(self):
        self.registration_button.click()

    # Метод, кликающий по кнопке Login
    def click_login_page_link(self):
        self.login_page_link.click()


