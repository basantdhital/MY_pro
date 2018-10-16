
import scrapy

class ScrapyBarItem(scrapy.Item):
	bar_name = scrapy.Field()
	bar_category = scrapy.Field()
	bar_price_range = scrapy.Field()
	num_reviews = scrapy.Field() 
	num_stars = scrapy.Field()
	bar_bestnights = scrapy.Field() 
	bar_nhood = scrapy.Field()
	bar_phone = scrapy.Field()
	bar_reservations = scrapy.Field()
	creditcard = scrapy.Field()
	bar_parking = scrapy.Field()
	bar_wheelchair = scrapy.Field()
	bar_dancing = scrapy.Field()
	bar_happy = scrapy.Field()
	bar_outdoor = scrapy.Field()
	bar_tV = scrapy.Field()
	bar_pool_table = scrapy.Field()
