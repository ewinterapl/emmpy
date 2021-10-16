"""Tests for the arraycoefficientexpansion2d module.

NOTE: These tests are for the unpadded, np.ndarray-based version of the
module.
"""


import unittest

import numpy as np

from emmpy.math.expansions.arraycoefficientexpansion2d import (
    ArrayCoefficientExpansion2D, add, createNullExpansion, createUnity
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
        self.assertIsInstance(negation, ArrayCoefficientExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    negation.getCoefficient(row, col),
                    -ace2d.getCoefficient(row, col)
        )

    def test_scale(self):
        """Test the scale method."""
        scale_factor = 1.1
        ace2d = ArrayCoefficientExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        scaled = ace2d.scale(scale_factor)
        self.assertIsInstance(scaled, ArrayCoefficientExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    scaled.getCoefficient(row, col),
                    scale_factor*ace2d.getCoefficient(row, col)
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

    def test_add(self):
        """Test the add function."""
        a = ArrayCoefficientExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        b = ArrayCoefficientExpansion2D(
            data + 1.0, iLowerBoundIndex, jLowerBoundIndex
        )
        sum = add(a, b)
        self.assertIsInstance(sum, ArrayCoefficientExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    sum.getCoefficient(row, col),
                    a.getCoefficient(row, col) + b.getCoefficient(row, col)
                )

    def test_createNullExpansion(self):
        """Test the createNullExpansion function."""
        null = createNullExpansion(
            iLowerBoundIndex, iUpperBoundIndex,
            jLowerBoundIndex, jUpperBoundIndex
        )
        self.assertIsInstance(null, ArrayCoefficientExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertTrue(np.isnan(null.getCoefficient(row, col)))

    def test_createUnity(self):
        """Test the createUnity function."""
        unity = createUnity(iLowerBoundIndex, iUpperBoundIndex,
                            jLowerBoundIndex, jUpperBoundIndex
        )
        self.assertIsInstance(unity, ArrayCoefficientExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(unity.getCoefficient(row, col), 1.0)


if __name__ == "__main__":
    unittest.main()
