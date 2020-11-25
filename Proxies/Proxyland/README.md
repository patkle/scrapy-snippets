# Proxyland middleware
This snippet lets you use [Proxyland](https://proxyland.io) for every request you process with Scrapy.
You can also simply set the `proxy` field of your request's meta attribute to `http://package_username:package_password@server.proxyland.io:9090`.
This middleware's only purpose is to achieve this in a more convenient manner.

## Settings
You need to specify your package credentials for Proxyland in your settings.py or settings object for tihs middleware to take effect. 

```python
PROXYLAND = {
    'username': 'package_username',
    'password': 'package_password'
}
```

Also you need to enable ProxylandMiddleware as well as Scrapy's HttpProxyMiddleware. 

```python
DOWNLOADER_MIDDLEWARES = {
    'your_project.middleware_file.ProxylandMiddleware': 350,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
}
```
