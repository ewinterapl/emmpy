import unittest

from emmpy.utilities.isrealnumber import isRealNumber


class TestDouble(unittest.TestCase):

    def test_isRealNumber(self):
        self.assertTrue(isRealNumber(0))
        self.assertTrue(isRealNumber(0.0))
        self.assertTrue(isRealNumber(-0))
        self.assertTrue(isRealNumber(-0.0))
        self.assertTrue(isRealNumber(1))
        self.assertTrue(isRealNumber(1.1))
        self.assertTrue(isRealNumber(-1))
        self.assertTrue(isRealNumber(-1.1))
        self.assertFalse(isRealNumber(None))
        self.assertFalse(isRealNumber("0"))


if __name__ == '__main__':
    unittest.main()
