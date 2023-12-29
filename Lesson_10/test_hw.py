import pytest
from Home_Work_10 import add_three_numbers


@pytest.mark.parametrize("number_1, number_2, number_3, expected_result", [
    pytest.param(3, 5, 36, 44, id="standard"),
    pytest.param(2, 5, 3, 10, id="negative"),
    pytest.param(4, 5, 3, 12, id="magic")
])
def test_add_three_numbers(number_1, number_2, number_3, expected_result):
    assert add_three_numbers(number_1, number_2, number_3) == expected_result
