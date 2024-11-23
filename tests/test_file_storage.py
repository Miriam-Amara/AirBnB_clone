#!/usr/bin/python3

"""
Unittest module for testing the FileStorage class.
"""

import unittest
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the save method of FileStorage class.
    """

    def setUp(self):
        """
        Set up a FileStorage instance for testing.
        """
        self.my_model = BaseModel()

    def test_save_first_base_model_instance(self):
        """
        Test the save method for correct serialization of data.
        """
        try:
            self.my_model.save()
        except Exception:
            self.fail(
                "save method of FileStorage class "
                f"failed to save {self.my_model}"
            )

    def test_save_second_base_model_instance(self):
        """
        Test the save method for correct serialization of data.
        """
        try:
            self.my_model.save()
        except Exception:
            self.fail(
                "save method of FileStorage class "
                f"failed to save {self.my_model}"
            )

    def test_save_third_base_model_instance(self):
        """
        Test the save method for correct serialization of data.
        """
        try:
            self.my_model.save()
        except Exception:
            self.fail(
                "save method of FileStorage class "
                f"failed to save {self.my_model}"
            )


if __name__ == "__main__":
    unittest.main()
