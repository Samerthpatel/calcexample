"""Testing Multiplication"""
from calc.operations.multiplication import Multiplication


def test_multiplication():

    """testing calc result is 0"""
    assert Multiplication.multiply(4, 2) == 8
