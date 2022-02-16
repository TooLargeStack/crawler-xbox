from re import findall
from typing import List

from models.response_model import ResponseModel
from sitemap import sitemap


class Game(ResponseModel):
    
    name: str = 'game'
    sitemap: sitemap.game

    def __init__(self, response, product_id=None) -> None:
        super().__init__(response=response)
        
        self.product_id = product_id
        self.__prices = []
        
    @staticmethod
    def get_url(product_id: str) -> str:
        return f"https://www.xbox.com/pt-br/games/store/u/{product_id}"
    
    @property
    def prices(self) -> List[str]:
        return self.__prices
    
    @prices.setter
    def prices(self, prices: List[str]):
        self.__prices = prices

    @property
    def title(self) -> str:
        return self.response.xpath(
            self.sitemap.title
        ).get(default='Title not found').strip()
        
    def set_prices(self):
        prices = self.response.xpath(
            self.sitemap.prices.format(id=self.product_id)
        ).getall()
        self.prices = [
            self.string_to_float(
                value=price
            )
            for price in prices
        ] or ["0.0"]
    
    @property
    def original_price(self):
        return max(self.prices)
        
    @property
    def discount_price(self):
        if len(self.prices) > 1:
            return min(self.prices)
        return 0
    
    @property
    def image_link(self):
        return self.response.xpath(
            self.sitemap.image_link
        ).get('').strip()
        
    def string_to_float(self, value: str) -> float:
        """
        Get a string containing the number and convert it to a float.
        
        :param str value: The string to convert.
        
        :return: The float value.
        """
        
        return float(
            '.'.join(
                findall(
                    pattern='\d+',
                    string=value
                )
            ) or 0
        )


# End Of File