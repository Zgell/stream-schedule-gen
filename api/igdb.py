'''
> igdb.py
Handles all connections to the IGDB database (igdb.com).
Contains the BoxArtScraper class, which handles all API stuff for IGDB.
'''

from api.twitch import TwitchHandler
from config.defaults import DEFAULT_AUTH_PATH as AUTH_PATH

from igdb.wrapper import IGDBWrapper
import json

class BoxArtScraper:
    def __init__(self, auth = AUTH_PATH):
        self.twitch = TwitchHandler(authpath=auth)
        self.twitch.fetch_credentials()
        self.twitch.fetch_access_token()
        client_id = self.twitch.get_client_id()
        access_token = self.twitch.get_access_token()

        self.igdb_api = IGDBWrapper(client_id, access_token)

    ''' Getters / Helper Functions '''
    def get_box_art_url(self, filename: str) -> str:
        # return 'https://images.igdb.com/igdb/image/upload/t_cover_big_2x/{}'.format(filename)
        BASE_URL = 'https://images.igdb.com/igdb/image/upload/t_cover_big_2x/'
        return BASE_URL + filename

    ''' Scraping '''
    def scrape_box_art(self, query: str) -> str:
        '''
        Takes in the name of a game (query) and returns a URL to an image of
        the box art for the queried game. Powered by the IGDB API.
        It does this using 3 queries to the API:
        1) First query finds the database ID for the game.
        2) Second query uses the game ID to find the cover art ID
        (because that's a separate ID, for some reason)
        3) Third query uses the cover art ID to find the cover art location.

        For more info on the queries, read up on APIcalypse in the IGDB docs.
        '''
        '''TODO: (Maybe) write my own IGDB API wrapper inspired by IGDBWrapper?'''
        # Step 1: Get the Game ID from the game's name
        game_id_response = json.loads(
            self.igdb_api.api_request('games', 'search "{}"; where version_parent = null;'.format(query))
        )
        game_id = game_id_response[0]['id']
        # Step 2: Get the game's cover art's ID from the game ID
        cover_id_response = json.loads(
            self.igdb_api.api_request('games', 'fields cover; where id = {};'.format(str(game_id)))
        )
        cover_id = cover_id_response[0]['cover']
        # Step 3: Get the cover art's filepath from its ID
        box_art_response = json.loads(
            self.igdb_api.api_request('covers', 'fields url; where id = {};'.format(str(cover_id)))
        )
        # Parse the file name (it's a filepath, but an incomplete one that doesn't work)
        box_art_fname = box_art_response[0]['url'].split('/')[-1]
        # Create the proper filepath using helper function
        box_art_url = self.get_box_art_url(box_art_fname)

        return box_art_url

