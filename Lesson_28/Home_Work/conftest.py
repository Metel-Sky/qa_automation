import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
