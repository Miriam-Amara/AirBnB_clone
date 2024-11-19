#!/usr/bin/python3

"""

"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
import f_console_functions as cf


class HBNBCommand(cmd.Cmd):
    """ """

    prompt = "(hbnb) "
    __classes = {
             "BaseModel": BaseModel,
             "User": User,
             "State": "State",
             "City": "City",
             "Amenity": "Amenity",
             "Place": "Place",
             "Review": "Review",
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
        """
        class_name = line.split()[0]
        error_message = cf.validate_command_args(line, "create")

        if error_message:
            print(error_message)
        else:
            # create a new instance for the given class
            new_instance = HBNBCommand.__classes[class_name]()
            new_instance.save()
            print(new_instance.id)


    def do_show(self, line):
        """
        Displays the string representation
        of a class instance based on the id

        Usage:
            show <class name> <id> 
            # replace <class name> and <id> with the actual values

        """
        class_name, instance_id = line.split()[0:2]
        error_message = cf.validate_command_args(line, "show")

        if error_message:
            print(error_message)
        else:
            all_instances = storage.all()
            # checks if the id exists for the class
            instance_info = cf.id_exists(instance_id, class_name, all_instances)
            if instance_info:
                instance_dict = instance_info[1]
                # recreates the instance using the given class
                instance = HBNBCommand.__classes[class_name](**instance_dict)
                print(instance)
            else:
                print("** no instance found **")


    def do_destroy(self, line):
        """
        Deletes an instance from the file using its id

        Usage:
            destroy <class name> <id>
            # replace <class name> and <id> with the actual values
        """
        class_name, instance_id = line.split()[0:2]
        error_message = cf.validate_command_args(line, "destroy")
        if error_message:
            print(error_message)
        else:
            all_instances = storage.all()
            instance_info = cf.id_exists(instance_id, class_name, all_instances)
            if instance_info:
                id_key = instance_info[0]
                del all_instances[id_key]
                storage.save()
            else:
                print("** no instance found **")


    def do_all(self, line):
        """ """
        class_name = line.split()[0]
        list_of_classes = HBNBCommand.__classes
        if not line or line in list_of_classes.keys():
            all_instances = storage.all()
            for key, instance_dict in all_instances.items():
                instance_dict = instance_dict.to_dict()
                instance = list_of_classes[class_name](**instance_dict)
                print(instance)
        else:
            print("** class doesn't exist **")


    def do_update(self, line):
        """
        Updates an instance with a new attribute and value.
        
        Usage:
            update <class name> <id> <attribute name> <value>
        """
        error_message = cf.validate_command_args(line, "update")

        if error_message:
            print(error_message)

        else:
            # class_name, instance_id = line.split()[0:2]
            line_split = line.split()
            class_name, instance_id = line_split[0:2]
            attribute_name, value = line_split[2:4]
            is_valid_attribute = cf.validate_attribute(attribute_name)
            attribute_value = cf.convert_value_type(value)

            if is_valid_attribute:
                all_instances = storage.all()
                # checks if the id exists for the class
                instance_info = cf.id_exists(instance_id, class_name, all_instances)
                if instance_info:
                    instance_key, instance_dict = instance_info
                    instance_dict[attribute_name] = attribute_value
                    # basemodel = BaseModel(**instance_dict)
                    instance = HBNBCommand.__classes[class_name](**instance_dict)
                    all_instances[instance_key] = instance
                    instance.save()
                else:
                    print("** no instance found **")




if __name__ == "__main__":
    HBNBCommand().cmdloop()
