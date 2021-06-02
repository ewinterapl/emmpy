import unittest

from emmpy.java.util.arrays import Arrays


class TestBuilder(unittest.TestCase):

    def test_hashCode(self):
        self.assertEqual(Arrays.hashCode([]), 0)

    def test_deepHashCode(self):
        self.assertEqual(Arrays.hashCode([]), 0)


if __name__ == '__main__':
    unittest.main()
