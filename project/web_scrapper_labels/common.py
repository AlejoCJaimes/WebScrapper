import yaml

__config = None #Cachea nuestrar configuracion

def config():
    global __config
    if not __config:
         with open('/home/alev/personalProjects/WebScrapper/project/web_scrapper_labels/config.yaml',mode = 'r') as f:
             __config =yaml.safe_load(f)

    return __config