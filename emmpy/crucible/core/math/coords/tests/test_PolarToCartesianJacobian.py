import unittest

from emmpy.crucible.core.math.coords.polartocartesianjacobian import (
    PolarToCartesianJacobian
)


class TestPolarToCartesianJacobian(unittest.TestCase):

    def test___init__(self):
        PolarToCartesianJacobian()


if __name__ == '__main__':
    unittest.main()
