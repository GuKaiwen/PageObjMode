from framework.basepage import BasePage

class SportHomePage(BasePage):

    nba_link_text = "xpath=>//*[@id='channel-all']/div/ul/li[7]/a"

    def nba_search(self):
        self.click(self.nba_link_text)
        self.sleep(2)
