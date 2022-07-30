'''
Used for generating an access token for the Twitch API.
'''
from igdb.wrapper import IGDBWrapper
import json
import requests

CLIENT_ID = 't0cc438a1wmij9in79okqz7lilla6w'
CLIENT_SECRET = 'pbgm4uhezqksc48uj1t66azxlnotfz'

def get_access_token():
    URL = 'https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials'.format(CLIENT_ID, CLIENT_SECRET)
    post_data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    # print('Sending POST request...')
    x = requests.post(URL, json=post_data, timeout=5.0)
    # print(type(x), x)
    print(x.text)
    x_json = json.loads(x.text)
    return x_json["access_token"]

def create_url(filename: str) -> str:
    '''Creates a URL to the cover art.'''
    return 'https://images.igdb.com/igdb/image/upload/t_cover_big_2x/{}'.format(filename)

def get_box_art_from_name(name: str, client_id: str, access_token: str) -> str:
    wrapper = IGDBWrapper(client_id, access_token)
    game_id_response = json.loads(wrapper.api_request('games', 'search "{}"; where version_parent = null;'.format(name)))
    game_id = game_id_response[0]['id']

    cover_id_response = json.loads(wrapper.api_request('games', 'fields cover; where id = {};'.format(str(game_id))))
    cover_id = cover_id_response[0]['cover']

    box_art_response = json.loads(wrapper.api_request('covers', 'fields url; where id = {};'.format(str(cover_id))))
    box_art_fname = box_art_response[0]['url'].split('/')[-1]
    box_art_url = create_url(box_art_fname)

    return box_art_url

if __name__ == '__main__':
    access_token = get_access_token()
    print('ACCESS TOKEN:', access_token)

    # wrapper = IGDBWrapper(CLIENT_ID, access_token)
    print("Enter the name of the game you wish to retrieve: ")
    game_name = input('')
    url = get_box_art_from_name(game_name, CLIENT_ID, access_token)
    print('URL: ', url)

    # Test
    # response = json.loads(wrapper.api_request('games', 'fields name; limit 10;'))
    # response = json.loads(wrapper.api_request('games', 'fields screenshots.*; where id = 1942;'))

    # response = json.loads(wrapper.api_request('games', 'search "Dark Souls 2"; where version_parent = null;'))
    # response_2 = json.loads(wrapper.api_request('games', 'fields cover; where id = 2368;'))
    # response_3 = json.loads(wrapper.api_request('covers', 'fields url; where id = 112344;'))
    # # response_3 = json.loads(wrapper.api_request('games', 'fields screenshots.*; where id = 2368;'))
    # print(response, '\n')
    # print(response_2, '\n')
    # print(response_3, '\n')
    # res = json.loads(wrapper.api_request('covers', '*; limit 10;'))

    # print(res, '\n')
    # import pdb; pdb.set_trace()
    # print([x for x in response_3 if x['width'] == 1280])

    # # Test POST request
    # post_data = "fields name; limit 10;"
    # post_headers = {
    #     'Content-Type': 'text/plain',
    #     'Content-Length': str(len(post_data.encode('utf-8'))),
    #     'Client-ID': CLIENT_ID,
    #     'Authentication': 'Bearer {}'.format(access_token)
    # }

    # print('Querying IGDB...')
    # print(post_headers)
    # print(post_data)
    # z = requests.post('https://api.igdb.com/v4/games/', data=post_data, headers=post_headers)
    # print(z.text)