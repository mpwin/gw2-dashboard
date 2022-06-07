import json
import re
import redis
import requests
import time


r = redis.Redis(decode_responses=True)
url = 'https://api.guildwars2.com/v2'
with open('key.txt') as f:
    key = f.readline().rstrip()


def fetch():
    fetch_account_skins()
    fetch_skins()
    fetch_dyes()
    create_collections()


def fetch_account_skins():
    response = requests.get(f'{url}/account/skins', params={'access_token': key})
    for i in response.json():
        r.sadd('skins:unlocked', i)
    print('%s skins unlocked.' %(r.scard('skins:unlocked')))
    time.sleep(2)


def fetch_skins():
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


def fetch_dyes():
    ids = requests.get(f'{url}/colors').json()
    for i in range(0, len(ids), 200):
        response = requests.get(f'{url}/colors', params={'ids': ','.join(map(str, ids[i:i+200]))})
        for dye in response.json():
            if not dye['name']: continue
            r.sadd('dyes', dye['id'])
            r.set('dye:%s' %(dye['id']), dye['name'])


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
