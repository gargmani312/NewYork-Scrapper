"""
Scrapper for fetching data from various sources like yelp etc
"""

import os
import traceback
import logging
from multiprocessing import Process
from config import *
from yelp import Yelp
from yellowpages import YellowPages
from groupon import Groupon
from craiglist import Craiglist
from utils import sleep_scrapper, txt_write


class Scrapper(object):

    def __init__(self):
        super(Scrapper, self).__init__()
        self.yelp = Yelp()
        self.yellowpages = YellowPages()
        self.groupon = Groupon()
        self.craiglist = Craiglist()

    #####################################
    #           Shoe Repair             #
    #####################################
    def srap_yelp_shoe_repair(self):
        """
        Scrap shoe repair data from Yelp
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = "%s/%s" % (dir_path, PROGRESS_YELP_SHOE_REPAIR_FILE)

        if not os.path.isfile(file_data):
            logging.error("Error: %s file not found" % file_data)
            txt_write(PROGRESS_YELP_SHOE_REPAIR_FILE, "1")

        logging.info("file is exist %s ..." % file_data)
        f = open(PROGRESS_YELP_SHOE_REPAIR_FILE, "r")
        i = int(f.readline())

        logging.info(
            "\n\nYelp-Shoe-Repair-Scrapper started at i: %d \n\n" % i
        )

        base_url = "https://www.yelp.com/search?find_desc" \
                   "=Shoe+repair&find_loc=New+York,+NY&start="

        for j in range(i, 820, 10):
            try:
                yelp_url = base_url + str(j)
                self.yelp.scrap_yelp(yelp_url, ST_SHOE_REPAIR)

                # progress of yelp_shoe_repair scrapping %
                percentage = float(j * 100 / 820)
                logging.info(
                    "\n\nYelp-Shoe-Repair-Scrapper %f percent "
                    "completed" % percentage
                )

                # update scrapping progress in yelp_shoe_repair progress file
                txt_write(PROGRESS_YELP_SHOE_REPAIR_FILE, str(j))

                # sleep scrapper for a while
                sleep_scrapper("Yelp-Shoe-Repair-Scrapper")
            except Exception as exp:
                logging.error(
                    "srap_yelp_shoe_repair() :: Got exception: %s" % exp
                )
                logging.error(traceback.format_exc())

    def scrap_yellowpages_shoe_repair(self):
        """
        Scrap shoe repair data from yellow pages
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = "%s/%s" % (
            dir_path,
            PROGRESS_YELLOWPAGES_SHOE_REPAIR_FILE
        )

        if not os.path.isfile(file_data):
            logging.error("Error: %s file not found" % file_data)
            txt_write(PROGRESS_YELLOWPAGES_SHOE_REPAIR_FILE, "1")

        logging.info("file is exist %s ..." % file_data)
        f = open(PROGRESS_YELLOWPAGES_SHOE_REPAIR_FILE, "r")
        i = int(f.readline())

        logging.info(
            "\n\nYellowpages-Shoe-Repair-Scrapper started at i: %d \n\n" % i
        )

        base_url = "https://www.yellowpages.com/search?" \
                   "search_terms=Shoe%20Repair" \
                   "&geo_location_terms=New%20York%2C%20NY&page="

        for j in range(i, 30, 1):
            try:
                yellowpages_url = base_url + str(j)
                self.yellowpages.scrap_yellowpages(yellowpages_url,
                                                   ST_SHOE_REPAIR)

                # progress of yellowpages_shoe_repair scrapping %
                percentage = float(j * 100 / 30)

                logging.info(
                    "\n\nYellowPages-Shoe-Repair-Scrapper %f percent "
                    "completed" % percentage
                )

                # update scrapping progress in
                # yellowpages_shoe_repair progress file
                txt_write(PROGRESS_YELLOWPAGES_FILE, str(j))

                # sleep scrapper for a while
                sleep_scrapper("YellowPages-Shoe-Repair-Scrapper")
            except Exception as exp:
                logging.error(
                    "scrap_yellowpages_shoe_repair() :: "
                    "Got Exception : %s" % exp
                )
                logging.error(traceback.format_exc())

    def scrap_groupon_shoe_repair(self):
        """
        Scrap shoe repair data from groupon
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = "%s/%s" % (dir_path, PROGRESS_GROUPON_SHOE_REPAIR_FILE)

        # if progress file is not found,
        # create a new one with default value 1
        if not os.path.isfile(file_data):
            logging.error("Error: %s file not found" % file_data)
            txt_write(PROGRESS_GROUPON_SHOE_REPAIR_FILE, "1")

        logging.info("file is exist %s ..." % file_data)
        f = open(PROGRESS_GROUPON_FILE, "r")
        i = int(f.readline())

        logging.info(
            "\n\nGroupon-Shoe-Repair-Scrapper started at i: %d \n\n" % i
        )

        base_url = "https://www.groupon.com/browse/chicago?" \
                   "lat=41.8795&lng=-87.6243&address=Chicago&query=" \
                   "new+york+shoe+repair&locale=en_US"

        for j in range(i, 400, 1):
            try:
                groupon_url = base_url + str(j)
                self.groupon.scrap_groupon(groupon_url, ST_SHOE_REPAIR)

                # progress of groupon_shoe_repair scrapping %
                percentage = float(j * 100 / 400)
                logging.info(
                    "\n\nGroupon-Shoe-Repair-Scrapper %f percent "
                    "completed" % percentage
                )

                # update scrapping progress in
                # groupon_shoe_repair progress file
                txt_write(PROGRESS_GROUPON_FILE, str(j))

                # sleep scrapper for a while
                sleep_scrapper("Groupon-Shoe-Repair-Scrapper")
            except Exception as exp:
                logging.error(
                    "scrap_groupon_shoe_repair() :: Got Exception : %s" % exp
                )
                logging.error(traceback.format_exc())

    def scrap_cragilist_shoe_repair(self):
        """
        Scrap shoe repair data from cragilist
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = "%s/%s" % (dir_path, PROGRESS_CRAIGLIST_SHOE_REPAIR_FILE)

        # if progress file is not found,
        # create a new one with default value 1
        if not os.path.isfile(file_data):
            logging.error("Error: %s file is not found" % file_data)
            txt_write(PROGRESS_CRAIGLIST_SHOE_REPAIR_FILE, "1")

        logging.info("file is exist %s ..." % file_data)
        f = open(PROGRESS_CRAIGLIST_SHOE_REPAIR_FILE, "r")
        i = int(f.readline())

        logging.info("\n\nCraiglist-Dry-Cleaner started at i: %d \n\n" % i)

        base_url = "https://newyork.craigslist.org/search" \
                   "/sss?query=shoe+repair&sort=rel"

        for j in range(i, 90, 1):
            try:
                craiglist_url = base_url + str(i)
                self.craiglist.scrap_craiglist(craiglist_url, ST_SHOE_REPAIR)

                # progress of craiglist_shoe_repair scrapping %
                percentage = float(j * 100 / 90)
                logging.info(
                    "\n\nCraiglist-Shoe-Repair-Scrapper %f "
                    "percent completed" % percentage
                )

                # update scrapping progress in
                # craiglist_shoe_repair progress file
                txt_write(PROGRESS_CRAIGLIST_SHOE_REPAIR_FILE, str(j))

                # sleep scrapper for a while
                sleep_scrapper("Craiglist-Shoe-Repair-Scrapper")
            except Exception as exp:
                logging.error(
                    "scrap_shoe_rapair_companies() :: "
                    "Got Exception : %s" % exp
                )
                logging.error(
                    traceback.format_exc()
                )

    #####################################
    #           Dry Cleaner             #
    #####################################
    def scrap_yelp_dry_cleaners(self):
        """
        Scrap dry cleaners data from yelp
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = "%s/%s" % (dir_path, PROGRESS_YELP_FILE)

        # if progress file is not found,
        # create a new one with default value 10
        if not os.path.isfile(file_data):
            logging.error("Error: %s file not found" % file_data)
            print("Error: %s file not found" % file_data)
            txt_write(PROGRESS_YELP_FILE, "10 ")

        logging.info("file is exist %s ..." % file_data)
        print("file is exist %s ..." % file_data)
        f = open(PROGRESS_YELP_FILE, "r")
        i = int(f.readline())

        logging.info(
            "\n\nYelp-Dry-Cleaner-Scrapper started at i: %d \n\n" % i
        )
        print("\n\nYelp-Dry-Cleaner-Scrapper started at i: %d \n\n" % i)

        base_url = "https://www.yelp.com/search?find_desc" \
                   "=Dry+Cleaners&find_loc=New+York%2C+NY&start="

        for j in range(i, 1000, 10):
            try:
                yelp_url = base_url + str(j)
                self.yelp.scrap_yelp(yelp_url, ST_DRY_CLEANERS)

                # progress % of yelp_dry_cleaner scrapping
                percentage = float(j * 100 / 1000)
                logging.info(
                    "\n\nYelp-Dry-Cleaner-Scrapper %f "
                    "percent completed" % percentage
                )
                print(
                    "\n\nYelp-Dry-Cleaner-Scrapper %f "
                    "percent completed" % percentage
                )
                # update scrapping progress in yelp_dry_cleaner progress file
                txt_write(PROGRESS_YELP_FILE, str(j))

                # sleep scrapper for a while
                sleep_scrapper("Yelp-Dry-Cleaner-Scrapper")
            except Exception as exp:
                logging.error(
                    "scrap_yelp_dry_cleaners() :: Got Exception : %s" % exp
                )
                logging.error(
                    traceback.format_exc()
                )

    def scrap_yellowpages_dry_cleaner(self):
        """
        Scrap dry cleaners data from yellow pages
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = "%s/%s" % (dir_path, PROGRESS_YELLOWPAGES_FILE)

        # if progress file is not found,
        # create a new one with default value 1
        if not os.path.isfile(file_data):
            logging.error("Error: %s file not found" % file_data)
            print("Error: %s file not found" % file_data)
            txt_write(PROGRESS_YELLOWPAGES_FILE, "1")

        logging.info("file is exist %s ..." % file_data)
        print("file is exist %s ..." % file_data)
        f = open(PROGRESS_YELLOWPAGES_FILE, "r")
        i = int(f.readline())

        logging.info(
            "\n\nYellowPages-Dry-Cleaner-Scrapper started at i: %d \n\n" % i
        )
        print("\n\nYellowPages-Dry-Cleaner-Scrapper started at i: %d \n\n" % i)

        base_url = "https://www.yellowpages.com/" \
                   "new-york-ny/dry-cleaners-laundries?page="

        for j in range(i, 86, 1):
            try:
                yellowpages_url = base_url + str(j)
                self.yellowpages.scrap_yellowpages(yellowpages_url,
                                                   ST_DRY_CLEANERS)

                # progress % of yellowpages_dry_cleaner scrapping
                percentage = float(j * 100 / 86)
                logging.info(
                    "\n\nYellowPages-Dry-Cleaner-Scrapper %f "
                    "percent completed" % percentage
                )
                print(
                    "\n\nYellowPages-Dry-Cleaner-Scrapper %f "
                    "percent completed" % percentage
                )

                # update scrapping progress in
                # yellowpages_dry_cleaner progress file
                txt_write(PROGRESS_YELLOWPAGES_FILE, str(j))

                # sleep scrapper for a while
                sleep_scrapper("YellowPages-Dry-Cleaner-Scrapper")
            except Exception as exp:
                logging.error(
                    "scrap_yellowpages_dry_cleaner() :: "
                    "Got Exception : %s" % exp
                )
                logging.error(
                    traceback.format_exc()
                )

    def scrap_groupon_dry_cleaner(self):
        """
        Scrap dry cleaners data from groupon
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = "%s/%s" % (dir_path, PROGRESS_GROUPON_FILE)

        # if progress file is not found,
        # create a new one with default value 1
        if not os.path.isfile(file_data):
            logging.error("Error: %s file not found" % file_data)
            print(
                "Error: %s file not found" % file_data
            )
            txt_write(PROGRESS_GROUPON_FILE, "1")

        logging.info("file is exist %s ..." % file_data)
        print(
            "file is exist %s ..." % file_data
        )
        f = open(PROGRESS_GROUPON_FILE, "r")
        i = int(f.readline())

        logging.info(
            "\n\nGroupon-Dry-Cleaner-Scrapper started at i: %d \n\n" % i
        )
        print(
            "\n\nGroupon-Dry-Cleaner-Scrapper started at i: %d \n\n" % i
        )

        base_url = "https://www.groupon.com/browse/chicago?" \
                   "lat=41.8795&lng=-87.6243&address=Chicago&query=" \
                   "dry+cleaners&locale=en_US&page="

        for j in range(i, 16, 1):
            try:
                groupon_url = base_url + str(j)
                self.groupon.scrap_groupon(groupon_url, ST_DRY_CLEANERS)

                # progress % of groupon_dry_cleaner scrapping
                percentage = float(j * 100 / 15)
                logging.info(
                    "\n\nGroupon-Dry-Cleaner-Scrapper %f "
                    "percent completed" % percentage
                )
                print(
                    "\n\nGroupon-Dry-Cleaner-Scrapper %f "
                    "percent completed" % percentage
                )

                # update scrapping progress in
                # groupon_dry_cleaner progress file
                txt_write(PROGRESS_GROUPON_FILE, str(j))

                # sleep scrapper for a while
                sleep_scrapper("Groupon-Dry-Cleaner-Scrapper")
            except Exception as exp:
                logging.error(
                    "scrap_groupon_dry_cleaner() :: Got Exception : %s" % exp
                )
                logging.error(
                    traceback.format_exc()
                )

    def scrap_craiglist_dry_cleaner(self):
        """
        Scrap dry cleaners data from craiglist
        :return:
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_data = "%s/%s" % (dir_path, PROGRESS_CRAIGLIST_FILE)

        # if progress file is not found,
        # create a new one with default value 1
        if not os.path.isfile(file_data):
            logging.error("Error: %s file is not found" % file_data)
            print(
                "file is exist %s ..." % file_data
            )
            txt_write(PROGRESS_CRAIGLIST_FILE, "1")

        logging.info("file is exist %s ..." % file_data)
        print(
            "file is exist %s ..." % file_data
        )
        f = open(PROGRESS_CRAIGLIST_FILE, "r")
        i = int(f.readline())

        logging.info(
            "\n\nCraiglist-Dry-Cleaner started at i: %d \n\n" % i
        )
        print(
            "\n\nCraiglist-Dry-Cleaner started at i: %d \n\n" % i
        )

        base_url = "https://newyork.craigslist.org/" \
                   "search/sss?query=dry%20cleaner&sort=rel"

        for j in range(i, 89, 1):
            try:
                craiglist_url = base_url + str(j)
                self.craiglist.scrap_craiglist(craiglist_url, ST_DRY_CLEANERS)

                # progress % of craiglist_dry_cleaner scrapping
                percentage = float(j * 100 / 89)
                logging.info(
                    "\n\nCraiglist-Dry-Cleaner-Scrapper %f "
                    "percent completed" % percentage
                )
                print(
                    "\n\nCraiglist-Dry-Cleaner-Scrapper %f "
                    "percent completed" % percentage
                )

                # update scrapping progress in
                # craiglist_dry_cleaner progress file
                txt_write(PROGRESS_CRAIGLIST_FILE, str(j))

                # sleep scrapper for a while
                sleep_scrapper("Craiglist-Dry-Cleaner-Scrapper")
            except Exception as exp:
                logging.error(
                    "scrap_craiglist_dry_cleaner() :: "
                    "Got Exception : %s" % exp
                )
                logging.error(
                    traceback.format_exc()
                )

    def dry_cleaner_processing(self):
        """
        Start Dry Cleaner Processing
        """

        ########################################
        #        dry_cleaner_processing        #
        ########################################
        yelp_dry_cleaner_processing = Process(
            target=self.scrap_yelp_dry_cleaners)
        yelp_dry_cleaner_processing.start()

        yellowpages_dry_cleaner_processing = Process(
            target=self.scrap_yellowpages_dry_cleaner)
        yellowpages_dry_cleaner_processing.start()

        groupon_dry_cleaner_processing = Process(
            target=self.scrap_groupon_dry_cleaner)
        groupon_dry_cleaner_processing.start()

    def shoe_repair_processing(self):
        """
        Start Shoe Repair Processing
        """
        ########################################
        #       shoe_repair_processing         #
        ########################################
        yelp_shoe_repair_processing = Process(
            target=self.srap_yelp_shoe_repair)
        yelp_shoe_repair_processing.start()

        yellowpages_shoe_repair_processing = Process(
            target=self.scrap_yellowpages_shoe_repair)
        yellowpages_shoe_repair_processing.start()

        groupon_shoe_repair_processing = Process(
            target=self.scrap_groupon_shoe_repair)
        groupon_shoe_repair_processing.start()


if __name__ == "__main__":
    scrapper = Scrapper()
    scrapper.dry_cleaner_processing()
    scrapper.shoe_repair_processing()
