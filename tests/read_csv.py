import unittest

import pandas

from src.read_csv import load_data


class ReadCsvTest(unittest.TestCase):
    def test_read_Csv(self):
        data = load_data()
        self.assertIsInstance(data, pandas.DataFrame)
