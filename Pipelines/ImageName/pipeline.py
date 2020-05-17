# coding: utf8
import scrapy
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline

class ImageNamePipeline(ImagesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None):
        super().__init__(store_uri, settings=settings, download_func=download_func)
        self.image_url_fields = settings.get('IMAGE_URL_FIELDS', {})

    def get_media_requests(self, item, info):
        for image_field_name, settings in self.image_url_fields.items():
            for i, image_url in enumerate(item.get(image_field_name, [])):
                yield Request(
                    image_url, 
                    meta = {
                        'image_name': item[settings.get('name_field', 'name')], 
                        'image_folder': settings.get('sub_folder', ''),
                        'image_count': i
                    }
                )

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        image_name = request.meta['image_name'].replace(" ", "_")
        image_folder = request.meta['image_folder']
        if not image_folder.endswith('/'):
            image_folder += '/'
        return f'{image_folder}{image_name}-{request.meta["image_count"]}.jpg'
