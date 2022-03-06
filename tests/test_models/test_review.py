#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def test_child(self):
        instance = Review()
        self.assertTrue(isinstance(instance, BaseModel))

    def test_fields(self):
       instance = Review()
       self.assertEqual(instance.place_id, "")
       self.assertEqual(instance.user_id, "")
       self.assertEqual(instance.text, "")


if __name__ == '__main__':
    unittest.main()
