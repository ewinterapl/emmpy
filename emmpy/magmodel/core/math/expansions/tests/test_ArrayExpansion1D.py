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


if __name__ == '__main__':
    unittest.main()
