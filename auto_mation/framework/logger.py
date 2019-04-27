#coding:utf-8
import  logging
import os
import time

class Logger(object):

    def __init__(self, logger):
        self.logger = logger

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        rq = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def get_log(self):
        return self.logger


if __name__ == "__main__":
    logger = Logger(logger="Logger").get_log()
    logger.info("日志测试")