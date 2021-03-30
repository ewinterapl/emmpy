import unittest

from emmpy.magmodel.core.math.deformation.basisvectorfielddeformation import (
    BasisVectorFieldDeformation
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            BasisVectorFieldDeformation()

    def test_evaluate(self):
        # IMPLEMENT
        pass

    def test_evaluateExpansion(self):
        # IMPLEMENT
        pass

    def test_getNumberOfBasisFunctions(self):
        # IMPLEMENT
        pass


if __name__ == '__main__':
    unittest.main()
