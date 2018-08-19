"""Project configuration file."""
import sys


"""Mysql database configuration"""

"""database host name"""
sys.modules['DB_HOST'] = 'localhost'
"""database account"""
sys.modules['DB_USER'] = 'root'
"""database password"""
sys.modules['DB_PASSWORD'] = 'root'
"""database port"""
sys.modules['DB_PORT'] = 3306
"""database name"""
sys.modules['DB_NAME'] = 'spider'
"""database character set"""
sys.modules['DB_CHARSET'] = 'utf8'


"""Http request configuration"""

"""request expiration time, unit: second"""
sys.modules['TIME_OUT'] = 10

"""
proxy User-Agent:
This parameter is a list type, you can configure multiple, randomly select one when accessing.
"""
sys.modules['HEADERS'] = [{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; W) Gecko/20100101 Firefox/59.0'}]

"""
proxy ip:
This parameter is a list type, you can configure multiple, randomly select one when accessing.
"""
#sys.modules['PROXIES'] = [{'http':'61.136.163.245:8103'}]
sys.modules['PROXIES'] = [{}]

"""
absolute path of phantomjs:
If you do not need to get the webpage after javascript is running, you can ignore this.
"""
sys.modules['PHANTOMJS'] = '/usr/local/phantomjs/bin/phantomjs'

"""webdriver waits for the page to finish loading, unit: second"""
sys.modules['WAIT_TIME'] = 10


"""File generation configuration"""

"""
project execution log directory:
If enabled, to ensure write access to this directory.
"""
sys.modules['LOG_DIR'] = ''

"""
excel file storage directory:
If enabled, to ensure that this directory has write permission.
"""
sys.modules['EXCEL_DIR'] = ''
