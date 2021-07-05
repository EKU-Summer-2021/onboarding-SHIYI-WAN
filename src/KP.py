'''
Example module for template project.
Pylint will check code in the src directory only!
'''
import pandas as pd


class KP:
    def __init__(self, dataset, max_weight, afa):
        '''
        initial
        '''
        self.weight = pd.DataFrame(data=dataset).iloc[:, 0]
        self.value = pd.DataFrame(data=dataset).iloc[:, 1]
        self.max_weight = max_weight
        self.afa = afa
