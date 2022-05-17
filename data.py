import redis
import requests
import time

def get_data():
    red = redis.Redis()

    url = 'https://api.guildwars2.com/v2/account/skins'
    with open('key.txt') as f:
        key = f.readline().rstrip()
    res = requests.get(url, params = { 'access_token': key })
    ids = list(res.json())

    for id in ids:
        red.sadd('unlocked_skin_ids', id)

    print(ids)
    time.sleep(2)

    url = 'https://api.guildwars2.com/v2/skins'
    res = requests.get(url)
    ids = list(res.json())

    for id in range(0, len(ids), 200):
        grp = ids[id:id + 200]
        res = requests.get(url, params = { 'ids': ','.join(map(str, grp)) })

        for skin in res.json():
            if not skin['name']: continue
            red.sadd('skin_ids', skin['id'])
            red.hset('skin:%s' %(skin['id']), 'name', skin['name'])

            if skin['type'] == 'Weapon':
                red.sadd('weapon_ids', skin['id'])
            if skin['type'] == 'Armor':
                match skin['details']['weight_class']:
                    case 'Heavy':
                        red.sadd('heavy_armor_ids',  skin['id'])
                    case 'Medium':
                        red.sadd('medium_armor_ids', skin['id'])
                    case 'Light':
                        red.sadd('light_armor_ids',  skin['id'])

            print('%s | %s' %(skin['id'], skin['name']))

        time.sleep(2)
