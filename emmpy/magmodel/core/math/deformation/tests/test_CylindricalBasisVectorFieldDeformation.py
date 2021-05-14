from emmpy.magmodel.core.math.vectorfields.cylindricalbasisvectorfield import CylindricalBasisVectorField
import unittest

from emmpy.magmodel.core.math.deformation.cylindricalbasisfielddeformation import (
    CylindricalBasisFieldDeformation
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(CylindricalBasisFieldDeformation(None, None))


if __name__ == '__main__':
    unittest.main()
