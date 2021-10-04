"""Tests for the cylindricalvectorfieldvalue module."""


import unittest

from emmpy.crucible.core.math.coords.cylindricalvectorfieldvalue import (
    CylindricalVectorFieldValue
)
from emmpy.math.coordinates.cylindricalvector import CylindricalVector


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricalvectorfieldvalue module."""

    def test___init__(self):
        """Test the __init__ method."""
        position = CylindricalVector(1, 2, 3)
        value = CylindricalVector(4, 5, 6)
        cvfv = CylindricalVectorFieldValue(position, value)
        self.assertIsInstance(cvfv, CylindricalVectorFieldValue)
        for i in range(3):
            self.assertAlmostEqual(cvfv.position[i], position[i])
            self.assertAlmostEqual(cvfv.value[i], value[i])


if __name__ == '__main__':
    unittest.main()
