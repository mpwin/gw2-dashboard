import json

from . import db


def get(category, _id):
    return db.get(f'collections:{category}', _id)


def get_set(name):
    return [get(name, _id) for _id in db.get_set('collections', name)]


def save(data):
    hash = {'name': data['name'], 'note': data['note']}
    db.save(f"collections:{data['category']}", data['id'], hash)
    db.add_to_sorted_set(f"collections:{data['category']}", data['id'])


def setup():
    for collection in collections_json():
        save(collection)


def collections_json():
    return CollectionIterator()


class CollectionIterator:

    def __init__(self):
        self.categories = ['weapon', 'heavy', 'medium', 'light']
        self.collections = []

        with open('collections.json') as f:
            self.data = json.load(f)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.collections:
            self.collections = self.next_category()

        if self.collections:
            return self.collections.pop(0)
        else:
            raise StopIteration

    def next_category(self):
        if self.categories:
            category = self.categories.pop(0)
        else:
            return None

        return [dict(collection, id=index, category=category)
                for index, collection in enumerate(self.data[category])]
