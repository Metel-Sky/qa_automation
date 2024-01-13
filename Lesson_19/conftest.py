import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("executable_path=Users/Vinch/Desktop/QA_automation/Lesson_18/chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

