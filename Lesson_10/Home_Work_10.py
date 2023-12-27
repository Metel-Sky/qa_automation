import pytest
def add_thre_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result







@pytest.mark.parametrize("number_1, number_2, number_3, result", [
    pytest.param(3, 5, 3, 11, id="standart"),
    pytest.param(2, 5, 3, 10, id="negativ"),
    pytest.param(4, 5, 3, 12, id="magic")
])
def test_set(number_1, number_2, number_3, result):
    assert add_thre_numbers(number_1, number_2, number_3) == result
