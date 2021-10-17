"""Tests for the arraycoefficientexpansion1d module.

NOTE: These tests are for the unpadded, np.ndarray-based version of the
module.
"""


import unittest

import numpy as np

from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D, createUnity
)


# Test data.
data = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
firstExpansionNumber = 1
lastExpansionNumber = firstExpansionNumber + len(data) - 1


class TestBuilder(unittest.TestCase):
    """Tests for the arraycoefficientexpansion1d module."""

    def test___new__(self):
        """Test the __new__ method."""
        ace1d = ArrayCoefficientExpansion1D.__new__(
            ArrayCoefficientExpansion1D, data, firstExpansionNumber
        )
        self.assertEqual(len(ace1d), len(data) + firstExpansionNumber)

    def test___init__(self):
        """Test the __init__ method."""
        ace1d = ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(ace1d[i], data[i - firstExpansionNumber])
        self.assertEqual(ace1d.firstExpansionNumber, firstExpansionNumber)
        self.assertEqual(ace1d.lastExpansionNumber, lastExpansionNumber)

    def test_invert(self):
        """Test the inverse method."""
        ace1d = ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        inverse = ace1d.invert()
        self.assertIsInstance(inverse, ArrayCoefficientExpansion1D)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(inverse[i],
                                   1/data[i - firstExpansionNumber])

    def test_scale(self):
        """Test the inverse method."""
        scaleFactor = 6.6
        ace1d = ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        scaled = ace1d.scale(scaleFactor)
        self.assertIsInstance(scaled, ArrayCoefficientExpansion1D)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(scaled[i],
                                   scaleFactor*data[i - firstExpansionNumber])

    def test_createUnity(self):
        """Test the createUnity function."""
        unity = createUnity(firstExpansionNumber, lastExpansionNumber)
        self.assertIsInstance(unity, ArrayCoefficientExpansion1D)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(unity[i], 1.0)


if __name__ == "__main__":
    unittest.main()
