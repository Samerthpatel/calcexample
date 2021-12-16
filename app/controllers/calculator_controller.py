"""Calculator controller"""

import pandas as pd
# pylint: disable=unused-import
from flask import render_template, request, flash, redirect, url_for, session
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator


class CalculatorController(ControllerBase):
    """Calculator controller"""

    @staticmethod
    def post():
        """Calculator controller"""

        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            Calculator.getHistoryFromCSV()
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            Calculator.writeHistoryToCSV()
            return render_template('result.html',
                                    data=Calculator.getHistory(), value1=value1, value2=value2,
                                    operation=operation, result=result)
            return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        """Calculator controller"""

        return render_template('calculator.html')
