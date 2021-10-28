"""Tests for the vectorfieldvalue module."""


import unittest

from emmpy.math.vectorfields.vectorfieldvalue import VectorFieldValue
from emmpy.math.vectors.vector3d import Vector3D


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfieldvalue module."""

    def test___init__(self):
        """Test the __init__ method."""
        position_data = [0, 1, 2]
        value_data = [3, 4, 5]
        position = Vector3D(position_data)
        value = Vector3D(value_data)
        vectorFieldValue = VectorFieldValue(position, value)
        for i in range(len(position_data)):
            self.assertAlmostEqual(vectorFieldValue.position[i], position[i])
        for i in range(len(value_data)):
            self.assertAlmostEqual(vectorFieldValue.value[i], value[i])


if __name__ == "__main__":
    unittest.main()
