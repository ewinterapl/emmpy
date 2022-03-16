"""Test the nones module."""


import unittest

from emmpy.utilities.nones import nones


class TestBuildser(unittest.TestCase):
    """Build and run tests for the nones module."""

    def test_nones(self):
        """Test the nones function."""
        shape = (2,)
        n = nones(shape)
        for i in range(shape[0]):
            self.assertIsNone(n[i])
        shape = (2, 3)
        n = nones(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                self.assertIsNone(n[i][j])
        shape = (2, 3, 4)
        n = nones(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    self.assertIsNone(n[i][j][k])


if __name__ == "__main__":
    unittest.main()
