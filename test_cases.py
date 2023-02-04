import vowels.py
import unittest

class TestCases(unittest.TestCase):
    def vowels_test(self):
        input = "hello"
        result = vowels.py.vowel_count(input)
        expected = 2
        self.assertEqual(expected,result)