#!/usr/bin/python3

"""
Defines the City class, which inherits from BaseModel and
represents a city in the system.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel.

    Attributes:
        state_id (str): The state identifier where the city is located.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
