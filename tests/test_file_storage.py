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
        cls.store_data = FileStorage()

    def setUp(self):
        """ """
        self.model = BaseModel()

    def test_new_all(self):
        """ """
        self.store_data.new(self.model)
        self.assertIsInstance(self.store_data.all(), dict)
        print('\n\n', self.store_data.all())
