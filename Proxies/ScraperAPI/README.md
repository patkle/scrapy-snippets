# Scraper API
## Accessing the base url
Since this sub class of Request returns a URL pointing to Scraper API, the base url can be accessed with `response.meta['base_url']`

## Settings
You need to specify your key for Scraper API in your settings.py or settings object. 
```Python
SCRAPER_API_KEY = 'your_key'
```

## TODO
- implement functionality for response.follow
