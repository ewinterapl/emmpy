"""Test code for the sphericalcoordconverter module."""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.sphericalcoordconverter import (
    SphericalCoordConverter
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.coordinates.sphericalvector import SphericalVector


# Test grids.
n = 25
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rs = np.linspace(0, 10, n)
thetas = np.linspace(0, pi, n)
phis = np.linspace(0, 2*pi, n)


class TestBuilder(unittest.TestCase):
    """Test code for the sphericalcoordconverter module."""

    def test___init__(self):
        """Test the __init__ method."""
        scc = SphericalCoordConverter()
        self.assertIsInstance(scc, SphericalCoordConverter)

    def test_toCoordinate(self):
        """Test the toCoordinate method."""
        scc = SphericalCoordConverter()
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = VectorIJK(x, y, z)
                    r = sqrt(x**2 + y**2 + z**2)
                    theta = atan2(sqrt(x**2 + y**2), z)
                    phi = atan2(y, x)
                    spherical = scc.toCoordinate(cartesian)
                    self.assertAlmostEqual(spherical.r, r)
                    self.assertAlmostEqual(spherical.theta, theta)
                    self.assertAlmostEqual(spherical.phi, phi)

    def test_toCartesian(self):
        """Test the toCartesian method."""
        scc = SphericalCoordConverter()
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    spherical = SphericalVector(r, theta, phi)
                    x = r*sin(theta)*cos(phi)
                    y = r*sin(theta)*sin(phi)
                    z = r*cos(theta)
                    cartesian = scc.toCartesian(spherical)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)


if __name__ == '__main__':
    unittest.main()
