#!/usr/bin/python3

"""
Unit tests for HBNBCommand Interpreter
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


def reset_buffer(buffer):
    """
    Clears and resets the provided StringIO buffer.
    """
    buffer.truncate(0)  # clear the buffer
    buffer.seek(0)  # reset position to the beginning.


class TestDefaultConsoleCommands(unittest.TestCase):
    """
    Test suite for default or system-level commands in the HBNBCommand console.

    This class contains unittests for commands that handle:
    - Help output for console usage.
    - Behavior when an empty line is entered.
    - Exit commands like 'quit' and 'EOF'.
    """

    def test_help(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue()

        self.assertIn("show <class name> <id>", output)

    def test_emptyline(self):
        """
        Test that emptyline does nothing when Enter is pressed.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().emptyline()
            output = f.getvalue()
        self.assertEqual(output, "")

    def test_quit(self):
        """
        Test that the do_quit method returns True and exits the program.
        """
        output = HBNBCommand().onecmd("quit")
        self.assertTrue(output)

    def test_EOF(self):
        """
        Test that the do_EOF method returns True and exits the program.
        """
        output = HBNBCommand().onecmd("EOF")
        self.assertTrue(output)


class TestInvalidArg(unittest.TestCase):
    """
    Tests for invalid arguments in HBNB commands
    (missing class name, invalid class, etc.)
    """

    def test_missing_classname(self):
        """
        Test that missing class name prints
        '** class name missing **' error.
        """
        cmd_list = ["create", "count", "show", "destroy", "update"]

        with patch("sys.stdout", new=StringIO()) as f:
            for cmd in cmd_list:
                HBNBCommand().onecmd(cmd)
                output = f.getvalue()
                self.assertIn("** class name missing **", output)
                reset_buffer(f)

    def test_invalid_classname(self):
        """
        Test that invalid class name prints
        '** class doesn't exist **' error.
        """
        arg_list = [
            "create Base",  # create command
            "Base.create()",
            "BaseModel.create('8575yhru5')",
            "count place",  # count command
            "Use.count()",
            'BaseModel.count("8575yhru5")',
            "all yyy",  # all commnand
            "zzz.all()",
            'state.all("465788")',
            "show review",  # show command
            "Stat.show()",
            'city.show("cd6f978a-dd87-4d4e-9afa-36dfbb027471")',
            "destroy aaa",  # destroy command
            "hbnb.destroy()",
            'alx.destroy("cd6f978a-dd87-4d4e-9afa-36dfbb027471")',
            "update city",  # update command
            "hhh.update()",
            'hhh.update("cd6f978a-dd87-4d4e-9afa-36dfbb027471")',
        ]
        with patch("sys.stdout", new=StringIO()) as f:
            for cmd in arg_list:
                HBNBCommand().onecmd(cmd)
                output = f.getvalue()
                self.assertIn("** class doesn't exist **", output)
                reset_buffer(f)

    def test_missing_id(self):
        """
        Test that missing instance ID prints
        '** instance id missing **' error.
        """
        arg_list = [
            "show City",  # show command
            "City.show()",
            "destroy Place",  # destroy command
            'Place.destroy("")',
            "update BaseModel",  # update command
            "BaseModel.update()",
        ]
        with patch("sys.stdout", new=StringIO()) as f:
            for arg in arg_list:
                HBNBCommand().onecmd(arg)
                output = f.getvalue()
                self.assertIn("** instance id missing **", output)
                reset_buffer(f)

    def test_no_instance_found(self):
        """
        Test that invalid instance ID prints
        '** no instance found **' error.
        """
        arg_list = [
            "show City 16888cb6f32e",  # show command
            'City.show("16888cb6f32e")',
            "destroy Place 16888cb6f32e",  # destroy command
            'Place.destroy("16888cb6f32e")',
            "update BaseModel 16888cb6f32e name Betty",  # update command
            'BaseModel.update("16888cb6f32e", name, "Betty")',
            'BaseModel.update("16888cb6f32e", {"name": Betty})',
        ]
        with patch("sys.stdout", new=StringIO()) as f:
            for arg in arg_list:
                HBNBCommand().onecmd(arg)
                output = f.getvalue()
                self.assertIn("** no instance found **", output)
                reset_buffer(f)

    def test_missing_attribute_name(self):
        """
        Test that missing attribute name prints
        '** attribute name missing **' error.
        """
        arg_list = [
            "update BaseModel 16888cb6f32e",
            'BaseModel.update("16888cb6f32e")',
        ]
        with patch("sys.stdout", new=StringIO()) as f:
            for arg in arg_list:
                HBNBCommand().onecmd(arg)
                output = f.getvalue()
                self.assertIn("** attribute name missing **", output)
                reset_buffer(f)

    def test_missing_attribute_value(self):
        """
        Test that missing attribute value prints
        '** value missing **' error.
        """
        arg_list = [
            "update BaseModel 16888cb6f32e name",
            'BaseModel.update("16888cb6f32e", "name")',
        ]
        with patch("sys.stdout", new=StringIO()) as f:
            for arg in arg_list:
                HBNBCommand().onecmd(arg)
                output = f.getvalue()
                self.assertIn("** value missing **", output)
                reset_buffer(f)

    def test_invalid_identifier(self):
        """
        Test that invalid attribute format prints error message
        '<attribute name> is not a valid identifier'.
        """

        attr_dict = {"First-name": "Betty"}
        objects = list(storage.all().values())
        if objects:
            obj = objects[0]
            cmd_list = [
                f"update BaseModel {obj.id} First-name Alx",
                f'BaseModel.update("{obj.id}", "First-name", Betty)',
                f'BaseModel.update("{obj.id}", {attr_dict})',
            ]

            with patch("sys.stdout", new=StringIO()) as f:
                for cmd in cmd_list:
                    HBNBCommand().onecmd(cmd)
                    output = f.getvalue()
                    self.assertIn(
                        "'First-name' is not a valid identifier.", output
                        )
                    reset_buffer(f)
        else:
            self.fail("No object found in storage.")

    def test_identifier_iskeyword(self):
        """
        Test that using a reserved keyword as an attribute name
        prints error message '<attribute name> is a reserved keyword'.
        """

        attr_dict = {"class": "Betty"}
        objects = list(storage.all().values())
        if objects:
            obj = objects[0]
            cmd_list = [
                f"update BaseModel {obj.id} class Alx",
                f'BaseModel.update("{obj.id}", "class", Betty)',
                f'BaseModel.update("{obj.id}", {attr_dict})',
            ]

            with patch("sys.stdout", new=StringIO()) as f:
                for cmd in cmd_list:
                    HBNBCommand().onecmd(cmd)
                    output = f.getvalue()
                    self.assertIn("'class' is a reserved keyword.", output)
                    reset_buffer(f)
        else:
            self.fail("No object found in storage.")


