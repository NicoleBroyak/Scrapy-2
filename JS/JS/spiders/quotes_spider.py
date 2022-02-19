import scrapy
from .scraper.scraper import scrap
import os


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = scrap.scrap_url_list('http://quotes.toscrape.com/js/')

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
    
    def close(self, spider):
        for url in spider.start_urls:
            os.remove(url[7:])
            print(url)
