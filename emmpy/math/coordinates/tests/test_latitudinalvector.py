"""Tests for the latitudinalvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np
from emmpy.math.coordinates.cartesianvector import CartesianVector

from emmpy.math.coordinates.latitudinalvector import (
    LatitudinalVector, latitudinalToCartesian, cartesianToLatitudinal
)


# Test grids.
n = 33
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rs = np.linspace(0, 10, n)
lats = np.linspace(-pi/2, pi/2, n)
lons = np.linspace(-pi, pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the latitudinalvector module."""

    def test___new__(self):
        """Test the __new__ method."""
        (r, lat, lon) = (1.1, 2.2, 3.3)
        v = LatitudinalVector(r, lat, lon)
        self.assertIsInstance(v, LatitudinalVector)
        self.assertAlmostEqual(v[0], r)
        self.assertAlmostEqual(v[1], lat)
        self.assertAlmostEqual(v[2], lon)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (r, lat, lon) = (1.1, 2.2, 3.3)
        v = LatitudinalVector(r, lat, lon)
        self.assertAlmostEqual(v.r, r)
        self.assertAlmostEqual(v.lat, lat)
        self.assertAlmostEqual(v.lon, lon)
        with self.assertRaises(KeyError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = LatitudinalVector(0, 0, 0)
        (r, lat, lon) = (1.1, 2.2, 3.3)
        v.r = r
        self.assertAlmostEqual(v.r, r)
        v.lat = lat
        self.assertAlmostEqual(v.lat, lat)
        v.lon = lon
        self.assertAlmostEqual(v.lon, lon)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_latitudinalToCartesian(self):
        """Test the latitudinalToCartesian function."""
        for r in rs:
            for lat in lats:
                for lon in lons:
                    latitudinal = LatitudinalVector(r, lat, lon)
                    x = r*cos(lat)*cos(lon)
                    y = r*cos(lat)*sin(lon)
                    z = r*sin(lat)
                    cartesian = latitudinalToCartesian(latitudinal)
                    self.assertAlmostEqual(cartesian.x, x)
                    self.assertAlmostEqual(cartesian.y, y)
                    self.assertAlmostEqual(cartesian.z, z)

    def test_cartesianToLatitudinal(self):
        """Test the cartesianToLatitudinal function."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = CartesianVector(x, y, z)
                    r = sqrt(x**2 + y**2 + z**2)
                    lat = atan2(z, sqrt(x**2 + y**2))
                    lon = atan2(y, x)
                    latitudinal = cartesianToLatitudinal(cartesian)
                    self.assertAlmostEqual(latitudinal.r, r)
                    self.assertAlmostEqual(latitudinal.lat, lat)
                    self.assertAlmostEqual(latitudinal.lon, lon)


if __name__ == '__main__':
    unittest.main()
