from typing import List

from scrapy.selector import Selector

from models.response_model import ResponseModel
from sitemap import sitemap


class Games(ResponseModel):
    
    name: str = 'games'
    sitemap: sitemap.games

    def __init__(self, response) -> None:
        super().__init__(response=response)

    @property
    def all_games(self) -> str:
        return self.response.xpath(
            self.sitemap.all_games
        ).get().split('?')[0]

# End Of File