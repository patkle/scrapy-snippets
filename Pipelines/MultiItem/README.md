# MultiItemPipeline

## Settings
When you include this pipeline in your scrapy project, you should set the following settings in settings.py:

```Python
OUTPUT_DIRECTORY = 'path_to_your_spiders_results'
EXPORTERS = {
    'filename': {
        'item': ItemClass,
        'exporter': ExporterClass
    }
}
```

## TODO

- [ ] items are only saved to files if scrapy yields more than a certain number of items. The number seems to be between 10 and 20 items required