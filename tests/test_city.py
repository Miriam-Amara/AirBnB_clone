#!/usr/bin/python3
"""
Unittest module for testing the City class.

This module includes test cases for:
- City class inheritance and attributes.
- Parent methods (__str__, save, and to_dict).
- Instance and class attribute behavior.
"""


import unittest
import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up a City instance for testing.
        """
        self.city = City()

    def test_class_inheritance(self):
        """
        Test that City inherits from BaseModel.
        """
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.city, City)

    def test_class_has_class_attribute(self):
        """
        Test that the City class has the 'name' and 'state_id'
        class-level attribute.
        """
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

    def test_instance_has_instance_attribute(self):
        """
        Test City instances have BaseModel attributes.
        """
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_class_attribute(self):
        """
        Test default value of class attributes
        and their types.
        """
        self.assertIsInstance(City.state_id, str)
        self.assertIsInstance(City.name, str)
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_instance_attribute(self):
        """
        Test the types of instance attributes.
        """
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)

    def test_instance_has_instance_method(self):
        """
        Test City has inherited BaseModel methods.
        """
        self.assertTrue(hasattr(self.city, "__str__"))
        self.assertTrue(hasattr(self.city, "save"))
        self.assertTrue(hasattr(self.city, "to_dict"))


class TestCityMethods(unittest.TestCase):
    """
    Test cases for City class methods.
    """

    def setUp(self):
        """
        Set up an City instance for testing.
        """
        self.city = City()

    def test_parent_str_method(self):
        """
        Test the inherited __str__ method.
        """
        obj_str = (
            f"[{self.city.__class__.__name__}] " +
            f"({self.id}) {self.__dict__}"
        )

        self.assertTrue(obj_str, str(self.city))

    def test_parent_save_method(self):
        """
        Test the inherited save method.
        """
        last_updated_at = self.city.updated_at
        self.city.save()
        current_updated_at = self.city.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """
        Test the inherited to_dict method.
        """
        self.assertNotEqual(self.city.to_dict(), self.city.__dict__)
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
