#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):

    def test_child(self):
        instance = City()
        self.assertTrue(isinstance(instance, BaseModel))

    def test_fields(self):
       instance = City()
       self.assertEqual(instance.name, "")
       self.assertEqual(instance.state_id, "")


if __name__ == '__main__':
    unittest.main()
