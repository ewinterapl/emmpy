"""Tests for the PolarVector class."""


import unittest

from emmpy.crucible.core.math.coords.polarvector import (
    PolarVector,
    ZERO
)


class TestBuilder(unittest.TestCase):
    """Tests for the PolarVector class."""

    def test___init__(self):
        """Test the __init__ function."""
        pv = PolarVector(0.0, 0.1)
        self.assertIsNotNone(pv)

    def test_getRadius(self):
        """Test the getRadius() function."""
        pv = PolarVector(0.0, 0.1)
        self.assertAlmostEqual(pv.getRadius(), 0.0)

    def test_getAngle(self):
        """Test the getAngle() function."""
        pv = PolarVector(0.0, 0.1)
        self.assertAlmostEqual(pv.getAngle(), 0.1)

    def test_ZERO(self):
        """Test the ZERO constant."""
        self.assertAlmostEqual(ZERO.getRadius(), 0)
        self.assertAlmostEqual(ZERO.getAngle(), 0)


if __name__ == '__main__':
    unittest.main()
