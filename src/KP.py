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
        
    def cost(self):
        '''
        cost function
        '''
        total_cost = self.value.sum()
        total_weight = self.weight.sum()
        if total_weight <= self.max_weight:
            total_cost = total_cost
        else:
            total_cost = total_cost - self.afa * (total_weight - self.max_weight)
        return total_cost
