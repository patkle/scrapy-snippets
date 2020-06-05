# Selenium requests with chromedriver for scrapy
Basic classes to use Selenium's chromedriver to make requests using Scrapy.

## Settings
You need to set the middleware in your settings like this:  
```python
'DOWNLOADER_MIDDLEWARES' = {
        'your_project.middleware_file.ChromeMiddleware': 100,
}
```
Only `ChromeRequest`s will be processed by this middleware.
