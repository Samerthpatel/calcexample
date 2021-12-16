"""CSV write function"""
# pylint: disable=unused-import
import os
import pandas as pd

from csvreader.absolutePath import absolutepath
# pylint: disable=invalid-name
in_file = "tests/testdata/csv_output.csv"

class Read:
    """CSV write function"""

    @staticmethod
    def DataFrameFromCSVFile():
        """CSV write function"""

        return pd.read_csv(absolutepath(in_file))
