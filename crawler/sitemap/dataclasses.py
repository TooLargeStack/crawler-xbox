from dataclasses import dataclass


@dataclass
class Home:
    
    name = 'home'

    link: str


@dataclass
class SiteMap:
    # The attributes must be added acording
    # the maped pages.

    name = 'sitemap'

    home: Home
    # One for each page.


# add each maped dataclass
all_dataclasses = [
    Home,
]

# End Of File