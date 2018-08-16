"""Project configuration file."""
import sys

"""mysql database configuration """
sys.modules['DB_HOST'] = 'localhost'
sys.modules['DB_USER'] = 'root'
sys.modules['DB_PASSWORD'] = 'root'
sys.modules['DB_PORT'] = 3306
sys.modules['DB_NAME'] = 'spider'
sys.modules['DB_CHARSET'] = 'utf8'

"""roxy user-agent"""
sys.modules['HEADERS'] = [{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; W) Gecko/20100101 Firefox/59.0'}]

"""
proxy ip:
The proxy ip is randomly obtained through the PROXIES list. If it is not enabled, the real ip is used.
"""
#sys.modules['PROXIES'] = [{'http':'61.136.163.245:8103'}]

"""project execution log directory"""
sys.modules['LOG_DIR'] = ''

"""excel file directory"""
sys.modules['EXCEL_DIR'] = ''
