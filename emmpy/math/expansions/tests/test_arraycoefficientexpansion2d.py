"""Tests for the arraycoefficientexpansion2d module.

NOTE: These tests are for the unpadded, np.ndarray-based version of the
module.
"""


import unittest

import numpy as np

from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D
)


# Test data.
n_rows = 3
n_cols = 4
data = np.arange(n_rows*n_cols).reshape(n_rows, n_cols)
iLowerBoundIndex = 1
iUpperBoundIndex = iLowerBoundIndex + n_rows - 1
jLowerBoundIndex = 2
jUpperBoundIndex = jLowerBoundIndex + n_cols - 1


class TestBuilder(unittest.TestCase):
    """Tests for the arraycoefficientexpansion2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        ace2d = ArrayCoefficientExpansion2D.__new__(
            ArrayCoefficientExpansion2D,
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        self.assertEqual(ace2d.shape[0], n_rows)
        self.assertEqual(ace2d.shape[1], n_cols)

    def test___init__(self):
        """Test the __init__ method."""
        ace2d = ArrayCoefficientExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    ace2d[row - iLowerBoundIndex, col - jLowerBoundIndex],
                    data[row - iLowerBoundIndex, col - jLowerBoundIndex]
        )
        self.assertEqual(ace2d.iLowerBoundIndex, iLowerBoundIndex)
        self.assertEqual(ace2d.iUpperBoundIndex, iUpperBoundIndex)
        self.assertEqual(ace2d.jLowerBoundIndex, jLowerBoundIndex)
        self.assertEqual(ace2d.jUpperBoundIndex, jUpperBoundIndex)

    def test_negate(self):
        """Test the negate method."""
        ace2d = ArrayCoefficientExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        negation = ace2d.negate()
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    negation.getCoefficient(row, col),
                    -ace2d.getCoefficient(row, col)
        )

    def test_getCoefficient(self):
        """Test the getCoefficient method."""
        ace2d = ArrayCoefficientExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    ace2d.getCoefficient(row, col),
                    data[row - iLowerBoundIndex, col - jLowerBoundIndex]
        )


if __name__ == "__main__":
    unittest.main()
