"""Tests for the radecvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.radecvector import (
    RaDecVector, raDecToCartesian, cartesianToRaDec
)


# Test grids.
n = 33
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rs = np.linspace(0, 10, n)
ras = np.linspace(0, 2*pi, n)
decs = np.linspace(-pi/2, pi/2, n)


class TestBuilder(unittest.TestCase):
    """Tests for the radecvector module."""

    def test___new__(self):
        """Test the __new__ method."""
        (r, ra, dec) = (1.1, 2.2, 3.3)
        v = RaDecVector(r, ra, dec)
        self.assertIsInstance(v, RaDecVector)
        self.assertAlmostEqual(v[0], r)
        self.assertAlmostEqual(v[1], ra)
        self.assertAlmostEqual(v[2], dec)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (r, ra, dec) = (1.1, 2.2, 3.3)
        v = RaDecVector(r, ra, dec)
        self.assertAlmostEqual(v.r, r)
        self.assertAlmostEqual(v.ra, ra)
        self.assertAlmostEqual(v.dec, dec)
        with self.assertRaises(KeyError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = RaDecVector(0, 0, 0)
        (r, ra, dec) = (1.1, 2.2, 3.3)
        v.r = r
        self.assertAlmostEqual(v.r, r)
        v.ra = ra
        self.assertAlmostEqual(v.ra, ra)
        v.dec = dec
        self.assertAlmostEqual(v.dec, dec)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_raDecToCartesian(self):
        """Test the raDecToCartesian function."""
        for r in rs:
            for ra in ras:
                for dec in decs:
                    celestial = RaDecVector(r, ra, dec)
                    x = r*cos(dec)*cos(ra)
                    y = r*cos(dec)*sin(ra)
                    z = r*sin(dec)
                    cartesian = raDecToCartesian(celestial)
                    self.assertAlmostEqual(cartesian.x, x)
                    self.assertAlmostEqual(cartesian.y, y)
                    self.assertAlmostEqual(cartesian.z, z)

    def test_cartesianToRaDec(self):
        """Test the cartesianToRaDec function."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = CartesianVector(x, y, z)
                    r = sqrt(x**2 + y**2 + z**2)
                    ra = atan2(y, x)
                    if ra < 0.0:
                        ra += 2*pi
                    dec = atan2(z, sqrt(x**2 + y**2))
                    celestial = cartesianToRaDec(cartesian)
                    self.assertAlmostEqual(celestial.r, r)
                    self.assertAlmostEqual(celestial.ra, ra)
                    self.assertAlmostEqual(celestial.dec, dec)


if __name__ == '__main__':
    unittest.main()
