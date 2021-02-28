import unittest

from emmpy.crucible.core.math.coords.cylindricaltocartesianbasistransformation import (
    CylindricalToCartesianBasisTransformation
)


class TestCylindricalToCartesianBasisTransformation(unittest.TestCase):

    def test___init__(self):
        CylindricalToCartesianBasisTransformation()


if __name__ == '__main__':
    unittest.main()
