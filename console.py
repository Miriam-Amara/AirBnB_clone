#!/usr/bin/python3

"""

"""

import cmd
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    
    """
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

    
    def validate_command(self, line, command):
        """
        Displays customized error messages when commands are invalid
        """
        args = line.split()
        if command == "create":
            if not args:
                return "** class name missing **"
            elif args[0] != "BaseModel":
                return "** class doesn't exist **"
                
        elif command in ["show", "destroy", "all"]:   
            if not args:
                return "** class name missing **"
            elif args[0] != "BaseModel":
                return "** class doesn't exist **"
            elif len(args) == 1:
                return "** instance id missing **"
        return False
    
    def read_basemodel_file(self):
        """
        Opens and reads file.json that contains all instances of BaseModel
        """
        file_path = os.path.abspath("basemodel_file.json")
        try:
            with open(file_path, "r") as file:
                all_basemodel_instance = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading file: {e}")
        return all_basemodel_instance
    
    def write_to_basemodel_file(self, basemodel_instances):
        """
        Opens and writes to file.json
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

    def id_exists(self, object_id, basemodel_instances=None):
        """
        Checks if the provided object_id matches any instance ID in basemodel_instances.

        Args:
            object_id (str): The ID to search for.
            basemodel_instances (dict, optional): A dictionary of instances, 
                where each value is a dictionary containing an "id" key. Defaults to None.

        Returns:
            tuple: A tuple (key, instance_dict) if a match is found.
            None: If no match is found.

        Raises:
            TypeError: If basemodel_instances is not a dictionary.
        """
        if basemodel_instances and isinstance(basemodel_instances, dict):
            for key, instance_dict in basemodel_instances.items():
                if object_id == instance_dict["id"]:
                    return (key, instance_dict)
        else:
            raise TypeError("Expected a dictionary for 'basemodel_instances'.")
        return None
    
    def do_create(self, line):
        """
        Creates a new instance of BaseModel.
        Prints the id of the new instance created.

        Usage:
            create BaseModel
        """
        error_message = self.validate_command(line, "create")

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
        error_message = self.validate_command(line, "show")

        if error_message:
            print(error_message)
        else:
            instance_id = line.split()[1]
            all_instances = self.read_basemodel_file()
            instance_info = self.id_exists(instance_id, basemodel_instances=all_instances)
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
        error_message = self.validate_command(line, "destroy")
        if error_message:
            print(error_message)
        else:
            instance_id = line.split()[1]
            all_instances = self.read_basemodel_file()
            instance_info = self.id_exists(instance_id, basemodel_instances=all_instances)
            if instance_info:
                key = instance_info[0]
                del all_instances[key]
                self.write_to_basemodel_file(all_instances)
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        
        """
        if not line or line == "BaseModel":
            all_instances = self.read_basemodel_file()
            for key, instance_dict in all_instances.items():
                instance = BaseModel(**instance_dict)
                print(instance)
        else:
            print("** class doesn't exist **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
















# def do_show(self, line):
#         """
#         Displays the string representation
#         of a class instance based on the id
        
#         Usage:
#             show Basemodel (id) # replace (id) with the actual id

#         """
#         error = self.err_messages(line, "show")

#         if not error:
#             args = line.split()
#             file_path = os.path.abspath("file.json")
#             id_found = False
#             with open(file_path, "r") as basemodel_file:
#                 base_model_obj = json.load(basemodel_file)
#             for key, obj in base_model_obj.items():
#                 if args[1] == obj["id"]:
#                     id_found = True
#                     base_model_instance = BaseModel(**obj)
#                     print(base_model_instance)
#                     break
#             if id_found == False:
#                 print("** no instance found **")
#         else:
#             print(error)