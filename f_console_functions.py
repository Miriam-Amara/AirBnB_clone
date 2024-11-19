#!/usr/bin/python3

"""

"""
import json
import os
import keyword
from models.base_model import BaseModel


def validate_command_args(line, command):
    """
    Validates the arguments of console commands.

    Args:
        line (str): The command line input.
        command (str): The specific command to validate.

    Returns:
        str: An error message if validation fails, otherwise False.
    """

    command_args = line.split()
    classes = [
        "BaseModel", "User", "State", "City",
        "Amenity", "Place", "Review"
        ]
    msg0 = "** class name missing **"
    msg1 = "** class doesn't exist **"
    msg2 = "** instance id missing **"
    msg3 = "** attribute name missing **"
    msg4 = "** value missing **"
    error_messages = {
        "create": [msg0, msg1],
        "show": [msg0, msg1, msg2],
        "destroy": [msg0, msg1, msg2],
        "update": [msg0, msg1, msg2, msg3, msg4],
    }
    if not command_args:
        return error_messages[command][0]  # class name missing

    if command_args[0] not in classes and command != "create":
        return error_messages[command][1]  # class doesn't exist

    if len(command_args) < 2 and command in ["show", "destroy", "update"]:
        return error_messages[command][2]  # instance id missing

    if command == "create" and (
        len(command_args) > 1 or command_args[0] not in classes
    ):
        return error_messages[command][1]  # class doesn't exist in create

    if command == "update":
        if len(command_args) < 3:
            return error_messages[command][3]  # attribute name missing
        if len(command_args) < 4:
            return error_messages[command][4]  # value missing

    return False


def id_exists(object_id, class_name, all_instances):
    """
    Check if the provided object_id exists in all_instances.

    Args:
        object_id (str): The ID to search for.
        all_instances (dict): A dictionary of instances, where each value
            is an object that provides a "to_dict" method and contains an "id" key.

    Returns:
        tuple: A tuple (key, instance_dict) if a match is found.
        None: If no match is found or an error occurs.
    """
    try:
        for key, instance_dict in all_instances.items():
            instance_dict = instance_dict.to_dict()
            if (object_id == instance_dict["id"] and
                class_name == instance_dict["__class__"]):
                return (key, instance_dict)
    except Exception as e:
        print(e)
    return None


def convert_value_type(value):
    """
    Attempts to convert the value into an integer, float,
    or keeps it as a string.

    Args:
        value (str): The value to be converted.

    Returns:
        int, float, or str: The value converted to the most appropriate type.
    """
    value = value.strip("'\"")  # remove surrounding quotes if any

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value  # return the value as a string if both conversions fail


def validate_attribute(attribute_name):
    """
    Validates if the given attribute is a valid Python identifier
    and not a reserved keyword.

    Args:
        attribute (str): The attribute name to validate.

    Returns:
        bool: True if the attribute is valid, False otherwise.
    """
    if not attribute_name.isidentifier():
        print(
            f"Invalid attribute name: "
            f"'{attribute_name}' is not a valid identifier."
        )
        return False

    if keyword.iskeyword(attribute_name):
        print(
            f"Invalid attribute name: "
            f"'{attribute_name}' is a reserved keyword."
            )
        return False

    return True
