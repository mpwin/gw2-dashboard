import requests


class Wrapper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://api.guildwars2.com/v2/'

    def skins(self):
        params = {'page': 0, 'page_size': 200}
        return requests.get(self.url + 'skins', params=params)