class TestCreate(unittest.TestCase):
    """
    Unit tests for the 'create' command in the HBNBCommand interpreter.
    """

    def test_create_class(self):
        """
        Test that 'create <classname>' and '<classname>.create()
        create a new instance of a given class.
        """
        classname_set = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "State",
            "Review",
        ]
        uuid_pattern = (
            r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
            )
        with patch("sys.stdout", new=StringIO()) as f:
            for classname in classname_set:
                # Test 'create <classname>'
                HBNBCommand().onecmd(f"create {classname}")
                cmd_output = f.getvalue().strip()
                self.assertRegex(cmd_output, uuid_pattern)
                reset_buffer(f)

                # Test '<classname>.create()
                HBNBCommand().onecmd(f"{classname}.create()")
                dot_cmd_output = f.getvalue().strip()
                self.assertRegex(dot_cmd_output, uuid_pattern)
                reset_buffer(f)


class TestCount(unittest.TestCase):
    """
    Unit tests for the 'all' command in the HBNBCommand interpreter.
    """

    def setUp(self):
        """
        Set up the initial count of instances for each class.
        """
        self.all_obj_count = {
            "BaseModel": 0,
            "User": 0,
            "Amenity": 0,
            "City": 0,
            "Place": 0,
            "State": 0,
            "Review": 0,
        }

        for classname_id in storage.all().keys():
            classname, obj_id = classname_id.split(".")
            if classname in self.all_obj_count:
                self.all_obj_count[classname] += 1

    def test_count(self):
        """
        Test that 'count <classname>' and '<classname>.count()
        correctly compute the number of instances for each class.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            for classname, class_count in self.all_obj_count.items():

                # Test 'count <classname>'
                HBNBCommand().onecmd(f"count {classname}")
                cmd_output = f.getvalue().strip()
                self.assertEqual(str(class_count), cmd_output)
                reset_buffer(f)

                # Test '<classname>.count()
                HBNBCommand().onecmd(f"{classname}.count()")
                dot_cmd_output = f.getvalue().strip()
                self.assertEqual(str(class_count), dot_cmd_output)
                reset_buffer(f)


class TestAll(unittest.TestCase):
    """
    Unit tests for the 'all' command in the HBNBCommand interpreter
    """

    def setUp(self):
        """
        Sets up test data for different classes.
        """
        self.class_objects = {
            "BaseModel": [],
            "User": [],
            "Amenity": [],
            "City": [],
            "Place": [],
            "State": [],
            "Review": [],
        }

        for clsname_id, obj in storage.all().items():
            classname, obj_id = clsname_id.split(".")
            if classname in self.class_objects:
                self.class_objects[classname].append(str(obj))

    def test_all(self):
        """
        Test that 'all' displays a list of all instances stored.
        """
        all_objects = [str(obj) for obj in storage.all().values()]
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
        self.assertEqual(str(all_objects), output)

    def test_all_class(self):
        """
        Test that 'all <class>' and '<class>.all()' displays
        a list of all the instances of a given class.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, obj_list in self.class_objects.items():
                # Test 'all <class>'
                HBNBCommand().onecmd(f"all {class_name}")
                cmd_output = f.getvalue().strip()
                self.assertEqual(str(obj_list), cmd_output)
                reset_buffer(f)

                # Test '<class>.all()'
                HBNBCommand().onecmd(f"{class_name}.all()")
                dot_cmd_output = f.getvalue().strip()
                self.assertEqual(str(obj_list), dot_cmd_output)
                reset_buffer(f)


