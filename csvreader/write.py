"""CSV write function"""

import os

class Write:

    """CSV write function"""
    @staticmethod
    def DataFrameToCSVFile(filename, df):

        """CSV write function"""
        return df.to_csv(os.path.abspath(filename),float_format='%.2f', index=True, header=True)
