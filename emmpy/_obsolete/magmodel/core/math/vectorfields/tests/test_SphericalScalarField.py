import unittest

from emmpy.magmodel.core.math.vectorfields.sphericalscalarfield import (
    SphericalScalarField
)


class TestBuilder(unittest.TestCase):

    def test_evaluate(self):
        pass

    def test_evaluateScalar(self):
        with self.assertRaises(Exception):
            SphericalScalarField.evaluateScalar(None, None)


if __name__ == '__main__':
    unittest.main()
