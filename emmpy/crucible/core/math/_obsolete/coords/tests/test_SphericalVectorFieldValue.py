import unittest

from emmpy.crucible.core.math.coords.sphericalvector import SphericalVector
from emmpy.crucible.core.math.coords.sphericalvectorfieldvalue import (
    SphericalVectorFieldValue
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        position = SphericalVector(1, 2, 3)
        value = SphericalVector(4, 5, 6)
        svfv = SphericalVectorFieldValue(position, value)
        self.assertIsNotNone(svfv)
        self.assertAlmostEqual(svfv.getPosition().getI(), 1)
        self.assertAlmostEqual(svfv.getPosition().getJ(), 2)
        self.assertAlmostEqual(svfv.getPosition().getK(), 3)
        self.assertAlmostEqual(svfv.getValue().getI(), 4)
        self.assertAlmostEqual(svfv.getValue().getJ(), 5)
        self.assertAlmostEqual(svfv.getValue().getK(), 6)


if __name__ == '__main__':
    unittest.main()
