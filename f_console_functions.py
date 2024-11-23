#!/usr/bin/python3


"""
This module provides utility functions to support the functionality
of the HBNBCommand class. These functions handle tasks such as
command validation, instance ID checking, attribute validation,
type conversion, and argument extraction.

Functions:
    - validate_command_args(line, cmd): Validates arguments
      for a given command.

    - id_exists(obj_id, cls_name, all_instances): Checks if an instance ID
      exists for a class.

    - convert_value_type(value): Converts a value to its
      appropriate type (int, float, or str).

    - validate_attribute(attribute_name): Validates attribute names.

    - extract_valid_args(line): Extracts valid arguments from
      a formatted input string.
"""


import re
import keyword


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
        "BaseModel", "User", "State",
        "City", "Amenity", "Place", "Review"
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

    if (cmd in ["create", "count"] and
            (len(cmd_args) > 1 or cmd_args[0] not in classes)):
        return err_msg[cmd][1]  # class doesn't exist in 'create' or 'count'

    if cmd == "update":
        if len(cmd_args) < 3:
            return err_msg[cmd][3]  # attribute name missing
        if len(cmd_args) < 4:
            return err_msg[cmd][4]  # value missing

    return False


def id_exists(cls_name, obj_id, all_instances):
    """
    Check if the provided object_id exists in all_instances.

    Args:
        object_id (str): The ID to search for.
        cls_name (str): The specified class of the obj.
        all_instances (dict): A dictionary of objects, where
        each value is a reference or address of an obj.

    Returns:
        tuple: A tuple (key, obj) if a match is found.
        None: If no match is found or an error occurs.
    """
    try:
        for key, obj in all_instances.items():
            if f"{cls_name}.{obj_id}" == key :
                return (key, obj)
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
        print(f"Invalid attribute name: "
              f"'{attribute_name}' is a reserved keyword.")
        return False

    return True


def extract_valid_args(line):
    """
    Extracts valid arguments from a string based on specific patterns.

    Args:
        line (str): The input string to extract arguments from.

    Returns:
        str: A space-separated string of extracted arguments or
        the original string if no patterns match.
    """

    # Pattern to match quoted strings or non-whitespace values
    pattern1 = r'"([^"]+)"|([^,\s]+)'
    # Pattern to match a class name, instance ID, and dictionary-like structure
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
