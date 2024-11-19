#!/usr/bin/python3
"""

"""


import unittest
import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    
    """
    def setUp(self):
        """ """
        self.place = Place()

    def test_class_inheritance(self):
        """ """
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(self.place, Place)
        
    def test_class_has_class_attribute(self):
        """

        """
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))


    def test_instance_has_instance_attribute(self):
        """
        Checks that Place instances has access to the
        parent (BaseModel) class attributes.
        """
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_class_attribute_value_type(self):
        """
        
        """
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

    def test_type_instance_attribute(self):
        """ """
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime.datetime)
        self.assertIsInstance(self.place.updated_at, datetime.datetime)
        
    def test_instance_has_instance_method(self):
        """ """
        self.assertTrue(hasattr(self.place, "__str__"))
        self.assertTrue(hasattr(self.place, "save"))
        self.assertTrue(hasattr(self.place, "to_dict"))



class TestPlaceMethods(unittest.TestCase):
    """
    
    """

    def setUp(self):
        """ """
        self.place = Place()

    def test_parent_str_method(self):
        """ """
        obj_str = (f"[{self.place.__class__.__name__}] " +
        f"({self.id}) {self.__dict__}")

        self.assertTrue(obj_str, str(self.place))

    def test_parent_save_method(self):
        """ """
        last_updated_at = self.place.updated_at
        self.place.save()
        current_updated_at = self.place.updated_at
        self.assertNotEqual(last_updated_at, current_updated_at)

    def test_parent_to_dict_method(self):
        """ """
        self.assertNotEqual(self.place.to_dict(), self.place.__dict__)
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
