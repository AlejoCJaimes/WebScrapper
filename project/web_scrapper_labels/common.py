import yaml
from vap_route import CONFIG_ROUTE
__config = None #Cachea nuestrar configuracion

def config():
    global __config
    if not __config:
         with open(CONFIG_ROUTE(),mode = 'r') as f:
             __config =yaml.safe_load(f)

    return __config