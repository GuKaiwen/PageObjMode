import unittest
import os
import time
import testsuits
from testsuits.baidu_search import BaiduSearch
from testsuits.test_get_baidu_title import GetPageTitle
from framework import HTMLTestRunner


suite = unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(BaiduSearch('test_search2'))
suite.addTest(GetPageTitle('test_get_title'))

# suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
#suite(unittest.makeSuite(GetPageTitle))

# suite = unittest.TestLoader.discover('testsuits')

report_path = os.path.dirname(os.path.abspath('.')) + '/report/'

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, 'wb')

if __name__ == '__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告',description=u'用例执行情况')
    runner.run(suite)