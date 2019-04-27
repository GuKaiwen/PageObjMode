#coding:utf-8
from framework.basepage import BasePage

class NewsHomePage(BasePage):

    sports_link = "xpath=>//*ul[@id='header-link-wrapper']/li[2]"

    def send_sport_link(self):
        self.click(self.sports_link)
        self.sleep(2)

