import unittest
from utils4mathpy import divisors, DivisorOptions

class DivisorsTests(unittest.TestCase):

    def test_should_return_divisors(self):
        divisor_numbers = [
            (20, [2, 4, 5, 10, 20]),
            (50, [2, 5, 10, 25, 50]),
            (128, [2, 4, 8, 16, 32, 64, 128])
        ]
        for number, expected_divisors in divisor_numbers:
            self.assertEqual(divisors(number), expected_divisors)

    def test_should_return_divisors_with_limit(self):
        self.assertEqual(divisors(20, DivisorOptions(limit = 2)), [2, 4])
    
    def test_should_return_divisors_with_limit_and_reverse(self):
        self.assertEqual(divisors(20, DivisorOptions(limit = 2, reverse = True)), [20, 10])

    def test_should_return_divisors_with_limit_and_include_self_set_to_false(self):
        self.assertEqual(divisors(20, DivisorOptions(limit = 2, include_self = False)), [2, 4])

    def test_should_return_divisors_with_limit_and_include_one_set_to_true(self):
        self.assertEqual(divisors(20, DivisorOptions(limit = 2, include_one = True)), [1, 2])

    # def test_should_raise_type_error_invalid_arguments(self):
    #     invalid_arguments = [
    #         [1.5, "1", "Hello!", True, None],
    #         [
    #             [10, ],
    #             []
    #         ]
    #     ]
    #     for arg in invalid_arguments:
    #         with self.assertRaises(TypeError):
    #             divisors(arg[0])

if __name__ == '__main__':
    unittest.main()