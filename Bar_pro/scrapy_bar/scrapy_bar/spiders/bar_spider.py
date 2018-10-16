

from scrapy import Spider, Request
#from scrapy.selector import Selector
from scrapy_bar.items import ScrapyBarItem

class Scrapy_bar(Spider):
	name = 'bar_spider'
	allowed_urls = ['https://www.yelp.com/']
	#start_urls = ['https://www.yelp.com/search?find_desc=Bars&find_loc=Manhattan%2C+NY&ns=']
	# start_urls = ['https://www.yelp.com/search?find_desc=best+bars&find_loc=Manhattan,+NY&start='.format(x) for x in range(0,990,30)]


	# def parse(self, response):
	# 	rest_urls = response.xpath('//a[contains(@data-analytics-label,"biz-name")]//@href').extract()[1:]
	# 	rest_urls = ['https://www.yelp.com' + x for x in rest_urls]
	# 	for url in rest_urls:
	# 		yield Request(url=url,callback=self.parse_bar)



	start_urls = ['https://www.yelp.com/search?find_desc=bars&find_loc=Manhattan,+NY&start=' + str(n) for n in range(0,990,30)]


	def parse(self, response):
		rest_urls = response.xpath('//a[contains(@data-analytics-label,"biz-name")]//@href').extract()
		rest_urls = ['https://www.yelp.com' + x for x in rest_urls]

		for url in rest_urls:
			yield Request(url, callback=self.parse_rest)


	def parse_rest(self, response):
		bar_name = response.xpath('//h1[contains(@class,"biz-page-title embossed-text-white shortenough")]/text()').extract()[0]
		bar_category = response.xpath('//span[contains(@class,"category-str-list")]/a/text()').extract()[0]
		bar_price_range = response.xpath('//span[contains(@class,"business-attribute price-range")]/text()').extract()[0]
		num_reviews = int(response.xpath('//span[contains(@class,"review-count rating-qualifier")]/text()').extract()[0].split()[0])
		num_stars = float(response.xpath('//div[contains(@class,"biz-rating biz-rating-very-large clearfix")]//@title').extract()[0].split()[0])
		bar_nhood = response.xpath('//span[contains(@class,"neighborhood-str-list")]/text()').extract()[0].strip()
		bar_phone = response.xpath('//span[contains(@class,"biz-phone")]/text()').extract()[0].strip()

		key=response.xpath('//div[contains(@class,"short-def-list")]//dt/text()').extract()
		key = [x.strip() for x in key]

		value = response.xpath('//div[contains(@class,"short-def-list")]//dd/text()').extract()
		value =  [x.strip() for x in value]

		attributes = dict(zip(key,value))

		bar_reservations = (attributes['Takes Reservations'] if 'Takes Reservations' in attributes.keys() else 'N/A')
		creditcard = (attributes['Accepts Credit Cards'] if 'Accepts Credit Cards' in attributes.keys() else 'N/A')
		bar_bestnights = (attributes['Best Nights'] if 'Best Nights' in attributes.keys() else 'N/A')
		bar_parking = (attributes['Parking'] if 'Parking' in attributes.keys() else 'N/A')
		bar_wheelchair = (attributes['Wheelchair Accessible'] if 'Wheelchair Accessible' in attributes.keys() else 'N/A')
		bar_dancing = (attributes['Good For Dancing'] if 'Good For Dancing' in attributes.keys() else 'N/A')
		bar_happy = (attributes['Happy Hour'] if 'Happy Hour' in attributes.keys() else 'N/A')
		bar_outdoor = (attributes['Outdoor Seating'] if 'Outdoor Seating' in attributes.keys() else 'N/A')
		bar_tV = (attributes['Has TV'] if 'Has TV' in attributes.keys() else 'N/A')
		bar_pool_table = (attributes['Has Pool Table'] if 'Has Pool Table' in attributes.keys() else 'N/A')


		item = ScrapyBarItem()
		item['bar_name'] = bar_name
		item['bar_category'] = bar_category
		item['bar_price_range'] = bar_price_range
		item['num_reviews'] = num_reviews 
		item['num_stars'] = num_stars
		item['bar_bestnights'] = bar_bestnights 
		item['bar_nhood'] = bar_nhood
		item['bar_phone'] = bar_phone
		item['bar_reservations'] = bar_reservations
		item['creditcard'] = creditcard
		item['bar_parking'] = bar_parking
		item['bar_wheelchair'] = bar_wheelchair
		item['bar_dancing'] = bar_dancing
		item['bar_happy'] = bar_happy
		item['bar_outdoor'] = bar_outdoor
		item['bar_tV'] = bar_tV
		item['bar_pool_table'] = bar_pool_table


		yield item
