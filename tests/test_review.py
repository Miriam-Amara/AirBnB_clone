#!/usr/bin/python3
"""

"""


import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    
    """
    def setUp(self):
        """ """
        self.review = Review()

    def test_class_inheritance(self):
        """ """
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
        Checks that Review instances has access to the
        parent (BaseModel) class attributes.
        """
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_class_attribute_value(self):
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_type_instance_attribute(self):
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)
        
    def test_instance_has_instance_method(self):
        self.assertTrue(hasattr(self.review, "__str__"))
        self.assertTrue(hasattr(self.review, "save"))
        self.assertTrue(hasattr(self.review, "to_dict"))



class TestReviewMethods(unittest.TestCase):
    """
    
    """

    def setUp(self):
        """ """
        self.review = Review()

    def test_parent_str_method(self):
        """ """
        obj_str = (f"[{self.review.__class__.__name__}] " +
        f"({self.id}) {self.__dict__}")

        self.assertTrue(obj_str, str(self.review))

    def test_parent_save_method(self):
        """ """
        last_updated_at = self.review.updated_at
        self.review.save()
        current_updated_at = self.review.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """ """
        self.assertNotEqual(self.review.to_dict(), self.review.__dict__)
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
