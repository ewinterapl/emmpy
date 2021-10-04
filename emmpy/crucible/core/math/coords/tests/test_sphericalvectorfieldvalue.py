"""Tests for the sphericalvectorfieldvalue module."""


import unittest

from emmpy.crucible.core.math.coords.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue
)
from emmpy.math.coordinates.sphericalvector import SphericalVector


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricalvectorfieldvalue module."""

    def test___init__(self):
        """Test the __init__ method."""
        position = SphericalVector(1, 2, 3)
        value = SphericalVector(4, 5, 6)
        svfv = SphericalVectorFieldValue(position, value)
        self.assertIsInstance(svfv, SphericalVectorFieldValue)
        for i in range(3):
            self.assertAlmostEqual(svfv.position[i], position[i])
            self.assertAlmostEqual(svfv.value[i], value[i])


if __name__ == '__main__':
    unittest.main()
