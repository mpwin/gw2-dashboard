from . import db


def get(_id):
    data = db.get('skins', _id)
    data['id'] = _id
    if db.in_set('skins', 'unlocked', _id):
        data['tags'] = 'unlocked'
    return data


def get_set(name):
    return [get(_id) for _id in db.ids(f'skins:{name}')]


def standalone(category=None):
    if category:
        ids = db.r.sinter('skins:standalone', f'skins:{category}')
    else:
        ids = db.ids('skins:standalone')
    return [get(i) for i in ids]


def save(data):
    if not data.get('id') or not data.get('name'):
        return

    hash = {
        'name': data['name'],
        'type': data.get('details', {}).get('type', ''),
        }
    db.save('skins', data['id'], hash)
    db.add_to_set('skins', 'all', data['id'])
    db.add_to_set('skins', 'standalone', data['id'])

    match data.get('type'):
        case 'Weapon':
            db.add_to_set('skins', 'weapon', data['id'])
        case 'Armor':
            match data.get('details', {}).get('weight_class'):
                case 'Heavy':
                    db.add_to_set('skins', 'heavy', data['id'])
                case 'Medium':
                    db.add_to_set('skins', 'medium', data['id'])
                case 'Light':
                    db.add_to_set('skins', 'light', data['id'])


def save_unlocked(ids):
    db.add_to_set('skins', 'unlocked', *ids)


def setup():
    db.create_sorted_set(
        'skins', 'skins:standalone_weapon',
        ('skins:standalone', 'skins:weapon'),
        )
    db.create_sorted_set(
        'skins', 'skins:standalone_heavy',
        ('skins:standalone', 'skins:heavy'),
        )
    db.create_sorted_set(
        'skins', 'skins:standalone_medium',
        ('skins:standalone', 'skins:medium'),
        )
    db.create_sorted_set(
        'skins', 'skins:standalone_light',
        ('skins:standalone', 'skins:light'),
        )
