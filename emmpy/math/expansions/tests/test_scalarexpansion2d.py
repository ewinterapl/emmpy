"""Tests for the scalarexpansion2d module."""


import unittest

import numpy as np

from emmpy.math.expansions.scalarexpansion2d import ScalarExpansion2D


# Test data.
data = np.arange(12).reshape(3, 4)
iLowerBoundIndex = 1
iUpperBoundIndex = iLowerBoundIndex + len(data) - 1
jLowerBoundIndex = 1
jUpperBoundIndex = jLowerBoundIndex + len(data[0]) - 1


class TestBuilder(unittest.TestCase):
    """Tests for the scalarexpansion2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        se2d = ScalarExpansion2D.__new__(
            ScalarExpansion2D, data, iLowerBoundIndex, jLowerBoundIndex
        )
        n_rows = iLowerBoundIndex + len(data)
        n_cols = jLowerBoundIndex + len(data[0])
        self.assertEqual(se2d.shape[0], n_rows)
        self.assertEqual(se2d.shape[1], n_cols)

    def test___init__(self):
        """Test the __init__ method."""
        se2d = ScalarExpansion2D(data, iLowerBoundIndex, jLowerBoundIndex)
        for i in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for j in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    se2d[i, j], data[i - iLowerBoundIndex, j - jLowerBoundIndex])
        self.assertEqual(se2d.iLowerBoundIndex, iLowerBoundIndex)
        self.assertEqual(se2d.iUpperBoundIndex, iUpperBoundIndex)
        self.assertEqual(se2d.jLowerBoundIndex, jLowerBoundIndex)
        self.assertEqual(se2d.jUpperBoundIndex, jUpperBoundIndex)


if __name__ == "__main__":
    unittest.main()
