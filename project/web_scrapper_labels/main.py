import argparse
import logging
import data_page_objects as dpage
import trf_json_list as json_decoder
import pandas as pd 
import sys
import os
import errno
from common import config
from vap_route import ROOT_RUOUTE
from vap_route import ETL_ROUTE
sys.path.append('..')
from ETL import credentials as cred
from ETL import job_ext_rnvb_vnyh as Api_dataset


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _data_gov_scraper(data_site_uid):
    host = config()['data_sites'][data_site_uid]['url']
    logging.info('Inicilializando scraper para {}'.format(host))
    homepage = _fetch_labels(data_site_uid, host)
    labels = _export_labels(homepage._path)
    if labels[1]:
        logger.info(
            'Ejecución exitosa. {} etiquetas encontradas'.format(len(labels[0])))
        #[print(label) for label in labels[0]]
    else:
        logger.error('Ha ocurrido un error en la automatización del proceso')
    df = _extract_dataset(data_site_uid)
    export_data(df,labels[0])


def _fetch_labels(data_site_uid, host):
    logger.info('Comenzando extracción de etiquetas para {}'.format(host))
    homepage = dpage.HomePage(data_site_uid, host)
    # print(homepage.page_labels)
    logger.info('Extracción en JSON realizada correctamente.')
    homepage.save_json_labels
    logger.info('Guardando dataset en {}'.format(
        homepage._path_relative_project))
    return homepage


def _export_labels(path):
    json_decode = json_decoder.UnstruscturedJson(path)
    logger.info('Compilando JSON - Status OK')
    logger.info('Convirtiendo JSON en etiqueta de listas')
    list_labels = json_decode.automated_convert_process
    return list_labels


def _extract_dataset(data_site_uid):
    user_access = cred.Credentials().ext()
    df = Api_dataset.Extract().extract(user_access[0],user_access[1],user_access[2])
    host = config()['data_sites'][data_site_uid]['url']
    logging.info('Extrayendo datos de  {}'.format(host))
    logger.info('{} filas extraidas.'.format(len(df.axes[0])))
    return df


def export_data(df, list):
    status = True
    logger.info('Exportando data ...')
    path_dir = ROOT_RUOUTE()[:-1]+ ETL_ROUTE() + 'RawFiles'
    try:
        #create dir
        os.mkdir(path_dir)

        #export df to excel
        #workbook = Workbook()
        excel_filename = 'data_saber_11_2020_2.xlsx'
        path_excel_file = path_dir + '/' + excel_filename

        #df.to_excel(path_excel_file, index=False, encoding='utf-8')
        df.to_excel(path_excel_file, index=False, encoding='utf-8', sheet_name= 'resultados_saber_11_2020_2')

        #export list to .txt
        textfile_name = 'labels_saber_11_2020_2.txt'
        path_text_file = path_dir + '/' + textfile_name
        textfile = open(path_text_file,'w')
        [textfile.write(element + ',') for element in list]
        textfile.close()

        logger.info('Archivos exportados correctamente - Status OK')
        logger.info('Ruta de archivos: {}'.format(ETL_ROUTE() + 'RawFiles'))
        logger.info('Arhivos exportados: \n{0}\n{1}'.format(excel_filename,textfile_name))
    except OSError as e:
        status = False
        if e.errno != errno.EEXIST:
            raise
    return status

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    new_sites_choices = list(config()['data_sites'].keys())
    parser.add_argument(
        'data_sites',
        help='Sitios de Datos abiertos para scrapear',
        type=str,
        choices=new_sites_choices
    )

    args = parser.parse_args()
    _data_gov_scraper(args.data_sites)
