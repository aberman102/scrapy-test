# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockxV2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_title = scrapy.Field()
    ticker = scrapy.Field()
    condition = scrapy.Field()
    description = scrapy.Field()
    lowest_ask = scrapy.Field()
    highest_bid = scrapy.Field()
    category = scrapy.Field()
    style = scrapy.Field()
    color = scrapy.Field()
    retail_price = scrapy.Field()
    release_date = scrapy.Field()
    year_high = scrapy.Field()
    year_low = scrapy.Field()
    annual_sales_quant = scrapy.Field()
    avg_sales_price = scrapy.Field()
    #dimension = scrapy.Field()
    #material = scrapy.Field()
    #hardware = scrapy.Field()

  
