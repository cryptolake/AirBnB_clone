#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def test_child(self):
        instance = State()
        self.assertTrue(isinstance(instance, BaseModel))

    def test_fields(self):
       instance = State()
       self.assertEqual(instance.name, "")


if __name__ == '__main__':
    unittest.main()
