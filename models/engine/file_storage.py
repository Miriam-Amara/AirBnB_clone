#!/usr/bin/python3

"""

"""

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
        pass

    def save(self):
        pass

    def reload(self):
        pass

