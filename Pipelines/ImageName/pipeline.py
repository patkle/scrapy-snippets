# coding: utf8
import scrapy
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline

class ImageNamePipeline(ImagesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None):
        super().__init__(store_uri, settings=settings, download_func=download_func)
        self.image_url_fields = settings.get('IMAGE_URL_FIELDS', {})

    def get_media_requests(self, item, info):
        for image_field_name, image_settings in self.image_url_fields.items():
            images = item.get(image_field_name, [])
            if not isinstance(images, str):
                for i, image_url in enumerate(images):
                    url = image_settings.get('base_url', '') + image_url
                    yield self.__get_media_requests(url, item, image_settings, i)
            else:
                url = image_settings.get('base_url', '') + images
                yield self.__get_media_requests(url, item, image_settings)

    def __get_media_requests(self, url, item, image_settings, counter=1):
        return Request(
            url, 
            meta = {
                'image_name': item[image_settings.get('name_field', 'name')], 
                'image_folder': image_settings.get('sub_folder', ''),
                'image_count': counter
            }
        )

    def item_completed(self, results, item, info):
        print(results)
        results = [x for ok, x in results if ok]
        for image_field_name, image_settings in self.image_url_fields.items():
            image_path_list = []
            for result in results:
                if result['url'] in item[image_field_name]:
                    image_path_list.append(result['path'])
            item[image_settings['path_field']] = image_path_list
            print(image_path_list)
        return item

    def file_path(self, request, response=None, info=None):
        image_name = request.meta['image_name'].replace(" ", "_")
        image_folder = request.meta['image_folder']
        if not image_folder.endswith('/'):
            image_folder += '/'
        return f'{image_folder}{image_name}-{request.meta["image_count"]}.jpg'
