# -*- coding: utf-8 -*-
from scrapy import signals
from random import choice

class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        self.rotate = False
        self.user_agents = crawler.settings.get('USER_AGENTS', [])

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls(crawler)
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        return middleware

    def spider_opened(self, spider):
        self.rotate = getattr(spider, 'random_user_agent', self.rotate)

    def process_request(self, request, spider):
        request.headers['user-agent'] = choice(self.user_agents)
