# -*- coding: utf-8 -*-

import unittest
from checker import is_balanced


class Test(unittest.TestCase):
    """ Testing brackets"""

    def setUp(self):
        self.valid_text = ["[{}({})]", "(5+4)/[3+2]*{1*5}", "()[]{{()}}", "", "str"]
        self.invalid_text = ["[[{}({})]", "[[", "}}", "{{(()}}", "}}", "(}"]

    def test_valid_brackets(self):
        """Testing valid brackets"""
        for t in self.valid_text:
            self.assertTrue(is_balanced(t))

    def test_invalid_brackets(self):
        """Testing invalid brackets"""
        for t in self.invalid_text: 
            self.assertFalse(is_balanced(t))


if __name__ == '__main__':
    unittest.main()
