import unittest
from utils4mathpy import is_prime

class IsPrimeTests(unittest.TestCase):
    
    def test_is_prime_should_return_true_for_prime_numbers(self):
        prime_numbers = [
            2, 3, 5, 7, 11, 13, 17, 19, 23,
            29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97
        ]
        for number in prime_numbers:
            self.assertEqual(is_prime(number), True)

    def test_is_prime_should_return_false_for_complex_numbers(self):
        complex_numbers = [
            4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21,
            22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35,
            36
        ]
        for number in complex_numbers:
            self.assertEqual(is_prime(number), False)
    
    def test_is_prime_should_return_false_for_negative_numbers(self):
        negative_numbers = [
            -1, -2, -3, -4, -5, -6, -7, -8, -9, -10,
            -11, -12, -13, -14, -15, -16, -17, -18,
            -19, -20
        ]
        for number in negative_numbers:
            self.assertEqual(is_prime(number), False)

    def test_is_prime_should_return_false_for_zero(self):
        self.assertEqual(is_prime(0), False)
    
    def test_is_prime_should_return_false_for_one(self):
        self.assertEqual(is_prime(1), False)
    
    def test_is_prime_should_raise_error_for_non_numbers(self):
        for value in [1.5, "1", "Hello!", True, None]:
            with self.assertRaises(TypeError):
                is_prime(value)

if __name__ == '__main__':
    unittest.main()
