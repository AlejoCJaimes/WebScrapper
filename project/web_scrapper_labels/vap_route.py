import os
import re
__PROJECT_ROUTE = None
__ROOT_RUOUTE = None
__ETL_ROUTE = None
__CREDENTIALS_ROUTE = None
__CONFIG_ROUTE = None


def ROOT_RUOUTE():
    global __ROOT_RUOUTE
    root_route = (os.path.dirname(os.path.realpath(__file__)))
    pattern = re.compile(r'(^/.+)$')
    __ROOT_RUOUTE = "".join(pattern.findall(root_route, 0, 28))
    return __ROOT_RUOUTE


def PROJECT_ROUTE():
    global __PROJECT_ROUTE
    root_route = (os.path.dirname(os.path.realpath(__file__)))
    pattern = re.compile(r'(/.+)')
    __PROJECT_ROUTE = "".join(pattern.findall(root_route, 27))
    return __PROJECT_ROUTE + '/'


def ETL_ROUTE():
    global __ETL_ROUTE
    root_route = (os.path.dirname(os.path.realpath(__file__)))
    pattern = re.compile(r'(/.+)')
    __ETL_ROUTE = "".join(pattern.findall(root_route, 27, 48))
    return __ETL_ROUTE + 'ETL' + '/'


def CREDENTIALS_ROUTE():
    global __CREDENTIALS_ROUTE
    root_route = (os.path.dirname(os.path.realpath(__file__)))
    pattern = re.compile(r'(/.+)')
    __CREDENTIALS_ROUTE = "".join(pattern.findall(root_route, 27, 48))
    return __CREDENTIALS_ROUTE + 'Acc.txt'


def CONFIG_ROUTE():
    global __CONFIG_ROUTE
    root_route = (os.path.dirname(os.path.realpath(__file__)))
    pattern = re.compile(r'(/.+)')
    __CONFIG_ROUTE = "".join(pattern.findall(root_route))
    return __CONFIG_ROUTE + '/config.yaml'

