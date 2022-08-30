import redis


r = redis.Redis(decode_responses=True)


def get(scope, _id):
    return r.hgetall(':'.join((scope, _id)))


def get_set(scope, name):
    name = ':'.join((scope, name))

    match r.type(name):
        case 'set':
            return r.smembers(name)
        case 'zset':
            return r.zrange(name, 0, -1)


def in_set(scope, name, data):
    return r.sismember(f'{scope}:{name}', data)


def save(scope, _id, data):
    r.hmset('%s:%s' %(scope, _id), data)


def add_to_set(scope, name, *data):
    r.sadd(f'{scope}:{name}', *data)


def add_to_sorted_set(name, _id, score=None):
    if not score:
        score = _id
    r.zadd(name, {_id: score})


def create_sorted_set(scope, name, sets):
    _list = sorted(r.sinter(sets), key=lambda i: get(scope, i)['name'])
    r.zadd(name, {i: score for score, i in enumerate(_list)})
