import pytest
from src.calculator import add, divide


def test_addition():
    assert add(2, 2) == 4


def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)