#!/usr/bin/python3
"""

"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.__dict__["created_at"].isoformat()
        dict_copy["updated_at"] = self.__dict__["updated_at"].isoformat()
        return dict_copy


if __name__ == "__main__":
    all_objs = models.storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
