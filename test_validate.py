import unittest
from validate import *

class TestIsNumber(unittest.TestCase):

    def test_is_number(self):

        self.assertTrue(is_number(5))
        self.assertTrue(is_number(-5))
        self.assertTrue(is_number(2.6))
        self.assertTrue(is_number("-50"))
        self.assertFalse(is_number("string"))


    def test_is_min_less_max(self):
        self.assertTrue(is_min_less_max(-1, 20))
        self.assertFalse(is_min_less_max(2, 2))
        self.assertFalse(is_min_less_max(30, 0))


    def test_is_equation(self):
        self.assertTrue(is_equation("-50"))
        self.assertTrue(is_equation("-50*x"))
        self.assertTrue(is_equation("5*x^3 + x**2 -8*x"))
        self.assertFalse(is_equation("5x"))
        self.assertFalse(is_equation("string"))


if __name__ == '__main__':
    unittest.main()
    