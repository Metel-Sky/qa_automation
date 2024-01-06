import pytest
import requests


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    def test_chuk_year(self):
        assert int(self.response.json()["created_at"][:4]) > 1995, "all our jokes were created until 1990"

    def test_status_code(self):
        assert self.status_code == 200  # Перевірка статус коду в evaluate


def test_category():
    URL = "https://api.chucknorris.io/jokes/categories"
    response = requests.request(method="GET", url=URL)
    print(response.json())


# def test_categories():
#     URL = "https://api.chucknorris.io/jokes/random?category=career"
#     response = requests.request(method="GET", url=URL)
    # print(response.text)
    # print()
    # print(response.json()["id"])
    # print()
    # assert len(response.json()["id"]) > 10

@pytest.mark.parametrize("category",
                         requests.request(method="GET", url="https://api.chucknorris.io/jokes/categories").json())

def test_categories(category):
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = requests.request(method="GET", url=URL)
    assert len(response.json()["id"]) >10
















# todo evaluate
#   assert response.status_code ==200 Перевірка статус коду в evaluate
#   assert int(response.json()["created_at"][:4]) > 1995, "all our jokes were created until 1990"
#   response.json()   інформація в форматі json
#   response.json()["created_at"] == дата створення
#
