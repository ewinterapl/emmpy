"""Test code for the latitudinalcoordconverter module."""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.latitudinalcoordconverter import (
    LatitudinalCoordConverter
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.coordinates.latitudinalvector import LatitudinalVector


# Test grids.
n = 25
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
radiuss = np.linspace(0, 10, n)
lats = np.linspace(-pi/2, pi/2, n)
lons = np.linspace(-pi, pi, n)


class TestBuilder(unittest.TestCase):
    """Test code for the latitudinalcoordconverter module."""

    def test___init__(self):
        """Test the __init__ method."""
        ccc = LatitudinalCoordConverter()
        self.assertIsInstance(ccc, LatitudinalCoordConverter)

    def test_toCoordinate(self):
        """Test the toCoordinate method."""
        lcc = LatitudinalCoordConverter()
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = VectorIJK(x, y, z)
                    radius = sqrt(x**2 + y**2 + z**2)
                    latitude = atan2(z, sqrt(x**2 + y**2))
                    longitude = atan2(y, x)
                    latitudinal = lcc.toCoordinate(cartesian)
                    self.assertAlmostEqual(latitudinal.r, radius)
                    self.assertAlmostEqual(latitudinal.lat, latitude)
                    self.assertAlmostEqual(latitudinal.lon, longitude)

    def test_toCartesian(self):
        """Test the toCartesian method."""
        ccc = LatitudinalCoordConverter()
        for r in radiuss:
            for lat in lats:
                for lon in lons:
                    latitudinal = LatitudinalVector(r, lat, lon)
                    x = r*cos(lat)*cos(lon)
                    y = r*cos(lat)*sin(lon)
                    z = r*sin(lat)
                    cartesian = ccc.toCartesian(latitudinal)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)


if __name__ == '__main__':
    unittest.main()
