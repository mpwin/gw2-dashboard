import redis


db = redis.Redis(decode_responses=True)


def get(scope, _id):
    return db.hgetall(':'.join((scope, _id)))


def get_set(scope, name):
    name = ':'.join((scope, name))

    match db.type(name):
        case 'set':
            return db.smembers(name)
        case 'zset':
            return db.zrange(name, 0, -1)


def in_set(scope, name, data):
    return db.sismember(f'{scope}:{name}', data)


def save(scope, _id, data):
    db.hmset('%s:%s' %(scope, _id), data)


def add_to_set(scope, name, *data):
    db.sadd(f'{scope}:{name}', *data)


def create_sorted_set(scope, name, sets):
    _list = sorted(db.sinter(sets), key=lambda i: get(scope, i)['name'])
    db.zadd(name, {i: score for score, i in enumerate(_list)})
