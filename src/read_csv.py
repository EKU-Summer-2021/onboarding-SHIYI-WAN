import pandas as pd
import urllib.request


def fetch_data():
    path = "https://github.com/EKU-Summer-2021/intelligent_system_data/blob/main/Intelligent%20System%20Data/KP/KP_10" \
           ".csv "
    urllib.request.urlretrieve(path, "10.csv")

    
    
def load_data():
    fetch_data()
    csv_path = "10.csv"
    return pd.read_csv(csv_path, names=["w", "v"])
