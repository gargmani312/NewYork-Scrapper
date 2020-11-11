import traceback
import requests
import logging
from bs4 import BeautifulSoup
from config import *
from utils import get_request_headers, csv_write


class Groupon(object):
    def __init__(self):
        super(Groupon, self).__init__()
        # self.mdb = Mdb()
        pass

    def scrap_groupon(self, url, scrap_type):
        logging.info("\n=======> Scrapping Groupon Url: %s \n" % url)

        r = requests.get(url, headers=get_request_headers())
        if not r.status_code == 200:
            logging.error(
                "scrap_groupon() :: Failed to get content of url: %s" % url
            )
            return

        html_doc = r.content
        soup = BeautifulSoup(html_doc, 'html.parser')

        div_class = "cui-content c-bdr-gray-clr ch-bdr-gray-md"

        # parsing html content to fet information about dry cleaners
        for div in soup.find_all('div', class_=div_class):
            try:
                self.scrap_row_groupon(div, scrap_type)
            except Exception as exp:
                logging.error("scrap_groupon() :: Got exception: %s" % exp)
                logging.error(traceback.format_exc())
            # break

    def scrap_row_groupon(self, div, scrap_type):

        #################################
        #  off percentage  	            #
        #################################
        off_percentage = ''
        data = div.find('div', class_='cui-udc-title-with-'
                                      'subtitle c-txt-black one-line-truncate')
        if data:
            off_percentage = data.text.strip()
            logging.info(
                "scrap_row_groupon() :: off_percentage: %s" % off_percentage
            )
        else:
            logging.info("scrap_row_groupon() :: off percentage: %s" % data)

        #################################
        #  title          	            #
        #################################
        title = ''
        sub = div.find('div', class_='cui-udc-subtitle c-txt-gray-dk')
        if sub:
            title = sub.text.strip()
            logging.info("scrap_row_groupon() :: title: %s" % title)
        else:
            logging.info("scrap_row_groupon() :: title: %s" % sub)

        #################################
        #  location      	            #
        #################################
        location = ''
        span = div.find('span', class_='cui-location-name')
        if span:
            location = span.text.strip()
            logging.info("scrap_row_groupon() :: location: %s" % location)
        else:
            logging.info("scrap_row_groupon() :: location: %s" % span)

        #################################
        #  locations distance           #
        #################################
        location_distance = ''
        span = div.find('span', class_='cui-location-distance')
        if span:
            location_distance = span.text.strip()
            logging.info(
                "scrap_row_groupon() :: location_distance: "
                "%s" % location_distance
            )
        else:
            logging.info(
                "scrap_row_groupon() :: location_distance: %s" % span
            )

        #################################
        #  quantity_bought              #
        #################################
        quantity = ''
        div = div.find('div', class_='cui-quantity-bought c-txt-gray-dk')
        if div:
            quantity = div.text.strip()
            logging.info(
                "scrap_row_groupon() :: quantity_bought: %s" % quantity
            )
        else:
            logging.info("scrap_row_groupon() :: quantity_bought: %s" % div)

        # saving data in csv
        data_src = 'groupon'
        if scrap_type == ST_DRY_CLEANERS:
            msg = "%s,%s,%s,%s,%s,%s,%s" % (off_percentage, title,
                                            location, location_distance,
                                            quantity,
                                            data_src, CITY)
            logging.info("add_groupon_dry_cleaner() :: msg:", msg)
            csv_write(CSV_DRY_CLEANERS, msg)
        elif scrap_type == ST_SHOE_REPAIR:
            msg = "%s,%s,%s,%s,%s,%s,%s" % (off_percentage, title,
                                            location, location_distance,
                                            quantity,
                                            data_src, CITY)
            logging.info("add_groupon_shoe_rapair() :: msg:", msg)
            csv_write(CSV_SHOE_REPAIR, msg)


if __name__ == '__main__':
    logging.info("Testing Groupon Scrapper")
    groupon = Groupon()
    groupon.scrap_groupon()
    logging.info("Testing Done !!!")
