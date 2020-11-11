#
# script for helper/utility functions
#

from random import randint
from config import SCRAPPER_SLEEP_MIN, SCRAPPER_SLEEP_MAX
import time
import logging


def get_request_headers():
    """
    Function returns header for HTTP request

    Each call to this function has a User-Agent
    in header
    """

    # FIXME add more agent names later !!!
    agents = ['Mozilla/5.0', 'Safari/533.1', 'Chrome/33.0.1750.117']

    return {'User-Agent': agents[randint(0, len(agents)-1)]}


def get_rand_in_range(min, max):
    return randint(min, max)


def get_scrapper_sleep():
    return get_rand_in_range(SCRAPPER_SLEEP_MIN, SCRAPPER_SLEEP_MAX)


def sleep_scrapper(scrapper_name):
    val = get_scrapper_sleep()
    logging.info("\n\n[%s] SLEEPING %d seconds...\n\n" % (scrapper_name, val))
    print("\n\n[%s] SLEEPING %d seconds...\n\n" % (scrapper_name, val))
    time.sleep(val)
    logging.info("\n\n[%s] RESUMED \n\n" % scrapper_name)
    print("\n\n[%s] RESUMED \n\n" % scrapper_name)


def csv_write(fname, msg):
    msg = msg.encode("utf-8")

    """
    with open(fname, "a") as csv_file:
        writer = csv.writer(csv_file)3
        writer.writerow(row)
    """

    f = open(fname, "a")
    f.write("%s\n" % msg)
    f.close()


def txt_write(fname, msg):
    msg = msg.encode("utf-8")
    f = open(fname, "w")
    f.write("%s" % msg)
    f.close()


if __name__ == "__main__":

    for i in range(0, 20):
        logging.info(get_request_headers())

    # test random numbers in range
    logging.info("random: ", get_rand_in_range(50, 150))
    logging.info("random: ", get_rand_in_range(100, 200))

    for i in range(0, 10):
        logging.info("Scrapper Sleep:", get_scrapper_sleep())
