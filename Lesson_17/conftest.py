import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="\Users\Vinch\Desktop\QA_automation\Lesson_18/chromedriver")
    yield driver
    driver.quit()