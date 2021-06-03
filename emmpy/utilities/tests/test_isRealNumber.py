"""Test the isrealnumber module."""


import unittest

from emmpy.utilities.isrealnumber import isRealNumber


class TestDouble(unittest.TestCase):
    """Build and run tests for the isrealnumber module."""

    def test_isRealNumber(self):
        """Test the isRealNumber() function."""
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
        self.assertFalse(isRealNumber(1 + 1j))


if __name__ == "__main__":
    unittest.main()
