'''
read csv module with 3 functions.
'''
import urllib.request
import pandas as pd

def load_data(path,filename):
    '''
    fuction to fetch data.
    '''
    urllib.request.urlretrieve(path, filename)
    return pd.read_csv(filename, names=["w", "v"])
