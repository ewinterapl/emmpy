import unittest

from emmpy.crucible.core.math.coords.polarcoordconverter import (
    PolarCoordConverter
)
from emmpy.crucible.core.math.coords.polarvector import (
    PolarVector
)
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        pcc = PolarCoordConverter()
        self.assertIsNotNone(pcc)

    def test_toCoordinate(self):
        pcc = PolarCoordConverter()
        cartesian = VectorIJ(1, 2)
        polar = pcc.toCoordinate(cartesian)
        self.assertAlmostEqual(polar.getI(), 2.2360679774998)
        self.assertAlmostEqual(polar.getJ(), 1.1071487177941)

    def test_toCartesian(self):
        pcc = PolarCoordConverter()
        polar = PolarVector(2.2360679774998, 1.1071487177941)
        cartesian = pcc.toCartesian(polar)
        self.assertAlmostEqual(cartesian.getI(), 1)
        self.assertAlmostEqual(cartesian.getJ(), 2)


if __name__ == '__main__':
    unittest.main()
