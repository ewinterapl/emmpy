import unittest

from emmpy.crucible.core.math.cruciblemath import CrucibleMath

class TestCrucibleMath(unittest.TestCase):

    def test_sin(self):
        self.assertAlmostEqual(CrucibleMath.sin(0), 0)

    def test_cos(self):
        self.assertAlmostEqual(CrucibleMath.cos(CrucibleMath.PI), -1)

    def test_tan(self):
        self.assertAlmostEqual(CrucibleMath.tan(CrucibleMath.PI), 0)

    def test_asin(self):
        self.assertAlmostEqual(CrucibleMath.asin(0), 0)

    def test_acos(self):
        self.assertAlmostEqual(CrucibleMath.acos(1), 0)

    def test_atan(self):
        self.assertAlmostEqual(CrucibleMath.atan(0), 0)

    def test_toRadians(self):
        self.assertAlmostEqual(CrucibleMath.toRadians(0), 0)

    def test_toDegrees(self):
        self.assertAlmostEqual(CrucibleMath.toDegrees(0), 0)

    def test_exp(self):
        self.assertAlmostEqual(CrucibleMath.exp(0), 1)

    def test_log(self):
        self.assertAlmostEqual(CrucibleMath.log(1), 0)

    def test_log10(self):
        self.assertAlmostEqual(CrucibleMath.log10(1), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(CrucibleMath.sqrt(4), 2)

    def test_cbrt(self):
        self.assertAlmostEqual(CrucibleMath.cbrt(8), 2)

    def test_IEEEremainder(self):
        pass

    def test_ceil(self):
        self.assertAlmostEqual(CrucibleMath.ceil(1.5), 2)

    def test_floor(self):
        self.assertAlmostEqual(CrucibleMath.floor(1.5), 1)

    def test_atan2(self):
        self.assertAlmostEqual(CrucibleMath.atan2(0, 1), 0)

    def test_pow(self):
        self.assertAlmostEqual(CrucibleMath.pow(2, 2), 4)

    def test_round(self):
        self.assertEqual(CrucibleMath.round(0.6), 1)

    def test_abs(self):
        self.assertAlmostEqual(CrucibleMath.abs(-2), 2)

    def test_max(self):
        self.assertEqual(CrucibleMath.max(1, 2), 2)

    def test_min(self):
        self.assertEqual(CrucibleMath.min(1, 2), 1)

    def test_ulp(self):
        pass

    def test_signum(self):
        self.assertAlmostEqual(CrucibleMath.signum(1), 1)

    def test_sinh(self):
        self.assertAlmostEqual(CrucibleMath.sinh(0), 0)

    def test_cosh(self):
        self.assertAlmostEqual(CrucibleMath.cosh(0), 1)

    def test_tanh(self):
        self.assertAlmostEqual(CrucibleMath.tanh(0), 0)

    def test_acosh(self):
        self.assertAlmostEqual(CrucibleMath.acosh(1), 0)

    def test_asinh(self):
        self.assertAlmostEqual(CrucibleMath.asinh(0), 0)

    def test_atanh(self):
        self.assertAlmostEqual(CrucibleMath.atanh(0), 0)

    def test_hypot(self):
        self.assertAlmostEqual(CrucibleMath.hypot(3, 4), 5)

    def test_rint(self):
        self.assertAlmostEqual(CrucibleMath.rint(0.5), 0)

if __name__ == '__main__':
    unittest.main()
