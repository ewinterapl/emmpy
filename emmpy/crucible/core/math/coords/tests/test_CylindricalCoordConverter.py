"""Test code for the cylindricalcoordconverter module."""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.cylindricalcoordconverter import (
    CylindricalCoordConverter
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.coordinates.cylindricalvector import CylindricalVector


# Test grids.
n = 25
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rhos = np.linspace(0, 10, n)
phis = np.linspace(0, 2*pi, n)
zs = np.linspace(-10, 10, n)


class TestBuilder(unittest.TestCase):
    """Test code for the cylindricalcoordconverter module."""

    def test___init__(self):
        """Test the __init__ method."""
        ccc = CylindricalCoordConverter()
        self.assertIsInstance(ccc, CylindricalCoordConverter)

    def test_toCoordinate(self):
        """Test the toCoordinate method."""
        ccc = CylindricalCoordConverter()
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = VectorIJK(x, y, z)
                    rho = sqrt(x**2 + y**2)
                    phi = atan2(y, x)
                    if phi < 0:
                        phi += 2*pi
                    cylindrical = ccc.toCoordinate(cartesian)
                    self.assertAlmostEqual(cylindrical.rho, rho)
                    self.assertAlmostEqual(cylindrical.phi, phi)
                    self.assertAlmostEqual(cylindrical.z, z)

    def test_toCartesian(self):
        """Test the toCartesian method."""
        ccc = CylindricalCoordConverter()
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    x = rho*cos(phi)
                    y = rho*sin(phi)
                    cylindrical = CylindricalVector(rho, phi, z)
                    cartesian = ccc.toCartesian(cylindrical)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)


if __name__ == '__main__':
    unittest.main()
