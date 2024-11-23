#!/usr/bin/python3

"""
Defines the State class, which inherits from BaseModel
and represents a state in the system.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Inherits from BaseModel and includes
    attributes related to a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
