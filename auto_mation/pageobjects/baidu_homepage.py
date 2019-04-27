#coding:utf-8
from framework.basepage import BasePage
from framework.logger import Logger

logger = Logger(logger="BaiduHomePage").get_log()
class BaiduHomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"
    news_link_text = "xpath=>//*[@id='u_sp']/a[1]"

    def type_text(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def send_news_link(self):
        self.click(self.news_link_text)
        self.sleep(2)




