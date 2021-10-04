"""Test code for the radeccoordconverter module."""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.radeccoordconverter import (
    RaDecCoordConverter
)
from emmpy.crucible.core.math.coords.radecvector import (
    RaDecVector
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


# Test grids.
n = 25
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rs = np.linspace(0, 10, n)
ras = np.linspace(0, 2*pi, n)
decs = np.linspace(-pi/2, pi/2, n)


class TestBuilder(unittest.TestCase):
    """Test code for the radeccoordconverter module."""

    def test___init__(self):
        """Test the __init__ method."""
        rdcc = RaDecCoordConverter()
        self.assertIsInstance(rdcc, RaDecCoordConverter)

    def test_toCoordinate(self):
        """Test the toCoordinate method."""
        rdcc = RaDecCoordConverter()
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = VectorIJK(x, y, z)
                    r = sqrt(x**2 + y**2 + z**2)
                    ra = atan2(y, x)
                    if ra < 0:
                        ra += 2*pi
                    dec = atan2(z, sqrt(x**2 + y**2))
                    celestial = rdcc.toCoordinate(cartesian)
                    self.assertAlmostEqual(celestial.getRadius(), r)
                    self.assertAlmostEqual(celestial.getRightAscension(), ra)
                    self.assertAlmostEqual(celestial.getDeclination(), dec)

    def test_toCartesian(self):
        """Test the toCartesian method."""
        rdcc = RaDecCoordConverter()
        for r in rs:
            for ra in ras:
                for dec in decs:
                    celestial = RaDecVector(r, ra, dec)
                    x = r*cos(dec)*cos(ra)
                    y = r*cos(dec)*sin(ra)
                    z = r*sin(dec)
                    cartesian = rdcc.toCartesian(celestial)
                    self.assertAlmostEqual(cartesian.i, x)
                    self.assertAlmostEqual(cartesian.j, y)
                    self.assertAlmostEqual(cartesian.k, z)


if __name__ == '__main__':
    unittest.main()
