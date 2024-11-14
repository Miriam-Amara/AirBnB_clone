#!/usr/bin/python3
"""

"""

import json
import os


class FileStorage:
    """
    
    """
    __file_path =  os.path.abspath("file.json")
    __objects = {}

    def all(self):
        """ """
        return FileStorage.__objects

    def new(self, obj):
        """ """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ """
        for key, value in FileStorage.__objects.items():
            base_model_instance = value.to_dict()
            FileStorage.__objects[key] = base_model_instance
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file, indent=4)

    def reload(self):
        """ """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json.load(file)
        except FileNotFoundError:
            pass

