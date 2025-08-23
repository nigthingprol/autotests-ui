from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent 
from components.navigation.sidebar_component import SidebarComponent
from playwright.sync_api import Page, expect

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)
        self.students_chart_view = ChartViewComponent(page, identifier='students', chart_type='bar')
        self.activities_chart_view = ChartViewComponent(page, identifier='activities', chart_type='line')
        self.courses_chart_view = ChartViewComponent(page, identifier='courses', chart_type='pie')
        self.scores_chart_view = ChartViewComponent(page, identifier='scores', chart_type='scatter')
