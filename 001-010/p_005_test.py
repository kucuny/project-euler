import unittest

from p_005 import get_smallest_multiple


class TestSmallestMultiple(unittest.TestCase):
    def test_get_smallest_multiple_value_is_valie(self):
        self.assertEqual(get_smallest_multiple(10), 2520)
        self.assertEqual(get_smallest_multiple(11), 27720)
        self.assertEqual(get_smallest_multiple(20), 232792560)


if __name__ == '__main__':
    unittest.main()
