'''
read csv module with 3 functions.
'''
import urllib.request
import pandas as pd

def fetch_data():
    '''
    fuction to fetch data.
    '''
    path = "https://github.com/EKU-Summer-2021/intelligent_system_data/blob/main/" \
    "Intelligent%20System%20Data/KP/KP_10.csv "
    urllib.request.urlretrieve(path, "10.csv")

def load_data():
    '''
    fuction to load data.
    '''
    fetch_data()
    csv_path = "10.csv"
    return pd.read_csv(csv_path, names=["w", "v"])

def summary_data():
    '''
    fuction to summary data.
    '''
    return load_data().describe()
