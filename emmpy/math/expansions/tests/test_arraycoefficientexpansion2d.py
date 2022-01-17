"""Tests for the arraycoefficientexpansion2d module.

NOTE: These tests are for the unpadded, np.ndarray-based version of the
module.
"""


import unittest

import numpy as np

from emmpy.math.expansions.arraycoefficientexpansion2d import ArrayCoefficientExpansion2D


# Test data.
n_rows = 3
n_cols = 4
data = np.arange(n_rows*n_cols).reshape(n_rows, n_cols)
iLowerBoundIndex = 0
iUpperBoundIndex = iLowerBoundIndex + n_rows - 1
jLowerBoundIndex = 2
jUpperBoundIndex = jLowerBoundIndex + n_cols - 1


class TestBuilder(unittest.TestCase):
    """Tests for the arraycoefficientexpansion2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        ace2d = ArrayCoefficientExpansion2D.__new__(
            ArrayCoefficientExpansion2D,
            data, jLowerBoundIndex
        )
        self.assertEqual(ace2d.shape[0], n_rows + iLowerBoundIndex)
        self.assertEqual(ace2d.shape[1], n_cols + jLowerBoundIndex)

    def test___init__(self):
        """Test the __init__ method."""
        ace2d = ArrayCoefficientExpansion2D(
            data, jLowerBoundIndex
        )
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    ace2d[row, col],
                    data[row - iLowerBoundIndex, col - jLowerBoundIndex]
        )
        self.assertEqual(ace2d.iLowerBoundIndex, iLowerBoundIndex)
        self.assertEqual(ace2d.iUpperBoundIndex, iUpperBoundIndex)
        self.assertEqual(ace2d.jLowerBoundIndex, jLowerBoundIndex)
        self.assertEqual(ace2d.jUpperBoundIndex, jUpperBoundIndex)
        self.assertEqual(ace2d.iSize, iUpperBoundIndex - iLowerBoundIndex + 1)
        self.assertEqual(ace2d.jSize, jUpperBoundIndex - jLowerBoundIndex + 1)

    def test_negate(self):
        """Test the negate method."""
        ace2d = ArrayCoefficientExpansion2D(
            data, jLowerBoundIndex
        )
        negation = ace2d.negate()
        self.assertIsInstance(negation, ArrayCoefficientExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(negation[row, col], -ace2d[row, col])

    def test_scale(self):
        """Test the scale method."""
        scale_factor = 1.1
        ace2d = ArrayCoefficientExpansion2D(
            data, jLowerBoundIndex
        )
        scaled = ace2d.scale(scale_factor)
        self.assertIsInstance(scaled, ArrayCoefficientExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    scaled[row, col], scale_factor*ace2d[row, col]
                )

    def test_add(self):
        """Test the add function."""
        a = ArrayCoefficientExpansion2D(
            data, jLowerBoundIndex
        )
        b = ArrayCoefficientExpansion2D(
            data + 1.0, jLowerBoundIndex
        )
        exp_sum = ArrayCoefficientExpansion2D.add(a, b)
        self.assertIsInstance(exp_sum, ArrayCoefficientExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    exp_sum[row, col], a[row, col] + b[row, col]
                )

    def test_createNullExpansion(self):
        """Test the createNullExpansion function."""
        null = ArrayCoefficientExpansion2D.createNullExpansion(n_rows, n_cols)
        self.assertIsInstance(null, ArrayCoefficientExpansion2D)
        for row in range(n_rows):
            for col in range(n_cols):
                self.assertTrue(np.isnan(null[row, col]))

    def test_createUnity(self):
        """Test the createUnity function."""
        unity = ArrayCoefficientExpansion2D.createUnity(
            n_rows, n_cols
        )
        self.assertIsInstance(unity, ArrayCoefficientExpansion2D)
        for row in range(n_rows):
            for col in range(n_cols):
                self.assertEqual(unity[row, col], 1.0)


if __name__ == "__main__":
    unittest.main()
