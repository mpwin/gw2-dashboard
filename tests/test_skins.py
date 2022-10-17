import unittest

from data import skins


class TestSkins(unittest.TestCase):

    def test_get(self):
        skin = skins.get('10')
        self.assertIsInstance(skin, dict)
        self.assertEqual(skin['id'], '10')
        self.assertEqual(skin['name'], 'Seer Pants')
        self.assertEqual(skin['type'], 'Leggings')
