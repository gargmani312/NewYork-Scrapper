import traceback
import requests
from bs4 import BeautifulSoup
import logging
from config import *
from utils import get_request_headers, csv_write


class YellowPages(object):

    def __init__(self):
        super(YellowPages, self).__init__()

    def scrap_yellowpages(self, url, scrap_type):

        logging.info("\nScrapping YellowPages Url: %s\n" % url)

        r = requests.get(url, headers=get_request_headers())

        if not r.status_code == 200:
            logging.error("Failed to get content of url: %s" % url)
            return

        html_doc = r.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        div_class = "info"
        for div in soup.find_all('div', class_=div_class):
            try:
                self.scrap_row_yellowpages(div, scrap_type)
            except Exception as exp:
                logging.error("scrap_yellowpages() :: Got exception: %s" % exp)
                logging.error(traceback.format_exc())
            # break

    def scrap_row_yellowpages(self, div, scrap_type):
        h2 = div.find('h2', class_='n')

        ####################################
        #         Getting title            #
        ####################################
        title = div.find('a', class_='business-name').text.strip()

        logging.info("title: %s" % title)

        ####################################
        #         Getting rating           #
        ####################################
        rating_count = 0
        span = div.find('span', class_='count')

        if span:
            span = span.text.strip()
            rating_count = span  # FIXME convert to
            # int, (2) was giving exception !!!

        logging.info("rating_count: %s" % rating_count)

        ####################################
        #         Getting address          #
        ####################################
        p = div.find('p', class_='adr')
        address = p.text
        logging.info("address: %s" % address)

        ####################################
        #         Getting phones           #
        ####################################
        phone = ''
        li = div.find('li', class_='phone primary')
        if li:
            phone = li.text.strip()
            logging.info("phone: %s" % phone)
        else:
            logging.info("phone: %s" % li)

        ####################################
        #         Getting categories       #
        ####################################
        categories = ''
        cat_div = div.find('div', class_='categories')
        if cat_div:
            categories = cat_div.text.strip()
            logging.info("categories: %s" % categories)
        else:
            logging.info("categories: %s" % cat_div)

        services = []

        # saving data in csv
        data_src = 'yellowpages'
        if scrap_type == ST_DRY_CLEANERS:
            msg = "%s,%s,%s,%s,%s,%s,%s,%s" % (title, rating_count,
                                               services, address, phone,
                                               categories, data_src, CITY)
            logging.info("add_dry_cleaner() :: msg:", msg)
            csv_write(CSV_DRY_CLEANERS, msg)
        elif scrap_type == ST_SHOE_REPAIR:
            msg = "%s,%s,%s,%s,%s,%s,%s,%s" % (title, rating_count,
                                               services,
                                               address, phone,
                                               categories, data_src, CITY)
            logging.info("add_shoe_rapair_company() :: msg:", msg)
            csv_write(CSV_SHOE_REPAIR, msg)
