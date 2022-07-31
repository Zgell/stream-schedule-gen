'''
> image_processor.py
Contains the ImageProcessor class, which takes in all the source material and
'''

from config.defaults import BOX_ART_RESIZE, MONDAY_POS, WEDNESDAY_POS, FRIDAY_POS

from datetime import datetime
import os
from PIL import Image

class ImageProcessor:
    def __init__(self):
        pass

    def get_schedule_name(self) -> str:
        '''Returns the filename of the schedule (a function of the date)'''
        date_code = datetime.today().strftime('%Y-%m-%d')
        return date_code + '.png'

    def clean_box_art(self):
        '''Deletes the generated box art images'''
        FILES = ['images/temp/monday.png', 'images/temp/wednesday.png', 'images/temp/friday.png']
        for img in FILES:
            if os.path.exists(img):
                os.remove(img)
                print('Removed images/{}'.format(img))
            else:
                raise FileNotFoundError('Box art {} not detected!'.format(img))

    def generate_schedule(self) -> Image:
        '''Generates the schedule image and saves it'''
        # Load schedule template + three box art images
        TEMPLATE_FILENAME = 'templates/schedule.png'
        schedule = Image.open(TEMPLATE_FILENAME)
        MONDAY = Image.open('images/temp/monday.png').resize(BOX_ART_RESIZE)
        WEDNESDAY = Image.open('images/temp/wednesday.png').resize(BOX_ART_RESIZE)
        FRIDAY = Image.open('images/temp/friday.png').resize(BOX_ART_RESIZE)

        # Superimpose the box arts on the schedule using Image.paste
        # (see here: https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=paste#PIL.Image.Image.paste)
        schedule.paste(MONDAY, MONDAY_POS)
        schedule.paste(WEDNESDAY, WEDNESDAY_POS)
        schedule.paste(FRIDAY, FRIDAY_POS)

        # Add text?

        # Return a copy of the image object (change this later??? idk)
        return schedule

