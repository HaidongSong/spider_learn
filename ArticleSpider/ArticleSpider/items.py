# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CnblogsAriticleSpiderItem(scrapy.Item):
    title = scrapy.Field()
    create_time = scrapy.Field()
    news_poster = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    url_hash = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()

    digging_count = scrapy.Field()
    comment_nums = scrapy.Field()
    total_view = scrapy.Field()
