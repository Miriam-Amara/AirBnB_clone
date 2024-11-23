#!/usr/bin/python3
"""
Defines the BaseModel class, a foundational model for other classes.
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
     A base class providing common functionality for other models.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The time the instance was created.
        updated_at (datetime): The time the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Key-value pairs for attribute initialization.
                      If present, uses the dictionary to set attributes,
                      otherwise generates default values.
        """
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
        """
        Returns a string representation of the instance.

        Format:
            [<class name>] (<id>) <instance attributes>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute and saves the instance to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Converts `created_at` and `updated_at` to ISO format strings and
        includes the class name.

        Returns:
            dict: A dictionary of the instance's attributes.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.__dict__["created_at"].isoformat()
        dict_copy["updated_at"] = self.__dict__["updated_at"].isoformat()
        return dict_copy
