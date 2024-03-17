
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from Lesson_24.src.pages.pages_buttons import PageButtons



@pytest.mark.usefixtures("chrome_class")
class TestButtons:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageButtons(driver=self.driver)

    def test_doubleclick_button(self):
        self.page.open()
        self.page.button_doubleclick().doubleclick()
        assert self.page.get_button_doubleclick_message() == 'You have done a double click'

    def test_right_click_button(self): # Right Click Me
        self.page.open()
        self.page.right_click_button().right_click()
        assert self.page.get_button_right_click_message() == 'You have done a right click'

    def test_dynamic_id_click_button(self):  # Click Me
        self.page.open()
        self.page.dymanic_id_click_button().click()
        text = self.page.get_button_dynamic_id_click_message()
        assert 'You have done a dynamic click' in text