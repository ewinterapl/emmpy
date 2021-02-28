import unittest

from emmpy.crucible.core.math.coords.sphericaltocartesianjacobian import (
    SphericalToCartesianJacobian
)


class TestSphericalToCartesianJacobian(unittest.TestCase):

    def test___init__(self):
        SphericalToCartesianJacobian()


if __name__ == '__main__':
    unittest.main()
