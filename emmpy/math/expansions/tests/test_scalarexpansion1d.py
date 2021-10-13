"""Tests for the scalarexpansion1d module."""


import unittest

import numpy as np

from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D


# Test data.
data = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
firstExpansionNumber = 1

class TestBuilder(unittest.TestCase):
    """Tests for the scalarexpansion1d module."""

    def test___new__(self):
        """Test the __new__ method."""
        se1d = ScalarExpansion1D.__new__(
            ScalarExpansion1D, data, firstExpansionNumber
        )
        self.assertEqual(len(se1d), len(data))

    def test___init__(self):
        """Test the __init__ method."""
        se1d = ScalarExpansion1D(data, firstExpansionNumber)
        for i in range(len(data)):
            self.assertAlmostEqual(se1d[i], data[i])
        for i in range(firstExpansionNumber,
                       firstExpansionNumber + len(data)):
            self.assertAlmostEqual(se1d[i - firstExpansionNumber],
                                   data[i - firstExpansionNumber])
        self.assertEqual(se1d.firstExpansionNumber, firstExpansionNumber)

    def test_getLowerBoundIndex(self):
        """Test the getLowerBoundIndex method."""
        se1d = ScalarExpansion1D(data, firstExpansionNumber)
        self.assertEqual(se1d.getLowerBoundIndex(), firstExpansionNumber)

    def test_getUpperBoundIndex(self):
        """Test the getUpperBoundIndex method."""
        se1d = ScalarExpansion1D(data, firstExpansionNumber)
        self.assertEqual(se1d.getUpperBoundIndex(),
                         firstExpansionNumber + len(data) - 1)

    def test_getComponent(self):
        """Test the getCoefficient method."""
        se1d = ScalarExpansion1D(data, firstExpansionNumber)
        for i in range(firstExpansionNumber,
                       firstExpansionNumber + len(data)):
            self.assertAlmostEqual(se1d.getComponent(i),
                                   data[i - firstExpansionNumber])


if __name__ == "__main__":
    unittest.main()
