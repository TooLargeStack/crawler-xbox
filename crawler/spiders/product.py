from scrapy.spiders import Spider
from scrapy.http.request import Request
from scrapy.responsetypes import Response

from crawler.models import Home


class ProductSpider(Spider):
    
    name = 'product_spider'
    
    base_url = 'https://www.xbox.com/pt-BR/'
    start_urls = [base_url]
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        
        self.home = Home
        
    def parse(self, response: Response):
        home = self.home(response)
        
        yield Request(
            url=home.explore_games,
            callback=self.parse_games
        )
    
    def parse_games(self, response: Response):
        pass
    
    def parse_all_games(self, response: Response):
        pass
    
    def parse_products(self, response: Response):
        pass
    
# End Of File