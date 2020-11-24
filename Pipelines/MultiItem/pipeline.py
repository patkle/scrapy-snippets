from __future__ import annotations
import os

class MultiItemPipeline(object):
    """Pipeline that can save different items in different files and formats, depending on their class"""
    _exporter_for_item = {}

    def __init__(self, crawler):
        self.stats = crawler.stats
        settings = crawler.settings
        self.exporters = settings.get('EXPORTERS', {})
        self.__set_output_directory(settings.get('OUTPUT_DIRECTORY', 'out'))
    
    @classmethod
    def from_crawler(cls, crawler) -> MultiItemPipeline:
        return cls(crawler)

    def process_item(self, item, spider):
        self.__export_item(item)
        return item

    def __set_output_directory(self, directory: str) -> None:
        """create output directory if it does not exist yet"""
        # ensure that directory path ends with a slash
        if not directory.endswith('/'):
            directory = directory + '/'
        # check if directory already exists
        if not os.path.exists(directory):
            # create directory
            os.mkdir(directory)
        self.output_directory = directory

    def __create_output_file(self, filename: str):
        file_path = self.output_directory + filename
        for i in range(1, 999999):
            if not os.path.exists(file_path + f'_{i}'):
                file_path = f'{file_path}_{i}'
                open(file_path, 'w').close()
                return file_path

    def close_spider(self, spider):
        # close all item exporters when spider finishes 
        for exporter in self._exporter_for_item.values():
            exporter.finish_exporting()

    def __export_item(self, item):
        """export item with exporter according to settings"""
        class_name = item.__class__.__name__
        exporter = self._exporter_for_item.get(class_name, None)
        if exporter is None:
            exporter = self.__start_exporter(class_name)
        self.stats.inc_value(class_name)
        exporter.export_item(item)

    def __start_exporter(self, class_name):
        filename, exporter_class = self.__get_exporter_class_by_item_class(class_name)
        file_path = self.__create_output_file(filename)
        exporter = exporter_class(open(file_path, 'wb'))
        exporter.start_exporting()
        self._exporter_for_item[class_name] = exporter
        self.stats.set_value(filename, 0)
        return exporter

    def __get_exporter_class_by_item_class(self, class_name: str):
        for filename in self.exporters:
            if class_name in self.exporters[filename]['item'].__name__:
                return filename, self.exporters[filename]['exporter']
