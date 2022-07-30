def print_title_card():
    '''Imports the text in templates/titlecard.txt and prints it'''
    TITLE_CARD_DIR = 'templates/titlecard.txt'
    f = open(TITLE_CARD_DIR, 'r')
    title_text = f.read()
    print(title_text)
    f.close()

def generate_google_image_search(query: str) -> str:
    '''
    Returns the URL to be searched for finding game art of an input string.

    Resources:
    https://stackoverflow.com/questions/21530274/format-for-a-url-that-goes-to-google-image-search
    https://stenevang.wordpress.com/2013/02/22/google-advanced-power-search-url-request-parameters/
    '''
    processed_query = query.lower().replace(' ', '+')
    # For Google URLs, the "?tbm=isch" just specifies image search, and "q" specifies query.
    return "https://www.google.com/search?tbm=isch&q={}".format(processed_query)


if __name__ == '__main__':
    # First, print the title card
    print_title_card()

    # Take the arguments from the user
    print('Enter the games you plan on streaming this week.')
    print('Games are not caps-sensitive, but remember that the output is determined by the results of Google images.')
    print('')
    monday_title = input('Enter the game you wish to stream on Monday: ')
    print('')
    wednesday_title = input('Enter the game you wish to stream on Wednesday: ')
    print('')
    friday_title = input('Enter the game you wish to stream on Friday: ')
    print('')
    print('Your results:', monday_title, wednesday_title, friday_title)
    
    # Get images for the three titles and download them
    # Images are sourced from twitch's categories database