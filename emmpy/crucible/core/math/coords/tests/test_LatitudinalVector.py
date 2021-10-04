"""Tests for the latitudinalvector module."""


import unittest

from emmpy.crucible.core.math.coords.latitudinalvector import (
    LatitudinalVector, ZERO
)


class TestBuilder(unittest.TestCase):
    """Tests for the latitudinalvector module."""

    def test___init__(self):
        """Test the __init__ method."""
        (r, lat, lon) = (1, 2, 3)
        data = [r, lat, lon]
        lv = LatitudinalVector(r, lat, lon)
        self.assertIsInstance(lv, LatitudinalVector)
        for i in range(3):
            self.assertAlmostEqual(lv[i], data[i])

    def test_getRadius(self):
        """Test the getRadius method."""
        (r, lat, lon) = (1, 2, 3)
        lv = LatitudinalVector(r, lat, lon)
        self.assertAlmostEqual(lv.getRadius(), r)

    def test_getLatitude(self):
        """Test the getLatitude method."""
        (r, lat, lon) = (1, 2, 3)
        lv = LatitudinalVector(r, lat, lon)
        self.assertAlmostEqual(lv.getLatitude(), lat)

    def test_getLongitude(self):
        """Test the getLongitude method."""
        (r, lat, lon) = (1, 2, 3)
        lv = LatitudinalVector(r, lat, lon)
        self.assertAlmostEqual(lv.getLongitude(), lon)

    def test_getI(self):
        """Test the getI method."""
        (i, j, k) = (1, 2, 3)
        lv = LatitudinalVector(i, j, k)
        self.assertAlmostEqual(lv.getI(), i)

    def test_getJ(self):
        """Test the getJ method."""
        (i, j, k) = (1, 2, 3)
        lv = LatitudinalVector(i, j, k)
        self.assertAlmostEqual(lv.getJ(), j)

    def test_getK(self):
        """Test the getK method."""
        (i, j, k) = (1, 2, 3)
        lv = LatitudinalVector(i, j, k)
        self.assertAlmostEqual(lv.getK(), k)

    def test_getVectorIJK(self):
        """Test the getVectorIJK method."""
        (r, lat, lon) = (1, 2, 3)
        data = [r, lat, lon]
        lv = LatitudinalVector(r, lat, lon)
        v = lv.getVectorIJK()
        for i in range(3):
            self.assertAlmostEqual(v[i], data[i])

    def test_ZERO(self):
        """Test the ZERO constant."""
        z = ZERO
        self.assertAlmostEqual(z[0], 0)
        self.assertAlmostEqual(z[1], 0)
        self.assertAlmostEqual(z[2], 0)


if __name__ == '__main__':
    unittest.main()
