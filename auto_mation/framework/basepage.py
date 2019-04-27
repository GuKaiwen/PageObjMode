from selenium import  webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger

logger = Logger(logger="BasePage").get_log()
class BasePage(object):
    '''
    back()
    open_url()
    get()
    quit()
    type()
    click()
    ...
    '''

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """
        :param url:
        :return:
        """
        self.driver.get(url)

    def click(self, locator):
        """
        :param locator:
        :return:
        """
        el = self.find_element(locator)
        try:
            el.click()
            logger.info("Click text in input box before typing.")
        except NameError as e:
            logger.error("Failed to click the element with %s"%e)


    def type(self, locator, text):
        """
        :param text:
        :return:
        """
        el = self.find_element(locator)
        el.clear()
        try:
            el.send_keys(text)
        except NameError as e:
            logger.error("Failed to type in input box with %s"%text)
            self.take_screenshot()

    def quit_browser(self):
        """
        :return:
        """
        self.driver.quit()

    def back(self):
        """
        :return:
        """
        self.driver.back()
        logger.info("Click back on current page")

    def forward(self):
        """
        :return:
        """
        self.driver.forward()
        logger.info("Click forward ion current page")

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds"%seconds)

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser")
        except NameError as e:
            logger.error("Failed to quit the browser with %s"%e)

    def take_screenshot(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screen_shots/'
        rq = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name = file_path + rq + '.png'

        try:
            self.driver.get_screenshot_as_file(screen_name)
        except NameError as e:
            logger.error("Failed to take screenshot! %s"%e)
            self.take_screenshot()

    def find_element(self, locator):
        '''
        param:locator
        return:element
        '''
        element = ''
        if "=>" not in locator:
            self.driver.find_element_by_id(locator)

        locator_by = locator.split('=>')[0]
        locator_value = locator.split('=>')[1]

        if  locator_by == "i" or locator_by == "id":
            try:
                element = self.driver.find_element_by_id(locator_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s"%e)
                self.take_screenshot()
        elif locator_by == "n" or locator_by == "name":
            element = self.driver.find_element_by_name(locator_value)
        elif locator_by == "c" or locator_by == "class_name":
            element = self.driver.find_element_by_class_name(locator_value)
        elif locator_by == "l" or locator_by == "link_text":
            element = self.driver.find_element_by_link_text(locator_value)
        elif locator_by == "p" or locator_by == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(locator_value)
        elif locator_by == "t" or locator_by == "tag_name":
            element = self.driver.find_element_by_tag_name(locator_value)
        elif locator_by == "x" or locator_by == "xpath":
            try:
                element = self.driver.find_element_by_xpath(locator_value)
                logger.info("Had find the element%s"%element)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s"%e)
                self.take_screenshot()
        elif locator_by == "s" or locator_by == "css_selector":
            element = self.driver.find_element_by_css_selector(locator_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def clear(self, locator):

        el = self.driver.find_element(locator)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s"%e)

    def get_page_title(self):
        logger.info("Current page title is %s"%self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %s seconds"%seconds)




