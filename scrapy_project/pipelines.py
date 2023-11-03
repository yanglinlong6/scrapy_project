# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# scrapy startproject project_name
# scrapy genspider get_data
# scrapy crawl  get_data

class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        return item
