# -*- coding: utf-8 -*-
from __future__ import annotations
from scrapy import signals
from random import choice

class RandomUserAgentMiddleware(object):
    """Middleware that set's a random user agent selected from a list provided in settings"""
    def __init__(self, settings) -> None:
        # get and save list of user agents from settings to set in process_request
        self.user_agents = settings.get('USER_AGENTS', [])

    @classmethod
    def from_crawler(cls, crawler) -> RandomUserAgentMiddleware:
        # instantiate object of RandomUserAgentMiddleware  
        middleware = cls(crawler.settings)
        # connect middleware's spider_opened method to crawler's spider_opened signal
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        return middleware

    def spider_opened(self, spider) -> None:
        # get value set for random_user_agent from spider. 
        # if none, set to False
        self.rotate = getattr(spider, 'random_user_agent', False)

    def process_request(self, request, spider) -> None:
        # check if rotate is set
        if self.rotate:
            # select and set a random user agent from provided settings
            request.headers['user-agent'] = choice(self.user_agents)
