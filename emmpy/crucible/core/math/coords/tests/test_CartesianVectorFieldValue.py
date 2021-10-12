"""Tests for the cartesianvectorfieldvalue module."""


import unittest

from emmpy.crucible.core.math.coords.cartesianvectorfieldvalue import (
    CartesianVectorFieldValue
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the cartesianvectorfieldvalue module."""

    def test___init__(self):
        """Test the __init__ method."""
        position = VectorIJK(1, 2, 3)
        value = VectorIJK(4, 5, 6)
        cvfv = CartesianVectorFieldValue(position, value)
        self.assertIsInstance(cvfv, CartesianVectorFieldValue)
        for i in range(3):
            self.assertAlmostEqual(cvfv.position[i], position[i])
            self.assertAlmostEqual(cvfv.value[i], value[i])


if __name__ == '__main__':
    unittest.main()
