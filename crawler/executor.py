from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider
from scrapy.utils.project import get_project_settings


class CrawlerExecutor(CrawlerProcess):

    def __init__(self, spider:CrawlSpider, settings=None, install_root_handler=True):
        default_settings = get_project_settings()
        if settings is not None:
            default_settings.update(settings)
        
        super().__init__(settings=settings, install_root_handler=install_root_handler)
        self.__spider = spider

    def execute(self):
        self.crawl(crawler_or_spidercls=self.__spider)
        self.start()

# End Of File