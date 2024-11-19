#!/usr/bin/python3

"""

"""

import unittest
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ """

    def setUp(self):
        """ """
        self.my_model = BaseModel()

    def test_save_first_base_model_instance(self):
        """ """
        try:
            self.my_model.save()
        except Exception:
            self.fail(
                f"save method of FileStorage class failed to save {self.my_model}"
            )

    def test_save_second_base_model_instance(self):
        """ """
        try:
            self.my_model.save()
        except Exception:
            self.fail(
                f"save method of FileStorage class failed to save {self.my_model}"
            )

    def test_save_third_base_model_instance(self):
        """ """
        try:
            self.my_model.save()
        except Exception:
            self.fail(
                f"save method of FileStorage class failed to save {self.my_model}"
            )


if __name__ == "__main__":
    unittest.main()
