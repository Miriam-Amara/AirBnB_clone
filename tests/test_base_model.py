#!/usr/bin/python3
"""

"""

import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """
    
    """

    @classmethod
    def setUpClass(cls):
        """ """
        cls.model = BaseModel()

    def setUp(self):
        """ """
        self.my_model = BaseModel()

    def test_initialization(self):
        """ """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)
        # self.assertNotEqual(self.model.id, self.my_model.id)

    def test_initialize_new_instance_with_to_dict(self):
        self.first_model = BaseModel()
        self.first_model.name = "My_First_Model"
        self.first_model.my_number = 89
        first_model_dict = self.first_model.to_dict()
        self.second_model = BaseModel(**first_model_dict)
        self.assertIsNot(self.first_model, self.second_model)   
        
    def test_str(self):
        """ """
        str_rep_model = f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), str_rep_model)
    
    def test_save(self):
        """ """
        pass

    def test_to_dict(self):
        """ """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict, self.model.__dict__)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)



if __name__ == "__main__":
    unittest.main()

