"""Test the isragged module."""


import unittest

from emmpy.utilities.isragged import isRagged


class TestBuilder(unittest.TestCase):
    """Build and run tests for the isragged module."""

    def test_isRagged(self):
        """Test the isRagged() function."""
        with self.assertRaises(TypeError):
            isRagged(None)
        self.assertTrue(isRagged([[0, ], [1, 2]]))
        self.assertFalse(isRagged([[0, 1], [2, 3]]))
        self.assertFalse(isRagged([[0]]))
        self.assertFalse(isRagged([[0, 1]]))


if __name__ == "__main__":
    unittest.main()
