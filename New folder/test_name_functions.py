import unittest
from name_functions import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_functions.py"""

    def test_first_last_name(self):
        formatted_name=get_formatted_name('faiz','khan')
        self.assertEqual(formatted_name,'faiz khan')

    def test_first_last_middle_name(self):
        formatted_name=get_formatted_name('faiz','khan','Muhammad')
        self.assertEqual(formatted_name,'faiz Muhammad khan')

unittest.main()
