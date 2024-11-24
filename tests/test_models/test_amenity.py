#!/usr/bin/python3


"""
Unittest module for testing the Amenity class.

This module includes test cases for:
- Amenity class inheritance and attributes.
- Parent methods (__str__, save, and to_dict).
- Instance and class attribute behavior.
"""


import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up an Amenity instance for testing.
        """
        self.amenity = Amenity()

    def test_class_inheritance(self):
        """
        Test that Amenity inherits from BaseModel.
        """
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.amenity, Amenity)

    def test_class_has_class_attribute(self):
        """
        Test that the Amenity class has the 'name' class-level attribute
        and does not have 'id', 'created_at', or 'updated_at' class-level
        attributes.
        """
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertFalse(hasattr(Amenity, "id"))
        self.assertFalse(hasattr(Amenity, "created_at"))
        self.assertFalse(hasattr(Amenity, "updated_at"))

    def test_instance_has_instance_attribute(self):
        """
        Test Amenity instances have BaseModel attributes.
        """
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_class_attribute_value(self):
        """
        Test default value of 'name' class attribute
        and its type.
        """
        self.assertIsInstance(Amenity.name, str)
        self.assertEqual(Amenity.name, "")

    def test_type_instance_attribute(self):
        """
        Test the types of instance attributes.
        """
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)

    def test_instance_has_instance_method(self):
        """
        Test Amenity has inherited BaseModel methods.
        """
        self.assertTrue(hasattr(self.amenity, "__str__"))
        self.assertTrue(hasattr(self.amenity, "save"))
        self.assertTrue(hasattr(self.amenity, "to_dict"))


class TestAmenityMethods(unittest.TestCase):
    """
    Test cases for Amenity class methods.
    """

    def setUp(self):
        """
        Set up an Amenity instance for testing.
        """
        self.amenity = Amenity()

    def test_parent_str_method(self):
        """
        Test the inherited __str__ method.
        """
        obj_str = (
            f"[{self.amenity.__class__.__name__}] " +
            f"({self.id}) {self.__dict__}"
        )

        self.assertTrue(obj_str, str(self.amenity))

    def test_parent_save_method(self):
        """
        Test the inherited save method.
        """
        last_updated_at = self.amenity.updated_at
        self.amenity.save()
        current_updated_at = self.amenity.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """
        Test the inherited to_dict method.
        """
        self.assertNotEqual(self.amenity.to_dict(), self.amenity.__dict__)
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
