import pytest
from Home_work_9 import add_thre_numbers


def test_first():
    assert add_thre_numbers(5, 3, 3) == 11


def test_second():
    assert add_thre_numbers(3, 3, 3) == 9


def test_end():
    assert add_thre_numbers(3, 4, 3) == 10


@pytest.mark.parametrize("number_1, number_2, number_3, result", [
    pytest.param(3, 5, 3, 11, id="standart"),
    pytest.param(2, 5, 3, 10, id="negativ"),
    pytest.param(4, 5, 3, 12, id="magic")
])
def test_set(number_1, number_2, number_3, result):
    assert add_thre_numbers(number_1, number_2, number_3) == result


list_test = [(3, 5, 3, 11),(3, 5, 4, 12),(1, 5, 3, 9)]

@pytest.mark.parametrize("number_1, number_2, number_3, result", list_test)
def test_set_1(number_1,number_2,number_3,result):
    assert add_thre_numbers(number_1,number_2,number_3)==result