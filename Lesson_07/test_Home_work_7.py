from Home_work_7 import sortUp
from Home_work_7 import sortDown
from Home_work_7 import sortLen


def test_sortUp():
    assert sortUp(5, 4, 3, 1, 2) == [1, 2, 3, 4, 5]


def test_sortDown():
    assert sortDown(5, 4, 3, 1, 2) == [5, 4, 3, 2, 1]


def test_sortLen():
    assert sortLen('abcffff', 'ddff', 'ddd', '77ddd') == ['ddd', 'ddff', '77ddd', 'abcffff']
