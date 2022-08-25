"""Tests for the arrayexpansion2d module."""


import unittest

import numpy as np

from emmpy.magmodel.math.expansions.arrayexpansion2d import (
    ArrayExpansion2D
)
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.utilities.nones import nones


# Test data
n_rows = 3
n_cols = 4
vector_size = 3
data1 = np.arange(n_rows*n_cols*vector_size).reshape((n_rows, n_cols, vector_size))
ve1 = nones((n_rows, n_cols))
for row in range(n_rows):
    for col in range(n_cols):
        ve1[row][col] = CartesianVector(data1[row][col][:])
data2 = 1.1*np.arange(n_rows*n_cols*vector_size).reshape((n_rows, n_cols, vector_size))
ve2 = nones((n_rows, n_cols))
for row in range(n_rows):
    for col in range(n_cols):
        ve2[row][col] = CartesianVector(data2[row][col][:])


class TestBuilder(unittest.TestCase):
    """Tests for the arrayexpansion2d module."""

    def test___init__(self):
        """Test the __init__ method."""
        ae2d = ArrayExpansion2D(data1)
        self.assertIsInstance(ae2d, ArrayExpansion2D)
        for row in range(n_rows):
            for col in range(n_cols):
                for k in range(vector_size):
                    self.assertAlmostEqual(ae2d[row][col][k], data1[row][col][k])

    def test_add(self):
        """Test the add method."""
        ae2d1 = ArrayExpansion2D(ve1)
        ae2d2 = ArrayExpansion2D(ve2)
        ae2d3 = ArrayExpansion2D.add(ae2d1, ae2d2)
        self.assertIsInstance(ae2d3, ArrayExpansion2D)
        for row in range(n_rows):
            for col in range(n_cols):
                for k in range(vector_size):
                    self.assertAlmostEqual(
                        ae2d3[row][col][k],
                        data1[row][col][k] + data2[row][col][k]
                    )


if __name__ == "__main__":
    unittest.main()
