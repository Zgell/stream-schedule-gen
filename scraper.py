'''
scraper.py

Fetches game box art from IGDB.
'''

import requests

class BoxArtScraper():
    def __init__(self, game: str):
        self.game_title_raw = game

    def get_box_art_url(self) -> str:
        '''Gets the URL for a game's IGDB page from its name'''
        URL_CONST = 'https://www.twitch.tv/search?term='
        query = self.raw_game_title.lower()
        return "{}{}".format(URL_CONST, query)

    def scrape_game_art(self):
        '''
        Strategy for scraping game art:
        1) Create a query on twitch.tv for the game
        2) Find the "Categories" section and find a link to the top game in categories
        3) From that page, scrape the box art (that's where the highest resolution one lives)
        '''
        # Fetch game page
        url = self.get_box_art_url()
        page = requests.get(url)
