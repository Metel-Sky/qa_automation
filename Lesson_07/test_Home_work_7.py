from Home_work_7 import sortUP
from Home_work_7 import sortDOWN
from Home_work_7 import sortLENG


def test_sortUP():
    assert sortUP(5, 4, 3, 1, 2) == [1, 2, 3, 4, 5]


def test_sortDOWN():
    assert sortDOWN(5, 4, 3, 1, 2) == [5, 4, 3, 2, 1]


def test_sortLEN():
    assert sortLENG('abcffff','ddff','ddd','77ddd') == ['ddd', 'ddff', '77ddd', 'abcffff']