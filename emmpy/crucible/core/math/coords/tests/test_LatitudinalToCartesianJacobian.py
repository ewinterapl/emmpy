import unittest

from emmpy.crucible.core.math.coords.latitudinaltocartesianjacobian import (
    LatitudinalToCartesianJacobian
)


class TestLatitudinalToCartesianJacobian(unittest.TestCase):

    def test___init__(self):
        LatitudinalToCartesianJacobian()


if __name__ == '__main__':
    unittest.main()
