# -*- coding: utf-8 -*-
from scrapy.exporters import CsvItemExporter, JsonItemExporter
import os
from .settings import OUTPUT_DIRECTORY, EXPORTERS

class MultiItemPipeline(object):
    def __init__(self):
        self.__output_directory = self.__create_output_directory()
        self.__exporter_settings = EXPORTERS

    def __create_output_directory(self):
        if not OUTPUT_DIRECTORY.endswith('/'):
            directory = OUTPUT_DIRECTORY + '/'
        else:
            directory = OUTPUT_DIRECTORY
        if not os.path.exists(directory):
            os.mkdir(directory)
        return directory

    def open_spider(self, spider):
        self.__exporter_for_item = {}
        for exporter, values in self.__exporter_settings.items():
            ex = self.start_exporter(exporter, values['exporter'])
            self.__exporter_for_item[values['item'].__name__] = ex

    def start_exporter(self, name, exporter_class=CsvItemExporter):
        filename = self.__create_output_file(name)
        exporter = exporter_class(open(filename, 'wb'))
        exporter.start_exporting()
        return exporter

    def __create_output_file(self, filename):
        filepath = self.__output_directory + filename
        for i in range(1, 999999):
            if not os.path.exists(filepath + f'_{i}'):
                filepath = filepath + f'_{i}'
                f = open(filepath, 'w') 
                f.close()
                return filepath

    def close_spider(self, spider):
        for exporter in self.__exporter_for_item.values():
            exporter.finish_exporting()

    def _exporter_for_item(self, item):
        item_class_name = item.__class__.__name__
        return self.__exporter_for_item[item_class_name]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item