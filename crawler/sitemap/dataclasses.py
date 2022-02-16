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
class Game:
    
    name = 'game'
    
    title: str
    prices: str
    image_link: str


@dataclass
class SiteMap:
    # The attributes must be added acording
    # the maped pages.

    name = 'sitemap'

    # One for each page.
    home: Home
    games: Games
    all_games: AllGames
    game: Game


# add each maped dataclass
all_dataclasses = [
    Home,
    Games,
    AllGames,
    Game,
]

# End Of File