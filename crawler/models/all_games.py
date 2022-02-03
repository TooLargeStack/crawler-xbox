from typing import List
from re import search
from json import loads

from models.response_model import ResponseModel
from sitemap import sitemap


class AllGames(ResponseModel):
    
    name: str = 'all_games'
    sitemap: sitemap.all_games

    def __init__(self, response) -> None:
        super().__init__(response=response)

    @property
    def access_link(self) -> str:
        return self.response.xpath(self.sitemap.explore_games).get()

    @property
    def data_script(self) -> str:
        return self.response.xpath(
            self.sitemap.data_script
        ).get()

    @property
    def products_regex(self) -> str:
        return self.sitemap.products_regex
    
    @property
    def all_games_code(self) -> List[str]:
        
        return list(
            loads(
                search(
                    pattern=self.products_regex,
                    string=self.data_script
                ).group(
                    2
                ) + '}'
            ).get(
                'data',
                {}
            ).keys()
        )

# End Of File