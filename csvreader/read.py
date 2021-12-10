"""CSV write function"""

import os
import pandas as pd

class Read:
    """CSV write function"""

    @staticmethod
    def DataFrameFromCSVFile(filename):
        """CSV write function"""

        return pd.read_csv(os.path.abspath(filename))
