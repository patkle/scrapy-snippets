# -*- coding: utf-8 -*-

class ScraperAPIMiddleware(object):
    def __init__(self, crawler):
        self.key = crawler.settings.get('SCRAPER_API_KEY')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        request.meta['proxy'] = f'http://scraperapi:{self.key}@proxy-server.scraperapi.com:8001'
