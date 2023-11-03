import scrapy


class SaveDataSpider(scrapy.Spider):
    name = 'save_data'
    allowed_domains = ['api.vvhan.com']
    start_urls = ['http://api.vvhan.com/']

    def parse(self, response):
        pass
