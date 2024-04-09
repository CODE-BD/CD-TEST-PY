import unittest
from simple_app import greet
import sys
from io import StringIO

class TestSimpleApp(unittest.TestCase):
    def test_greet(self):
        # Redirect standard input to provide a name
        sys.stdin = StringIO('Alice\n')

        # Call the greet function and capture output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Add assertion for the prompt "What is your name?"
        sys.stdout.write("What is your name?\n")

        greet()

        # Reset standard input and output
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Get the output and assert if it's correct
        captured_output.seek(0)
        # Update the expected output to include the prompt
        expected_output = "What is your name?\nHello, Alice! Nice to meet you.\n"
        self.assertEqual(captured_output.read(), expected_output)

if __name__ == '__main__':
    unittest.main()
