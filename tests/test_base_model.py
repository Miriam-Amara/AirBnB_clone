#!/usr/bin/python3
"""

"""

import unittest
import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    
    """

    def setUp(self):
        """ """
        self.my_model = BaseModel()
    
    def tearDown(self):
        """ """
        FileStorage._FileStorage__objects = {}

    def test_initialization(self):
        """ """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_initialize_new_instance_with_to_dict(self):
        """ """
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        my_model_dict = self.my_model.to_dict()
        self.new_model = BaseModel(**my_model_dict)
        self.assertIsNot(self.my_model, self.new_model)
        self.assertEqual(self.new_model.name, self.my_model.name)
        self.assertEqual(self.new_model.my_number, self.my_model.my_number)
        self.assertNotEqual((self.new_model.created_at), (self.my_model.created_at))
        self.assertNotEqual((self.new_model.updated_at), (self.my_model.updated_at))
        self.assertIsInstance((self.new_model.created_at), datetime.datetime)
        self.assertIsInstance((self.new_model.updated_at), datetime.datetime)
        # calling self.my_model.to_dict changed the type of created_at and updated_at attributes
        self.assertIsInstance((self.my_model.created_at), str)
        self.assertIsInstance((self.my_model.updated_at), str)

    def test_str(self):
        """ """
        str_rep_model = f"[{self.my_model.__class__.__name__}] ({self.my_model.id}) {self.my_model.__dict__}"
        self.assertEqual(str(self.my_model), str_rep_model)
    
    def test_save(self):
        """ """
        self.assertEqual(len(FileStorage._FileStorage__objects), 1)
        self.my_model.save()
        self.assertTrue(self.my_model.updated_at > self.my_model.created_at)
        key = f"{self.my_model.__class__.__name__}.{self.my_model.id}"
        self.assertEqual((FileStorage._FileStorage__objects[key]), self.my_model.__dict__)
        

    def test_to_dict(self):
        """ """
        model_dict = self.my_model.to_dict()
        self.assertEqual(model_dict, self.my_model.__dict__)
        self.assertIsInstance(model_dict, dict)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    # def test_file_storage(self):
        # self.assertIsInstance(storage.all(), dict)
        
        



if __name__ == "__main__":
    unittest.main()

