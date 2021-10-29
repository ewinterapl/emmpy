"""Tests for the scalarexpansion2d module."""


import unittest

import numpy as np

from emmpy.math.expansions.scalarexpansion2d import (
    ScalarExpansion2D, add, createNullExpansion, createUnity
)


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

    def test_negate(self):
        """Test the negate method."""
        ace2d = ScalarExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        negation = ace2d.negate()
        self.assertIsInstance(negation, ScalarExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(negation[row, col], -ace2d[row, col])

    def test_scale(self):
        """Test the scale method."""
        scale_factor = 1.1
        ace2d = ScalarExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        scaled = ace2d.scale(scale_factor)
        self.assertIsInstance(scaled, ScalarExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    scaled[row, col], scale_factor*ace2d[row, col]
                )

    def test_add(self):
        """Test the add function."""
        a = ScalarExpansion2D(
            data, iLowerBoundIndex, jLowerBoundIndex
        )
        b = ScalarExpansion2D(
            data + 1.0, iLowerBoundIndex, jLowerBoundIndex
        )
        exp_sum = add(a, b)
        self.assertIsInstance(exp_sum, ScalarExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(
                    exp_sum[row, col], a[row, col] + b[row, col]
                )

    def test_createNullExpansion(self):
        """Test the createNullExpansion function."""
        null = createNullExpansion(
            iLowerBoundIndex, iUpperBoundIndex,
            jLowerBoundIndex, jUpperBoundIndex
        )
        self.assertIsInstance(null, ScalarExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertTrue(np.isnan(null[row, col]))

    def test_createUnity(self):
        """Test the createUnity function."""
        unity = createUnity(iLowerBoundIndex, iUpperBoundIndex,
                            jLowerBoundIndex, jUpperBoundIndex
        )
        self.assertIsInstance(unity, ScalarExpansion2D)
        for row in range(iLowerBoundIndex, iUpperBoundIndex + 1):
            for col in range(jLowerBoundIndex, jUpperBoundIndex + 1):
                self.assertAlmostEqual(unity[row, col], 1.0)


if __name__ == "__main__":
    unittest.main()
