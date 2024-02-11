from selenium.webdriver.remote.webelement import WebElement

from Lesson_20.DynamicPropertiesPage import PageDynamicProperties
from Lesson_20.ElementsPage import ElementsPage
import pytest


class TestElementsPage:
    def test_page(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33
