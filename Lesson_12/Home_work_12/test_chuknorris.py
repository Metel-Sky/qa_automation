import pytest


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    def test_chuk_year(self):
        assert int(self.response.json()["created_at"][:4]) > 1995, "all our jokes were created until 1990"

    def test_status_code(self):
        assert self.status_code ==200 #Перевірка статус коду в evaluate


# todo evaluate
#   assert response.status_code ==200 Перевірка статус коду в evaluate
#   assert int(response.json()["created_at"][:4]) > 1995, "all our jokes were created until 1990"
#   response.json()   інформація в форматі json
#   response.json()["created_at"] == дата створення
#








