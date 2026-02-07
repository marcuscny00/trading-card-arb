from scraping.base_scraper import load_sites_config
from scraping.yuyutei_parser import yuyutei_parser

# read yamls and get list of urls
sites_config = load_sites_config()

# fetch htmls according to site

for site, site_data in sites_config['sites'].items():
    if site == 'yuyutei':
        yuyutei_cards = yuyutei_parser(site_data['urls'])


# results