"""Project configuration file."""
import sys

"""mysql database configuration """
DB_HOST = sys.modules['DB_HOST']
DB_USER = sys.modules['DB_USER']
DB_PASSWORD = sys.modules['DB_PASSWORD']
DB_PORT = sys.modules['DB_PORT']
DB_NAME = sys.modules['DB_NAME']
DB_CHARSET = sys.modules['DB_CHARSET']

"""roxy user-agent"""
HEADERS = sys.modules['HEADERS']

"""
proxy ip:
The proxy ip is randomly obtained through the PROXIES list. If it is not enabled, the real ip is used.
"""
#PROXIES = sys.modules['PROXIES']

"""project execution log directory"""
LOG_DIR = sys.modules['LOG_DIR']

"""excel file directory"""
EXCEL_DIR = sys.modules['EXCEL_DIR']
