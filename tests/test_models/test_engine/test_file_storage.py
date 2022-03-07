#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_file_path(self):
        self.assertIsInstance(FileStorage.__file_path, str)
        self.assertTrue(len(FileStorage.__file_path) > 0)

    def test_objects(self):
        self.assertIsInstance(FileStorage.__objects, list)
        self.assertTrue(len(FileStorage.__objects) > 0)
    
    def test_all(self):
        self.assertTrue(len(storage.all()) > 0)





if __name__ == '__main__':
    unittest.main()
