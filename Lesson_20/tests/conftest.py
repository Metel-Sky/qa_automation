import pytest
from selenium import webdriver

# @pytest.fixture
# def chrome():
#     driver = webdriver.Chrome("executable_path=/home/vinch/Стільниця/Hilel/Lesson_18/Home_Work_22/chromedriver")
#     yield driver
#     driver.quit()

# @pytest.fixture
# def chrome():
#     driver = webdriver.Chrome(executable_path=r"Vinch\Desktop\QA_automation\Lesson_20\chromedriver.exe")
#     yield driver
#     driver.quit()


# @pytest.fixture(scope="class")
# def firefox(request):
#     driver = webdriver.Chrome(executable_path=r"Vinch\Desktop\QA_automation\Lesson_20\chromedriver.exe")
#     request.cls.driver = driver
#     driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
#     yield driver
#     driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome(executable_path="Users\Vinch\Desktop\QA_automation\Lesson_20\chromedriver.exe")
    request.cls.driver = driver
    yield driver
    driver.quit()