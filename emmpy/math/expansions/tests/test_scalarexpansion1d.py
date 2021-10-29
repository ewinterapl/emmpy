"""Tests for the scalarexpansion1d module."""


import unittest

import numpy as np

from emmpy.math.expansions.scalarexpansion1d import (
    ScalarExpansion1D, createUnity
)


# Test data.
data = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
firstExpansionNumber = 1
lastExpansionNumber = firstExpansionNumber + len(data) - 1


class TestBuilder(unittest.TestCase):
    """Tests for the scalarexpansion1d module."""

    def test___new__(self):
        """Test the __new__ method."""
        se1d = ScalarExpansion1D.__new__(
            ScalarExpansion1D, data, firstExpansionNumber
        )
        self.assertEqual(len(se1d), len(data) + firstExpansionNumber)

    def test___init__(self):
        """Test the __init__ method."""
        se1d = ScalarExpansion1D(data, firstExpansionNumber)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(se1d[i], data[i - firstExpansionNumber])
        self.assertEqual(se1d.firstExpansionNumber, firstExpansionNumber)
        self.assertEqual(se1d.lastExpansionNumber, lastExpansionNumber)

    def test_invert(self):
        """Test the invert method."""
        se1d = ScalarExpansion1D(data, firstExpansionNumber)
        inverse = se1d.invert()
        self.assertIsInstance(inverse, ScalarExpansion1D)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(inverse[i],
                                   1/data[i - firstExpansionNumber])

    def test_scale(self):
        """Test the scale method."""
        scaleFactor = 6.6
        se1d = ScalarExpansion1D(data, firstExpansionNumber)
        scaled = se1d.scale(scaleFactor)
        self.assertIsInstance(scaled, ScalarExpansion1D)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(scaled[i],
                                   scaleFactor*data[i - firstExpansionNumber])

    def test_createUnity(self):
        """Test the createUnity function."""
        unity = createUnity(firstExpansionNumber, lastExpansionNumber)
        self.assertIsInstance(unity, ScalarExpansion1D)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(unity[i], 1.0)


if __name__ == "__main__":
    unittest.main()
