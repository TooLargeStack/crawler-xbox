from typing import List

from scrapy.selector import Selector

from crawler.models.response_model import ResponseModel
from crawler.sitemap import sitemap


class Home(ResponseModel):
    
    name: str = 'home'
    sitemap: sitemap.home

    def __init__(self, response) -> None:
        super().__init__(response=response)

    @property
    def explore_games(self) -> List[Selector]:
        return self.response.xpath(self.sitemap.explore_games).get()

# End Of File