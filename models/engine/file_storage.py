#!/usr/bin/python3
"""

"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review

class FileStorage:
    """ """

    __file_path = os.path.abspath("basemodel_file.json")
    __objects = {}

    def all(self):
        """ """
        return FileStorage.__objects

    def new(self, obj):
        """ """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ """
        to_json = {}
        for key, value in FileStorage.__objects.items():
            to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(to_json, file, indent=4)

    def reload(self):
        """ """
        from_json = {}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                from_json = json.load(file)
        except Exception:
            pass
        
        classes = {
             "BaseModel": BaseModel,
             "User": User,
             "State": State,
             "City": City,
             "Amenity": Amenity,
             "Place": Place,
             "Review": Review,
        }
        for key, value in from_json.items():
            class_name = value["__class__"]
            instance = classes[class_name](**value)
            FileStorage.__objects[key] = instance
