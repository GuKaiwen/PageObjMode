import os
from configparser import ConfigParser

class TestReadConfig(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))
        print(root_dir)

        config_path = root_dir + '/config/config.ini'
        config = ConfigParser()
        config.read(config_path)

        browser = config.get("browserType", "browserName")
        URL = config.get("testServer","URL")

        return (browser, URL)


readconfig = TestReadConfig()
print(readconfig.get_value())


