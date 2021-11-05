import argparse
import logging

from common import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _news_scraper(news_site_uid):
    host = config()['data_sites'][news_site_uid]['url']
    logging.info('Inicilializando scraper para {}'.format(host))

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
    _news_scraper(args.data_sites)

# import argparse
# import logging
# logging.basicConfig(level=logging.INFO)
# from common import config

# logger = logging.getLogger(__name__)


# def _labels_scraper(site_uid):
#     host = config()['sites'][site_uid]['url']
#     logging.info('Inicilializando scraper para {}'.format(host))

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     new_sites_choices = list(config()['sites'].keys())
#    # new_sites_choices = list(config()['news_sites'].keys())
#     parser.add_argument('sites',help='Los labels del sitio a scrapear',type=str,choices=new_sites_choices)

#     args = parser.parse_args()
#     _labels_scraper(args.sites)