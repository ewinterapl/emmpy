"""Test the doubletolongbits module."""


import unittest

from emmpy.utilities.doubletolongbits import doubleToLongBits


class TestBuilder(unittest.TestCase):
    """Build and run tests for the doubletolongbits module."""

    def test_doubleToLongBits(self):
        """Test the doubleToLongBits() function."""
        self.assertEqual(doubleToLongBits(14.5), 1097334784)


if __name__ == '__main__':
    unittest.main()
