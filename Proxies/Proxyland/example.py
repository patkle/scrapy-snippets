# -*- coding: utf-8 -*-
import scrapy
from scrapy.settings import Settings
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapy.http import Request
from json import loads

class IpSpider(scrapy.Spider):
    name = 'ip'
    
    def start_requests(self):
        for i in range(0, 5):
            yield Request(
                'http://httpbin.org/ip', 
                self.parse, 
                dont_filter=True
            )
    
    def parse(self, response):
        ip = loads(response.text)['origin']
        print(ip)
        yield {'ip': ip}

def get_settings():
    settings = Settings()
    # TODO: Enter your package credentials here!
    settings.set('PROXYLAND', {
        'username': 'package_username',
        'password': 'package_password'
    })
    settings.set('DOWNLOADER_MIDDLEWARES', {
        'middleware.ProxylandMiddleware': 350,
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    })
    return settings

if __name__ == '__main__':
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(IpSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
