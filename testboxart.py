'''
A test case for the Twitch API access and box art scraping.
'''

from api.igdb import BoxArtScraper

if __name__ == '__main__':
    scraper = BoxArtScraper(auth='config/auth.json')
    print('-= Twitch API Information =-')
    print('Client ID:     ', scraper.twitch.client_id)
    print('Client Secret: ', scraper.twitch.client_secret)
    print('Access Token:  ', scraper.twitch.access_token)
    print('')
    print('-= IGDB API Test =-')
    print('Type in the name of a game on IGDB:')
    title = input()
    print('Retrieving box art for given title...')
    url = scraper.scrape_box_art(title)
    print('Box art URL: ', url)
    # access_token = get_access_token()
    # print('ACCESS TOKEN:', access_token)

    # # wrapper = IGDBWrapper(CLIENT_ID, access_token)
    # print("Enter the name of the game you wish to retrieve: ")
    # game_name = input('')
    # url = get_box_art_from_name(game_name, CLIENT_ID, access_token)
    # print('URL: ', url)