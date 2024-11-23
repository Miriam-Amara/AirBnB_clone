#!/usr/bin/python3

"""

"""


import cmd
import re
import ast
import f_console_functions as cf
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ """

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
        """
        err_message = cf.validate_command_args(line, "create")

        if err_message:
            print(err_message)
        else:
            cls_name = line.split()[0]
            # create a new instance for the given class
            new_instance = HBNBCommand.__classes[cls_name]()
            new_instance.save()
            print(new_instance.id)

    def do_count(self, line):
        """ """
        err_message = cf.validate_command_args(line, "count")

        if err_message:
            print(err_message)
        else:
            cls_name = line.split()[0]
            count = 0
            inst_addr = list(storage.all().values())
            for i in range(len(inst_addr)):
                inst_dict = inst_addr[i].to_dict()
                if inst_dict["__class__"] == cls_name:
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
            cls_name, inst_id = line.split()[0:2]
            all_instances = storage.all()
            # checks if the id exists for the class
            inst_info = cf.id_exists(inst_id, cls_name, all_instances)
            if inst_info:
                inst = inst_info[1]
                print(inst)
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
            cls_name, inst_id = line.split()[0:2]
            all_instances = storage.all()
            inst_info = cf.id_exists(inst_id, cls_name, all_instances)
            if inst_info:
                id_key = inst_info[0]
                del all_instances[id_key]
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
        cls = HBNBCommand.__classes
        inst_addr = list(storage.all().values())

        if line:
            cls_name = line.split()[0]
            if cls_name in cls:
                filtered_inst = []
                for inst in inst_addr:
                    inst_dict = inst.to_dict()
                    if inst_dict["__class__"] == cls_name:
                        filtered_inst.append(str(inst))
                print(filtered_inst)
            else:
                print("** class doesn't exist **")
        else:

            all_inst_str = [str(inst) for inst in inst_addr]
            print(all_inst_str)

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
            cls_name, inst_id, attr_data = args.split(maxsplit=2)
            all_instances = storage.all()
            inst_info = cf.id_exists(inst_id, cls_name, all_instances)
            try:
                # Parse string representation of dictionary into a Python dict
                attr_dict = ast.literal_eval(attr_data)
            except (ValueError, SyntaxError) as e:
                print(f"Did you parse a dictionary? If Yes! -> Failed to parse dictionary: {e}")
                attr_name, attr_value = attr_data.split()[0:2]
                attr_value = cf.convert_value_type(attr_value)
                attr_dict = {attr_name: attr_value}

            if inst_info:
                instance = inst_info[1]
                for attr_name, attr_value in attr_dict.items():
                    attr_name = attr_name.strip('"')
                    if cf.validate_attribute(attr_name):
                        setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """ """
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
            if cmd in cmd_dict.keys():
                if cmd != "update":
                    inst_id = inst_id.strip('"')
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
