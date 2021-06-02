import unittest

from emmpy.magmodel.core.math.vectorfields.cylindricalbasisvectorfield import (
    CylindricalBasisVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(CylindricalBasisVectorField)

    def test_evaluateExpansion(self):
        pass


if __name__ == '__main__':
    unittest.main()
