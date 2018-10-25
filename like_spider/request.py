import requests, random
from .config import *
from selenium import webdriver

class Request():
    """This is a class that handles http requests."""

    def __init__(self):
        """initialize"""
        self.session = requests.Session()

    def getProxy(self):
        """get proxy ip"""
        proxy = {}
        if 'PROXY_API' in globals() and PROXY_API != '':
            req = self.session.get(PROXY_API)
            ipStr = req.text
            if ipStr != '':
                ipList = ipStr.split('--')
                proxy = {ipList[2]: ipList[0] + ':' + ipList[1]}
        else:
            if 'PROXIES' in globals():
                proxyLen = len(PROXIES)
                if proxyLen > 0:
                    proxy = random.sample(PROXIES, 1)[0]
        return proxy

    def getHeader(self):
        """get client information"""
        header = {}
        if 'HEADERS' in globals():
            headerLen = len(HEADERS)
            if headerLen > 0:
                header = random.sample(HEADERS, 1)[0]
        return header

    def get(self, url, data = {}, referer = ''):
        """http get request"""
        header = self.getHeader()
        header['Referer'] = referer
        req = self.session.get(url, data = data, headers = header, proxies = self.getProxy(), timeout = TIME_OUT)

        if req.status_code == 200:
            return req.text
        else:
            print('request status code : ', req.status_code)
            return ''

    def post(self, url, data = {}, referer = ''):
        """http post request"""
        header = self.getHeader()
        header['Referer'] = referer
        req = self.session.post(url, data = data, headers = header, proxies = self.getProxy(), timeout = TIME_OUT)

        if req.status_code == 200:
            return req.text
        else:
            print('request status code : ', req.status_code)
            return ''

    def final(self, url):
        """webdriver loads webpage"""
        driver = webdriver.PhantomJS(executable_path = PHANTOMJS)
        driver.get(url)
        driver.implicitly_wait(WAIT_TIME)
        content = driver.page_source
        driver.quit()

        return content
