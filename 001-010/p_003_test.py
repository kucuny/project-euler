from p_003 import largest_prime_factor
import unittest


class TestLargestPrimeFactor(unittest.TestCase):
    def test_valid_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13), 13)
        self.assertEqual(largest_prime_factor(14), 7)
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(600851475143), 6857)


if __name__ == '__main__':
    unittest.main()
