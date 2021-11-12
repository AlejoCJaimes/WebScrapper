import os


def load_dataset_dirty():
    path = '/home/alev/personalProjects//WebScrapper/project/ETL/RawFiles'
    contenido = os.listdir(path)
    datasets_excel = []
    size_files = []
    for fichero in contenido:
        if os.path.isfile(os.path.join(path, fichero)) and fichero.endswith('.xlsx'):
            datasets_excel.append(fichero)
            size_files.append(convert_bytes(os.path.getsize(path + '/' + fichero),'MB'))
    print(datasets_excel, size_files)
    
def convert_bytes(size, unit=None):
    if unit == "KB":
        return str(round(size / 1024, 3)) + 'KB'
    elif unit == "MB":
        return  str(round(size / (1024 * 1024), 3)) + ' MB'
    elif unit == "GB":
        return  str(round(size / (1024 * 1024 * 1024), 3)) + ' GB'
    else:
        return  str(size) + ' bytes'

load_dataset_dirty()