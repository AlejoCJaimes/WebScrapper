import sys
import os
import errno
sys.path.append('.')

from web_scrapper_labels.vap_route import CREDENTIALS_ROUTE
from web_scrapper_labels.vap_route import ROOT_RUOUTE

class Credentials:
    def __init__(self):
        self._username = None
        self._passwd = None
        self._app_token = None

    def ext(self):
        with open(ROOT_RUOUTE()[:-1]+CREDENTIALS_ROUTE(), 'r') as f:
            data = f.read()
        res = [x.strip() for x in data.split(',')]
        self._username = res[0]
        self._passwd = res[1]
        self._app_token = res[2]
        return self._app_token, self._username, self._passwd
