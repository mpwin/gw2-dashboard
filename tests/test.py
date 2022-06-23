import unittest

import data_redis as data


class TestData(unittest.TestCase):

    def test_skin_init(self):
        skin = data.Skin(10)
        self.assertIsInstance(skin, data.Skin)
        self.assertEqual(skin.name, 'Seer Pants')
        self.assertEqual(skin.type, 'Leggings')

    def test_class_get(self):
        skins = data.Skin.get('weapon')
        self.assertIsInstance(skins, list)
        self.assertTrue(all(isinstance(i, data.Skin) for i in skins))


if __name__ == '__main__':
    unittest.main()
