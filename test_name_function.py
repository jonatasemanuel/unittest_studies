import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Test for name_function/ return.py"""
    def test_first_name(self):
        """Names like 'Janis Joplin' works?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Names like 'Wolfgang Amadeus Mozart' works?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
