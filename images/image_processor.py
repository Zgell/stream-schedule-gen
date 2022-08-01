'''
> image_processor.py
Contains the ImageProcessor class, which takes in all the source material and
'''

from config.defaults import (BOX_ART_RESIZE, MONDAY_POS, WEDNESDAY_POS, FRIDAY_POS, 
PRIMARY_FONT_SIZE, DATE_FONT_SIZE)

from datetime import datetime
from math import sqrt
import os
from PIL import Image, ImageDraw, ImageFont

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

    def apply_gradient(self, boxart: Image) -> Image:
        '''Applies a gradient to a box art image.'''
        game_art = boxart.copy()  # There's a weird bug where boxart is modified by the function otherwise
        if game_art.mode != 'RGBA':
            game_art.convert('RGBA')
        gradient = Image.open('templates/gradient.png').convert('RGBA')
        game_art.paste(gradient, (0, 0), gradient)
        return game_art

    def draw_spaced_text(self, text: str, font: ImageFont, kerning: int = 0) -> Image:
        '''Returns a text image object with custom spacing.'''
        text_width = font.getbbox(text)[2] + (kerning * (len(text) - 1))
        text_height = font.getbbox(text)[3]
        text_size = (text_width, text_height)

        img = Image.new('L', text_size)
        imdraw = ImageDraw.Draw(img)
        acc = ''  # Accumulator for the text
        for char in text:
            if acc == '':
                current_width = 0
            else:
                current_width = font.getbbox(acc)[2] + (kerning * len(acc))
            imdraw.text((current_width, 0), char, font=font, fill=255)
            acc += char

        return img


    def apply_text(self, boxart: Image, title: str = 'LIVE ON TWITCH', date_text: str = 'SOMEDAY', 
                    spacing_main: int = 0, spacing_date: int = 0) -> Image:
        '''Adds the title and date text to the image, after getting a gradient'''
        RELATIVE_TITLE_POS = (201, 32)  #prev: 217
        RELATIVE_DATE_POS = (156, 32)  # prev: 172
        # Ensure title/date text are all uppercase
        title = title.upper()
        date_text = date_text.upper()

        game_art = boxart.copy()
        main_font = ImageFont.truetype('fonts/montserrat-bold.ttf', PRIMARY_FONT_SIZE)
        date_font = ImageFont.truetype('fonts/montserrat-regular.ttf', DATE_FONT_SIZE)
        main_text_size = main_font.getbbox(title)[2:]  # First two tuple vars are irrelevant
        date_text_size = date_font.getbbox(date_text)[2:]  # Same as above

        # To rotate text, create an image, rotate it, and paste it on boxart
        # see here: https://stackoverflow.com/questions/245447/how-do-i-draw-text-at-an-angle-using-pythons-pil
        # Do the main title text
        '''
        main_text_img = Image.new('L', main_text_size)
        main_imdraw = ImageDraw.Draw(main_text_img)
        main_imdraw.text((0, 0), title, font=main_font, fill=255)  # Adds text to main_text_img
        '''
        main_text_img = self.draw_spaced_text(title, main_font, spacing_main)  # Generate text
        # Before generating text, see if text is too big. Width shouldn't exceed 586 (650-2*32).
        main_text_size = main_font.getbbox(title)[2:]
        if main_text_size[0] > 586:
            main_text_img = main_text_img.resize((586, main_text_size[1]))
        main_text_img = main_text_img.rotate(90, expand=True)
        # Do the date text
        ''''
        date_text_img = Image.new('L', date_text_size)
        date_imdraw = ImageDraw.Draw(date_text_img)
        date_imdraw.text((0, 0), date_text, font=date_font, fill=255)
        '''
        date_text_img = self.draw_spaced_text(date_text, date_font, spacing_date)
        # Perform the same size check as above, although this should never fail
        date_text_size = date_font.getbbox(date_text)[2:]
        if date_text_size[0] > 586:
            date_text_img = date_text_img.resize((586, date_text_size[1]))
        date_text_img = date_text_img.rotate(90, expand=True)
        # Paste the images onto the main image
        game_art.paste(main_text_img, RELATIVE_TITLE_POS, main_text_img)
        game_art.paste(date_text_img, RELATIVE_DATE_POS, date_text_img)
        return game_art
        
    def generate_schedule(self, monday_text='Streaming', wednesday_text='Streaming', friday_text='Streaming') -> Image:
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

        # Add text to the box arts
        monday = self.apply_text(monday, spacing_main=10, spacing_date=6)
        wednesday = self.apply_text(wednesday, spacing_main=10, spacing_date=6)
        friday = self.apply_text(friday, spacing_main=10, spacing_date=6)

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

