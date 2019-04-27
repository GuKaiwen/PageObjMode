#coding:utf-8
from selenium import webdriver
from framework.browser_engine import BrowserEngine
import time
import unittest
from pageobjects.baidu_homepage import BaiduHomePage
from pageobjects.news_homepage import NewsHomePage

class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUp(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_baidu_search(self):
        homepage = BaiduHomePage(self.driver)
        homepage.type_text("selenium")
        homepage.send_submit_btn()
        time.sleep(1)
        homepage.take_screenshot()
        try:
            assert 'selenium' in homepage.get_page_title()
            print("Test Pass")
        except NameError as e:
            print("Test Fail." ,format(e))

    def test_search2(self):
        homepage = BaiduHomePage(self.driver)
        homepage.type_text("python")
        homepage.send_submit_btn()
        time.sleep(1)
        homepage.take_screenshot()


if __name__ == '__main__':
    unittest.main()



