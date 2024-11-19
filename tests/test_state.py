#!/usr/bin/python3
"""

"""


import unittest
import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    
    """
    def setUp(self):
        """ """
        self.state = State()

    def test_class_inheritance(self):
        """ """
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.state, State)
        
    def test_class_has_class_attribute(self):
        """
        
        """
        self.assertTrue(hasattr(State, "name"))

    def test_instance_has_instance_attribute(self):
        """
        Checks that State instances has access to the
        parent (BaseModel) class attributes.
        """
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_class_attribute_value(self):
        self.assertIsInstance(State.name, str)
        self.assertEqual(State.name, "")

    def test_type_instance_attribute(self):
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)
        
    def test_instance_has_instance_method(self):
        self.assertTrue(hasattr(self.state, "__str__"))
        self.assertTrue(hasattr(self.state, "save"))
        self.assertTrue(hasattr(self.state, "to_dict"))



class TestStateMethods(unittest.TestCase):
    """
    
    """

    def setUp(self):
        """ """
        self.state = State()

    def test_parent_str_method(self):
        """ """
        obj_str = (f"[{self.state.__class__.__name__}] " +
        f"({self.id}) {self.__dict__}")

        self.assertTrue(obj_str, str(self.state))

    def test_parent_save_method(self):
        """ """
        last_updated_at = self.state.updated_at
        self.state.save()
        current_updated_at = self.state.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """ """
        self.assertNotEqual(self.state.to_dict(), self.state.__dict__)
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
