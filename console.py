#!/usr/bin/python3

"""

"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import f_console_functions as cf


class HBNBCommand(cmd.Cmd):
    """ """

    prompt = "(hbnb) "

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
            create BaseModel
        """
        error_message = cf.validate_command_args(line, "create")

        if error_message:
            print(error_message)
        else:
            storage = FileStorage()
            storage.reload()
            new_base_model = BaseModel()
            new_base_model.save()
            print(new_base_model.id)

    def do_show(self, line):
        """
        Displays the string representation
        of a class instance based on the id

        Usage:
            show Basemodel (id) # replace (id) with the actual id

        """
        error_message = cf.validate_command_args(line, "show")

        if error_message:
            print(error_message)
        else:
            instance_id = line.split()[1]
            all_instances = cf.read_basemodel_file()
            instance_info = cf.id_exists(instance_id, all_instances)
            if instance_info:
                instance_dict = instance_info[1]
                base_model_instance = BaseModel(**instance_dict)
                print(base_model_instance)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance from the file using its id

        Usage:
            destroy BaseModel (id) # replace (id) with the actual id
        """
        error_message = cf.validate_command_args(line, "destroy")
        if error_message:
            print(error_message)
        else:
            instance_id = line.split()[1]
            all_instances = cf.read_basemodel_file()
            instance_info = cf.id_exists(instance_id, all_instances)
            if instance_info:
                key = instance_info[0]
                del all_instances[key]
                cf.write_to_basemodel_file(all_instances)
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ """
        if not line or line == "BaseModel":
            all_instances = cf.read_basemodel_file()
            for key, instance_dict in all_instances.items():
                instance = BaseModel(**instance_dict)
                print(instance)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ """
        error_message = cf.validate_command_args(line, "update")

        if error_message:
            print(error_message)

        else:
            line_split = line.split()
            instance_id = line_split[1]
            attribute_name, value = line_split[2:4]
            is_valid_attribute = cf.validate_attribute(attribute_name)
            attribute_value = cf.convert_value_type(value)

            if is_valid_attribute:
                all_instances = cf.read_basemodel_file()
                instance_info = cf.id_exists(instance_id, all_instances)
                if instance_info:
                    key, instance_dict = instance_info
                    instance_dict[attribute_name] = attribute_value
                    all_instances[key] = instance_dict
                    cf.write_to_basemodel_file(all_instances)
                else:
                    print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
