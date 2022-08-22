import requests
import time


class Wrapper:

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.url = 'https://api.guildwars2.com/v2/'

    def account_skins(self):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        return requests.get(self.url + 'account/skins', headers=headers).json()

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
                self.page = 0
                self.page_total = self._get_page_total()

            def __iter__(self):
                return self

            def __next__(self):
                if self.page < self.page_total:
                    response = requests.get(self.endpoint, params=self._params())
                    self.page += 1
                    time.sleep(2)
                    return response.json()
                else:
                    raise StopIteration

            def _get_page_total(self):
                response = requests.get(self.endpoint, params=self._params())
                return int(response.headers.get('X-Page-Total'))

            def _params(self):
                return {'page': self.page, 'page_size': 200}
