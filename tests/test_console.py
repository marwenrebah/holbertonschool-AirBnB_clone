import unittest
import sys
from console import HBNBCommand


class TestHBNBCommandMethods(unittest.TestCase):
    def setUp(self):
        """Set up the HBNBCommand instance for testing"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down after testing"""
        pass

    def capture_output(self, func, *args):
        """Capture the output of the function execution"""
        sys.stdout = sys.__stdout__
        result = None
        try:
            func(*args)
            result = sys.stdout.getvalue().strip()
        finally:
            sys.stdout = sys.__stdout__
        return result

    def test_quit_command(self):
        """Test quit command"""
        result = self.console.onecmd("quit")
        self.assertTrue(result)

    def test_EOF_command(self):
        """Test EOF command"""
        result = self.console.onecmd("EOF")
        self.assertTrue(result)

    def test_emptyline(self):
        """Test emptyline method"""
        result = self.console.onecmd("")
        self.assertIsNone(result)

    def test_help_quit(self):
        """Test help for quit command"""
        result = self.capture_output(self.console.onecmd, "help quit")
        self.assertEqual(result, "Quit command to exit the program")

    def test_create_missing_class_name(self):
        """Test create command with missing class name"""
        result = self.capture_output(self.console.onecmd, "create")
        self.assertEqual(result, "** class name missing **")

    def test_create_invalid_class_name(self):
        """Test create command with invalid class name"""
        result = self.capture_output(
            self.console.onecmd, "create InvalidClassName")
        self.assertEqual(result, "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create command with valid class name"""
        result = self.capture_output(
            self.console.onecmd, "create User")
        self.assertTrue(result)  # Ensure that an ID is generated

    def test_show_missing_class_name(self):
        """Test show command with missing class name"""
        result = self.capture_output(self.console.onecmd, "show")
        self.assertEqual(result, "** class name missing **")


if __name__ == '__main__':
    unittest.main()
