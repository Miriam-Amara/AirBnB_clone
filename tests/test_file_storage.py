#!/usr/bin/python3

"""

"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    
    """

    def setUp(self):
        """ """
        self.my_model = BaseModel()
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """ """
        FileStorage._FileStorage__objects = {}

    def test_save_first_base_model_instance(self):
        """ """
        try:
            self.my_model.save()
        except Exception:
            self.fail(f"save method of FileStorage class failed to save {self.my_model}")

    
    def test_save_second_base_model_instance(self):
        """ """
        try:
            self.my_model.save()
        except Exception:
            self.fail(f"save method of FileStorage class failed to save {self.my_model}")

    def test_save_third_base_model_instance(self):
        """ """
        try:
            self.my_model.save()
        except Exception:
            self.fail(f"save method of FileStorage class failed to save {self.my_model}")

if __name__ == "__main__":
    unittest.main()