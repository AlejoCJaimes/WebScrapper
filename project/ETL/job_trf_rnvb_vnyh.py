'''Reglas del Negocio
1. Extraer 2000 datos
2. Mostrar el número de estudiantes, con tarjeta de identidad
que presentaron el icfes en zonas rurales y zonas urbanas.
'''

import pandas as pd
import numpy as np

class Transform:
    def __init__(self, file_name, path_file):
        self._data_set_load = None
        self._data_set_dirty = None
        self._data_set_clean = None
        self._path_file = path_file + file_name.strip()

    def load_dataset(self):
        self._data_set_load = pd.read_csv(self._path_file, encoding='utf-8')

    def change_case_to_upper(self):
        self._data_set_load = self._data_set_load.columns.str.upper()
    
    def fix_missing_data(self):
        pass


    def drop_columns(self, dataset):
        dataset = dataset.drop(columns=['estu_tipodocumento'])
        return dataset

    # def print_dataset(self):
    #     saber_11_ds_trf = pd.DataFrame(self._data_set_extract, columns=[
    #                                    'estu_tipodocumento', 'estu_nacionalidad', 'estu_genero', 'estu_fechanacimiento', 'periodo'])
    #     print(self._data_set_extract.columns)


if __name__ == '__main__':
    df_pss = Transform()
    df_pss.load_dataset()
    print(df_pss.getDataset())
    # operations with pandas
    #dataset = df_pss.drop_columns(dataset)
    # f_pss.print_dataset()
