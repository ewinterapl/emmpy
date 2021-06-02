import math
import unittest

from emmpy.java.lang.illegalargumentexception import IllegalArgumentException
from emmpy.magmodel.core.math.bessel.arithmetic import Arithmetic


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            Arithmetic()

    def test_binomial(self):
        self.assertEqual(Arithmetic.binomial(4.0, 2), 6)
        self.assertEqual(Arithmetic.binomial(4, 2), 6)

    def test_ceil(self):
        self.assertEqual(Arithmetic.ceil(0), 0)
        self.assertEqual(Arithmetic.ceil(1.2), 2)
        self.assertEqual(Arithmetic.ceil(-1.2), -1)

    def test_chbevl(self):
        x = 0.5
        coef = [0.2, 0.4, 0.6, 0.8]
        N = len(coef)
        self.assertAlmostEqual(Arithmetic.chbevl(x, coef, N), 0.0625)

    def test_fac1(self):
        self.assertEqual(Arithmetic.fac1(0), 1)
        self.assertEqual(Arithmetic.fac1(20), 2432902008176640000)
        self.assertEqual(Arithmetic.fac1(-20), -2432902008176640000)
        with self.assertRaises(IllegalArgumentException):
            Arithmetic.fac1(22)

    def test_fac2(self):
        self.assertAlmostEqual(Arithmetic.fac2(0), 1)
        self.assertAlmostEqual(Arithmetic.fac2(20), 2432902008176640000)
        self.assertAlmostEqual(Arithmetic.fac2(-20), -2432902008176640000)

    def test_factorial(self):
        with self.assertRaises(IllegalArgumentException):
            Arithmetic.factorial(-1)
        self.assertAlmostEqual(Arithmetic.factorial(0), 1)
        self.assertAlmostEqual(Arithmetic.factorial(20), 2432902008176640000)
        self.assertAlmostEqual(Arithmetic.factorial(21), 5.109094217170944E19)
        self.assertAlmostEqual(Arithmetic.factorial(170),
                               7.257415615308004E306)
        self.assertAlmostEqual(Arithmetic.factorial(171), math.inf)

    def test_floor(self):
        self.assertEqual(Arithmetic.floor(1.1), 1)
        self.assertEqual(Arithmetic.floor(-1.1), -2)

    def test_log(self):
        self.assertAlmostEqual(Arithmetic.log(10, 1), 0)
        self.assertAlmostEqual(Arithmetic.log(2, 8), 3)

    def test_log10(self):
        self.assertAlmostEqual(Arithmetic.log10(1), 0)
        self.assertAlmostEqual(Arithmetic.log10(1000), 3)

    def test_log2(self):
        self.assertAlmostEqual(Arithmetic.log2(1), 0)
        self.assertAlmostEqual(Arithmetic.log2(8), 3)

    def test_logFactorial(self):
        nf = 10*9*8*7*6*5*4*3*2*1
        lnf = math.log(nf)
        self.assertAlmostEqual(Arithmetic.logFactorial(10), lnf)

    def test_longFactorial(self):
        n = 10
        nf = 10*9*8*7*6*5*4*3*2*1
        self.assertEqual(Arithmetic.longFactorial(n), nf)

    def test_stirlingCorrection(self):
        self.assertAlmostEqual(Arithmetic.stirlingCorrection(10),
                               8.330563433362871e-03)

    def test_xlongBinomial(self):
        self.assertEqual(Arithmetic.xlongBinomial(4, 2), 6)


if __name__ == '__main__':
    unittest.main()
