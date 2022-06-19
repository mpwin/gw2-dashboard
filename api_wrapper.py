import requests


class Wrapper:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.url = 'https://api.guildwars2.com/v2/'

    def skins(self):
        endpoint = self.url + 'skins'
        return self.PageIterator(endpoint)


    class PageIterator:
        def __init__(self, endpoint):
            self.endpoint = endpoint
            self.page_total = _get_page_total(endpoint)
            self.page = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.page >= self.page_total:
                raise StopIteration
            response = requests.get(self.endpoint, params=_params(page=self.page))
            self.page += 1
            return response.json()


def _get_page_total(endpoint):
    response = requests.get(endpoint, params=_params())
    return int(response.headers.get('X-Page-Total'))


def _params(**keys):
    params = {
        'page': keys.get('page') or 0,
        'page_size': keys.get('page_size') or 200,
        }
    return params
