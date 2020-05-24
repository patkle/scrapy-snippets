# Scraper API middleware
This snippet let's you use [Scraper API](https://www.scraperapi.com/?fp_ref=patrick50) for every request you process with Scrapy.

## Settings
You need to specify your key for Scraper API in your settings.py or settings object. 
```Python
SCRAPER_API_KEY = 'your_key'
```
Also you need to enable ScraperAPIMiddleware as well as Scrapy's HttpProxyMiddleware. 
```python
DOWNLOADER_MIDDLEWARES = {
    'your_project.middleware_file.ScraperAPIMiddleware': 350,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
}
```

## Affiliate link
If this example is helpful to you and you do not yet have a subscription to Scraper API, consider using [my affiliate link](https://www.scraperapi.com/pricing?fp_ref=patrick50) if you plan on getting one.
