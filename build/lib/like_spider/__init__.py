"""
like spider: a crawler framework that allows developers to easily extract web page information and quickly store data.

copyright: (c) 2018 by Yingjie Wu.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

author: wyjhaha@foxmail.com

github: https://github.com/wuyingjie1002/like_spider

Note: please read the development documentation and sample code in detail during development.
github wiki: https://github.com/wuyingjie1002/like_spider/wiki

If you have any questions or suggestions, please contact me by email.
"""

import time, re, os, pymysql, zipfile
from .config import *
from .request import Request
from .html import Html
from .mysql import Mysql
from .excel import Excel
from .fireFox import FireFox

def filterBlankChar(sourceStr):
    """filter whitespace characters in a string"""
    newStr = re.sub(r'[\f\n\r\t\v]+', '', sourceStr)
    return newStr.strip()

def escapeString(sourceStr):
    """escape special characters"""
    return pymysql.escape_string(sourceStr)

def executeLog(content):
    """project execution log"""
    localTime = time.localtime()
    month = time.strftime('%Y%m', localTime)
    day = time.strftime('%Y%m%d', localTime)
    strTime = time.strftime('%Y-%m-%d %H:%M:%S', localTime)
    if 'LOG_DIR' in globals() and LOG_DIR != "":
        if LOG_DIR[-1] == "/":
            path = LOG_DIR + month
        else:
            path = LOG_DIR + "/" + month
        if os.path.exists(path) == False:
            os.makedirs(path)
        fileName = path + "/" + day + ".log"
        f = open(fileName, 'a+')
        content = strTime + " | " + content + "\n"
        f.write(content)
        f.close()
    else:
        print('file directory error')

def zipCompress(fileList, outputPath):
    """compress the folder into a zip"""
    f = zipfile.ZipFile(outputPath, 'w', zipfile.ZIP_DEFLATED)
    for fl in fileList:
        f.write(fl)
    f.close()

__all__ = ['Request', 'Html', 'Mysql', 'Excel', 'FireFox', 'filterBlankChar', 'escapeString', 'executeLog', 'zipCompress']