class TestShow(unittest.TestCase):
    """
    Unit tests for the 'show' command in the HBNBCommand interpreter
    """

    def test_show(self):
        """
        Test that 'show <class> <id>' and '<class>.show(<id>)'
        correctly display the string representation of the objects.
        """

        with patch("sys.stdout", new=StringIO()) as f:
            for key, obj in storage.all().items():
                class_name, obj_id = key.split(".")

                # Test 'show <class> <id>'
                HBNBCommand().onecmd(f"show {class_name} {obj_id}")
                cmd_output = f.getvalue().strip()
                self.assertEqual(str(obj), cmd_output)
                reset_buffer(f)

                # Test '<class>.show(<id>)'
                HBNBCommand().onecmd(f'{class_name}.show("{obj_id}")')
                dot_cmd_output = f.getvalue().strip()
                self.assertEqual(str(obj), dot_cmd_output)
                reset_buffer(f)


class TestDestroy(unittest.TestCase):
    """
    Unit tests for the 'destroy' command in the HBNBCommand interpreter.
    """

    def test_destroy(self):
        """
        Test that 'destroy <class> <id>' and '<class>.destroy(<id>)'
        correctly deletes the object from storage (file or database).
        """
        all_objects = list(storage.all().keys())[:14]

        for idx, classname_id in enumerate(all_objects, start=1):
            class_name, obj_id = classname_id.split(".")

            if idx % 2 == 1:
                HBNBCommand().onecmd(f"destroy {class_name} {obj_id}")
            else:
                HBNBCommand().onecmd(f'{class_name}.destroy("{obj_id}")')

            self.assertNotIn(classname_id, storage.all())


class TestUpdate(unittest.TestCase):
    """
    Unit tests for the 'update' command in the HBNBCommand interpreter.
    """

    def test_update(self):
        """
        Test to confirm that;
        - 'update <class> <id> <attribute name> <attribute value',
        - '<class>.update(<id>, <attribute name>, <attribute value>)'
        - '<class>.update(<id>, <dictionary representation>)'
        correctly updates an object attributes.
        """
        all_cls_obj = {}
        cls_list = {
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "State",
            "Review",
        }

        for classname_id, obj in storage.all().items():
            cls_name, obj_id = classname_id.split(".")
            if cls_name in cls_list and cls_name not in all_cls_obj:
                all_cls_obj[cls_name] = obj
            if len(cls_list) == len(all_cls_obj):
                break

        with patch("sys.stdout", new=StringIO()) as f:
            for class_name, obj in all_cls_obj.items():
                HBNBCommand().onecmd(
                    f"update {class_name} {obj.id} name Alx year 2023"
                    )
                self.assertEqual(obj.name, "Alx")
                self.assertFalse(hasattr(obj, "year"))

                HBNBCommand().onecmd(
                    f'{class_name}.update("{obj.id}", "age", 34)'
                    )
                self.assertEqual(obj.age, 34)

                attr_dict = {"age": 50, "height": 6.78}
                HBNBCommand().onecmd(
                    f'{class_name}.update("{obj.id}", {attr_dict})'
                    )
                self.assertEqual(obj.age, 50)
                self.assertEqual(obj.height, 6.78)


if __name__ == "__main__":
    unittest.main()
