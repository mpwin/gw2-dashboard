import redis
import requests
import time

red = redis.Redis()
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
        print('%s | %s' %(skin['id'], skin['name']))

    time.sleep(2)
