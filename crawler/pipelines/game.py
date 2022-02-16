from re import findall

from scrapy.exceptions import DropItem

from items.game import GameItem


class GamePipeline:
    
    item_type = GameItem
    
    def process_item(self, item, spider):
        if type(item) != self.item_type:
            return item
        
        self.set_default_item(item)
        self.convert_string_numbers(item)
        return {
            "siteId": item['site_id'].strip(),
            "title": item['title'].strip(),
            "originalPrice": item['original_price'],
            "discountPrice": item['discount_price'],
            "imageLink": item['image_link'].strip(),
        }
        
    def set_default_item(self, item):
        
        item.setdefault('title', "not found")
        item.setdefault('original_price', 0.0)
        item.setdefault('discount_price', 0.0)
        item.setdefault('image_link', '')
        
    def check_valid_item(self, item):
        # TODO: add log here
        if item['original_price'] == 0 or not item['site_id']:
            print(f"item droped {item}")
            raise DropItem
        
    def convert_string_numbers(self, item):
        
        for key, value in item.items():
            if type(value) is str and key in (
                'original_price', 'discount_price'
            ):
                numbers = findall(
                    pattern='\d+',
                    string=value
                )
                if numbers:
                    print(value)
                    item[key] = float('.'.join(numbers))

# End Of File