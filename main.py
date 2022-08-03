'''
> main.py
The file that runs the entire program when executed.
Asks the user for three DB search queries for box art,
plus three more game titles (the same three but fully stylized)
'''

from images.image_downloader import ImageDownloader
from images.image_processor import ImageProcessor

def print_title_card():
    '''Imports the text in templates/titlecard.txt and prints it'''
    TITLE_CARD_DIR = 'templates/titlecard.txt'
    f = open(TITLE_CARD_DIR, 'r')
    title_text = f.read()
    print(title_text)
    f.close()

if __name__ == '__main__':
    # Initialize relevant stuff
    scraper = ImageDownloader()
    processor = ImageProcessor()
    
    # First, print the title card
    print_title_card()

    # Take the arguments from the user
    print('Enter the games you plan on streaming this week.')
    print('Games are not caps-sensitive, but these terms are letter-sensitive (ie. you need to include accents and whatnot for it to be accurate).')
    print('')
    monday_title    = input('Enter the game you wish to stream on Monday:    ')
    print('')
    wednesday_title = input('Enter the game you wish to stream on Wednesday: ')
    print('')
    friday_title    = input('Enter the game you wish to stream on Friday:    ')
    print('')

    # Get images for the three titles and download them
    print('Cleaning cached box art...')
    scraper.clear_cached_box_art()
    print('Fetching query for Monday\'s stream...')
    scraper.download_box_art_from_query('images/temp/monday.png', monday_title)
    print('Fetching query for Wednesday\'s stream...')
    scraper.download_box_art_from_query('images/temp/wednesday.png', wednesday_title)
    print('Fetching query for Friday\'s stream...')
    scraper.download_box_art_from_query('images/temp/friday.png', friday_title)
    print('')
    
    # Generate schedule from the downloaded box art
    print('Now, label your three streams on the schedule.')
    print('(Basically retype all the game\'s names but EXACTLY how you want them formatted)')
    print('Default option: "STREAMING ON TWITCH" (just press enter without typing for this)')
    print('')
    monday_label    = input('Monday:    ')
    wednesday_label = input('Wednesday: ')
    friday_label    = input('Friday:    ')
    print('Generating schedule image...')
    schedule_img = processor.generate_schedule(monday_text=monday_label, wednesday_text=wednesday_label, friday_text=friday_label)
    # schedule_filename = 'output/{}'.format(processor.get_schedule_name())
    schedule_filename = processor.get_schedule_name()
    schedule_img.save(schedule_filename)
    print('Scheduled successfully generated! Image saved to {}'.format(schedule_filename))
    print('')
    print('Press any key to continue...')
    x = input('')
