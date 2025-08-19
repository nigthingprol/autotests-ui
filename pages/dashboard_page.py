from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Локатор заголовка
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    # Метод для проверки видимости заголовка
    def check_title_text(self):
        expect(self.dashboard_title).to_have_text('Dashboard')

