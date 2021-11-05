# Representa la página principal de la web
import requests
import bs4
from common import config


class HomePage:
    def __init__(self, data_site_uid, url):
        self._config = config()['data_sites'][data_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self._visit(url)

    #generate propertys -> page object pattern
    @property
    def page_labels(self):
        label_list = []
        for label in self._select(self._queries['homepage_page_labels']):
            if label and label.has_attr('href'):
                label_list.append(label)
        return set(label['href'] for label in label_list)

    def select(self, query_string):
        return self._html.select(query_string)
    
    def _visit(self, url):
        response = requests.get(url)
        response.raise_for_status() # levantar un error, si no sucedió correctamente
        self._html = bs4.BeautifulSoup(response.text, 'html.parser')