# -*- coding: utf-8 -*-
import os

class MultiItemPipeline(object):
    def __init__(self, crawler):
        self.stats = crawler.stats
        self.settings = crawler.settings
        self.exporters = self.settings.get('EXPORTERS', {})
        self.export_path = self.__create_directory(self.settings.get('OUTPUT_DIRECTORY', 'out'))
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def __create_directory(self, directory):
        if not directory.endswith('/'):
            directory = directory + '/'
        if not os.path.exists(directory):
            os.mkdir(directory)
        return directory

    def open_spider(self, spider):
        self.__exporter_for_item = {}

    def __start_exporter(self, filename, exporter_class):
        file_path = self.__create_output_file(filename)
        exporter = exporter_class(open(file_path, 'wb'))
        exporter.start_exporting()
        self.stats.set_value(filename, 0)
        return exporter

    def __create_output_file(self, filename):
        file_path = self.export_path + filename
        for i in range(1, 999999):
            if not os.path.exists(file_path + f'_{i}'):
                file_path = file_path + f'_{i}'
                f = open(file_path, 'w') 
                f.close()
                return file_path

    def close_spider(self, spider):
        for exporter in self.__exporter_for_item.values():
            exporter.finish_exporting()

    def get_exporter_by_class_name(self, class_name):
        for exporter in self.exporters:
            if class_name in self.exporters[exporter]['item'].__name__:
                return exporter, self.exporters[exporter]['exporter']

    def __add_exporter(self, class_name):
        if class_name not in self.__exporter_for_item:
            filename, exporter_class = self.get_exporter_by_class_name(class_name)
            exporter = self.__start_exporter(filename, exporter_class)
            self.__exporter_for_item[class_name] = exporter

    def get_exporter_for_item(self, item):
        class_name = item.__class__.__name__
        self.__add_exporter(class_name)
        self.stats.inc_value(class_name)
        return self.__exporter_for_item[class_name]

    def process_item(self, item, spider):
        exporter = self.get_exporter_for_item(item)
        exporter.export_item(item)
        return item