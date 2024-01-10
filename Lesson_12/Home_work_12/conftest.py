import pytest
import requests

from Lesson_12.Home_work_12.test_chuknorris import ChuckNorrisJokeSearch


@pytest.fixture(scope="class")
def fixture_random(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response


@pytest.fixture
def joke_search():
    return ChuckNorrisJokeSearch()