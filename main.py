#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest
from fraction import FractionTest

def count_vowels(string):
    ''' takes a string as an argument and returns the number of vowels in the string '''

    count = 0
    vowels = ['a','e', 'i', 'o', 'u']

    for char in string.lower():
        if char in vowels:
            count += 1

    return count

# def lastOccurrence(target, targetList):
#     ''' returns the index (offset from 0) of the last occurrence of the target item
#         or None if the target is not found '''
    
#     # lastOccurrence = None

#     for index, item in enumerate(targetList):
#         if item == target:
#             lastOccurrence = index

#     return lastOccurrence

def lastOccurrence(target, targetList):
    ''' faster approach '''

    offset = None
    for index, item in enumerate(reversed(targetList)):
        if item == target:
            offset = index
            break

    if offset is not None:
        return len(targetList) - offset - 1
    else:
        return None

# def my_enumerate(seq):
#     ''' provides the same functionality as enumerate WITHOUT calling enumerate() '''
#     counter = 0

#     for element in seq:
#         yield counter, element
#         counter += 1

def my_enumerate(seq):
    for i in range(len(seq)):
        yield i, seq[i]

def digits(n):
    ''' return num of digits in n '''

    digits = 1
    n = abs(n)

    while True:
        n //= 10
        if n > 0:
            digits += 1
        else:
            break

    return digits

def updown(n):
    ''' count from 0 to n and back to 0 '''

    yield from range(n)
    yield from range(n, -1, -1)

def fib_gen(n):
    ''' use generator to get n Fibo nums '''

    n1, n2 = 0, 1
    
    for i in range(n):
        yield n1
        n1, n2 = n2, n1 + n2

'''
    Test cases
'''

class AllTest(unittest.TestCase):
    ''' Test cases for all functions '''

    def test_count_vowels(self):
        ''' test count_vowels() '''
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('HELLO WORLD'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)
        self.assertEqual(count_vowels(''), 0)

    def test_lastOccurrence(self):
        ''' test lastOccurrence '''
        self.assertEqual(lastOccurrence(33, [ 42, 33, 21, 33 ]), 3)
        self.assertEqual(lastOccurrence(42, [ 42, 33, 21, 33 ]), 0)
        self.assertIsNone(lastOccurrence(100, [ 42, 33, 21, 33 ]))
        self.assertEqual(lastOccurrence('p', 'apple'), 2)
        self.assertIsNone(lastOccurrence('P', 'apple'))
        self.assertEqual(lastOccurrence(33, ['Coffee', 42, 33, 21, 33, '!Java' ]), 4)

    def my_enumerate(self):
        ''' test my_enumerate '''
        self.assertEquals([(i, x ) for i, x in my_enumerate('hello')], [(i, x ) for i, x in enumerate('hello')])
        self.assertEquals([(i, x ) for i, x in my_enumerate('hi! Pythonista')], [(i, x ) for i, x in enumerate('hi! Pythonista')])
        self.assertEquals([(i, x ) for i, x in my_enumerate([10, 20, 30, 40])], [(i, x ) for i, x in enumerate([10, 20, 30, 40])])
        self.assertEquals([(i, x ) for i, x in my_enumerate([])], [(i, x ) for i, x in enumerate([])])


if __name__ == "__main__":
    """ This is executed when run from the command line """
    
    unittest.main(exit=False, verbosity=2)
    
    # print(digits(1))
    
    # for i in updown(5):
    #     print(i)

    # for i in fib_gen(7):
    #     print(i)

