from dotenv import load_dotenv

from spiders.product import ProductSpider
from executor import CrawlerExecutor

if __name__ == '__main__':
    load_dotenv('.env')
    
    CrawlerExecutor(
        spider=ProductSpider
    ).execute()

# End Of File