import pandas as pd
import numpy as np

def load_dataset():
    ds = pd.read_csv('project/ETL/RawFiles/ds_saber_11_2020_1_191120210656.csv', encoding='utf-8')
    ls =ds.isnull().sum()
    return print(ls)

load_dataset()