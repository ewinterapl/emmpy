"""Tests for the polarvector package."""


import unittest

import numpy as np

from emmpy.crucible.core.math.coords.polarvector import (
    PolarVector,
    ZERO
)


class TestBuilder(unittest.TestCase):
    """Tests for the PolarVector class."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        pv = PolarVector()
        self.assertIsInstance(pv, PolarVector)
        for i in range(2):
            self.assertTrue(np.isnan(pv[i]))
        # 2-argument form.
        (radius, angle) = (1.1, 2.2)
        pv = PolarVector(radius, angle)
        self.assertIsInstance(pv, PolarVector)
        self.assertAlmostEqual(pv[0], radius)
        self.assertAlmostEqual(pv[1], angle)

    def test_getRadius(self):
        """Test the getRadius method."""
        (radius, angle) = (1.1, 2.2)
        pv = PolarVector(radius, angle)
        self.assertAlmostEqual(pv.getRadius(), radius)

    def test_getAngle(self):
        """Test the getAngle method."""
        (radius, angle) = (1.1, 2.2)
        pv = PolarVector(radius, angle)
        self.assertAlmostEqual(pv.getAngle(), angle)

    def test_getVectorIJ(self):
        """Test the getVectorIJ method."""
        (radius, angle) = (1.1, 2.2)
        pv = PolarVector(radius, angle)
        vij = pv.getVectorIJ()
        # self.assertIsInstance(vij, VectorIJ)
        self.assertAlmostEqual(vij.getI(), radius)
        self.assertAlmostEqual(vij.getJ(), angle)

    def test_getI(self):
        """Test the getI method."""
        (radius, angle) = (1.1, 2.2)
        pv = PolarVector(radius, angle)
        self.assertAlmostEqual(pv.getI(), radius)

    def test_getJ(self):
        """Test the getJ method."""
        (radius, angle) = (1.1, 2.2)
        pv = PolarVector(radius, angle)
        self.assertAlmostEqual(pv.getJ(), angle)

    def test_ZERO(self):
        """Test the ZERO constant."""
        self.assertAlmostEqual(ZERO.getRadius(), 0)
        self.assertAlmostEqual(ZERO.getAngle(), 0)


if __name__ == '__main__':
    unittest.main()
