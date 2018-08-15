"""Project configuration file."""

global DB_HOST
global DB_USER
global DB_PASSWORD
global DB_NAME
global DB_PORT
global DB_CHARSET
global PROXIES
global HEADERS
global LOG_DIR
global EXCEL_DIR

"""mysql database configuration """
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_PORT = 3306
DB_NAME = 'spider'
DB_CHARSET = 'utf8'

"""roxy user-agent"""
HEADERS = [{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; W) Gecko/20100101 Firefox/59.0'}]

"""
proxy ip:
The proxy ip is randomly obtained through the PROXIES list. If it is not enabled, the real ip is used.
"""
#PROXIES = [{'http':'61.136.163.245:8103'}]

"""project execution log directory"""
LOG_DIR = ''

"""excel file directory"""
EXCEL_DIR = ''
