"""Tests for the scalarexpansion1d module."""


import unittest

import numpy as np

from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D


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

    def test_getComponent(self):
        """Test the getCoefficient method."""
        se1d = ScalarExpansion1D(data, firstExpansionNumber)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(se1d.getComponent(i),
                                   data[i - firstExpansionNumber])


if __name__ == "__main__":
    unittest.main()
