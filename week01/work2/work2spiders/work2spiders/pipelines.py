# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class Work2SpidersPipeline:
    def process_item(self, item, spider):

        with open('data.csv', 'a+', encoding="utf8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [item['movie_name'], item['movie_type'], item['movie_time']])
        return item
