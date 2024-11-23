#!/usr/bin/python3
"""
This module contains the FileStorage class
that manages the storage of objects. It provides methods
to save, retrieve, and reload objects to and from a JSON file.
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
    """
    Handles the storage of objects in a JSON file.
    The class manages the saving, reloading, and
    retrieval of objects in memory.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary of all objects stored in memory.
    """

    __file_path = os.path.abspath("basemodel_file.json")
    __objects = {}

    def all(self):
        """
        Retrieves all stored objects.

        Returns:
            dict: A dictionary of all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to store.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves all objects in memory to a JSON file.

        Converts each object to a dictionary and
        writes the data to the file specified by __file_path.
        """
        to_json = {}
        for key, value in FileStorage.__objects.items():
            to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(to_json, file, indent=4)

    def reload(self):
        """
        Reloads objects from the JSON file into memory.

        Reads data from the JSON file and creates instances
        of the appropriate classes based on the data.
        The objects are then stored in memory.
        """
        from_json = {}
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                from_json = json.load(file)
        except Exception:
            pass

        for key, value in from_json.items():
            class_name = value["__class__"]
            instance = classes[class_name](**value)
            FileStorage.__objects[key] = instance
