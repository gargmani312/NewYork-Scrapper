#
# config/settings for scrapper
#

DB_HOST = '127.0.0.1'
DB_PORT = 27017

# authorization database used to authenticate username/password
AUTH_DB_NAME = 'admin'

DB_NAME = 'nycdb'
DB_USER = 'admin'
DB_PASS = '123'

# scrap types
ST_DRY_CLEANERS = 'DRY-CLEANERS'
ST_SHOE_REPAIR = 'SHOE-REPAIR'

# currently using New York for scraping,
# may use more cities in future
CITY = 'New York'

CSV_DRY_CLEANERS = 'output/dry_cleaners.csv'
CSV_SHOE_REPAIR = 'output/shoe_repair.csv'


SCRAPPER_SLEEP_MIN = 30  # in seconds
SCRAPPER_SLEEP_MAX = 60  # in seconds

PROGRESS_YELP_FILE = "progress/yelp.txt"
PROGRESS_YELLOWPAGES_FILE = "progress/yellowpages.txt"
PROGRESS_GROUPON_FILE = "progress/groupon.txt"
PROGRESS_CRAIGLIST_FILE = "progress/craiglist.txt"

PROGRESS_YELP_SHOE_REPAIR_FILE = "progress/yelp_shoe_repair.txt"
PROGRESS_YELLOWPAGES_SHOE_REPAIR_FILE = "progress/yellowpages_shoe_repair.txt"
PROGRESS_GROUPON_SHOE_REPAIR_FILE = "progress/groupon_shoe_repair.txt"
PROGRESS_CRAIGLIST_SHOE_REPAIR_FILE = "progress/craiglist_shoe_repair.txt"

"""
CSV_GROUP_DRY_CLEANERS = 'groupon_dry_cleaners.csv'
CSV_GROUP_SHOE_REPAIR = 'groupon_shoe_repair.csv'

CSV_CRAIGLIST_DRY_CLEANERS = 'craiglist_dry_cleaners.csv'
CSV_CRAIGLIST_SHOE_REPAIR = 'craiglist_shoe_repair.csv'
"""
