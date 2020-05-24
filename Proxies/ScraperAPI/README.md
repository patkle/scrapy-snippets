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

## Additional options 
Scraper API supports additional options as documented [here](https://www.scraperapi.com/documentation?fp_ref=patrick50#proxy-mode).
You could use these options by adding them to your settings as dictionary.
```python
SCRAPER_API_OPTIONS = {
    'render': 'true', 
    'country_code': 'us'
}
```
However, this feature is untested since I am only on a free plan. Also, make sure to pass the values for these options as strings.
If you encounter any errors with this, please let me know. 

## Affiliate link
If this example is helpful to you and you do not yet have a subscription to Scraper API, consider using [my affiliate link](https://www.scraperapi.com/pricing?fp_ref=patrick50) if you plan on getting one.
