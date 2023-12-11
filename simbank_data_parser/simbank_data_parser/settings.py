BOT_NAME = "simbank_data_parser"

SPIDER_MODULES = ["simbank_data_parser.spiders"]
NEWSPIDER_MODULE = "simbank_data_parser.spiders"


RETRY_ENABLED = False
ROBOTSTXT_OBEY = False

LOG_FILE = 'errors.log'
LOG_LEVEL = 'ERROR'


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
