#!/usr/bin/python3
# from models import FileStorage
from models.base_model import BaseModel

import inspect
# print(inspect.getsource(TestCase))

class MyClass:
    __objects = {}

    def new(self):
        self.id = "10"
        MyClass.__objects[f"{self.__class__.__name__}.{self.id}"] = {'my_class_id': 10}
        return MyClass.__objects

new_class = MyClass()
print(new_class.new())
