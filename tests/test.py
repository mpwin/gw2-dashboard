import unittest
from unittest.mock import patch

import data_redis as data


class TestData(unittest.TestCase):

    @patch('data_redis.db')
    def test_skin_init(self, mock_db):
        mock_db.get.return_value = {
            'name': 'Seer Pants',
            'type': 'Leggings',
            }
        skin = data.Skin(10)
        self.assertIsInstance(skin, data.Skin)
        self.assertEqual(skin.name, 'Seer Pants')
        self.assertEqual(skin.type, 'Leggings')

    @patch('data_redis.db')
    def test_class_get(self, mock_db):
        skins = data.Skin.get('weapon')
        self.assertIsInstance(skins, list)
        self.assertTrue(all(isinstance(i, data.Skin) for i in skins))


if __name__ == '__main__':
    unittest.main()
