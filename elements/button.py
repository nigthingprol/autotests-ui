from playwright.sync_api import expect
from elements.base_element import BaseElement
import allure


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"


    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f"Checking that {self.type_of} '{self.name}' in enabled"):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f"Checking that {self.type_of} '{self.name}' in disabled"):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()
    
    
     