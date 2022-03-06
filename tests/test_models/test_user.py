#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def test_child(self):
        user = User()
        self.assertTrue(isinstance(user, BaseModel))

    def test_fields(self):
       user = User()
       self.assertEqual(user.email, "")
       self.assertEqual(user.password, "")
       self.assertEqual(user.first_name, "")
       self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
