# Proxyland middleware
This snippet let's you use [Proxyland](https://proxyland.io) for every request you process with Scrapy.

## Settings
You need to specify your package credentials for Proxyland in your settings.py or settings object. 
```Python
PROXYLAND = {
    'username': 'package_username',
    'password': 'package_password'
}
```
Also you need to enable ProxylandMiddleware as well as Scrapy's HttpProxyMiddleware. 
```python
DOWNLOADER_MIDDLEWARES = {
    'your_project.middleware_file.ScraperAPIMiddleware': 350,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
}
```
