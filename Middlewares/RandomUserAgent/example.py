# -*- coding: utf-8 -*-
import requests
from scrapy import Spider, Request
from scrapy.settings import Settings
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from json import loads

class UserAgentSpider(Spider):
    """Spider to test user agents"""
    name = 'user_agent'
    # this must be set to a truthy value in order for the middleware to take effect
    random_user_agent = True

    def start_requests(self):
        # send 5 requests to httpbin.org in order to retrieve the user-agent the page sees
        for i in range(0, 5):
            yield Request(
                'https://httpbin.org/user-agent',
                self.parse,
                # disable duplication filter for scrapy requests
                dont_filter=True
            )

    def parse(self, response):
        # get user-agent from json string
        user_agent = loads(response.text)['user-agent']
        print(user_agent)
        yield {'user_agent': user_agent}

def get_settings() -> Settings:
    """create and return a scrapy settings object"""
    settings = Settings()
    # load a list of user agents from http://51.158.74.109
    settings.set('USER_AGENTS', [x['useragent'] for x in requests.get('http://51.158.74.109/useragents/?format=json').json()])
    # enable the RandomUserAgentMiddleware middleware
    settings.set('DOWNLOADER_MIDDLEWARES', {
        'middleware.RandomUserAgentMiddleware': 150,
    })
    return settings

if __name__ == '__main__':
    # routine to run scrapy from a script
    # see: https://docs.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(UserAgentSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
