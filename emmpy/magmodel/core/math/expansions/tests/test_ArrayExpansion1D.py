import unittest

from emmpy.magmodel.core.math.expansions.arrayexpansion1d import (
    ArrayExpansion1D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        e = ArrayExpansion1D([0, 1, 2], 1)
        self.assertAlmostEqual(e.array, [0, 1, 2])
        self.assertEqual(e.firstRadialExpansionNumber, 1)
        self.assertEqual(e.lastRadialExpansionNumber, 3)

    def test_getLowerBoundIndex(self):
        e = ArrayExpansion1D([0, 1, 2], 1)
        self.assertEqual(e.getLowerBoundIndex(), 1)

    def test_getUpperBoundIndex(self):
        e = ArrayExpansion1D([0, 1, 2], 1)
        self.assertEqual(e.getUpperBoundIndex(), 3)

    def test_getExpansion(self):
        e = ArrayExpansion1D([0, 1, 2], 1)
        self.assertEqual(e.getExpansion(1), 0)

    def test_toString(self):
        e = ArrayExpansion1D([0, 1, 2], 1)
        self.assertEqual(
            e.toString(),
            "ArraySymmetricScalarCylindricalExpansion [array=[0, 1, 2]"
            ", firstRadialExpansionNumber=1, lastRadialExpansionNumber=3]")

    def test_hashCode(self):
        e = ArrayExpansion1D([0, 1, 2], 1)
        self.assertEqual(e.hashCode(), 29825)

    def test_equals(self):
        e1 = ArrayExpansion1D([0, 1, 2], 1)
        e2 = ArrayExpansion1D([0, 1, 2], 1)
        self.assertTrue(e1.equals(e2))
        e3 = ArrayExpansion1D([0, 1, 2], 0)
        self.assertFalse(e1.equals(e3))


if __name__ == '__main__':
    unittest.main()
