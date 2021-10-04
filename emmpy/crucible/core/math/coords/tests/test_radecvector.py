"""Tests for the radecvector module."""


import unittest

from emmpy.crucible.core.math.coords.radecvector import RaDecVector


class TestBuilder(unittest.TestCase):
    """Tests for the radecvector module."""

    def test___init__(self):
        """Test the __init__ method."""
        (r, ra, dec) = (1, 3, 1.5)
        data = [r, ra, dec]
        rdv = RaDecVector(r, ra, dec)
        self.assertIsInstance(rdv, RaDecVector)
        for i in range(3):
            self.assertAlmostEqual(rdv[i], data[i])

    def test_getRadius(self):
        """Test the getRadius method."""
        (r, ra, dec) = (1, 3, 1.5)
        rdv = RaDecVector(r, ra, dec)
        self.assertAlmostEqual(rdv.getRadius(), r)

    def test_getRightAscension(self):
        """Test the getRightAscension method."""
        (r, ra, dec) = (1, 3, 1.5)
        rdv = RaDecVector(r, ra, dec)
        self.assertAlmostEqual(rdv.getRightAscension(), ra)

    def test_getDeclination(self):
        """Test the getDeclination method."""
        (r, ra, dec) = (1, 3, 1.5)
        rdv = RaDecVector(r, ra, dec)
        self.assertAlmostEqual(rdv.getDeclination(), dec)

    def test_getI(self):
        """Test the getI method."""
        (r, ra, dec) = (1, 3, 1.5)
        rdv = RaDecVector(r, ra, dec)
        self.assertAlmostEqual(rdv.getI(), r)

    def test_getJ(self):
        """Test the getJ method."""
        (r, ra, dec) = (1, 3, 1.5)
        rdv = RaDecVector(r, ra, dec)
        self.assertAlmostEqual(rdv.getJ(), ra)

    def test_getK(self):
        """Test the getK method."""
        (r, ra, dec) = (1, 3, 1.5)
        rdv = RaDecVector(r, ra, dec)
        self.assertAlmostEqual(rdv.getK(), dec)

    def test_getVectorIJK(self):
        """Test the getVectorIJK method."""
        (r, ra, dec) = (1, 3, 1.5)
        data = [r, ra, dec]
        rdv = RaDecVector(r, ra, dec)
        for i in range(3):
            self.assertAlmostEqual(rdv[i], data[i])


if __name__ == '__main__':
    unittest.main()
