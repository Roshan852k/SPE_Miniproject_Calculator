import unittest
import math
from io import StringIO
import sys

from calculator import main 

class TestScientificCalculator(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(math.factorial(0), 1)
        self.assertEqual(math.factorial(1), 1)
        self.assertEqual(math.factorial(5), 120)
        self.assertEqual(math.factorial(10), 3628800)
    
    def test_square_root(self):
        self.assertEqual(math.sqrt(0), 0)
        self.assertEqual(math.sqrt(4), 2)
        self.assertEqual(math.sqrt(9), 3)
        self.assertAlmostEqual(math.sqrt(2), 1.4142, places=4)
    
    def test_natural_log(self):
        self.assertAlmostEqual(math.log(1), 0, places=4)
        self.assertAlmostEqual(math.log(math.e), 1, places=4)
    
    def test_power_function(self):
        self.assertEqual(math.pow(2, 3), 8)
        self.assertEqual(math.pow(5, 0), 1)
        self.assertEqual(math.pow(3, 2), 9)
        self.assertAlmostEqual(math.pow(2, 0.5), 1.4142, places=4)
    
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            math.sqrt(-1)
        with self.assertRaises(ValueError):
            math.log(0)
        with self.assertRaises(ValueError):
            math.log(-5)
    
if __name__ == "__main__":
    unittest.main()

