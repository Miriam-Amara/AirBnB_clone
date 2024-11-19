#!/usr/bin/python3
"""

"""


import unittest
import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    
    """
    def setUp(self):
        """ """
        self.user = User()

    def test_class_inheritance(self):
        """ """
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.user, User)
        
    def test_class_has_class_attribute(self):
        """
        Test that the User class has the 'name' class-level attribute.
        """
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        

    def test_instance_has_instance_attribute(self):
        """
        Checks that User instances has access to the
        parent (BaseModel) class attributes.
        """
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_class_attribute_value(self):
        """ """
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_type_instance_attribute(self):
        """ """
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)
        
    def test_instance_has_instance_method(self):
        """ """
        self.assertTrue(hasattr(self.user, "__str__"))
        self.assertTrue(hasattr(self.user, "save"))
        self.assertTrue(hasattr(self.user, "to_dict"))



class TestUserMethods(unittest.TestCase):
    """
    
    """

    def setUp(self):
        """ """
        self.user = User()

    def test_parent_str_method(self):
        """ """
        obj_str = (f"[{self.user.__class__.__name__}] " +
        f"({self.id}) {self.__dict__}")

        self.assertTrue(obj_str, str(self.user))

    def test_parent_save_method(self):
        """ """
        last_updated_at = self.user.updated_at
        self.user.save()
        current_updated_at = self.user.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """ """
        self.assertNotEqual(self.user.to_dict(), self.user.__dict__)
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
