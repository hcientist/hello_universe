import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from jmu_gradescope_utils import JmuTestCase, required, check_submitted_files
import jmu_gradescope_utils

class TestHelloWorld(JmuTestCase):

    FILENAME = 'hello.py'

    def to_lower(s):
        return s.lower()

    @required()
    @weight(0)
    def test_submitted_files(self):
        """Check submitted files"""
        self.assertRequiredFilesPresent([self.FILENAME])
        
    @weight(8)
    def test_output(self):
        """Outputs "hello"."""
        string_in = ""
        expected = "hello"
        self.assertOutputCorrect(self.FILENAME, string_in, expected, processor=to_lower)