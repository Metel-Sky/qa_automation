
import pytest
import requests
from selenium import webdriver

@pytest.fixture
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # ������ �� ����, ����� ��� ����� Ѳ��
    options.add_argument("--disable-gpu")  # �� ����������� ���������
    options.add_argument("--headless")  # ��� �������� ���������� ��������.
    driver = webdriver.Chrome(options=options, executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_22/chromedriver")
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_22/geckodriver")
    request.cls.driver = driver
    driver.implicitly_wait(5)  # ������ ���� �� ��� ���������
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_22/chromedriver")
    request.cls.driver = driver
    yield driver
    driver.quit()

#�������� ��� ������ ������� ���������.
@pytest.fixture(scope="class", params=['fashion', 'food', 'history'])
def fixture_chuck_category(request):
    category = request.param
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    print(URL)
    response = requests.request(method="GET", url=URL)
    request.cls.response = response
    yield response