import unittest

from emmpy.crucible.core.math.coords.sphericaltocartesianbasistransformation import (
    SphericalToCartesianBasisTransformation
)


class TestSphericalToCartesianBasisTransformation(unittest.TestCase):

    def test___init__(self):
        SphericalToCartesianBasisTransformation()


if __name__ == '__main__':
    unittest.main()
