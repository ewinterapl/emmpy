"""Tests for the vectorfields module."""


import unittest

from emmpy.crucible.core.math.vectorfields.vectorfields import (
    addAll, scale, scaleLocation
)
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import VectorField


# Create vector fields for testing.

# An identity mapping field.
vf1 = VectorField()
def my_eval1(location, buffer):
    buffer[:] = location
    return buffer
vf1.evaluate = my_eval1

# A unit field.
vf2 = VectorField()
def my_eval2(location, buffer):
    buffer[:] = 1
    return buffer
vf2.evaluate = my_eval2

# A shifted-by-2 location field.
vf3 = VectorField()
def my_eval3(location, buffer):
    buffer[:] = location + 2
    return buffer
vf3.evaluate = my_eval3


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfields module."""

    def test_addAll(self):
        """Test the addAll method."""
        vf = addAll([vf1, vf2, vf3])
        (x, y, z) = (1, 2, 3)
        location = VectorIJK(x, y, z)
        sum = 2*location + 3
        buffer = VectorIJK()
        v = vf.evaluate(location, buffer)
        self.assertIs(v, buffer)
        for i in range(3):
            self.assertAlmostEqual(v[i], sum[i])

    def test_scale(self):
        """Test the scale method."""
        scaleFactor = -1.1
        vf = scale(vf1, scaleFactor)
        (x, y, z) = (1, 2, 3)
        location = VectorIJK(x, y, z)
        vs = location*scaleFactor
        buffer = VectorIJK()
        v = vf.evaluate(location, buffer)
        self.assertIs(v, buffer)
        for i in range(3):
            self.assertAlmostEqual(v[i], vs[i])

    def test_scaleLocation(self):
        """Test the scaleLocation method."""
        scaleFactor = -1.1
        vf = scaleLocation(vf1, scaleFactor)
        (x, y, z) = (1, 2, 3)
        location = VectorIJK(x, y, z)
        location_scaled = VectorIJK(x, y, z)*scaleFactor
        vs = location_scaled
        buffer = VectorIJK()
        v = vf.evaluate(location, buffer)
        self.assertIs(v, buffer)
        for i in range(3):
            self.assertAlmostEqual(v[i], vs[i])


if __name__ == '__main__':
    unittest.main()
