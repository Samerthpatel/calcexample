"""Testing Division"""
from calc.operations.division import Division


def test_division():

    """testing calc result is 0"""
    assert Division.divide(4, 2) == 2
