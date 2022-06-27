import redis


db = redis.Redis(decode_responses=True)


def get(name, _id):
    return db.hgetall(f'{name}:{_id}')


def ids(name, tag):
    return db.smembers(f'{plural[name]}:{tag}')


def set(name, _id, data):
    db.sadd(plural[name], _id)
    db.hmset(f'{name}:{_id}', data)


def tag(name, _id, tag):
    db.sadd(f'{plural[name]}:{tag}', _id)


plural = {
    'skin': 'skins',
    }
