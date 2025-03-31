#!/usr/bin/env python3

import unittest
import math
from cal import square_root, factorial, natural_log, power

class TestCalculator(unittest.TestCase):
    
    def test_square_root(self):
        self.assertEqual(square_root(36),6)
        with self.assertRaises(ValueError):
            square_root(-1)
    
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-3)
    
    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(1), 0)
        self.assertAlmostEqual(natural_log(10), math.log(10))
        with self.assertRaises(ValueError):
            natural_log(0)
        with self.assertRaises(ValueError):
            natural_log(-5)
    
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(10, -1), 0.1)

if __name__ == '__main__':
    unittest.main()

