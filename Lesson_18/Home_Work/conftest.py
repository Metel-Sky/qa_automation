from selenium import webdriver
import pytest

@pytest.fixture
def chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("executable_path=/home/vinch/Стільниця/Hilel/Lesson_18/Home_Work/chromedriver")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
