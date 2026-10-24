import unittest
from unittest.mock import patch
import sys
import os

# Import the main function from main.py
from main import main

class TestMainProgram(unittest.TestCase):

    def setUp(self):
        # Create a temporary test file
        self.test_filename = "test_data.txt"
        with open(self.test_filename, "w", encoding="utf-8") as f:
            f.write("\n".join(["1000", "221", "392", "621", "47", "448", "163", "120", "197", "781"]))

    def tearDown(self):
        # Remove the temporary test file
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    @patch("builtins.input", return_value="test_data.txt")
    def test_run_with_input_prompt(self, mock_input):
        sys.argv = ["main.py"]
        try:
            main()
        except SystemExit:
            self.fail("Program exited unexpectedly when using input prompt.")

    @patch("sys.argv", ["main.py", "test_data.txt"])
    def test_run_with_cli_argument(self):
        try:
            main()
        except SystemExit:
            self.fail("Program exited unexpectedly when using CLI argument.")

if __name__ == "__main__":
    unittest.main()
