#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest

def count_vowels(string):
    count = 0
    vowels = ['a','e', 'i', 'o', 'u']

    for char in string.lower():
        if char in vowels:
            count += 1

    return count


def main():
    ''' Main entry point of the script '''
    print()

'''
    Test cases
'''

class AllTest(unittest.TestCase):
    ''' Test cases for all functions '''

    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('HELLO WORLD'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)
        self.assertEqual(count_vowels(''), 0)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    
    unittest.main(exit=False, verbosity=2)
    main()