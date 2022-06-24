import json
import unittest
from unittest.mock import patch

import data_redis as data


class TestData(unittest.TestCase):

    def get_data(self, name, _id):
        with open('tests/fixtures/test_data.json') as f:
            data = json.load(f)
        return data[name][str(_id)]

    def test_skin_init(self):
        with patch('data_redis.db') as mock_db:
            mock_db.get.side_effect = self.get_data
            skin = data.Skin(10)
            self.assertIsInstance(skin, data.Skin)
            self.assertEqual(skin.name, 'Seer Pants')
            self.assertEqual(skin.type, 'Leggings')

    def test_class_get(self):
        with patch('data_redis.db') as mock_db:
            skins = data.Skin.get('weapon')
            self.assertIsInstance(skins, list)
            self.assertTrue(all(isinstance(i, data.Skin) for i in skins))


if __name__ == '__main__':
    unittest.main()
