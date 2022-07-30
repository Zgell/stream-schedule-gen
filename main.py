def print_title_card():
    '''Imports the text in templates/titlecard.txt and prints it'''
    TITLE_CARD_DIR = 'templates/titlecard.txt'
    f = open(TITLE_CARD_DIR, 'r')
    title_text = f.read()
    print(title_text)
    f.close()


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