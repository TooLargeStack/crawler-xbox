from scrapy.spiders import Spider
from scrapy.http.request import Request
from scrapy.responsetypes import Response

from models import (
    Home, 
    Games,
    AllGames,
    Game,
)
from items.game import GameItem


class ProductSpider(Spider):
    
    name = 'product_spider'
    
    base_url = 'https://www.xbox.com/pt-BR/'
    start_urls = [base_url]
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        
        self.home = Home
        self.games = Games
        self.all_games = AllGames
        self.game = Game
        
    def parse(self, response: Response):
        home = self.home(response)
        
        yield Request(
            url=home.explore_games,
            callback=self.parse_games
        )
    
    def parse_games(self, response: Response):
        games = self.games(response)
        
        yield Request(
            url=games.all_games,
            callback=self.parse_all_games
        )
    
    def parse_all_games(self, response: Response):
        all_games = self.all_games(response)
        
        all_codes: list[str] = all_games.all_games_code
        for game_code in all_codes:
            yield Request(
                url=self.game.get_url(product_id=game_code),
                callback=self.parse_game,
                cb_kwargs={
                    'product_id': game_code
                }
            )
    
    def parse_game(self, response: Response, product_id=None):
        if not product_id:
            return
        game = self.game(response, product_id=product_id)
        game.set_prices()
        yield GameItem({
            'title': game.title,
            'site_id': product_id,
            'original_price': game.original_price,
            'discount_price': game.discount_price,
            'image_link': game.image_link
        })
    
# End Of File