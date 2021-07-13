'''
read csv module with 3 functions.
'''
import pandas as pd

def load_data(path):
    '''
    fuction to fetch data.
    '''
    return pd.read_csv(path)
