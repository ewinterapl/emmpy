"""Tests for the vectorfield module."""


import unittest

from emmpy.exceptions.abstractmethodexception import AbstractMethodException
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.math.vectorfields.vectorfield import (
    VectorField, negate
)


# An identity mapping field.
vf1 = VectorField()
def my_eval1(location, buffer):
    buffer[:] = location
    return buffer
vf1.evaluate = my_eval1


class TestBuilder(unittest.TestCase):
    """Tests for the vectorfield module."""

    def test_evaluate(self):
        """Test the evaluate method."""
        with self.assertRaises(AbstractMethodException):
            VectorField.evaluate(None, None)

    def test_negate(self):
        """Test the negate function."""
        vf = negate(vf1)
        (x, y, z) = (1, 2, 3)
        location = VectorIJK(x, y, z)
        neg = -location
        v = vf.evaluate(location)
        for i in range(3):
            self.assertAlmostEqual(v[i], neg[i])


if __name__ == "__main__":
    unittest.main()
