import argparse
import logging
import data_page_objects as dpage
import functions_handling as aux_func
import trf_json_list as json_decoder
import sys
import os
import errno
from common import config
from vap_route import ROOT_RUOUTE
from vap_route import ETL_ROUTE
from dataset_rows import MaxRowData
from tabulate import tabulate
sys.path.append('..')
from ETL import credentials as cred
from ETL import job_ext_rnvb_vnyh as Api_dataset
from ETL import job_trf_rnvb_vnyh as trf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# core function
def _data_gov_scraper(data_site_uid):
    host = config()['data_sites'][data_site_uid]['url']
    logging.info('Inicilializando scraper para {}'.format(host))
    homepage = _fetch_labels(data_site_uid, host)
    labels = _export_labels(homepage._path)
    logger.info('Ejecución exitosa. {} etiquetas encontradas'.format(len(labels[0]))) if labels[1] else logger.error('Ha ocurrido un error en la automatización del proceso')
    #[print(label) for label in labels[0]]

    df = _extract_dataset(data_site_uid,aux_func.AuxiliarFunctions().site_url_location(host))
    _export_data(df,labels[0],data_site_uid)
    _load_dataset_dirty()
    


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


def _extract_dataset(data_site_uid, site_location):
    
    # helpful
    host = config()['data_sites'][data_site_uid]['url']
    logging.info('Extrayendo datos de  {}'.format(host))

    host = config()['data_sites'][data_site_uid]['url_main_page']
    user_access = cred.Credentials().ext()


    df = Api_dataset.Extract().extract(user_access[0],user_access[1],user_access[2],site_location,MaxRowData().RowsDataset(host))
    logger.info('{} filas extraidas.'.format(len(df.axes[0])))
    return df

def _export_data(df, list, data_site_uid):
    status = True
    logger.info('Exportando data ...')
    path_dir = ROOT_RUOUTE()[:-1]+ ETL_ROUTE() + 'RawFiles'
    try:
        
        os.mkdir(path_dir) if os.path.exists(path_dir) == False else False
        
        #export excel
        csv_filename =   'ds_'+data_site_uid + aux_func.AuxiliarFunctions().format_date() + '.csv'# 'ds_saber_11_2020_2_07112021.xlsx'
        path_csv_file = path_dir + '/' + csv_filename

        df.to_csv(path_csv_file, index=False, encoding='utf-8')

        #export list to .txt
        textfile_name = 'labels_'+data_site_uid + aux_func.AuxiliarFunctions().format_date() + '.txt'
        path_text_file = path_dir + '/' + textfile_name
        textfile = open(path_text_file,'w')
        [textfile.write(element + ',') for element in list]
        textfile.close()

        logger.info('Archivos exportados correctamente - Status OK')
        logger.info('Ruta de archivos: {}'.format(ETL_ROUTE() + 'RawFiles'))
        logger.info('Arhivos exportados: \n{0}\n{1}'.format(csv_filename,textfile_name))
    except OSError as e:
        status = False
        if e.errno != errno.EEXIST:
            raise
    return status

def _load_dataset_dirty():
    path_dir = ROOT_RUOUTE()[:-1]+ ETL_ROUTE() + 'RawFiles'
    logging.info('Cargando datasets desde  {}'.format(ETL_ROUTE() + 'RawFiles'))
    files_out = aux_func.AuxiliarFunctions().found_files(path_dir,'.csv')
    headers = ['Archivos', 'Peso'] 
    print(tabulate(zip(files_out.keys(),files_out.values()), headers, tablefmt="fancy_grid"))
    logger.info('Datasets cargados correctamente - Status OK')
    print(f'Datasets encontrados {len(files_out.keys())}')
    filename = str(input('\nDataset a transformar: '))
    logger.info('Empezando Limpieza... - Status OK')
    _clean_dataset(filename,path_dir)
    return 0
    #exist_ds =  os.path.exists(path_dir+filename)
    # os.mkdir(path_dir) if os.path.exists(path_dir) == False else False
    # logging.info('Cargando datasets...  {}'.format(ETL_ROUTE() + 'RawFiles'))
    # content = os.listdir(path_dir)
    # datasets_excel = []
    # for file in content:
    #     if os.path.isfile(os.path.join(path_dir, file)) and file.endswith('.xlsx'):
    #         datasets_excel.append(file)
    # print(datasets_excel)
    # content = os.listdir(ETL_ROUTE() + 'RawFiles/')
    # logging.info('Iniciando transformación...  {}'.format(host))
    # logger.info('Archivos exportados correctamente - Status OK')

def _clean_dataset(filename, path_dir):
    # Call job transformation
    labels_name = filename.replace('ds','labels')
    dataset = filename 
    logging.info('Iniciando transformación...  ')
    process = trf.Transform(filename,path_dir)
    # Start TRF
    process.load_labels(labels_name)
    process.load_dataset()
    process.missing_data()
    process.null_handling_values()
    logging.info('Eliminando duplicados y llenando nulos')
    process.fill_null_values()
    df = process.get_clean_dataset()
    logger.info('Exportando dataset limpio ...')
    # export excel
    csv_filename =   'clean_ds'+ aux_func.AuxiliarFunctions().format_date() + '.csv'# clean
    path_csv_file = path_dir + '/' + csv_filename

    df.to_csv(path_csv_file, index=False, encoding='utf-8')
    logger.info('Dataset {} exportado correctamente.'.format(csv_filename))
    


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
