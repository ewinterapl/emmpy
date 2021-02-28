import unittest

from emmpy.crucible.core.math.coords.cylindricaltocartesianjacobian import (
    CylindricalToCartesianJacobian
)


class TestCylindricalToCartesianJacobian(unittest.TestCase):

    def test___init__(self):
        CylindricalToCartesianJacobian()


if __name__ == '__main__':
    unittest.main()
