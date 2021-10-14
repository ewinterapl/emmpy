import unittest

from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)


class TestBuilder(unittest.TestCase):

    def test___init__(self):
        data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        e = ArrayCoefficientExpansion2D(data, 1, 1)
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.assertAlmostEqual(e[row][col], data[row][col])
        self.assertEqual(e.iLowerBoundIndex, 1)
        self.assertEqual(e.jLowerBoundIndex, 1)


if __name__ == "__main__":
    unittest.main()
