# -*- coding: utf-8 -*-
import scrapy
from scrapy.settings import Settings
from scrapy.exporters import CsvItemExporter, JsonItemExporter
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

class CSVItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()

class JSONItem(CSVItem):
    pass

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for container in response.xpath('//div[@class="quote"]'):
            quote = container.xpath('.//span[@class="text"]/text()').extract_first()
            author = container.xpath('.//small[@class="author"]/text()').extract_first()
            print(author)
            yield CSVItem(quote=quote, author=author)
            yield JSONItem(quote=quote, author=author)

def get_settings():
    settings = Settings()
    settings.set('OUTPUT_DIRECTORY', 'export')
    settings.set('EXPORTERS', {
        'csv_quotes': {
            'item': CSVItem,
            'exporter': CsvItemExporter
        }, 'json_quotes': {
            'item': JSONItem,
            'exporter': JsonItemExporter
        }
    })
    settings.set('ITEM_PIPELINES', {
        'pipeline.MultiItemPipeline': 200
    })
    return settings

if __name__ == '__main__':
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(QuotesSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
