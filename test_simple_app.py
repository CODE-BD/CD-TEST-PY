import unittest
from simple_app import greet

class TestSimpleApp(unittest.TestCase):
    def test_greet(self):
        # Redirect standard input to provide a name
        import sys
        from io import StringIO
        sys.stdin = StringIO('Alice\n')

        # Call the greet function and capture output
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        greet()

        # Reset standard input and output
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        # Get the output and assert if it's correct
        captured_output.seek(0)
        self.assertEqual(captured_output.read(), "Hello, Alice! Nice to meet you.\n")

if __name__ == '__main__':
    unittest.main()
