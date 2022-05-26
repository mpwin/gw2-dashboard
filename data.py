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

    res = requests.get(f'{url}/skins')
    ids = list(res.json())

    for i in range(0, len(ids), 200):
        grp = ids[i:i + 200]
        res = requests.get(f'{url}/skins', params={'ids': ','.join(map(str, grp))})

        for skin in res.json():
            if not skin['name']: continue
            r.sadd('skin_ids', skin['id'])
            r.hset('skin:%s' %(skin['id']), 'name', skin['name'])

            if skin['type'] == 'Weapon':
                r.sadd('weapon_ids', skin['id'])
            if skin['type'] == 'Armor':
                match skin['details']['weight_class']:
                    case 'Heavy':
                        r.sadd('heavy_armor_ids', skin['id'])
                    case 'Medium':
                        r.sadd('medium_armor_ids', skin['id'])
                    case 'Light':
                        r.sadd('light_armor_ids', skin['id'])

            print('%s | %s' %(skin['id'], skin['name']))

        time.sleep(2)


def get_account_skins():
    response = requests.get(f'{url}/v2/account/skins', params={'access_token': key})
    for i in response.json():
        r.sadd('skins:unlocked', i)
    print('%s skins unlocked.' %(r.scard('skins:unlocked')))
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
    for id in r.smembers('weapon_ids'):
        name = r.hget('skin:%s' %(int(id)), 'name')
        tag = 'unlocked' if r.sismember('unlocked_skin_ids', id) else 'locked'
        list.append({'name': name, 'tag': tag})
    list = sorted(list, key=itemgetter('name'))
    return list


def heavy_armor_list():
    list = []
    for id in r.smembers('heavy_armor_ids'):
        name = r.hget('skin:%s' %(int(id)), 'name')
        tag = 'unlocked' if r.sismember('unlocked_skin_ids', id) else 'locked'
        list.append({'name': name, 'tag': tag})
    list = sorted(list, key=itemgetter('name'))
    return list


def medium_armor_list():
    list = []
    for id in r.smembers('medium_armor_ids'):
        name = r.hget('skin:%s' %(int(id)), 'name')
        tag = 'unlocked' if r.sismember('unlocked_skin_ids', id) else 'locked'
        list.append({'name': name, 'tag': tag})
    list = sorted(list, key=itemgetter('name'))
    return list


def light_armor_list():
    list = []
    for id in r.smembers('light_armor_ids'):
        name = r.hget('skin:%s' %(int(id)), 'name')
        tag = 'unlocked' if r.sismember('unlocked_skin_ids', id) else 'locked'
        list.append({'name': name, 'tag': tag})
    list = sorted(list, key=itemgetter('name'))
    return list
