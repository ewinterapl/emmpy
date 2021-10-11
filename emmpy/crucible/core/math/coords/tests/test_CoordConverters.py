"""Tests for the coordconverters module."""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.coordconverters import CoordConverters
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.exceptions.abstractmethodexception import AbstractMethodException
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.coordinates.sphericalvector import SphericalVector


# Test grids.
n = 25
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rhos = np.linspace(0, 10, n)
phis = np.linspace(0, 2*pi, n)
radiuss = np.linspace(0, 10, n)
lats = np.linspace(-pi/2, pi/2, n)
lons = np.linspace(-pi, pi, n)
angles = np.linspace(0, 2*pi, n)
ras = np.linspace(0, 2*pi, n)
decs = np.linspace(-pi/2, pi/2, n)
rs = np.linspace(0, 10, n)
thetas = np.linspace(0, pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the coordconverters module."""

    def test_convert(self):
        """Test the convert method."""
        # Cylindrical to Cartesian
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    x = rho*cos(phi)
                    y = rho*sin(phi)
                    cylindrical = CylindricalVector(rho, phi, z)
                    cartesian = CoordConverters.convert(cylindrical)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)
        # Spherical to Cartesian
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    x = r*sin(theta)*cos(phi)
                    y = r*sin(theta)*sin(phi)
                    z = r*cos(theta)
                    spherical = SphericalVector(r, theta, phi)
                    cartesian = CoordConverters.convert(spherical)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)
        # Invalid args.
        with self.assertRaises(ValueError):
            CoordConverters.convert(None)


if __name__ == '__main__':
    unittest.main()
