import unittest

from emmpy.java.lang.double import Double


class TestDouble(unittest.TestCase):

    def test_doubleToLongBits(self):
        self.assertEqual(Double.doubleToLongBits(14.5), 1097334784)


if __name__ == '__main__':
    unittest.main()
