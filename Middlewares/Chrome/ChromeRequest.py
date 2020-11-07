from scrapy import Request
from selenium.webdriver.common.keys import Keys

class Flow(object):
    def __init__(self, driver):
        self.driver = driver
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

class Textbox(object):
    def __init__(self, driver, xpath_query, text):
        self.driver = driver
        self.xpath = xpath_query
        self.text = text

    def execute(self):
        textbox = self.driver.find_element_by_xpath(self.xpath).click()
        textbox.send_keys(self.text)
        textbox.send_keys(Keys.RETURN)

class ChromeRequest(Request):
    def __init__(self, flow=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flow = flow
