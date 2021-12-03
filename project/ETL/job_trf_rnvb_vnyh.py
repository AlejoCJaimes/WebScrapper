import sys
import pandas as pd
from tabulate import tabulate
sys.path.append('..')
from web_scrapper_labels.vap_route import ROOT_RUOUTE
from web_scrapper_labels.vap_route import ETL_ROUTE

class Transform:
    def __init__(self, file_name, path_file):
        self._data_set_dirty = None
        self._data_set_clean = None
        self._data_set_process = None
        self._path_file = path_file + '/' + file_name.strip()

    def load_labels(self,labelname):
        aux = ROOT_RUOUTE()[:-1]+ ETL_ROUTE() + 'RawFiles/'
        labelname = labelname.replace('.csv','.txt')
        labels = open(aux+labelname)
        return [label for label in "".join(labels.readlines()).split(',')]

    def load_dataset(self):
        self._data_set_dirty = pd.read_csv(self._path_file, encoding='utf-8')
        return self._data_set_dirty

    def missing_data(self):
        data_nulls_values = [
            nan for nan in self._data_set_dirty.isnull().sum()]
        data_nulls_labels = [nan_l for nan_l in self._data_set_dirty.columns]
        nulls_values = dict(zip(data_nulls_labels, data_nulls_values))
        self._data_set_process = (
            nulls_values, self._data_set_dirty.isnull().sum().sum())
        return self._data_set_process

    def show_missing_data(self):
        nulls_values = dict(zip([k for k, v in self._data_set_process[0].items() if v > 0], [
                            v for k, v in self._data_set_process[0].items() if v > 0]))
        return nulls_values, ['Etiquetas', '#Datos']

    def null_handling_values(self):
        print('Se encontraron {} datos vacios o nulos.'.format(
            self._data_set_process[1])) if self._data_set_process[1] > 0 else print('No se encontraron datos vacios.')
        if self._data_set_process[1] > 0:
            info = self.show_missing_data()
            print(tabulate(info[0].items(), headers=info[1])) if bool(
                input('¿Desea ver detalle de datos vacios? n/y\t').lower() == 'y') else None
            return info[0]

    def fill_null_values(self):
        self._data_set_clean = self._data_set_dirty.fillna(0)

    def get_clean_dataset(self):
        return self._data_set_clean


if __name__ == '__main__':
    df_pss = Transform('2','2')
    x = df_pss.load_labels('labels_saber_11_2020_1_021220212327.csv')
    
    #labels_saber_11_2020_1_021220212327.txt
    print(x)
    #labels_saber_11_2020_1_021220212327
    # ds_saber_11_2020_1_191120210656.csv
    # labels_saber_11_2020_1_191120210656.txt

    # operations with pandas
    #dataset = df_pss.drop_columns(dataset)
    # f_pss.print_dataset()
