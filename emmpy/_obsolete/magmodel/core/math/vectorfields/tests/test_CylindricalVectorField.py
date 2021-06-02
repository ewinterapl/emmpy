import unittest

from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            CylindricalVectorField()

    def test_asCylindrical(self):
        pass

    def test_evaluate(self):
        pass


if __name__ == '__main__':
    unittest.main()
