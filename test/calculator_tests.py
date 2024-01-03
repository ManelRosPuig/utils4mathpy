import unittest
from calculator import Calculator as calc

class CalculatorTests(unittest.TestCase):
    
    def test_is_prime(self):
        tests = [
            (2, True), (3, True), (4, False),
            (5, True), (6, False), (7, True),
            (8, False), (9, False), (10, False),
            (11, True), (12, False), (13, True),
            (14, False), (15, False), (16, False),
            (17, True), (18, False), (19, True),
            (20, False), (21, False), (22, False),
            (23, True), (24, False), (25, False),
            (26, False), (27, False), (28, False),
            (29, True), (30, False), (31, True),
            (32, False), (33, False), (34, False),
            (35, False), (36, False), (37, True)
        ]
        for value, expected in tests:
            self.assertEqual(calc.Calculator.is_prime(value), expected)

if __name__ == '__main__':
    unittest.main()
