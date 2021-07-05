'''
read csv module with 3 functions.
'''
import urllib.request
import pandas as pd
'''
fuction to fetch data.
'''
def fetch_data():
    path = "https://github.com/EKU-Summer-2021/intelligent_system_data/blob/main/" \
    "Intelligent%20System%20Data/KP/KP_10.csv "
    urllib.request.urlretrieve(path, "10.csv")
'''
fuction to load data.
'''
def load_data():
    fetch_data()
    csv_path = "10.csv"
    return pd.read_csv(csv_path, names=["w", "v"])
'''
fuction to summary data.
'''
def summary_data():
    return load_data().describe()
