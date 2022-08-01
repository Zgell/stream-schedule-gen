'''
> image_downloader.py
Contains the ImageDownloader class, which is a subclass of the BoxArtScraper
class specifically for downloading box art for queried images and saving it
in this directory.
'''

from api.igdb import BoxArtScraper
from config.defaults import DEFAULT_AUTH_PATH as AUTH_PATH

import os
import requests

class ImageDownloader(BoxArtScraper):
    def __init__(self, auth = AUTH_PATH):
        super().__init__(auth)

    def clear_cached_box_art(self):
        '''Deletes any monday/wednesday/friday pics left over'''
        FILES = ['images/temp/monday.png', 'images/temp/wednesday.png', 'images/temp/friday.png']
        for f in FILES:
            if os.path.exists(f):
                os.remove(f)
            else:
                raise FileNotFoundError('Box art {} not detected!'.format(f))

    def download_box_art(self, fname: str, url: str):
        # Found here: https://stackoverflow.com/questions/30229231/python-save-image-from-url
        image_data = requests.get(url).content
        with open(fname, 'wb') as f:
            f.write(image_data)
            f.close()

    def download_box_art_from_query(self, fname: str, query: str):
        url = self.scrape_box_art(query)
        self.download_box_art(fname, url)
