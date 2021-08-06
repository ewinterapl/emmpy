import unittest

from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.coords.cylindricalvectorfieldvalue import (
    CylindricalVectorFieldValue
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        position = CylindricalVector(1, 2, 3)
        value = CylindricalVector(4, 5, 6)
        cvfv = CylindricalVectorFieldValue(position, value)
        self.assertAlmostEqual(cvfv.position.rho, 1)
        self.assertAlmostEqual(cvfv.position.phi, 2)
        self.assertAlmostEqual(cvfv.position.z, 3)
        self.assertAlmostEqual(cvfv.value.rho, 4)
        self.assertAlmostEqual(cvfv.value.phi, 5)
        self.assertAlmostEqual(cvfv.value.z, 6)


if __name__ == '__main__':
    unittest.main()
