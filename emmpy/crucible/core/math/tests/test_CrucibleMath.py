import unittest

import emmpy.crucible.core.math.cruciblemath as cruciblemath


class TestCrucibleMath(unittest.TestCase):

    def test_cbrt(self):
        self.assertAlmostEqual(cruciblemath.cbrt(8), 2)

    def test_IEEEremainder(self):
        with self.assertRaises(Exception):
            cruciblemath.IEEEremainder(0, 0)

    def test_ulp(self):
        with self.assertRaises(Exception):
            cruciblemath.ulp(0)

    def test_signum(self):
        self.assertAlmostEqual(cruciblemath.signum(-2.2), -1.0)
        self.assertAlmostEqual(cruciblemath.signum(-0.0), 0)
        self.assertAlmostEqual(cruciblemath.signum(3.3), 1.0)

    def test_rint(self):
        self.assertAlmostEqual(cruciblemath.rint(-0.6), -1)
        self.assertAlmostEqual(cruciblemath.rint(-0.5), 0)
        self.assertAlmostEqual(cruciblemath.rint(-0.4), 0)
        self.assertAlmostEqual(cruciblemath.rint(0), 0)
        self.assertAlmostEqual(cruciblemath.rint(0.4), 0)
        self.assertAlmostEqual(cruciblemath.rint(0.5), 0)
        self.assertAlmostEqual(cruciblemath.rint(0.6), 1)


if __name__ == '__main__':
    unittest.main()
