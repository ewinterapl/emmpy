"""Tests for the arraycoefficientexpansion1d module."""


import unittest

from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)


class TestBuilder(unittest.TestCase):
    """Tests for the arraycoefficientexpansion1d module."""

    def test___init__(self):
        """Test the __init__ method."""
        ArrayCoefficientExpansion1D([0], 0)

    def test_getCoefficient(self):
        """Test the getCoefficient method."""
        c = ArrayCoefficientExpansion1D([0.0, 1.1, 2.2, 3.3], 1)
        self.assertAlmostEqual(c.getCoefficient(2), 1.1)


if __name__ == '__main__':
    unittest.main()
