import redis


db = redis.Redis(decode_responses=True) 


class Skin:

    @classmethod
    def save(cls, data):
        if not data.get('id') or not data.get('name'):
            return

        db.sadd('skins', data['id'])
        db.sadd('skins:standalone', data['id'])

        hash = {
            'name': data['name'],
            'type': data.get('details', {}).get('type', ''),
            }
        db.hmset('skin:%s' %(data['id']), hash)

        match data.get('type'):
            case 'Weapon':
                db.sadd('skins:weapon', data['id'])
            case 'Armor':
                match data.get('details', {}).get('weight_class'):
                    case 'Heavy':
                        db.sadd('skins:heavy', data['id'])
                    case 'Medium':
                        db.sadd('skins:medium', data['id'])
                    case 'Light':
                        db.sadd('skins:light', data['id'])
