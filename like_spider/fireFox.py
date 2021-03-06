import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from .config import *
from .request import Request

class FireFox():
    """This is a class that simulates the behavior of Firefox browsers."""

    def __init__(self, show = False):
        """initialize"""
        options = webdriver.FirefoxOptions()

        if show == False:
            options.set_headless()

        req = Request()

        proxy = req.getProxy()
        if len(proxy) > 0:
            proxyStr = list(proxy.values())[0]
            proxyList = proxyStr.split(':')
            options.set_preference('network.proxy.type', 1)
            options.set_preference('network.proxy.http', proxyList[0])
            options.set_preference('network.proxy.http_port', int(proxyList[1]))

        header = req.getHeader()
        if len(header) > 0:
            options.set_preference("general.useragent.override", list(header.values())[0])

        self.browser = webdriver.Firefox(executable_path = FIREFOX_DRIVER, options = options)

    def load(self, url, sleepTime = 0):
        """browser loading page"""
        self.browser.get(url)
        if sleepTime > 0:
            time.sleep(sleepTime)
        else:
            self.browser.implicitly_wait(WAIT_TIME)
        
        self.content = self.browser.page_source

    def refresh(self, sleepTime = 0):
        """browser refresh page"""
        self.browser.refresh()
        if sleepTime > 0:
            time.sleep(sleepTime)
        else:
            self.browser.implicitly_wait(WAIT_TIME)
        
        self.content = self.browser.page_source

    def click(self, elementXpath, waitElementXpath = '', sleepTime = 0):
        """mouse click"""
        element = self.browser.find_element_by_xpath(elementXpath)
        ActionChains(self.browser).click(element).perform()
        if sleepTime > 0:
            time.sleep(sleepTime)
        elif waitElementXpath != '':
            WebDriverWait(self.browser, WAIT_TIME).until(lambda driver : driver.find_element_by_xpath(waitElementXpath))
        self.content = self.browser.page_source

    def moveElementTo(self, elementXpath, xpos, ypos, waitElementXpath = '', sleepTime = 0):
        """drag the element to a position"""
        element = self.browser.find_element_by_xpath(elementXpath)
        ActionChains(self.browser).drag_and_drop_by_offset(element, xpos, ypos).perform()
        if sleepTime > 0:
            time.sleep(sleepTime)
        elif waitElementXpath != '':
            WebDriverWait(self.browser, WAIT_TIME).until(lambda driver : driver.find_element_by_xpath(waitElementXpath))
        self.content = self.browser.page_source

    def isElement(self, elementXpath):
        """Whether the element exists"""
        try:
            self.browser.find_element_by_xpath(elementXpath)
            return True
        except:
            return False

    def moveTo(self, elementXpath, waitElementXpath = '', sleepTime = 0):
        """mouse move to element"""
        element = self.browser.find_element_by_xpath(elementXpath)
        ActionChains(self.browser).move_to_element(element).perform()
        if sleepTime > 0:
            time.sleep(sleepTime)
        elif waitElementXpath != '':
            WebDriverWait(self.browser, WAIT_TIME).until(lambda driver : driver.find_element_by_xpath(waitElementXpath))
        self.content = self.browser.page_source

    def scrollTo(self, xpos, ypos, waitElementXpath = '', sleepTime = 0):
        """window scroll to a location"""
        self.browser.execute_script("window.scrollTo(arguments[0], arguments[1]);", xpos, ypos)
        if sleepTime > 0:
            time.sleep(sleepTime)
        elif waitElementXpath != '':
            WebDriverWait(self.browser, WAIT_TIME).until(lambda driver : driver.find_element_by_xpath(waitElementXpath))
        self.content = self.browser.page_source

    def scrollToBottom(self, waitElementXpath = '', sleepTime = 0):
        """window scroll to the bottom"""
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if sleepTime > 0:
            time.sleep(sleepTime)
        elif waitElementXpath != '':
            WebDriverWait(self.browser, WAIT_TIME).until(lambda driver : driver.find_element_by_xpath(waitElementXpath))
        self.content = self.browser.page_source

    def setValue(self, elementXpath, value):
        """set the value attribute of the element"""
        element = self.browser.find_element_by_xpath(elementXpath)
        self.browser.execute_script("arguments[0].value = arguments[1];", element, value)
        self.content = self.browser.page_source

    def setText(self, elementXpath, value):
        """set the content of the element"""
        element = self.browser.find_element_by_xpath(elementXpath)
        self.browser.execute_script("arguments[0].innerHTML = arguments[1];", element, value)
        self.content = self.browser.page_source

    def sendKey(self, elementXpath, key):
        """keyboard input"""
        self.browser.find_element_by_xpath(elementXpath).send_keys(key)

    def switchToFrame(self, elementXpath, sleepTime = 0):
        """switch to a frame"""
        element = self.browser.find_element_by_xpath(elementXpath)
        self.browser.switch_to.frame(element)
        if sleepTime > 0:
            time.sleep(sleepTime)
        self.content = self.browser.page_source

    def returnToPage(self, sleepTime = 0):
        """return to page"""
        self.browser.switch_to_default_content()
        if sleepTime > 0:
            time.sleep(sleepTime)
        self.content = self.browser.page_source

    def screenShot(self, fileName):
        """screen capture"""
        self.browser.save_screenshot(fileName)

    def quit(self):
        """browser quit"""
        self.browser.quit()
