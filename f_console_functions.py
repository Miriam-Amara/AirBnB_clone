#!/usr/bin/python3

"""

"""
import json
import os
import keyword


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

    if command_args[0] != "BaseModel" and command != "create":
        return error_messages[command][1]  # class doesn't exist

    if len(command_args) < 2 and command in ["show", "destroy", "update"]:
        return error_messages[command][2]  # instance id missing

    if command == "create" and (
        len(command_args) > 1 or command_args[0] != "BaseModel"
    ):
        return error_messages[command][1]  # class doesn't exist in create

    if command == "update":
        if len(command_args) < 3:
            return error_messages[command][3]  # attribute name missing
        if len(command_args) < 4:
            return error_messages[command][4]  # value missing

    return False


def read_basemodel_file():
    """
    Reads and returns the data from 'basemodel_file.json'.

    Returns:
        dict: The data loaded from the JSON file,
        containing all BaseModel instances.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    file_path = os.path.abspath("basemodel_file.json")
    try:
        with open(file_path, "r") as file:
            all_basemodel_instance = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading file: {e}")
    return all_basemodel_instance


def write_to_basemodel_file(basemodel_instances):
    """
    Writes the given dictionary of basemodel instances
    to 'basemodel_file.json'.

    Args:
        basemodel_instances (dict): The dictionary to write to the file.

    Raises:
        TypeError: If the provided argument is not a dictionary.
    """
    file_path = os.path.abspath("basemodel_file.json")
    if basemodel_instances and isinstance(basemodel_instances, dict):
        try:
            with open(file_path, "w") as file:
                json.dump(basemodel_instances, file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        raise TypeError("Expected a dictionary for 'basemodel_instances'.")


def id_exists(object_id, all_instances):
    """
    Checks if the provided object_id matches
    any instance ID in basemodel_instances.

    Args:
        object_id (str): The ID to search for.
        basemodel_instances (dict, optional): A dictionary of instances,
            where each value is a dictionary containing an "id" key.

    Returns:
        tuple: A tuple (key, instance_dict) if a match is found.
        None: If no match is found.

    Raises:
        TypeError: If basemodel_instances is not a dictionary.
    """
    if all_instances and isinstance(all_instances, dict):
        for key, instance_dict in all_instances.items():
            if object_id == instance_dict["id"]:
                return (key, instance_dict)
    else:
        raise TypeError("Expected a dictionary for 'basemodel_instances'.")
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
