import unittest

from p_007 import is_prime_number, get_xst_prime_number


class Test10001stPrimeNumber(unittest.TestCase):
    def test_is_prime_number_is_valid(self):
        self.assertTrue(is_prime_number(3))
        self.assertTrue(is_prime_number(5))
        self.assertTrue(is_prime_number(7))
        self.assertTrue(is_prime_number(11))
        self.assertTrue(is_prime_number(13))
        self.assertFalse(is_prime_number(12))
        self.assertFalse(is_prime_number(14))
        self.assertTrue(is_prime_number(19))
        self.assertTrue(is_prime_number(31))

    def test_10001st_prime_number_is_valid(self):
        self.assertEqual(get_xst_prime_number(1), 2)
        self.assertEqual(get_xst_prime_number(2), 3)
        self.assertEqual(get_xst_prime_number(3), 5)
        self.assertEqual(get_xst_prime_number(4), 7)
        self.assertEqual(get_xst_prime_number(5), 11)
        self.assertEqual(get_xst_prime_number(6), 13)
        self.assertEqual(get_xst_prime_number(10001), 104743)


if __name__ == '__main__':
    unittest.main()
