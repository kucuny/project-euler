from p_002 import fibo, even_fibonacci_numbers
import unittest


class TestFibonacci(unittest.TestCase):
    def test_valid_fibonacci(self):
        self.assertEqual(fibo(1), 1)
        self.assertEqual(fibo(2), 2)
        self.assertEqual(fibo(3), 3)
        self.assertEqual(fibo(4), 5)
        self.assertEqual(fibo(5), 8)
        self.assertEqual(fibo(6), 13)
        self.assertEqual(fibo(7), 21)
        self.assertEqual(fibo(8), 34)
        self.assertEqual(fibo(9), 55)
        self.assertEqual(fibo(10), 89)

    def test_valid_even_fibonacci_numbers(self):
        self.assertEqual(even_fibonacci_numbers(1), 0)
        self.assertEqual(even_fibonacci_numbers(2), 2)
        self.assertEqual(even_fibonacci_numbers(3), 2)
        self.assertEqual(even_fibonacci_numbers(4), 2)
        self.assertEqual(even_fibonacci_numbers(10), 10)
        self.assertEqual(even_fibonacci_numbers(34), 44)

        self.assertEqual(even_fibonacci_numbers(4000000), 4613732)

if __name__ == '__main__':
    unittest.main()
