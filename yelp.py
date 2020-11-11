import traceback
import requests
import logging
from bs4 import BeautifulSoup
from config import *
from utils import get_request_headers, csv_write


class Yelp(object):

    def __init__(self):
        super(Yelp, self).__init__()

    def scrap_yelp(self, url, scrap_type):
        logging.info("\nScrapping Yelp Url: %s \n" % url)

        r = requests.get(url, headers=get_request_headers())

        if not r.status_code == 200:
            logging.error("Failed to get content of url: %s" % url)
            return

        html_doc = r.content
        soup = BeautifulSoup(html_doc, 'html.parser')

        li_class = "regular-search-result"

        # parsing html content to fet information about dry cleaners
        for li in soup.find_all('li', class_=li_class):
            try:
                self.scrap_row_yelp(li, scrap_type)
            except Exception as exp:
                logging.error("scrap_yelp() :: Got exception: %s" % exp)
                logging.error(traceback.format_exc())

            # break  # just use it for testing only

    def scrap_row_yelp(self, li, scrap_type):

        h3 = li.find('h3', class_='search-result-title')

        #################################
        # Getting title                 #
        #################################
        title = ''
        spans = h3.find_all('span')
        i = 0
        for span in spans:
            i += 1
        if i == 2:
            title = span.text.strip()

        logging.info("title: %s" % title)

        ##################################
        #  Getting reviews count         #
        ##################################
        reviews_count = 0
        span = li.find('span', class_='review-count rating-qualifier')
        text = span.text
        lst = text.split()
        reviews_count = int(lst[0])

        logging.info("reviews count: %d" % reviews_count)

        ##################################
        # Getting services               #
        ##################################
        services = []
        span = li.find('span', class_='category-str-list')
        text = span.text
        lst = text.split(',')
        services = [itm.strip() for itm in lst]

        logging.info("services: %s" % services)

        #################################
        #  Getting address	            #
        #################################
        address = li.find('address').text.strip()

        logging.info("address: %s" % address)

        #################################
        # Getting phone  	            #
        #################################
        phone = li.find('span', class_='biz-phone').text.strip()

        logging.info("phone: %s" % phone)

        #################################
        #   Getting snippet             #
        #################################
        p = li.find('p', class_='snippet').text.strip()

        lst = p.split('read more')
        snippet = lst[0].strip()

        logging.info("snippet: %s" % snippet)

        # saving data in csv
        data_src = 'yelp'
        if scrap_type == ST_DRY_CLEANERS:
            msg = "%s,%s,%s,%s,%s,%s,%s,%s" % (title, reviews_count,
                                               services, address, phone,
                                               snippet, data_src, CITY)
            logging.info("add_dry_cleaner() :: msg:", msg)
            csv_write(CSV_DRY_CLEANERS, msg)
        elif scrap_type == ST_SHOE_REPAIR:
            msg = "%s,%s,%s,%s,%s,%s,%s,%s" % (title, reviews_count,
                                               services,
                                               address, phone,
                                               snippet, data_src, CITY)
            logging.info("add_shoe_rapair_company() :: msg:", msg)
            csv_write(CSV_SHOE_REPAIR, msg)
