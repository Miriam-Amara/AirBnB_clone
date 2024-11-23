#!/usr/bin/python3

"""

"""
import json
import os
import re
import keyword
from models.base_model import BaseModel


def validate_command_args(line, cmd):
    """
    Validates the arguments of console commands.

    Args:
        line (str): The command line input.
        command (str): The specific command to validate.

    Returns:
        str: An error message if validation fails, otherwise False.
    """

    cmd_args = line.split()
    classes = [
        "BaseModel", "User", "State", "City",
        "Amenity", "Place", "Review"
        ]
    msg0 = "** class name missing **"
    msg1 = "** class doesn't exist **"
    msg2 = "** instance id missing **"
    msg3 = "** attribute name missing **"
    msg4 = "** value missing **"
    err_msg = {
        "create": [msg0, msg1],
        "count": [msg0, msg1],
        "show": [msg0, msg1, msg2],
        "destroy": [msg0, msg1, msg2],
        "update": [msg0, msg1, msg2, msg3, msg4],
    }
    if not cmd_args:
        return err_msg[cmd][0]  # class name missing

    if cmd_args[0] not in classes and cmd not in ["create", "count"]:
        return err_msg[cmd][1]  # class doesn't exist

    if len(cmd_args) < 2 and cmd in ["show", "destroy", "update"]:
        return err_msg[cmd][2]  # instance id missing

    if cmd in ["create", "count"] and (
        len(cmd_args) > 1 or cmd_args[0] not in classes
    ):
        return err_msg[cmd][1] # class doesn't exist in 'create' or 'count'

    if cmd == "update":
        if len(cmd_args) < 3:
            return err_msg[cmd][3]  # attribute name missing
        if len(cmd_args) < 4:
            return err_msg[cmd][4]  # value missing

    return False


def id_exists(obj_id, cls_name, all_instances):
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
        for key, inst_addr in all_instances.items():
            inst_dict = inst_addr.to_dict()
            if (obj_id == inst_dict["id"] and
                cls_name == inst_dict["__class__"]):
                return (key, inst_addr)
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


def extract_valid_args(line):
    """
    
    """
    pattern1 = r'"([^"]+)"|([^,\s]+)'
    dict_pattern = r'([^"]+)\s"([^"]+)",?\s*(\{.*?\})'
    
    if "{" not in line:
        first_match = re.findall(pattern1, line)
        if first_match:
            found_match = [match[0] or match[1] for match in first_match]
            return " ".join(found_match)
    else:
        second_match = re.search(dict_pattern, line)
        if second_match:
            return " ".join(second_match.groups())
    
    return line
        

if __name__ == "__main__":
    line1 =  'Place "39eaf3b1-f641-4fd0-94a0-d071b7b868ed", "age", 54, firsname, Betty'
    line2 = """BaseModel "38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89}"""
    line3 = "User 39eaf3b1-f641-4fd0-94a0-d071b7b868ed age 54"
    line4 = 'User "95c0f625-a76f-4c75-9fe2-a2a7531d8b2d" {"first_name": Kelly, "age": 26}'

    result = extract_valid_args(line2)
    print(result)