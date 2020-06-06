# RandomUserAgent
This middleware lets you choose a random user agent for each request. The user agent is selected from a list set in your Scrapy settings. 

## Settings
You need to set a list of user agents in `USER_AGENTS` and add the middleware to `DOWNLOADER_MIDDLEWARES` in your settings.py file or your settings object.
```python
'USER_AGENTS' = [
    # user agents of your choice
]
'DOWNLOADER_MIDDLEWARES' = {
        'your_project.middleware_file.RandomUserAgentMiddleware': 150,
}
```
You also need to add the field `random_user_agent` to your spider.
```python
class YourSpider(scrapy.Spider):
    random_user_agent = True
```
