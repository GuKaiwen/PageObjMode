import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHomePage

class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUp(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_get_title(self):

        homepage = BaiduHomePage(self.driver)
        print(homepage.get_page_title())

