#!/usr/bin/python3

"""

"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestDefaultCommands(unittest.TestCase):
    """
    
    """
    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue()
        
        self.assertIn("show <class name> <id>", output)


class TestCreate(unittest.TestCase):
    """
    
    """

    def test_missing_classname(self):
        """ Test for missing class name """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue()
        self.assertIn("** class name missing **", output)


    def test_invalid_classname(self):
        """ Test for invalid class names """
        cmd_list = [
            "create Base", "Base.create()", "Base.create('8575yhru5')", "create BaseModel"
            ]
        print(cmd_list)
        with patch('sys.stdout', new=StringIO()) as f:
            for idx in range(3):
                # print("yes")
                HBNBCommand().onecmd(cmd_list[idx])
                # print(cmd_list[idx])
                output = f.getvalue()
                self.assertIn("** class doesn't exist **", output)
        print(output)


    def test_successful_execution(self):
        """
        Test that create successfully created a new instance.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue()
        self.assertIn("-", output)
        


if __name__ == "__main__":
    unittest.main()