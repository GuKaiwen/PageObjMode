#coding:utf-8
from framework.logger import Logger
from selenium import webdriver
from configparser import ConfigParser
import os

logger = Logger(logger="BrowserEngine").get_log()
class BrowserEngine(object):

    logger.info("获取项目根目录")
    file_path = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = file_path + '/tools/chromedriver.exe'
    firefox_driver_path = file_path + '/tools/geckodriver.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):
        config_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config = ConfigParser()
        config.read(config_path,encoding='utf-8')

        browser = config.get("browserType","browserName")
        url = config.get("testServer", "URL")

        if browser == "Chrome":
            logger.info("")
            driver = webdriver.Chrome(self.chrome_driver_path)
        elif browser == "IE":
            logger.info("")
            driver = webdriver.Ie()
        elif browser == "Firefox":
            logger.info("")
            driver = webdriver.Firefox(self.firefox_driver_path)

        logger.info("open browser with this URL")
        driver.get(url)

        return driver

    def quit_browser(self):
        logger.INFO("quit browser")
        self.driver.quit()











