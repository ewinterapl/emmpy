import unittest

from emmpy.magmodel.core.math.coords.vectorfields.basisvectorfield import (
    BasisVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            BasisVectorField()

    def test_evaluate(self):
        with self.assertRaises(Exception):
            BasisVectorField.evaluate(None, None, None)

    def test_evaluateExpansion(self):
        with self.assertRaises(Exception):
            BasisVectorField.evaluateExpansion(None, None)

    def test_getNumberOfBasisFunctions(self):
        with self.assertRaises(Exception):
            BasisVectorField.getNumberOfBasisFunctions(None)


if __name__ == '__main__':
    unittest.main()