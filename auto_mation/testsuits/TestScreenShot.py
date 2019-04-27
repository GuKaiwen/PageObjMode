from pageobjects.basepage import BasePage
from selenium import webdriver
import time

class TestScreenShot(object):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(1)
    basepage = BasePage(driver)

    def getScreenShot(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)
        self.basepage.take_screenshot()
        self.basepage.quit_browser()

screenshot = TestScreenShot()
screenshot.getScreenShot()


