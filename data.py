import redis
from operator import itemgetter


r = redis.Redis(decode_responses=True)


def collections(category):
    l = []
    for i in r.smembers(f'collections:{category}'):
        name = r.get(f'collection:{category}:{i}')
        children = skins(category, i)
        l.append({'id': i, 'name': name, 'tag': '', 'children': children})
    l = sorted(l, key=itemgetter('name'))
    return l


def skins(category, collection=None):
    if collection:
        ids = r.smembers(f'collection:{category}:{collection}:skins')
    else:
        ids = r.sinter('skins:standalone', f'skins:{category}')

    l = []
    for i in ids:
        name = r.get(f'skin:{i}')
        tag = 'unlocked' if r.sismember('skins:unlocked', i) else 'locked'
        l.append({'id': i, 'name': name, 'tag': tag})
    l = sorted(l, key=itemgetter('name'))
    return l


def dyes(rarity):
    l = []
    for i in r.smembers(f'dyes:{rarity}'):
        name = r.get(f'dye:{i}')
        l.append({'id': i, 'name': name, 'tag': ''})
    l = sorted(l, key=itemgetter('name'))
    return l
