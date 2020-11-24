# coding: utf8
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline


class ImagesFieldException(Exception):
    pass


class ImageNamePipeline(ImagesPipeline):
    """Pipeline to set names for downloaded images"""

    def __init__(self, store_uri, download_func=None, settings=None) -> None:
        super().__init__(store_uri, settings=settings, download_func=download_func)
        self.image_url_fields = settings.get('IMAGE_URL_FIELDS', {})

    def get_media_requests(self, item, info):
        for image_field_name, image_settings in self.image_url_fields.items():
            images = item.get(image_field_name, [])
            if isinstance(images, str):
                # if images only contains a single image as string, return a single request
                url = image_settings.get('base_url', '') + images
                yield self.__get_media_requests(url, item, image_settings)
            elif isinstance(images, list):
                # if images is a list, return a request for every list item
                for i, image_url in enumerate(images):
                    url = image_settings.get('base_url', '') + image_url
                    yield self.__get_media_requests(url, item, image_settings, i)
            elif images is None:
                pass
            else:
                # raise Exception if images is not str, list or None 
                raise ImagesFieldException(f'{image_field_name} must be of type str, list or None')

    def __get_media_requests(self, url, item, image_settings, counter=1) -> Request:
        # create Request with meta attribute from item to create the image name from them later
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
            image_paths = []
            for result in results:
                if result['url'] in item[image_field_name]:
                    image_paths.append(result['path'])
            item[image_settings['path_field']] = image_paths
        return item

    def __image_folder(self, image_folder: str) -> str:
        """append slash to image_folder string if not present"""
        if not image_folder.endswith('/'):
            image_folder += '/'
        return image_folder

    def file_path(self, request, response=None, info=None) -> str:
        """create and return the path to which the image should be saved"""
        image_folder = self.__image_folder(request.meta['image_folder'])
        return f'{image_folder}{request.meta["image_name"]}-{request.meta["image_count"]}.jpg'
