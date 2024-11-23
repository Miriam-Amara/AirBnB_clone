#!/usr/bin/python3
"""
Unittest module for testing the State class.

This module includes test cases for:
- State class inheritance and attributes.
- Parent methods (__str__, save, and to_dict).
- Instance and class attribute behavior.
"""


import unittest
import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up an State instance for testing.
        """
        self.state = State()

    def test_class_inheritance(self):
        """
        Test that State inherits from BaseModel.
        """
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.state, State)

    def test_class_has_class_attribute(self):
        """
        Test that State class has class-level attribute.
        """
        self.assertTrue(hasattr(State, "name"))

    def test_instance_has_instance_attribute(self):
        """
        Test State instances have BaseModel attributes.
        """
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_class_attribute_value(self):
        """
        Test default value of class attributes
        and its type.
        """
        self.assertIsInstance(State.name, str)
        self.assertEqual(State.name, "")

    def test_type_instance_attribute(self):
        """
        Test the types of instance attributes.
        """
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

    def test_instance_has_instance_method(self):
        """
        Test State has inherited BaseModel methods.
        """
        self.assertTrue(hasattr(self.state, "__str__"))
        self.assertTrue(hasattr(self.state, "save"))
        self.assertTrue(hasattr(self.state, "to_dict"))


class TestStateMethods(unittest.TestCase):
    """
    Test cases for State class methods.
    """

    def setUp(self):
        """
        Set up a State instance for testing.
        """
        self.state = State()

    def test_parent_str_method(self):
        """
        Test the inherited __str__ method.
        """
        obj_str = (
            f"[{self.state.__class__.__name__}] " +
            f"({self.id}) {self.__dict__}"
        )

        self.assertTrue(obj_str, str(self.state))

    def test_parent_save_method(self):
        """
        Test the inherited save method.
        """

        last_updated_at = self.state.updated_at
        self.state.save()
        current_updated_at = self.state.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """
        Test the inherited to_dict method.
        """
        self.assertNotEqual(self.state.to_dict(), self.state.__dict__)
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
