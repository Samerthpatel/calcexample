"""Testing the Calculator"""


from calc.calculator import Calculator


def test_calculator_add_static():
    """testing that our calculator has a static method for addition"""
    assert Calculator.add_numbers(1, 2) == 3


def test_calculator_subtract():
    """Testing the subtract method of the calc"""

    assert Calculator.subtract_numbers(1, 2) == -1


def test_calculator_multiply():
    """Testing the multiply method of the calc"""

    assert Calculator.multiply_numbers(4, 2) == 8


def test_calculator_divide():
    """Testing the divide method of the calc class"""

    assert Calculator.divide_numbers(4, 2) == 2
