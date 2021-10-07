"""Tests for the radecvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


import unittest

import numpy as np

from emmpy.math.coordinates.radecvector import RaDecVector


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


if __name__ == '__main__':
    unittest.main()
