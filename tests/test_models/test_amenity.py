#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_child(self):
        instance = Amenity()
        self.assertTrue(isinstance(instance, BaseModel))

    def test_fields(self):
       instance = Amenity()
       self.assertEqual(instance.name, "")


if __name__ == '__main__':
    unittest.main()
