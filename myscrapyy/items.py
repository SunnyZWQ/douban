# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class bookLink(scrapy.Item):
    book_name = scrapy.Field()
    book_link = scrapy.Field()


class book(scrapy.Item):
    book_name = scrapy.Field()
    ave_rate = scrapy.Field()
    comment_num = scrapy.Field()
    rate5 = scrapy.Field()
    rate4 = scrapy.Field()
    rate3 = scrapy.Field()
    rate2 = scrapy.Field()
    rate1 = scrapy.Field()
    author = scrapy.Field()
    original_name = scrapy.Field()
    translator = scrapy.Field()
    public_year = scrapy.Field()
    pages = scrapy.Field()
    price = scrapy.Field()
    packing = scrapy.Field()
    ISBN = scrapy.Field()

























