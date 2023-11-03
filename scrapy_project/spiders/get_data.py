import scrapy


class GetDataSpider(scrapy.Spider):
    name = 'get_data'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
