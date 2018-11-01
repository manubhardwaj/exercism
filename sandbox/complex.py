#!/usr/bin/env python3
import unittest

class complex:

    def __init__(self, r = 0, i = 0):
        self.r = r
        self.i = i

    def multiply(self, elem):
        a = self.r
        b = self.i
        c = elem.r
        d = elem.i
        return complex(a*c - b*d, a*d + b*c)

class ComplexTests(unittest.TestCase):

    def test_math(self):
        x = complex(1,1)
        y = complex(1,1)
        self.assertEqual(x.multiply(y).r, 0)
        self.assertEqual(x.multiply(y).i, 1)


if __name__ == '__main__':
    unittest.main()
