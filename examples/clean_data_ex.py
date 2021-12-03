import pandas as pd
import numpy as np
from tabulate import tabulate


def load_dataset():
    ds = pd.read_csv(
        'project/ETL/RawFiles/ds_saber_11_2020_1_191120210656.csv', encoding='utf-8')
    return ds


def load_labels(filename):
    labels = open(filename+'.txt')
    return [label for label in "".join(labels.readlines()).split(',')]


def missing_data(ds_saber_11_2020):
    data_nulls_values = [nan for nan in ds_saber_11_2020.isnull().sum()]
    data_nulls_labels = [nan_l for nan_l in ds_saber_11_2020.columns]
    nulls_values = dict(zip(data_nulls_labels, data_nulls_values))
    return nulls_values, ds_saber_11_2020.isnull().sum().sum()


def show_missing_data(dict_nulls):
    nulls_values = dict(zip([k for k, v in dict_nulls[0].items() if v > 0], [
                        v for k, v in dict_nulls[0].items() if v > 0]))
    return nulls_values, ['Etiquetas', '#Datos']


def null_handling_values(ds):
    nulls_values = missing_data(ds)
    print('Se encontraron {} datos vacios o nulos.'.format(
        nulls_values[1])) if nulls_values[1] > 0 else print('No se encontraron datos vacios.')
    if nulls_values[1] > 0:
        info = show_missing_data(nulls_values)
        print(tabulate(info[0].items(), headers=info[1])) if bool(
            input('¿Desea ver detalle de datos vacios? n/y').lower() == 'y') else None
        return info[0]
    else:
        pass
    return 0
