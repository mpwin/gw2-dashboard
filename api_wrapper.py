import requests


class Wrapper:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.url = 'https://api.guildwars2.com/v2/'

    def skins(self):
        endpoint = self.url + 'skins'
        params = {'page': 0, 'page_size': 200}
        response = requests.get(endpoint, params=params)
        page_total = int(response.headers['X-Page-Total'])
        return self.PageIterator(endpoint, page_total)


    class PageIterator:
        def __init__(self, endpoint, page_total):
            self.endpoint = endpoint
            self.page_total = page_total
            self.page = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.page >= self.page_total:
                raise StopIteration
            params = {'page': self.page, 'page_size': 200}
            response = requests.get(self.endpoint, params=params)
            self.page += 1
            return response.json()
