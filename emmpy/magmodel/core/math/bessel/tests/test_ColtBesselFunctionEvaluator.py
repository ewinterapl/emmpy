import unittest

import scipy.special as ss

from emmpy.magmodel.core.math.bessel.coltbesselfunctionevaluator import (
    ColtBesselFunctionEvaluator
)


class TestTestColtBesselFunctionEvaluatorr(unittest.TestCase):

    def test_besselj0(self):
        for x in range(-10, 11):
            self.assertAlmostEqual(ColtBesselFunctionEvaluator.besselj0(x),
                                   ss.jv(0, x))

    def test_besselj1(self):
        for x in range(-10, 11):
            self.assertAlmostEqual(ColtBesselFunctionEvaluator.besselj1(x),
                                   ss.jv(1, x))

    def test_besseljn(self):
        for n in range(10):
            for x in range(-10, 11):
                self.assertAlmostEqual(
                    ColtBesselFunctionEvaluator.besseljn(n, x),
                    ss.jv(n, x), places=6)

    def test_besselj0jn(self):
        n = 5
        orders = list(range(n + 1))
        for x in range(-10, 11):
            xx = ColtBesselFunctionEvaluator.besselj0jn(n, x)
            yy = ss.jv(orders, x)
            for i in range(n + 1):
                self.assertAlmostEqual(xx[i], yy[i], places=6)


if __name__ == '__main__':
    unittest.main()
