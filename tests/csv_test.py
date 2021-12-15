"""Testing CSV Functions"""

import os.path
import pandas
# pylint: disable=reimported
import pandas as pd
from csvreader.write import Write
from csvreader.read import Read


def test_write_csv():
    """testing that our calculator has a static method for addition"""
    # Arrange
    filename = 'csv_output.csv'
    path = 'tests/testdata'
    fullPath = path + '/' + filename
    name_dict = {
        'value1': ['1.0', '2.0', '3.0', '4.0'],
        'value2': ['1.0', '2.0', '3.0', '4.0'],
        'value3': [2.0, 4.0, 6.0, 8.0]
    }
    os.remove(fullPath)
    df = pd.DataFrame(name_dict)
    # Act

    Write.DataFrameToCSVFile(fullPath, df)
    # Assert
    assert os.path.exists(fullPath)


def test_read_csv():
    """testing that our calculator has a static method for addition"""
    # Arrange
    filename = 'csv_output.csv'
    path = 'tests/testdata'
    fullPath = path + '/' + filename
    # Act
    df = Read.DataFrameFromCSVFile(fullPath)
    # Assert
    # pylint: disable=unidiomatic-typecheck
    assert type(df) is pandas.DataFrame
