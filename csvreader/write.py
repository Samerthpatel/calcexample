"""CSV write function"""

class Write:

    """CSV write function"""
    @staticmethod
    def DataFrameToCSVFile(df):

        """CSV write function"""
        df.to_csv('tests/testdata/csv_output.csv', mode='a', index=False, header=False)
