# -*- coding: utf-8 -*-
import scrapy
from scrapy.settings import Settings
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapy.http import Request
from json import loads

class UserAgentSpider(scrapy.Spider):
    name = 'user_agent'
    random_user_agent = True

    def start_requests(self):
        for i in range(0, 5):
            yield Request(
                'https://httpbin.org/user-agent', 
                self.parse, 
                dont_filter=True
            )
    
    def parse(self, response):
        user_agent = loads(response.text)['user-agent']
        print(user_agent)
        yield {'user_agent': user_agent}

def get_settings():
    settings = Settings()
    import requests
    settings.set('USER_AGENTS', [x['useragent'] for x in requests.get('http://51.158.74.109/useragents/?format=json').json()])
    settings.set('DOWNLOADER_MIDDLEWARES', {
        'middleware.RandomUserAgentMiddleware': 150,
    })
    return settings

if __name__ == '__main__':
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(UserAgentSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
