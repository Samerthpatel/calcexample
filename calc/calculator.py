""" This is the increment function"""
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculator:

    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adds two numbers"""
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ subtract number from result"""
        return Subtraction.subtract(value_a, value_b)

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply number from result"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide number from result"""
        return Division.divide(value_a, value_b)
