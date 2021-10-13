import unittest

from emmpy.magmodel.core.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        e = ArrayCoefficientExpansion2D(
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 1, 1
        )
        self.assertAlmostEqual(e.data, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(e.iLowerBoundIndex, 1)
        self.assertEqual(e.jLowerBoundIndex, 1)


if __name__ == "__main__":
    unittest.main()
