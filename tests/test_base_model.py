#!/usr/bin/python3
"""
Unittest module for testing the BaseModel class.
"""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class methods
    """

    def setUp(self):
        """
        Set up an BaseModel instance for testing.
        """
        self.my_model = BaseModel()

    def test_initialization(self):
        """
        Test the initialization method of BaseModel class.

        Initializes new instances with no argumen.
        """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_initialize_new_instance_with_to_dict(self):
        """
        Test the initialization method of BaseModel class.

        Recreates BaseModel instances by parsing an instace dict
        as keyword argument during initialization.
        """
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        my_model_dict = self.my_model.to_dict()  # calling to_dict() method
        self.new_model = BaseModel(
            **my_model_dict
        )  # recreating a new BaseModel instance
        self.assertNotEqual(self.my_model, self.new_model)
        self.assertEqual(self.new_model.name, self.my_model.name)
        self.assertEqual(self.new_model.my_number, self.my_model.my_number)
        self.assertEqual((self.new_model.created_at),
                         (self.my_model.created_at))
        self.assertEqual((self.new_model.updated_at),
                         (self.my_model.updated_at))
        self.assertIsInstance((self.new_model.created_at), datetime.datetime)
        self.assertIsInstance((self.new_model.updated_at), datetime.datetime)
        self.assertIsInstance((self.my_model.created_at), datetime.datetime)
        self.assertIsInstance((self.my_model.updated_at), datetime.datetime)

    def test_str(self):
        """
        Test the str method of BaseModel
        """
        str_rep_model = (
            f"[{self.my_model.__class__.__name__}] "
            + f"({self.my_model.id}) {self.my_model.__dict__}"
        )
        self.assertEqual(str(self.my_model), str_rep_model)

    def test_save(self):
        """
        Test the save method of BaseModel
        """
        # calls the save method in the BaseModel class
        self.my_model.save()
        # checks that updated_at records the time instance is saved to a file
        self.assertTrue(self.my_model.updated_at > self.my_model.created_at)

    def test_to_dict(self):
        """
        Test to_dict method of BaseModel
        """
        my_model_dict = self.my_model.to_dict()  # returns a copy of __dict__
        self.assertNotEqual(my_model_dict, self.my_model.__dict__)
        self.assertIsInstance(my_model_dict, dict)
        self.assertIsInstance(my_model_dict["created_at"], str)
        self.assertIsInstance(my_model_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
