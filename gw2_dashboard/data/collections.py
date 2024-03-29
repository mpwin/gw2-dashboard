import json
import re

from . import db
from . import skins


def get(category, _id):
    collection = db.get(f'collections:{category}', _id)
    collection['category'] = category
    collection['id'] = _id
    collection['children'] = get_skins_for(collection)
    if is_unlocked(category, _id):
        collection['tags'] = 'unlocked'
    return collection


def get_set(name):
    return [get(name, _id) for _id in db.ids(f'collections:{name}')]


def get_skins_for(collection):
    key = f"collections:{collection['category']}:{collection['id']}:skins"
    return [skins.get(i) for i in db.ids(key)]


def is_unlocked(class_, id_):
    key = f"collections:{class_}:{id_}:skins"
    unlocked = [db.r.sismember('skins:unlocked', i) for i in db.ids(key)]
    return True if all(unlocked) else False


def setup():

    def save(data):
        hash = {'name': data['name'], 'note': data['note']}
        db.save(f"collections:{data['category']}", data['id'], hash)
        db.add_to_sorted_set(f"collections:{data['category']}", data['id'])

    def save_skins_to_collection(collection):
        key = f"collections:{collection['category']}:{collection['id']}:skins"
        for skin in collection['skins']:
            skin_type = skins.get(str(skin))['type']
            db.r.zadd(key, {skin: score[skin_type]})
            db.r.srem('skins:standalone', skin)

    types = [
        'Sword', 'Hammer', 'Longbow', 'Shortbow', 'Axe',
        'Dagger', 'Greatsword', 'Mace', 'Pistol', 'Rifle',
        'Scepter', 'Staff', 'Focus', 'Torch', 'Warhorn',
        'Shield', 'Spear', 'Speargun', 'Trident', 'Helm',
        'Shoulders', 'Coat', 'Gloves', 'Leggings', 'Boots',
        ]
    score = dict(zip(types, range(len(types))))

    for collection in collections_json():
        save(collection)
        save_skins_to_collection(collection)


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
