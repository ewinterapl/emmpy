import unittest

from emmpy.magmodel.core.math.vectorfields.differentiablesphericalvectorfield import (
    DifferentiableSphericalVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            DifferentiableSphericalVectorField()

    def test_differentiate(self):
        with self.assertRaises(Exception):
            DifferentiableSphericalVectorField.differentiate(None, None)


if __name__ == '__main__':
    unittest.main()
