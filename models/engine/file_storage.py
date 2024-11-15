#!/usr/bin/python3
"""

"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ """

    __file_path = os.path.abspath("file.json")
    __objects = {}

    def all(self):
        """ """
        return FileStorage.__objects

    def new(self, obj):
        """ """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ """
        to_json = {}
        for key, value in FileStorage.__objects.items():
            to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(to_json, file, indent=4)

    def reload(self):
        """ """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                from_json = json.load(file)
                for key, value in from_json.items():
                    base_model = BaseModel(**value)
                    FileStorage.__objects[key] = base_model
        except FileNotFoundError:
            pass
