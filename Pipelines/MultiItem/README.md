# MultiItemPipeline
This is a pipeline demonstrating how one could export different items to different files using a Scrapy pipeline.

## Settings
As with every item pipeline in Scrapy, you should enable it in the `ITEM_PIPELINES` dictionary which you pass to your settings object or save in your `settings.py`.

```python
ITEM_PIPELINES = {
        'your_project.your_pipeline_file.MultiItemPipeline': 200
}
```

When you include this pipeline in your scrapy project, you'll need to set the following additional settings to make it work as intended:

```Python
OUTPUT_DIRECTORY = 'path_to_your_spiders_results'
EXPORTERS = {
    'filename': {
        'item': ItemClass,
        'exporter': ExporterClass
    }
}
```

The key `filename` in this dictionary is the value on which the output filename will be based. The resulting file will be named a combination of your filename plus an underscore and an integer. This is to prevent overwriting existing files. 
Let's say filename_1 already exists, then the pipeline will automatically create filename_2. 

The ExporterClass should be an exporter provided by Scrapy, depending on the export format you expect. There are a lot of available options in [`scrapy.exporters`](https://github.com/scrapy/scrapy/blob/master/scrapy/exporters.py), like `CsvItemExporter`, `PickleItemExporter`, `XmlItemExporter`, `JsonItemExporter`, `JsonLinesItemExporter`, etc.
