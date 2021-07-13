'''
Example module for template project.
Pylint will check code in the src directory only!
'''
import unittest

import pandas as pd

from src.read_csv import load_data


class ReadCsvTest(unittest.TestCase):
    '''
    read csv test class
    '''
    def test(self):
        '''
        test method
        '''
        data = load_data('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data'
                         '/main/Intelligent'
                         '%20System%20Data/CSP/CSP_360.csv')
        dataframe = pd.DataFrame(data)
        self.assertIsInstance(dataframe, pd.DataFrame)

