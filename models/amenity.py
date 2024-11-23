#!/usr/bin/python3


"""
Defines the Amenity class, which inherits from BaseModel and
represents an amenity in the system.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from BaseModel and adds a 'name' attribute.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
