import unittest

from p_004 import is_valid_input, get_converted_string, is_palindrome, \
    get_largest_palindrome_product, get_numbers


class TestBaseFunction(unittest.TestCase):
    def test_is_valid_input(self):
        self.assertTrue(is_valid_input('abc'))
        self.assertFalse(is_valid_input(''))
        self.assertFalse(is_valid_input(None))
        self.assertTrue(is_valid_input('a'))

    def test_get_converted_string_is_valid(self):
        self.assertEqual(get_converted_string('aaa'), 'aaa')
        self.assertEqual(get_converted_string(123), '123')
        self.assertEqual(get_converted_string(None), None)
        self.assertEqual(get_converted_string(321), '321')

    def test_is_palindrome_valid(self):
        self.assertTrue(is_palindrome('aa'))
        self.assertTrue(is_palindrome('abcddcba'))
        self.assertTrue(is_palindrome('abcdcba'))
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(5432112345))
        self.assertTrue(is_palindrome(543212345))
        self.assertTrue(is_palindrome(10244201))
        self.assertTrue(is_palindrome(1024201))
        self.assertFalse(is_palindrome(None))
        self.assertFalse(is_palindrome(''))
        self.assertFalse(is_palindrome(342943))
        self.assertTrue(is_palindrome(9009))

    def test_get_numbers_is_valid(self):
        self.assertEquals(get_numbers(13), (1, 13))
        self.assertEquals(get_numbers(9009), (91, 99))

    def test_get_largesst_palindrome_product_is_valid(self):
        self.assertEquals(get_largest_palindrome_product(95), (9009, 91, 99))
        self.assertEquals(get_largest_palindrome_product(999), (906609, 913, 993))


if __name__ == '__main__':
    unittest.main()
