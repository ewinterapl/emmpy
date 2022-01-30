import unittest

from emmpy.magmodel.core.math.expansions.arrayexpansion2d import (
    ArrayExpansion2D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        e = ArrayExpansion2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1)
        self.assertAlmostEqual(e.data, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(e.firstAzimuthalExpansionNumber, 1)
        self.assertEqual(e.lastAzimuthalExpansionNumber, 3)
        self.assertEqual(e.firstRadialExpansionNumber, 1)
        self.assertEqual(e.lastRadialExpansionNumber, 3)

    def test_getJUpperBoundIndex(self):
        e = ArrayExpansion2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1)
        self.assertEqual(e.getJUpperBoundIndex(), 3)

    def test_getExpansion(self):
        e = ArrayExpansion2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1)
        self.assertAlmostEqual(e.getExpansion(1, 2), 1)


if __name__ == '__main__':
    unittest.main()
