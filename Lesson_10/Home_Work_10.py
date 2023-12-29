import pytest


def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


@pytest.mark.parametrize("number_1, number_2, number_3, expected_result", [
    pytest.param(3, 5, 3, 11, id="standard"),
    pytest.param(2, 5, 3, 10, id="negative"),
    pytest.param(4, 5, 3, 12, id="magic")
])
def test_add_three_numbers(number_1, number_2, number_3, expected_result):
    assert add_three_numbers(number_1, number_2, number_3) == expected_result
    with open("log.txt", "a") as file:
        file.write(f"\n{number_1}, {number_2}, {number_3} => {expected_result}\n")
