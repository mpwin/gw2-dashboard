import json
import re
import redis
import requests
import time
from operator import itemgetter


r = redis.Redis(decode_responses=True)
url = 'https://api.guildwars2.com/v2'
with open('key.txt') as f:
    key = f.readline().rstrip()


def get_data():
    get_account_skins()
    get_skins()


def get_account_skins():
    response = requests.get(f'{url}/account/skins', params={'access_token': key})
    for i in response.json():
        r.sadd('skins:unlocked', i)
    print('%s skins unlocked.' %(r.scard('skins:unlocked')))
    time.sleep(2)


def get_skins():
    ids = requests.get(f'{url}/skins').json()
    for i in range(0, len(ids), 200):
        response = requests.get(f'{url}/skins', params={'ids': ','.join(map(str, ids[i:i+200]))})
        for skin in response.json():
            if not skin['name']: continue
            r.sadd('skins', skin['id'])
            r.sadd('skins:standalone', skin['id'])
            r.set('skin:%s' %(skin['id']), skin['name'])

            if skin['type'] == 'Weapon':
                r.sadd('skins:weapon', skin['id'])
            if skin['type'] == 'Armor':
                match skin['details']['weight_class']:
                    case 'Heavy':
                        r.sadd('skins:heavy', skin['id'])
                    case 'Medium':
                        r.sadd('skins:medium', skin['id'])
                    case 'Light':
                        r.sadd('skins:light', skin['id'])

            print('%s | %s' %(skin['id'], skin['name']))
        time.sleep(2)


def create_collections():
    with open('collections.json') as f:
        data = json.load(f)

    for category in ['weapon', 'heavy', 'medium', 'light']:
        for index, collection in enumerate(data[category]):
            r.sadd(f'collections:{category}', index)
            r.set(f'collection:{category}:{index}', collection['name'])

            for i in r.sinter('skins:standalone', f'skins:{category}'):
                name = r.get(f'skin:{i}')
                if re.match((collection['name'] + ' '), name):
                    r.smove('skins:standalone', f'collection:{category}:{index}:skins', i)


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
