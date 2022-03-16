"""Tests for the magnetopauseoutput module."""


import unittest

from numpy import isin

from emmpy.geomagmodel.magnetopause.magnetopauseoutput import (
    MagnetopauseOutput
)
from emmpy.math.coordinates.vectorijk import VectorIJK


class TestBuilder(unittest.TestCase):
    """Tests for the magnetopauseoutput module."""

    def test___init__(self):
        """Test the __init__ method."""
        (x, y, z) = (1, 2, 3)
        location = VectorIJK(x, y, z)
        d = 10.0
        isInside = False
        mo = MagnetopauseOutput(location, d, isInside)
        self.assertIsInstance(mo, MagnetopauseOutput)
        self.assertAlmostEqual(mo.magnetopauseLocation.i, x)
        self.assertAlmostEqual(mo.magnetopauseLocation.j, y)
        self.assertAlmostEqual(mo.magnetopauseLocation.k, z)
        self.assertAlmostEqual(mo.distanceToMagnetopause, d)
        self.assertEqual(mo.withinMagnetosphere, isInside)


if __name__ == "__main__":
    unittest.main()
