'''
> image_processor.py
Contains the ImageProcessor class, which takes in all the source material and
'''

from config.defaults import BOX_ART_RESIZE, MONDAY_POS, WEDNESDAY_POS, FRIDAY_POS

from PIL import Image

class ImageProcessor:
    def __init__(self):
        pass

    def get_schedule_name(self) -> str:
        '''Returns the filename of the schedule (a function of the date)'''

    def generate_schedule(self):
        '''Generates the schedule image and saves it'''
        # Load schedule template + three box art images

        # Superimpose the box arts on the schedule using Image.paste
        # (see here: https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=paste#PIL.Image.Image.paste)

        # Add text?

        # Save schedule to file in output folder (name should be based off date)

