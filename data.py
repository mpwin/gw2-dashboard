import db_redis as db


class Skin:

    def __init__(self, i):
        data = db.get('skin', i)
        self.name = data.get('name')
        self.type = data.get('type')

    @classmethod
    def get(cls, category):
        ids = db.ids('skin', category)
        return [Skin(i) for i in ids]

    @classmethod
    def save(cls, data):
        if not data.get('id') or not data.get('name'):
            return

        hash = {
            'name': data['name'],
            'type': data.get('details', {}).get('type', ''),
            }
        db.set('skin', data['id'], hash)
        db.tag('skin', data['id'], 'standalone')

        match data.get('type'):
            case 'Weapon':
                db.tag('skin', data['id'], 'weapon')
            case 'Armor':
                match data.get('details', {}).get('weight_class'):
                    case 'Heavy':
                        db.tag('skin', data['id'], 'heavy')
                    case 'Medium':
                        db.tag('skin', data['id'], 'medium')
                    case 'Light':
                        db.tag('skin', data['id'], 'light')
