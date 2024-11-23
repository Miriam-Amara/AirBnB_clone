#!/usr/bin/python3
"""
Unittest module for testing the Review class.

This module includes test cases for:
- Review class inheritance and attributes.
- Parent methods (__str__, save, and to_dict).
- Instance and class attribute behavior.
"""


import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up an Review instance for testing.
        """
        self.review = Review()

    def test_class_inheritance(self):
        """
        Test that Review inherits from BaseModel.
        """
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review, Review)

    def test_class_has_class_attribute(self):
        """
        Test that the Review class has the 'name' class-level attribute.
        """
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_instance_has_instance_attribute(self):
        """
        Test Review instances have BaseModel attributes.
        """
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_type_class_attribute(self):
        """
        Test the types of class attributes.
        """
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_type_instance_attribute(self):
        """
        Test the types of instance attributes.
        """
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)

    def test_instance_has_instance_method(self):
        """
        Test Review has inherited BaseModel methods.
        """
        self.assertTrue(hasattr(self.review, "__str__"))
        self.assertTrue(hasattr(self.review, "save"))
        self.assertTrue(hasattr(self.review, "to_dict"))


class TestReviewMethods(unittest.TestCase):
    """
    Test cases for Review class methods.
    """

    def setUp(self):
        """
        Set up a Review instance for testing.
        """
        self.review = Review()

    def test_parent_str_method(self):
        """
        Test the inherited __str__ method.
        """
        obj_str = (
            f"[{self.review.__class__.__name__}] " +
            f"({self.id}) {self.__dict__}"
        )

        self.assertTrue(obj_str, str(self.review))

    def test_parent_save_method(self):
        """
        Test the inherited save method.
        """
        last_updated_at = self.review.updated_at
        self.review.save()
        current_updated_at = self.review.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """
        Test the inherited to_dict method.
        """
        self.assertNotEqual(self.review.to_dict(), self.review.__dict__)
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
