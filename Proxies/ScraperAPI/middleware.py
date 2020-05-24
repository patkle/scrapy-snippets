# -*- coding: utf-8 -*-

class ScraperAPIMiddleware(object):
    def __init__(self, crawler):
        self.key = crawler.settings.get('SCRAPER_API_KEY')
        self.user = self.__get_user(crawler.settings.get('SCRAPER_API_OPTIONS'))

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def __get_user(self, options):
        user = 'scraperapi'
        if options is not None and isinstance(options, dict):
            for key, value in options.items():
                user = f'{user}.{key}={value}'
        return user

    def process_request(self, request, spider):
        request.meta['proxy'] = f'http://{self.user}:{self.key}@proxy-server.scraperapi.com:8001'
