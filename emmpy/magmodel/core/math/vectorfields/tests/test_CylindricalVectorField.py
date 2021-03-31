import unittest

from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            CylindricalVectorField()


if __name__ == '__main__':
    unittest.main()
