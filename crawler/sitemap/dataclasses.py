from dataclasses import dataclass


@dataclass
class Home:
    
    name = 'home'

    explore_games: str
    

@dataclass
class Games:
    
    name = 'games'
    
    all_games: str
    

@dataclass
class AllGames:
    
    name = 'all_games'
    
    access_link: str
    data_script: str
    products_regex: str
    
    
@dataclass
class Product:
    
    name = 'product'
    
    purchase_section: str
    details: str
    title: str
    pricing: str
    original_price: str
    discount_price: str
    detail_price: str


@dataclass
class SiteMap:
    # The attributes must be added acording
    # the maped pages.

    name = 'sitemap'

    # One for each page.
    home: Home
    games: Games
    all_games: AllGames
    product: Product


# add each maped dataclass
all_dataclasses = [
    Home,
    Games,
    AllGames,
    Product,
]

# End Of File