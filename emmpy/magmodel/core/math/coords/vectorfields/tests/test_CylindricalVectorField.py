import unittest

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.magmodel.core.math.coords.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        cvf = CylindricalVectorField()
        self.assertIsNotNone(cvf)

    def test_asCylindrical(self):
        cvf = CylindricalVectorField()
        cvf2 = CylindricalVectorField.asCylindrical(cvf)
        self.assertIs(cvf2, cvf)
        # cartesian = VectorField()
        # cvfw = CylindricalVectorField.asCylindrical(cartesian)
        # NEED PROPER TEST CODE HERE

    def test_evaluate(self):
        pass
        # NEED PROPER TEST CODE HERE


if __name__ == '__main__':
    unittest.main()
