import unittest

from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        c = ArrayCoefficientExpansion1D([0], 0)

    def test_getLowerBoundIndex(self):
        c = ArrayCoefficientExpansion1D([0], 0)
        self.assertEqual(c.getLowerBoundIndex(), 0)

    def test_getUpperBoundIndex(self):
        c = ArrayCoefficientExpansion1D([0, 1, 2, 3], 1)
        self.assertEqual(c.getUpperBoundIndex(), 4)

    def test_getCoefficient(self):
        c = ArrayCoefficientExpansion1D([0.0, 1.1, 2.2, 3.3], 1)
        self.assertAlmostEqual(c.getCoefficient(2), 1.1)

    def test_toString(self):
        c = ArrayCoefficientExpansion1D([0.0, 1.1, 2.2, 3.3], 1)
        self.assertEqual(
            c.toString(),
            "ArrayCoefficientExpansion1D [array=[0.0, 1.1, 2.2, 3.3], "
            "getLowerBoundIndex()=1, getUpperBoundIndex()=4]")

    def test_hashCode(self):
        c = ArrayCoefficientExpansion1D([0.0, 1.1, 2.2, 3.3], 1)
        self.assertEqual(c.hashCode(), 962)

    def test_equals(self):
        c1 = ArrayCoefficientExpansion1D([0.0, 1.1, 2.2, 3.3], 1)
        c2 = ArrayCoefficientExpansion1D([0.0, 1.1, 2.2, 3.3], 1)
        self.assertTrue(c1.equals(c2))
        c3 = ArrayCoefficientExpansion1D([0.0, 1.1, 2.2, 4.4], 1)
        self.assertFalse(c1.equals(c3))


if __name__ == '__main__':
    unittest.main()
