# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubanmovietop250Item(scrapy.Item):
    ranking = scrapy.Field()
    movie_id = scrapy.Field()
    name = scrapy.Field()
    info = scrapy.Field()
    rating = scrapy.Field()
    comments_num = scrapy.Field()
    quote = scrapy.Field()
    poster_url = scrapy.Field()
    pass
