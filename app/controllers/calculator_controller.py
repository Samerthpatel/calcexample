"""Calculator controller"""
# pylint: disable=line-too-long
# pylint: disable=unused-import
# pylint: disable=no-member
# pylint: disable=unused-variable
from flask import render_template, request, flash, redirect, url_for, session
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from csvreader.read import Read

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
            # Hey if you copy this it will not work you need to think about it
            data = {
                'value1': [value1],
                'value2': [value2],
                'operation': [operation]
            }
            Calculator.writeHistoryToCSV()
            Calculations.create_dataframe_to_write(value1, value2, result, operation)
            df = Read.DataFrameFromCSVFile()
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result,
                                   tables=[df.to_html(classes='data')], titles=df.columns.values,
                                   row_data=list(df.values.tolist()), zip=zip)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        """Calculator controller"""

        return render_template('calculator.html')
