import datetime

import pytest


@pytest.fixture(scope="class")
def setup_teardown(request):
    with open("test_log.txt", "a") as file:
        file.write(f"Тест почався о: {datetime.datetime.now()}\n")

    def teardown():
        with open("test_log.txt", "a") as file:
            file.write(f"Тест закінчився о: {datetime.datetime.now()}\n")

    request.addfinalizer(teardown)