#!/usr/bin/python3

"""

"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    
    """
    @classmethod
    def setUpClass(cls):
        """ """
        cls.storage = FileStorage()

    def setUp(self):
        """ """
        self.model = BaseModel()

    def test_new(self):
        """ """
        self.storage.new(str(self.model))

    def test_all(self):
        """ """
        self.assertIsInstance(self.storage.all(), dict)
        print(type(self.storage.all()))
        print('\n', self.storage.all())
