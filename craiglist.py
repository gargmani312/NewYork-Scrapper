import traceback
import requests
import logging
from bs4 import BeautifulSoup
from config import *
from utils import get_request_headers, csv_write


class Craiglist(object):

    def __init__(self):
        super(Craiglist, self).__init__()

    def scrap_craiglist(self, base_url, scrap_type):
        i = 1
        while i < 90:
            url = base_url + str(i)
            logging.info("\nScrapping CraigList Url: %s \n" % url)

            r = requests.get(url, headers=get_request_headers())
            # print "<<======content is: >>", r
            if not r.status_code == 200:
                logging.error("Failed to get content of url: %s" % url)
                return

            html_doc = r.content
            soup = BeautifulSoup(html_doc, 'html.parser')

            # print(soup.prettify())
            li_class = "result-row"

            # parsing html content to fet information about dry cleaners
            for li in soup.find_all('li', class_=li_class):
                try:
                    # print "<<=======li====>>", li
                    self.scrap_row_craiglist(li, scrap_type)
                    # self.scrap_row_craiglist(li)
                except Exception as exp:
                    logging.error("scrap_groupon() :: Got exception: %s" % exp)
                    logging.error(traceback.format_exc())
                # break
            i = i+1
            # break

    def scrap_row_craiglist(self, li, scrap_type):

        ##############################
        #        date                #
        ##############################
        date = li.find('time', class_='result-date').text.strip()
        logging.info("date: %s" % date)

        ##############################
        #       title                #
        ##############################
        title = li.find('a', class_='result-title hdrlnk').text.strip()
        logging.info("title: %s" % title)

        ##############################
        #       price                #
        ##############################
        price = ''
        cost = li.find('span', class_='result-price')
        if cost:
            price = cost.text.strip()
            logging.info("price: %s" % price)
        else:
            logging.info("price: %s" % cost)

        ##############################
        #      nearby                #
        ##############################
        nearby = ''
        by = li.find('span', class_='nearby')
        if by:
            nearby = by.text.strip()
            logging.info("nearby: %s" % nearby)
        else:
            logging.info("nearby: %s" % by)

        # saving data in csv
        data_src = 'craiglist'
        if scrap_type == ST_DRY_CLEANERS:
            msg = "%s,%s,%s,%s,%s,%s" % (date, title,
                                         price, nearby,
                                         data_src, CITY)
            logging.info("add_craiglist_shoe_repair() :: msg:", msg)
            csv_write(CSV_SHOE_REPAIR, msg)
        elif scrap_type == ST_SHOE_REPAIR:
            msg = "%s,%s,%s,%s,%s,%s" % (date, title,
                                         price, nearby,
                                         data_src, CITY)
            logging.info("add_craiglist_dry_cleaner() :: msg:", msg)
            csv_write(CSV_DRY_CLEANERS, msg)


if __name__ == '__main__':
    craiglist = Craiglist()
    craiglist.scrap_craiglist()
