from scrapy import Request
from .settings import SCRAPER_API_KEY
from scraper_api import ScraperAPIClient

client = ScraperAPIClient(SCRAPER_API_KEY)

class ScraperAPIRequest(Request):
    def __init__(self, url, *args, **kwargs):
        meta = kwargs.pop('meta', {})
        meta['base_url'] = url
        super().__init__(client.scrapyGet(url), meta=meta, *args, **kwargs)
