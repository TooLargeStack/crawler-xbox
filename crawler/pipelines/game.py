from re import findall

from items.game import GameItem


class GamePipeline:
    
    item_type = GameItem
    
    def process_item(self, item, spider):
        if type(item) != self.item_type:
            return item
        
        item.set_default('title', "not found")
        item.set_default('original_price', "0.0")
        item.set_default('discount_price', "0.0")
        
        return {
            "title": item['title'].strip(),
            "originalPrice": self.string_to_float(
                value=item['original_price'].strip()
            ),
            "discountPrice": self.string_to_float(
                value=item['discount_price'].strip()
            )
        }
        
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
            )
        )

# End Of File