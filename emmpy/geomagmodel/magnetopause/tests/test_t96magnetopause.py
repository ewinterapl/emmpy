"""Tests for the t96magnetopause module."""


import unittest

from emmpy.geomagmodel.magnetopause.t96magnetopause import (
    T96Magnetopause
)


class TestBuilder(unittest.TestCase):
    """Tests for the t96magnetopause module."""

    def test___init__(self):
        """Test the __init__ method."""
        t96mp = T96Magnetopause(1, 1, 1, 1, 1)
        self.assertIsInstance(t96mp, T96Magnetopause)
        self.assertAlmostEqual(t96mp.scaledA0, 2.0)
        self.assertAlmostEqual(t96mp.sigma0, 1.0)
        self.assertAlmostEqual(t96mp.scaledX0, 2.0)
        self.assertAlmostEqual(t96mp.XM, 0.0)
        self.assertAlmostEqual(t96mp.semiMinorAxis, 0.0)

    def test_createGeopack(self):
        """Test the createGeopack method."""
        t96mp = T96Magnetopause.createGeopack(1)
        self.assertIsInstance(t96mp, T96Magnetopause)
        self.assertAlmostEqual(t96mp.scaledA0, 77.13335811136275)
        self.assertAlmostEqual(t96mp.sigma0, 1.08)
        self.assertAlmostEqual(t96mp.scaledX0, 6.038440035003827)
        self.assertAlmostEqual(t96mp.XM, -71.09491807635892)
        self.assertAlmostEqual(t96mp.semiMinorAxis, 31.464359852702326)

    def test_createTS07(self):
        """Test the createTS07 method."""
        t96mp = T96Magnetopause.createTS07(1)
        self.assertIsInstance(t96mp, T96Magnetopause)
        self.assertAlmostEqual(t96mp.scaledA0, 38.50880008805735)
        self.assertAlmostEqual(t96mp.sigma0, 1.196)
        self.assertAlmostEqual(t96mp.scaledX0, 3.8298363402212128)
        self.assertAlmostEqual(t96mp.XM, -34.678963747836136)
        self.assertAlmostEqual(t96mp.semiMinorAxis, 25.26412084621354)


if __name__ == "__main__":
    unittest.main()
