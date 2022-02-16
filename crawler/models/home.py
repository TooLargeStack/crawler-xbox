from typing import List
from os import getenv

from scrapy.selector import Selector

from models.response_model import ResponseModel
from sitemap import sitemap


class Home(ResponseModel):
    
    name: str = 'home'
    sitemap: sitemap.home

    def __init__(self, response) -> None:
        super().__init__(response=response)
        
        self.__url = getenv('ACCESS_LINK')
        
    @property
    def url(self) -> str:
        return self.__url

    @property
    def explore_games(self) -> str:
        sufix_url = self.response.xpath(
            self.sitemap.explore_games
        ).get().split('/')[-1]
        return f"{self.url}{sufix_url}"

# End Of File