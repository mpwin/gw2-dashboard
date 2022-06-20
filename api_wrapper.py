import requests
import time


class Wrapper:

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.url = 'https://api.guildwars2.com/v2/'

    def skins(self):
        return self.ObjectIterator(self.url + 'skins')


    class ObjectIterator:

        def __init__(self, endpoint):
            self.objects = []
            self.page = self.PageIterator(endpoint)

        def __iter__(self):
            return self

        def __next__(self):
            if not self.objects:
                self.objects = next(self.page)

            if self.objects:
                return self.objects.pop(0)
            else:
                raise StopIteration


        class PageIterator:

            def __init__(self, endpoint):
                self.endpoint = endpoint
                self.page_total = self._get_page_total(endpoint)
                self.page = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self.page < self.page_total:
                    response = requests.get(self.endpoint, params=self._params(page=self.page))
                    self.page += 1
                    time.sleep(2)
                    return response.json()
                else:
                    raise StopIteration

            def _get_page_total(self, endpoint):
                response = requests.get(endpoint, params=self._params())
                return int(response.headers.get('X-Page-Total'))

            def _params(self, **keys):
                params = {
                    'page': keys.get('page') or 0,
                    'page_size': keys.get('page_size') or 200,
                    }
                return params
