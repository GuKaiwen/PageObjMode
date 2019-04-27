from pageobjects.sports_homepage import SportHomePage
from pageobjects.baidu_homepage import BaiduHomePage
from pageobjects.news_homepage import NewsHomePage
from framework.browser_engine import BrowserEngine
import unittest
import time

class NbaSearch(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser()

    def tearDown(self):
        self.driver.quit()

    def test_sports_search(self):
        baiduhome = BaiduHomePage(self.driver)
        baiduhome.send_news_link()

        newhome = NewsHomePage(self.driver)
        newhome.send_sport_link()

        sportsearch = SportHomePage(self.driver)
        sportsearch.nba_search()
        sportsearch.take_screenshot()

if __name__ == "__main__":
    unittest.main()