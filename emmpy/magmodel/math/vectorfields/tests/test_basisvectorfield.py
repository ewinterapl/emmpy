import unittest

from emmpy.magmodel.math.vectorfields.basisvectorfield import (
    BasisVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        self.assertIsNotNone(BasisVectorField)
        # with self.assertRaises(Exception):
        #     BasisVectorField()

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
