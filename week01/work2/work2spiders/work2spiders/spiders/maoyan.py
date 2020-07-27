# -*- coding: utf-8 -*-
import scrapy
from work2spiders.items import Work2SpidersItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        movies = Selector(response=response).xpath(
            '//div[@class="movie-hover-info"]')

        for movie in movies:
            item=Work2SpidersItem()
            # name= movie.xpath('./div[@class="movie-hover-title"]/span[@class="name"]/text()')
            # name= movie.xpath('./div[@class="movie-hover-title"]/span[@class="name "]/text()')
            item['movie_name']= movie.xpath('./div[@class="movie-hover-title"]/span[@class="name "]/text()').extract_first()
            item['movie_type']= movie.xpath('./div[2]/text()[2]').extract_first()
            item['movie_time']=movie.xpath('./div[4]/text()[2]').extract_first()
            yield item

        # for a in range(1, 10):
        #     item = Work2SpidersItem()
        #     item['movie_name'] = a*2
        #     item['movie_type'] = a*3
        #     item['movie_time'] = a*4
            
        #     yield item
            # item['movie_type']= movie.xpath('./div[2]/text()')
            # item['movie_time']= movie.xpath('./div[4]/text()')
