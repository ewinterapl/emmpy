import unittest

from emmpy.utilities.doubletolongbits import doubleToLongBits


class TestBuilder(unittest.TestCase):

    def test_doubleToLongBits(self):
        self.assertEqual(doubleToLongBits(14.5), 1097334784)


if __name__ == '__main__':
    unittest.main()
