#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_child(self):
        instance = Place()
        self.assertTrue(isinstance(instance, BaseModel))

    def test_fields(self):
       instance = Place()
       self.assertEqual(instance.city_id, "")
       self.assertEqual(instance.user_id, "")
       self.assertEqual(instance.name, "")
       self.assertEqual(instance.description, "")
       self.assertEqual(instance.number_rooms, 0)
       self.assertEqual(instance.number_bathrooms, 0)
       self.assertEqual(instance.max_guest, 0)
       self.assertEqual(instance.price_by_night, 0)
       self.assertEqual(instance.latitude, 0.0)
       self.assertEqual(instance.longitude, 0.0)
       self.assertEqual(instance.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
