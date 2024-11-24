#!/usr/bin/python3
"""
Unittest module for testing the User class.

This module includes test cases for:
- User class inheritance and attributes.
- Parent methods (__str__, save, and to_dict).
- Instance and class attribute behavior.
"""


import unittest
import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up an User instance for testing.
        """
        self.user = User()

    def test_class_inheritance(self):
        """
        Test that User inherits from BaseModel.
        """
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.user, User)

    def test_class_has_class_attribute(self):
        """
        Test that User class has class-level attributes.
        """
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_instance_has_instance_attribute(self):
        """
        Test User instances have BaseModel attributes.
        """
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_type_class_attribute(self):
        """
        Test the types of class attributes.
        """
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_type_instance_attribute(self):
        """
        Test the types of instance attributes.
        """
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_instance_has_instance_method(self):
        """
        Test User has inherited BaseModel methods.
        """
        self.assertTrue(hasattr(self.user, "__str__"))
        self.assertTrue(hasattr(self.user, "save"))
        self.assertTrue(hasattr(self.user, "to_dict"))


class TestUserMethods(unittest.TestCase):
    """
    Test cases for User class methods.
    """

    def setUp(self):
        """
        Set up a User instance for testing.
        """
        self.user = User()

    def test_parent_str_method(self):
        """
        Test the inherited __str__ method.
        """
        obj_str = (
            f"[{self.user.__class__.__name__}] " +
            f"({self.id}) {self.__dict__}"
        )

        self.assertTrue(obj_str, str(self.user))

    def test_parent_save_method(self):
        """
        Test the inherited save method.
        """
        last_updated_at = self.user.updated_at
        self.user.save()
        current_updated_at = self.user.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """
        Test the inherited to_dict method.
        """
        self.assertNotEqual(self.user.to_dict(), self.user.__dict__)
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
