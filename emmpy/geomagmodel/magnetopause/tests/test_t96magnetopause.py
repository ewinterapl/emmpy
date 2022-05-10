"""Tests for the t96magnetopause module."""


import unittest
from emmpy.geomagmodel.magnetopause.magnetopauseoutput import MagnetopauseOutput

from emmpy.geomagmodel.magnetopause.t96magnetopause import (
    T96Magnetopause
)
from emmpy.math.coordinates.vectorijk import VectorIJK


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

    def test_evaluate(self):
        """Test the evaluate method."""
        t96mp = T96Magnetopause.createTS07(1)
        location = VectorIJK(1, 2, 3)
        mo = t96mp.evaluate(location)
        self.assertIsInstance(mo, MagnetopauseOutput)
        self.assertAlmostEqual(mo.distanceToMagnetopause, 9.330655552712768)
        self.assertAlmostEqual(mo.magnetopauseLocation.i, 6.996781730613225)
        self.assertAlmostEqual(mo.magnetopauseLocation.j, 5.965223513682737)
        self.assertAlmostEqual(mo.magnetopauseLocation.k, 8.947835270524108)
        self.assertTrue(mo.withinMagnetosphere)

    def test_apply(self):
        """Test the apply method."""
        t96mp = T96Magnetopause.createTS07(1)
        location = VectorIJK(1, 2, 3)
        self.assertTrue(t96mp.apply(location))

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

    def test_createBentTS07(self):
        """Test the createBentTS07 method."""
        # t96mp = T96Magnetopause.createBentTS07(2, 23, 10, 0.5, 0.5)
        # self.assertIsInstance(t96mp, T96Magnetopause)
        # self.assertAlmostEqual(t96mp.scaledA0, 34.586)
        # self.assertAlmostEqual(t96mp.sigma0, 1.196)
        # self.assertAlmostEqual(t96mp.scaledX0, 3.4397)
        # self.assertAlmostEqual(t96mp.XM, -31.146299999999997)
        # self.assertAlmostEqual(t96mp.semiMinorAxis, 22.690524804436233)
        # location = VectorIJK(1, 2, 3)
        # result = t96mp.apply(location)
        # self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
