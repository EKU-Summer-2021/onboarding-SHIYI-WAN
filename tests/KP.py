import unittest
import pandas as pd
from src import KP


class KPTest(unittest.TestCase):
    def test_cost_function(self):
        d = {'col1': [1, 2], 'col2': [3, 4]}
        kp = KP.KP(d, 8, 2)
        df = pd.DataFrame(data=d)
        cost = kp.cost()
        expected = 7
        self.assertEqual(cost, expected)
