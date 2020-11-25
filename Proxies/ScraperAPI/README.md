# Scraper API middleware
This snippet lets you use [Scraper API](https://www.scraperapi.com/?fp_ref=patrick50) for every request you process with Scrapy.
You could instead simply set the `proxy` field of your request's meta attribute to `http://scraperapi.your=options:your_key@proxy-server.scraperapi.com:8001` and enable `HttpProxyMiddleware`.
This middleware's only purpose is to achieve this in a more convenient manner.

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

## Additional options 
Scraper API supports additional options as documented [here](https://www.scraperapi.com/documentation?fp_ref=patrick50#proxy-mode).
You could use these options by adding them to your settings as dictionary.

```python
SCRAPER_API_OPTIONS = {
    'render': 'true', 
    'country_code': 'us'
}
```

## Affiliate link
If this example is helpful to you and you do not yet have a subscription to Scraper API, consider using [my affiliate link](https://www.scraperapi.com/pricing?fp_ref=patrick50) if you plan on getting one.
