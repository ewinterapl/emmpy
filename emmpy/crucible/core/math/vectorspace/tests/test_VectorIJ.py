from math import sqrt
import unittest

import numpy as np

from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class TestBuilder(unittest.TestCase):

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v1 = VectorIJ()
        self.assertIsInstance(v1, VectorIJ)
        for i in range(2):
            self.assertTrue(np.isnan(v1[i]))
        # 1-argument forms
        (i, j) = (1.1, 2.2)
        # list
        v1 = VectorIJ([i, j])
        self.assertIsInstance(v1, VectorIJ)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        # tuple
        v1 = VectorIJ((i, j))
        self.assertIsInstance(v1, VectorIJ)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        # vector
        v2 = VectorIJ(v1)
        self.assertIsInstance(v2, VectorIJ)
        self.assertAlmostEqual(v2[0], v1[0])
        self.assertAlmostEqual(v2[1], v1[1])
        # invalid single argument
        with self.assertRaises(ValueError):
            v2 = VectorIJ(None)
        with self.assertRaises(ValueError):
            v2 = VectorIJ({'i': i, 'j': j})
        # 2-argument forms
        # offset and list
        v1 = VectorIJ(1, [0, i, j])
        self.assertIsInstance(v1, VectorIJ)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        # offset and tuple
        v1 = VectorIJ(1, (0, i, j))
        self.assertIsInstance(v1, VectorIJ)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        # scale and vector
        scale = -2.2
        v2 = VectorIJ(scale, v1)
        self.assertIsInstance(v2, VectorIJ)
        self.assertAlmostEqual(v2[0], scale*v1[0])
        self.assertAlmostEqual(v2[1], scale*v1[1])
        # 2 bad args
        with self.assertRaises(ValueError):
            v1 = VectorIJ(i, j, 0)
        # set components
        v1 = VectorIJ(i, j)
        self.assertIsInstance(v1, VectorIJ)
        self.assertAlmostEqual(v1[0], i)
        self.assertAlmostEqual(v1[1], j)
        # >= 3 args is invalid
        with self.assertRaises(ValueError):
            v1 = VectorIJ(0, i, j)


if __name__ == '__main__':
    unittest.main()
