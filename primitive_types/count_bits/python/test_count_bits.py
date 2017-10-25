import sys
import unittest

from count_bits import count_bits


class TestCountBits(unittest.TestCase):

    def test_count_bits(self):
        self.assertEqual(count_bits(15), 4)
        self.assertEqual(count_bits(10), 2)
        self.assertEqual(count_bits(0), 0)
        self.assertEqual(count_bits(1), 1)
        self.assertEqual(count_bits(15333333333442434), 34)

    def test_count_bits_with_string(self):
        self.assertEqual(count_bits("sfsdfs"), 0)

    def test_count_bits_with_negative(self):
        self.assertEqual(count_bits(-10), 0)


if __name__ == '__main__':
    unittest.main()
