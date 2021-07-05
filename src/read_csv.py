'''
read csv module with 3 functions.
'''
import urllib.request
import pandas as pd

def fetch_data(path,filename):
    '''
    fuction to fetch data.
    '''
    urllib.request.urlretrieve(path, filename)

def load_data(path,filename):
    '''
    fuction to load data.
    '''
    fetch_data(path,filename)
    return pd.read_csv(filename, names=["w", "v"])

def summary_data():
    '''
    fuction to summary data.
    '''
    return load_data(path,filename).describe()
