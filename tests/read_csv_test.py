import unittest

import pandas

from src import read_csv


class ReadCsvTest(unittest.TestCase):
    def test_read_Csv(self):
        data = read_csv.load_data()
        self.assertIsInstance(data, pandas.DataFrame)
