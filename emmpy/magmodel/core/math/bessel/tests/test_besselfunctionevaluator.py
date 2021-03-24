import unittest

from emmpy.magmodel.core.math.bessel.besselfunctionevaluator import (
    BesselFunctionEvaluator
)


class TestAlbertBesselFunctionEvaluator(unittest.TestCase):

    def test_besselj0(self):
        with self.assertRaises(Exception):
            BesselFunctionEvaluator().besselj0(0)

    def test_besselj1(self):
        with self.assertRaises(Exception):
            BesselFunctionEvaluator().besselj1(0)

    def test_besseljn(self):
        with self.assertRaises(Exception):
            BesselFunctionEvaluator().besseljn(0, 0)

    def test_besselj0jn(self):
        with self.assertRaises(Exception):
            BesselFunctionEvaluator().besselj0jn(0, 0)


if __name__ == '__main__':
    unittest.main()
