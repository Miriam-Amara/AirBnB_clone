#!/usr/bin/python3

"""
Module for the HBNB command interpreter.

Defines the 'HBNBCommand' class, which provides commands to manage
objects in the HBNB application.
"""


import ast
import cmd
import re
import f_console_functions as cf
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB application.

    This class provides commands to manage objects such as 'BaseModel',
    'User', 'State', 'City', 'Amenity', 'Place', and 'Review'.

    Supported commands include:
        - 'create': Creates a new object.
        - 'show': Displays an object by ID.
        - 'destroy': Deletes an object by ID.
        - 'all': Displays all objects or those of a specific class.
        - 'update': Updates an object with attributes.
        - 'count': Counts objects of a specific class.

    Attributes:
        prompt (str): The command prompt displayed to the user.
        __classes (dict): A mapping of class names to their corresponding
                          classes.

    Usage:
        Enter interactive mode by running the command interpreter.
        Use the available commands to interact with the application.

    Type 'help' or '?' at the prompt for a list of available commands.
    Type 'help <command>' for command details.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def emptyline(self):
        """
        Overides emptyline method to do nothing when a user press enter.
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel.
        Prints the id of the new instance created.

        Usage:
            create <class name>
            <class name>.create()
            # replace <class name> with the actual value
        """
        err_message = cf.validate_command_args(line, "create")

        if err_message:
            print(err_message)
        else:
            cls_name = line.split()[0]
            # create a new instance for the given class
            new_obj = HBNBCommand.__classes[cls_name]()
            new_obj.save()
            print(new_obj.id)

    def do_count(self, line):
        """
        Counts the number of instances of a specific class.

        Usage:
            count <class name>
            <class name>.count()
            # replace <class name> with the actual value
        """
        err_message = cf.validate_command_args(line, "count")

        if err_message:
            print(err_message)
        else:
            cls_name = line.split()[0]
            count = 0
            for obj in storage.all().values():
                if cls_name == obj.__class__.__name__:
                    count += 1
            print(count)

    def do_show(self, line):
        """
        Displays the string representation
        of a class instance based on the id

        Usage:
            show <class name> <id>
            <class name>.show(<id>)
            # replace <class name> and <id> with the actual values

        """
        err_message = cf.validate_command_args(line, "show")

        if err_message:
            print(err_message)
        else:
            cls_name, obj_id = line.split()[0:2]
            all_objects = storage.all()
            obj_info = cf.id_exists(cls_name, obj_id, all_objects)
            if obj_info:
                print(obj_info[1])  # Display string representation of object
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance from the file using its id

        Usage:
            destroy <class name> <id>
            <class name>.destroy(<id>)
            # replace <class name> and <id> with the actual values
        """
        err_message = cf.validate_command_args(line, "destroy")
        if err_message:
            print(err_message)
        else:
            cls_name, obj_id = line.split()[0:2]
            all_objects = storage.all()
            obj_info = cf.id_exists(cls_name, obj_id, all_objects)
            if obj_info:
                del all_objects[obj_info[0]]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Lists all instances or instances of a specific class.

        If no class name is provided, all instances are listed.
        If a class name is provided, only instances of that class are listed.

        Usage:
            all                # Lists all instances of all classes
            all <class name>   # Lists all instances of the specified class
            <class name>.all() # Lists all instances of the specified class
            # replace <class name> with the actual value
        """
        obj_ref = storage.all().values()
        if line:
            cls_name = line.split()[0]
            if cls_name in HBNBCommand.__classes:
                filtered_obj = [str(obj) for obj in obj_ref
                                if cls_name == obj.__class__.__name__]
                print(filtered_obj)
            else:
                print("** class doesn't exist **")
        else:

            all_obj_str = [str(obj) for obj in obj_ref]
            print(all_obj_str)

    def do_update(self, line):
        """
        Updates an instance with a new attribute and value.

        Usage:
            update <class name> <id> <attribute name> <value>
            <class name>.update(<id>, <attribute name>, <value>)
            <class name>.update(<id>, <dictionary representation>)
        """
        args = cf.extract_valid_args(line)
        err_message = cf.validate_command_args(args, "update")

        if err_message:
            print(err_message)

        else:
            cls_name, obj_id, attr_data = args.split(maxsplit=2)
            all_objects = storage.all()
            obj_info = cf.id_exists(cls_name, obj_id, all_objects)
            try:
                # Convert string representation of dictionary to a Python dict
                attr_dict = ast.literal_eval(attr_data)
            except (ValueError, SyntaxError) as e:
                print(
                    "Did you parse a dictionary? If Yes! "
                    f"-> Failed to parse dictionary: {e}"
                )
                attr_name, attr_value = attr_data.split()[0:2]
                attr_value = cf.convert_value_type(attr_value)
                attr_dict = {attr_name: attr_value}

            if obj_info:
                obj = obj_info[1]
                for attr_name, attr_value in attr_dict.items():
                    attr_name = attr_name.strip('"')
                    if cf.validate_attribute(attr_name):
                        setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """
        Handles input that doesn't match standard commands.

        This method checks if the input follows the format
        <class name>.<command>(<arguments>). If it does,
        it runs the corresponding command for the class.
        Otherwise, it prints an error message.
        """
        cmd_dict = {
            "create": self.do_create,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "update": self.do_update,
        }
        cmd_pattern = r"^(\w+)\.(\w+)\(([^\(]*)\)$"
        is_valid_cmd = re.search(cmd_pattern, line)
        if is_valid_cmd:
            cls_name, cmd, inst_id = is_valid_cmd.groups()
            if cmd in cmd_dict:
                if cmd != "update":
                    inst_id = inst_id.strip("'\"")
                args = f"{cls_name} {inst_id}"
                cmd_dict[cmd](args)
            else:
                print(
                    f"{cmd} is not a valid command"
                    + "\nType 'help' to display lists of valid commands."
                )
        else:
            print(f"**Invalid syntax: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
