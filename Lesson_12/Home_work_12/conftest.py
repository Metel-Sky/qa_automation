import pytest
import requests


@pytest.fixture(scope="session")
def fixture_random():
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/random")
    print(1)
    yield response