import unittest

import pandas

from src.read_csv import load_data


class ReadCsvTest(unittest.TestCase):
    def test_read_Csv(self):
        data = load_data('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent'
                        '%20System%20Data/CSP/CSP_360.csv',"360.csv")
        self.assertIsInstance(data, pandas.DataFrame)
