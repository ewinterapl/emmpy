"""Tests for the polarcoordconverter module."""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.polarcoordconverter import (
    PolarCoordConverter
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.math.coordinates.polarvector import PolarVector


# Test grids.
n = 25
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
radiuss = np.linspace(0, 10, n)
angles = np.linspace(0, 2*pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the polarcoordconverter module."""

    def test___init__(self):
        """Test the __init__ method."""
        ccc = PolarCoordConverter()
        self.assertIsInstance(ccc, PolarCoordConverter)

    def test_toCoordinate(self):
        """Test the toCoordinate method."""
        pcc = PolarCoordConverter()
        for x in xs:
            for y in ys:
                cartesian = VectorIJ(x, y)
                radius = sqrt(x**2 + y**2)
                angle = atan2(y, x)
                polar = pcc.toCoordinate(cartesian)
                self.assertAlmostEqual(polar.r, radius)
                self.assertAlmostEqual(polar.phi, angle)

    def test_toCartesian(self):
        """Test the toCartesian method."""
        pcc = PolarCoordConverter()
        for radius in radiuss:
            for angle in angles:
                x = radius*cos(angle)
                y = radius*sin(angle)
                polar = PolarVector(radius, angle)
                cartesian = pcc.toCartesian(polar)
                self.assertAlmostEqual(cartesian.i, x)
                self.assertAlmostEqual(cartesian.j, y)


if __name__ == '__main__':
    unittest.main()
