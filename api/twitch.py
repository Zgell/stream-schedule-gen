'''
> twitch.py
Handles all connections to the Twitch API for auth purposes.
Includes a TwitchHandler class which does the following:
- Loads credentials from config/auth.json
- Fetches an access token for use with the IGDB API
'''
from config.defaults import DEFAULT_AUTH_PATH as AUTH_PATH

import json
import requests

class TwitchHandler:
    def __init__(self, client_id='', client_secret='', access_token='', authpath=AUTH_PATH):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.auth_path = authpath

    ''' Getters / Minor Quality-of-Life Functions '''
    def get_client_id(self) -> str:
        return self.client_id
    
    def get_access_token(self) -> str:
        return self.access_token
    
    def get_twitch_api_url(self):
        '''
        Returns a URL to send POST request to for access tokens.
        '''
        # return 'https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials'
        if (self.client_id == '' or self.client_secret == ''):
            raise ValueError('Client ID and/or Client Secret have not been set yet!')
        url = 'https://id.twitch.tv/oauth2/token'
        url += '?client_id={}'.format(self.client_id)
        url += '&client_secret={}'.format(self.client_secret)
        url += '&grant_type=client_credentials'
        return url


    ''' API Fetch Functions '''
    def fetch_credentials(self):
        '''
        Reads in credentials stored in config/auth.json.
        Credentials are then stored internally in the class instance.
        '''
        with open(self.auth_path, 'r') as auth:
            tokens_raw = ''.join(auth.readlines())  # Combine all lines into one string
            tokens = json.loads(tokens_raw)
            self.client_id = tokens['CLIENT_ID']
            self.client_secret = tokens['CLIENT_SECRET']
            auth.close()

    def fetch_access_token(self):
        '''
        Sends a POST request to the Twitch API with the client ID and secret,
        waits for a response and saves access token (+ metadata) to object.
        '''
        # URL = 'https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials'.format(CLIENT_ID, CLIENT_SECRET)
        url = self.get_twitch_api_url()
        post_data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        # Send the POST request to the Twitch API and parse response
        x = requests.post(url, json=post_data, timeout=5.0)
        x_json = json.loads(x.text)

        if "access_token" not in list(x_json.keys()):
            raise Exception("Access token not found in Twitch API response!\n{}".format(x_json))
        else:
            # return x_json["access_token"]
            self.access_token = x_json["access_token"]



if __name__ == '__main__':
    # Perform some test checks
    twitch = TwitchHandler()
    twitch.fetch_credentials()
    print('CLIENT ID:', twitch.client_id)
    print('CLIENT SECRET:', twitch.client_secret)