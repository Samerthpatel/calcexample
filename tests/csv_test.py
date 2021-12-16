"""Testing CSV Functions"""

import os.path
import pandas
# pylint: disable=reimported
import pandas as pd
from csvreader.write import Write
from csvreader.read import Read


def test_write_csv():
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = 'csv_output.csv'
    path = 'tests/testdata'
    fullPath = path + '/' + filename
    name_dict = {
        'value_1': ['1'],
        'value_2': ['2'],
        'result': [3.0],
        'operation performed': "addition"
    }
    os.remove(fullPath)
    df = pd.DataFrame(name_dict)
    #Act

    Write.DataFrameToCSVFile(df)
    #Assert
    assert os.path.exists(fullPath)

def test_read_csv():
    """testing that our calculator has a static method for addition"""
    #Arrange
    # pylint: disable=unused-variable
    filename = 'csv_output.csv'
    path = 'tests/testdata'
    fullPath = path + '/' + filename
    #Act
    df = Read.DataFrameFromCSVFile()
    #Assert
    # pylint: disable=unidiomatic-typecheck
    assert type(df) is pandas.DataFrame
