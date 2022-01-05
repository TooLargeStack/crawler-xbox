from typing import Union, List

from scrapy.responsetypes import Response
from scrapy.selector import Selector

from crawler.sitemap import sitemap


class ResponseModel:

    def __init__(self, response: Union[Selector, Response]) -> None:
        self.response: Union[Selector, Response] = response
        self.sitemap = getattr(sitemap, self.name)

# End Of File