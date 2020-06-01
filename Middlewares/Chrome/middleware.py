# -*- coding: utf-8 -*-
from scrapy import signals
from scrapy.http import HtmlResponse
from .ChromeRequest import ChromeRequest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class ChromeMiddleware:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver', chrome_options=options)

    @classmethod
    def from_crawler(cls, crawler):
        """Initialize the middleware with the crawler settings"""
        middleware = cls()
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        """Process a request using the selenium driver if applicable"""
        if not isinstance(request, ChromeRequest):
            return None
        self.driver.get(request.url)
        request.meta.update({'driver': self.driver})
        return HtmlResponse(
            self.driver.current_url,
            body=str.encode(self.driver.page_source),
            encoding='utf-8',
            request=request
        )

    def spider_closed(self):
        self.driver.quit()
