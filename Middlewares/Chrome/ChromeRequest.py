from scrapy import Request

class Flow(object):
    def __init__(self, driver):
        self.driver = driver

class Textbox(object):
    def __init__(self, driver):
        self.driver = driver

class ChromeRequest(Request):
    def __init__(self, flow=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flow = flow
