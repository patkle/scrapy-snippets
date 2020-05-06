# -*- coding: utf-8 -*-
from scrapy.exporters import CsvItemExporter, JsonItemExporter
from .items import TestItem, Test2Item

OUTPUT_DIRECTORY = 'output'

EXPORTERS = {
    'test': {
        'item': TestItem,
        'exporter': CsvItemExporter
    }, 'test_2': {
        'item': Test2Item,
        'exporter': JsonItemExporter
    }
}
