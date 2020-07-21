# -*- coding: utf-8 -*-
import scrapy
from ..items import Doubanmovietop250Item


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # 首先爬取电影列表
        movie_list = response.xpath("//ol[@class='grid_view']/li")
        for selector in movie_list:
            # 遍历电影列表，从每个电影条目中抓取所需要的信息并保存为item对象
            item = Doubanmovietop250Item()

            item['ranking'] = selector.xpath(".//div[@class='pic']/em/text()").extract_first()
            item['movie_id'] = selector.xpath(".//div[@class='pic']/a[1]/@href").extract_first().lstrip('https://movie.douban.com/subject/').rstrip('/')
            item['name'] = selector.xpath(".//span[@class='title']/text()").extract_first()
            text = selector.xpath(".//div[@class='bd']/p[1]/text()").extract()
            info = ""
            for s in text:  # 将简介放到一个字符串
                info += " ".join(s.split())  # 去掉空格
            item['info'] = info
            item['rating'] = selector.css('.rating_num::text').extract_first()
            item['comments_num'] = selector.xpath(".//div[@class='star']/span[4]/text()").extract_first().rstrip('人评价')
            item['quote'] = selector.xpath(".//span[@class='inq']/text()").extract_first()
            item['poster_url'] = selector.xpath(".//div[@class='pic']/a[1]/img[1]/@src").extract_first()

            yield item  # 将结果item对象返回给Item管道

        # 爬取网页中的下一个页面的url
        next_page = response.xpath("//span[@class='next']/a[1]/@href").extract_first()
        if next_page:
            next_page = "https://movie.douban.com/top250" + next_page
            # 将Request请求提交给调度器
            yield scrapy.Request(next_page, callback=self.parse)
