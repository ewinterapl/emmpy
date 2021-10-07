"""Tests for the latitudinalvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.math.coordinates.latitudinalvector import LatitudinalVector


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


if __name__ == '__main__':
    unittest.main()
