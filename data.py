import json
import redis
import requests
import time
from operator import itemgetter


r = redis.Redis()
url = 'https://api.guildwars2.com/v2'
with open('key.txt') as f:
    key = f.readline().rstrip()


def get_data():
    get_account_skins()
    get_skins()


def get_account_skins():
    response = requests.get(f'{url}/v2/account/skins', params={'access_token': key})
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


def collection_list(category):
    l = []
    for i in r.smembers(f'collections:{category}'):
        name = r.mget(f'collection:{category}:{int(i)}')
        l.append({'name': name, 'tag': ''})
    l = sorted(l, key=itemgetter('name'))
    return l


def weapon_list():
    list = []
    for id in r.smembers('skins:weapon'):
        name = r.mget('skin:%s' %(int(id)))
        tag = 'unlocked' if r.sismember('skins:unlocked', id) else 'locked'
        list.append({'name': name, 'tag': tag})
    list = sorted(list, key=itemgetter('name'))
    return list


def heavy_armor_list():
    list = []
    for id in r.smembers('skins:heavy'):
        name = r.mget('skin:%s' %(int(id)))
        tag = 'unlocked' if r.sismember('skins:unlocked', id) else 'locked'
        list.append({'name': name, 'tag': tag})
    list = sorted(list, key=itemgetter('name'))
    return list


def medium_armor_list():
    list = []
    for id in r.smembers('skins:medium'):
        name = r.mget('skin:%s' %(int(id)))
        tag = 'unlocked' if r.sismember('skins:unlocked', id) else 'locked'
        list.append({'name': name, 'tag': tag})
    list = sorted(list, key=itemgetter('name'))
    return list


def light_armor_list():
    list = []
    for id in r.smembers('skins:light'):
        name = r.mget('skin:%s' %(int(id)))
        tag = 'unlocked' if r.sismember('skins:unlocked', id) else 'locked'
        list.append({'name': name, 'tag': tag})
    list = sorted(list, key=itemgetter('name'))
    return list
