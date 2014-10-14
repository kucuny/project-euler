import unittest

from p_006 import get_sum_of_the_squares, get_squares_of_the_sum, get_sum_square_difference


class TestSumSquareDifference(unittest.TestCase):
    def test_get_sum_of_the_squares_is_valid(self):
        self.assertEqual(get_sum_of_the_squares(10), 385)

    def test_get_squares_of_the_sum_is_valid(self):
        self.assertEqual(get_squares_of_the_sum(10), 3025)

    def test_get_sum_square_difference_is_first_hundred(self):
        self.assertEqual(get_sum_square_difference(100), 25164150)


if __name__ == '__main__':
    unittest.main()
