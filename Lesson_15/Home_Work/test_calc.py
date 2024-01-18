import datetime
import pytest
from Home_Work_15 import Calc

@pytest.fixture(scope="class")
def setup_teardown(request):
    with open("test_log.txt", "a") as file:
        file.write(f"Тест почався о: {datetime.datetime.now()}\n")

    def teardown():
        with open("test_log.txt", "a") as file:
            file.write(f"Тест закінчився о: {datetime.datetime.now()}\n")

    request.addfinalizer(teardown)

@pytest.mark.parametrize("a, b, expected_result", [(2, 3, 5), (0, 0, 0), (-1, 1, 0), (10, -5, 5), (7, 8, 15)])
def test_addition(a, b, expected_result, setup_teardown):
    calc = Calc()
    result = calc.add(a, b)
    assert result == expected_result

@pytest.mark.parametrize("a, b, expected_result", [(6, 2, 3), (10, 2, 5), (15, 3, 5), (-8, 2, -4), (0, 1, 0)])
def test_division(a, b, expected_result, setup_teardown):
    calc = Calc()
    result = calc.divide(a, b)
    assert result == expected_result