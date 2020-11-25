# -*- coding: utf-8 -*-
import scrapy
from scrapy.settings import Settings
from scrapy.exporters import CsvItemExporter, JsonItemExporter
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor


class CSVItem(scrapy.Item):
    quote = scrapy.Field()


class JSONItem(scrapy.Item):
    author = scrapy.Field()


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield CSVItem(quote=quote.xpath('.//span[@class="text"]/text()').get())
            yield JSONItem(author=quote.xpath('.//small[@class="author"]/text()').get())


def get_settings() -> Settings:
    """Get scrapy settings"""
    settings = Settings()
    # set directory in which output files will be saved
    settings.set('OUTPUT_DIRECTORY', 'export')
    settings.set('EXPORTERS', {
        # key = filename
        'csv_quotes': {
            # item class which to export to csv_quotes 
            'item': CSVItem,
            # use the CsvItemExporter to export to csv
            'exporter': CsvItemExporter
        }, 
        # filename for the second file
        'json_quotes': {
            # JSONItems get saved to file json_quotes
            'item': JSONItem,
            # use the JsonItemExporter to export to json
            'exporter': JsonItemExporter
        }
    })
    settings.set('ITEM_PIPELINES', {
        'pipeline.MultiItemPipeline': 200
    })
    return settings

if __name__ == '__main__':
    # routine to run scrapy from a script
    # see: https://docs.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(QuotesSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
