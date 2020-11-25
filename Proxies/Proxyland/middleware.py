from __future__ import annotations


class ProxylandMiddleware:
    """This middleware sets the proxy value to your Proxyland package for every request processed"""
    def __init__(self, proxyland_settings) -> None:
        self.username = proxyland_settings['username']
        self.password = proxyland_settings['password']
        
    @classmethod
    def from_crawler(cls, crawler) -> ProxylandMiddleware:
        # instantiate class with PROXYLAND settings from crawler
        return cls(crawler.settings.get('PROXYLAND'))

    def process_request(self, request, spider) -> None:
        # set proxy to proxyland server 
        request.meta['proxy'] = f'http://{self.username}:{self.password}@server.proxyland.io:9090'
