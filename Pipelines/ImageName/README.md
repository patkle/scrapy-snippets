# ImageNamePipeline
ImageNamePipeline is a sub class of [ImagesPipeline](https://doc.scrapy.org/en/latest/_modules/scrapy/pipelines/images.html)

To enable the pipeline in your project you need to set [ITEM_PIPELINES](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#activating-an-item-pipeline-component) in [settings.py](https://docs.scrapy.org/en/latest/topics/settings.html)
```Python
ITEM_PIPELINES = {
    'your_project.pipelines.ImageNamePipeline': 200,
    
}
```
Also you need to define IMAGE_URL_FIELDS in settings.py as a Dictionary like this:
```Python
IMAGE_URL_FIELDS = {
    'your_items_image_url_field': {
        'name_field': 'item_field_used_to_name_image',
        'sub_folder': 'folder_to_which_file_gets_downloaded'
    }, 'second_image_url_field': {
        'name_field': 'name',
        'sub_folder': 'folder'
    }
}
```
