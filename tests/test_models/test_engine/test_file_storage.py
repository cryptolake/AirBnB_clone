#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_save(self):
        a = BaseModel()
        a.save()
        self.assertTrue(len(storage.all()) > 0)

    def test_file_path(self):
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertTrue(len(storage._FileStorage__file_path) > 0)

    def test_objects(self):
        a = BaseModel()
        a.save()
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertTrue(len(storage._FileStorage__objects) > 0)
    
    def test_all(self):
        a = BaseModel()
        a.save()
        self.assertTrue(len(storage.all()) > 0)


if __name__ == '__main__':
    unittest.main()
