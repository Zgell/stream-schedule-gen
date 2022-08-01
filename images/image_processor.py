'''
> image_processor.py
Contains the ImageProcessor class, which takes in all the source material and
'''

from config.defaults import BOX_ART_RESIZE, MONDAY_POS, WEDNESDAY_POS, FRIDAY_POS

from datetime import datetime
from math import sqrt
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

    def apply_black_gradient(self, input_im: Image, gradient=1., initial_opacity=1.):
        """
        Applies a black gradient to the image, going from left to right.

        Arguments:
        ---------
            path_in: string
                path to image to apply gradient to
            path_out: string (default 'out.png')
                path to save result to
            gradient: float (default 1.)
                gradient of the gradient; should be non-negative;
                if gradient = 0., the image is black;
                if gradient = 1., the gradient smoothly varies over the full width;
                if gradient > 1., the gradient terminates before the end of the width;
            initial_opacity: float (default 1.)
                scales the initial opacity of the gradient (i.e. on the far left of the image);
                should be between 0. and 1.; values between 0.9-1. give good results
        """
        # get image to operate on
        if input_im.mode != 'RGBA':
            input_im = input_im.convert('RGBA')
        width, height = input_im.size

        # create a gradient that
        # starts at full opacity * initial_value
        # decrements opacity by gradient * x / width
        # Size: width x 1
        max_dimension = int(sqrt(width**2 + height**2))
        alpha_gradient = Image.new('L', (width, 1), color=0xFF)  # (width, 1)
        for x in range(width):
            a = int((initial_opacity * 255.) * (1. - gradient * float(x)/width))
            if a > 0:
                alpha_gradient.putpixel((x, 0), a)
            else:
                alpha_gradient.putpixel((x, 0), 0)
            # print '{}, {:.2f}, {}'.format(x, float(x) / width, a)
        alpha = alpha_gradient.resize((width, height))
        alpha = alpha.rotate(210)

        # create black image, apply gradient
        black_im = Image.new('RGBA', (width, height), color=0) # i.e. black
        black_im.putalpha(alpha)

        # make composite with original image
        output_im = Image.alpha_composite(input_im, black_im)
        return output_im

    def apply_gradient(self, boxart: Image) -> Image:
        '''Applies a gradient to a box art image.'''
        game_art = boxart.copy()  # There's a weird bug where boxart is modified by the function otherwise
        if game_art.mode != 'RGBA':
            game_art.convert('RGBA')
        gradient = Image.open('templates/gradient.png').convert('RGBA')
        game_art.paste(gradient, (0, 0), gradient)
        return game_art
        

    def generate_schedule(self) -> Image:
        '''Generates the schedule image and saves it'''
        # Load schedule template + three box art images
        TEMPLATE_FILENAME = 'templates/schedule.png'
        schedule = Image.open(TEMPLATE_FILENAME)
        monday = Image.open('images/temp/monday.png').resize(BOX_ART_RESIZE)
        wednesday = Image.open('images/temp/wednesday.png').resize(BOX_ART_RESIZE)
        friday = Image.open('images/temp/friday.png').resize(BOX_ART_RESIZE)

        # Modify the box arts with gradients
        monday = self.apply_gradient(monday)
        wednesday = self.apply_gradient(wednesday)
        friday = self.apply_gradient(friday)

        # Superimpose the box arts on the schedule using Image.paste
        # (see here: https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=paste#PIL.Image.Image.paste)
        schedule.paste(monday, MONDAY_POS)
        schedule.paste(wednesday, WEDNESDAY_POS)
        schedule.paste(friday, FRIDAY_POS)

        # Add a gradient for the text
        if schedule.mode != 'RGBA':
            schedule = schedule.convert('RGBA')
        # schedule = self.apply_black_gradient(schedule)
        # Add text?

        # Return a copy of the image object (change this later??? idk)
        return schedule

