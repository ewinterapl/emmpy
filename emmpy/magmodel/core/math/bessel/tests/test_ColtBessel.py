import unittest

import scipy.special as ss

from emmpy.magmodel.core.math.bessel.coltbessel import ColtBessel


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        with self.assertRaises(Exception):
            ColtBessel()

    def test_i0(self):
        for x in range(-10, 11):
            self.assertAlmostEqual(ColtBessel.i0(x), ss.iv(0, x))

    def test_i0e(self):
        for x in range(-10, 11):
            self.assertAlmostEqual(ColtBessel.i0e(x), ss.ive(0, x))

    def test_i1(self):
        for x in range(-10, 11):
            self.assertAlmostEqual(ColtBessel.i1(x), ss.iv(1, x))

    def test_i1e(self):
        for x in range(-10, 11):
            self.assertAlmostEqual(ColtBessel.i1e(x), ss.ive(1, x))

    def test_j0(self):
        for x in range(-10, 11):
            self.assertAlmostEqual(ColtBessel.j0(x), ss.jv(0, x))

    def test_j1(self):
        for x in range(-10, 11):
            self.assertAlmostEqual(ColtBessel.j1(x), ss.jv(1, x))

    def test_jn(self):
        for n in range(10):
            for x in range(-10, 11):
                self.assertAlmostEqual(ColtBessel.jn(n, x), ss.jv(n, x),
                                       places=6)

    def test_k0(self):
        for x in range(1, 11):
            self.assertAlmostEqual(ColtBessel.k0(x), ss.kv(0, x))

    def test_k0e(self):
        for x in range(1, 11):
            self.assertAlmostEqual(ColtBessel.k0e(x), ss.kve(0, x))

    def test_k1(self):
        for x in range(1, 11):
            self.assertAlmostEqual(ColtBessel.k1(x), ss.kv(1, x))

    def test_k1e(self):
        for x in range(1, 11):
            self.assertAlmostEqual(ColtBessel.k1e(x), ss.kve(1, x))

    def test_kn(self):
        pass
        # for n in range(1, 10):
        #     for x in range(1, 11):
        #         self.assertAlmostEqual(ColtBessel.kn(n, x), ss.kv(n, x))

    def test_y0(self):
        for x in range(1, 11):
            self.assertAlmostEqual(ColtBessel.y0(x), ss.y0(x))

    def test_y1(self):
        for x in range(1, 11):
            self.assertAlmostEqual(ColtBessel.y1(x), ss.y1(x))

    def test_yn(self):
        for n in range(10):
            for x in range(1, 11):
                self.assertAlmostEqual(ColtBessel.yn(n, x), ss.yv(n, x),
                                       delta=0.1)


if __name__ == '__main__':
    unittest.main()
