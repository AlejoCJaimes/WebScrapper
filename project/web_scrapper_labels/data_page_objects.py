# Representa la página principal de la web
import requests
import bs4
import json
import os
from common import config
from vap_route import ROOT_RUOUTE
from vap_route import PROJECT_ROUTE


class HomePage:
    def __init__(self, data_site_uid, url):
        self._config = config()['data_sites'][data_site_uid]
        self._sodaQueries = '$limit=1'
        self._html = None
        self._path = None
        self._path_relative_project = None
        self._name_file = None
        self._visit(url)

    #generate propertys -> page object pattern
    @property
    def page_labels(self):
        return self._html
    
    @property
    def save_json_labels(self):
        self._name_file = 'unstructured_labels.json'
        self._path = ROOT_RUOUTE() + PROJECT_ROUTE() + self._name_file
        self._path_relative_project = PROJECT_ROUTE()
        with open(self._path, 'w') as json_file:
            json.dump(self._html.text,json_file)
        return self._path
    
    
    def _visit(self, url):
        response = requests.get(url + self._sodaQueries)
        response.raise_for_status() # levantar un error, si no sucedió correctamente
        self._html = bs4.BeautifulSoup(response.text, 'html.parser')
        
    