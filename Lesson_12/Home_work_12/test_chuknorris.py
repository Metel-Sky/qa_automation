import pytest
import requests


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    # перевірити поля "icon_url" чи він не пустий + чи це картинка - 2 теста  ^-^

    def test_chuk_year(self):
        assert int(self.response.json()["created_at"][:4]) > 1995, "all our jokes were created until 1990"

    def test_status_code(self):
        assert self.status_code == 200  # Перевірка статус коду в evaluate

    def test_icon_url(self):
        URL = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(URL)
        icon = response.json()
        assert icon['icon_url']
        print(type(icon))

    def test_icon_url_image(self):
        URL = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(URL)
        icon = response.json()
        assert 'icon_url' in icon
        print(*icon)

    def test_jpg_extension(self):
        URL = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(URL)
        icon = response.json()
        assert icon['icon_url'].endswith('.jpg') != True  # Заглушка

    # ========================================================================================
    # перевірити чи є ключ "value"  і перевірити його значення - 2 теста

    def test_value_key_exists(self):
        chuck_api_url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(chuck_api_url)
        value = response.json()

        assert 'value' in value

    def test_value_key_content(self):
        chuck_api_url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(chuck_api_url)
        value = response.json()

        assert 'value' in value
        assert value['value'] is not None
        assert len(value['value']) > 0


# Зробити окремий клас
class ChuckNorrisJokeSearch:
    def __init__(self):
        self.base_url = 'https://api.chucknorris.io/jokes/search'

    def search_jokes_by_keyword(self, query):
        url = f'{self.base_url}?query={query}'
        response = requests.get(url)
        return response.status_code, response.json()


def test_search_jokes_status_code(joke_search):
    status_code, _ = joke_search.search_jokes_by_keyword('python')
    assert status_code == 200


def test_search_jokes_count(joke_search):
    _, data = joke_search.search_jokes_by_keyword('testing')
    assert 'total' in data
    assert data['total'] >= 0


def test_search_jokes_content(joke_search):
    _, data = joke_search.search_jokes_by_keyword('Chuck')
    assert 'result' in data
    assert isinstance(data['result'], list)
    assert len(data['result']) > 0
    assert 'value' in data['result'][0]


def test_search_jokes_invalid_keyword(joke_search):
    status_code, data = joke_search.search_jokes_by_keyword('invalid_keyword')
    assert status_code == 200
    assert 'total' in data
    assert data['total'] == 0


def test_search_jokes_special_characters(joke_search):
    status_code, data = joke_search.search_jokes_by_keyword('$%^&*')
    assert status_code == 200
    assert 'total' in data
    assert data['total'] == 0


def test_category():
    URL = "https://api.chucknorris.io/jokes/categories"
    response = requests.request(method="GET", url=URL)
    print(response.json())


def test_categories():
    URL = "https://api.chucknorris.io/jokes/random?category=career"
    response = requests.request(method="GET", url=URL)
    print(response.text)
    print()
    print(response.json()["id"])
    print()
    assert len(response.json()["id"]) > 10


@pytest.mark.parametrize("category",
                         requests.request(method="GET", url="https://api.chucknorris.io/jokes/categories").json())
def test_categories(category):
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = requests.request(method="GET", url=URL)
    assert len(response.json()["id"]) > 10

# ======================================================
