"""Project configuration file."""
import sys

"""mysql database configuration """
DB_HOST = sys.modules['DB_HOST']
DB_USER = sys.modules['DB_USER']
DB_PASSWORD = sys.modules['DB_PASSWORD']
DB_PORT = sys.modules['DB_PORT']
DB_NAME = sys.modules['DB_NAME']
DB_CHARSET = sys.modules['DB_CHARSET']

"""request expiration time, unit: second"""
TIME_OUT = sys.modules['TIME_OUT']

"""roxy user-agent"""
HEADERS = sys.modules['HEADERS']

"""
proxy ip:
The proxy ip is randomly obtained through the PROXIES list. If it is not enabled, the real ip is used.
"""
#PROXIES = sys.modules['PROXIES']

"""
absolute path of phantomjs:
If you do not need to get the webpage after javascript is running, you can ignore this.
"""
PHANTOMJS = sys.modules['PHANTOMJS']

"""webdriver waits for the page to finish loading, unit: second"""
WAIT_TIME = sys.modules['WAIT_TIME']

"""project execution log directory"""
LOG_DIR = sys.modules['LOG_DIR']

"""excel file directory"""
EXCEL_DIR = sys.modules['EXCEL_DIR']
