import unittest

from emmpy.magmodel.core.math.vectorfields.differentiablecylindricalvectorfield import (
    DifferentiableCylindricalVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            DifferentiableCylindricalVectorField()

    def test_differentiate(self):
        with self.assertRaises(Exception):
            DifferentiableCylindricalVectorField.differentiate(None, None)


if __name__ == '__main__':
    unittest.main()
