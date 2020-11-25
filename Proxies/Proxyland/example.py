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
        # load IP which made the request from json string
        ip = loads(response.text)['origin']
        yield {'ip': ip}

def get_settings() -> Settings:
    settings = Settings()
    # Enter your package credentials here!
    settings.set('PROXYLAND', {
        'username': 'package_username',
        'password': 'package_password'
    })
    # enable ProxylandMiddleware and HttpProxyMiddleware
    settings.set('DOWNLOADER_MIDDLEWARES', {
        'middleware.ProxylandMiddleware': 350,
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    })
    return settings

if __name__ == '__main__':
    # routine to run scrapy from a script
    # see: https://docs.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(IpSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
