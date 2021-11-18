"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """division calculation object"""

    def get_result(self):
        """get the division results"""
        divisionresult = 1.0
        for value in self.values:
            divisionresult = divisionresult / value
        return divisionresult
