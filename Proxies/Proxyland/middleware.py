# -*- coding: utf-8 -*-

class ProxylandMiddleware(object):
    def __init__(self, crawler):
        settings = crawler.settings.get('PROXYLAND')
        self.username = settings['username']
        self.password = settings['password']
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        request.meta['proxy'] = f'http://{self.username}:{self.password}@server.proxyland.io:9090'
