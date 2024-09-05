# Created by trilo at 05-09-2024
from src.math_oper import add, sub


def test_add():
    assert add(2, -3) == -1
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(-2, 2) == 0


def test_sub():
    assert sub(2, -3) == 5
    assert sub(2, 3) == -1
    assert sub(-2, 3) == -5
    assert sub(-2, 2) == -4
    assert sub(3, 2) == 1
