import pathlib
import scrapy
from scrapy.settings import Settings
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor


class CatItem(scrapy.Item):
    title = scrapy.Field()
    white = scrapy.Field()
    white_path = scrapy.Field()
    black = scrapy.Field()
    black_path = scrapy.Field()
    images = scrapy.Field()


class CatSpider(scrapy.Spider):
    name = 'cats'
    start_urls = ['https://commons.wikimedia.org/wiki/Category:Domestic_cats']

    def parse(self, response):
        title = response.xpath('.//h1/text()').get().replace('Category:', '')
        white = [
            'https://upload.wikimedia.org/wikipedia/commons/e/e5/Cat_mouse_1.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/7/72/Cat_In_My_Garden.jpg'
        ]
        black = [
            'https://upload.wikimedia.org/wikipedia/commons/e/e2/Black_Cat_Nala.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/28/Benson_-_Outside_%28wgtn%2C_churtprk%29.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/e/ef/Ahhh-sunlight_2_%2815447982169%29.jpg'
        ]
        yield CatItem(title=title, white=white, black=black)

def get_settings() -> Settings:
    """create and return a scrapy settings object"""
    settings = Settings()
    # get current working directory
    cwd = str(pathlib.Path().absolute())
    # set path in which to store images
    settings.set('IMAGES_STORE', cwd + '\\')
    settings.set('IMAGE_URL_FIELDS', {
        'white': {
            'name_field': 'title',
            'sub_folder': 'white',
            'path_field': 'white_path',
        }, 'black': {
            'name_field': 'title',
            'sub_folder': 'black',
            'path_field': 'black_path',
        }
    })
    # enable the pipeline
    settings.set('ITEM_PIPELINES', {
        'pipeline.ImageNamePipeline': 200
    })
    return settings

if __name__ == '__main__':
    # routine to run scrapy from a script
    # see: https://docs.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(CatSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
