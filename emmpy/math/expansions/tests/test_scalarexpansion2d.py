"""Tests for the scalarexpansion2d module."""


import unittest

import numpy as np

from emmpy.math.expansions.scalarexpansion2d import ScalarExpansion2D


# Test data.
n_rows = 3
n_cols = 4
data = np.linspace(1.0, 2.0, n_rows*n_cols).reshape(n_rows, n_cols)


class TestBuilder(unittest.TestCase):
    """Tests for the scalarexpansion2d module."""

    def test___new__(self):
        """Test the __new__ method."""
        se2d = ScalarExpansion2D.__new__(ScalarExpansion2D, data)
        self.assertEqual(se2d.shape, data.shape)

    def test___init__(self):
        """Test the __init__ method."""
        se2d = ScalarExpansion2D(data)
        self.assertTrue(np.isclose(se2d, data).all())

    def test_negate(self):
        """Test the negate method."""
        se2d = ScalarExpansion2D(data)
        negation = se2d.negate()
        self.assertIsInstance(negation, ScalarExpansion2D)
        self.assertTrue(np.isclose(negation, -data).all())

    def test_scale(self):
        """Test the scale method."""
        scaleFactor = 6.6
        se2d = ScalarExpansion2D(data)
        scaled = se2d.scale(scaleFactor)
        self.assertIsInstance(scaled, ScalarExpansion2D)
        self.assertTrue(np.isclose(scaled, scaleFactor*data).all())

    def test_add(self):
        """Test the add function."""
        a = ScalarExpansion2D(data)
        b = ScalarExpansion2D(data + 1.0)
        expansionSum = ScalarExpansion2D.add(a, b)
        self.assertIsInstance(expansionSum, ScalarExpansion2D)
        self.assertTrue(np.isclose(expansionSum, a + b).all())

    def test_createNullExpansion(self):
        """Test the createNullExpansion function."""
        null = ScalarExpansion2D.createNullExpansion(n_rows, n_cols)
        self.assertIsInstance(null, ScalarExpansion2D)
        self.assertEqual(null.shape, (n_rows, n_cols))
        self.assertTrue(np.isnan(null).all())

    def test_createUnity(self):
        """Test the createUnity function."""
        unity = ScalarExpansion2D.createUnity(n_rows, n_cols)
        self.assertIsInstance(unity, ScalarExpansion2D)
        self.assertEqual(unity.shape, (n_rows, n_cols))
        self.assertTrue(np.isclose(unity, 1.0).all())


if __name__ == "__main__":
    unittest.main()
