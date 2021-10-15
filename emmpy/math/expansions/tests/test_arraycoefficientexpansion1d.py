"""Tests for the arraycoefficientexpansion1d module.

NOTE: These tests are for the unpadded, np.ndarray-based version of the
module.
"""


import unittest

import numpy as np

from emmpy.math.expansions.arraycoefficientexpansion1d import (
    ArrayCoefficientExpansion1D
)


# Test data.
data = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
firstExpansionNumber = 1
lastExpansionNumber = firstExpansionNumber + len(data) - 1


class TestBuilder(unittest.TestCase):
    """Tests for the arraycoefficientexpansion1d module."""

    def test___new__(self):
        """Test the __new__ method."""
        se1d = ArrayCoefficientExpansion1D.__new__(
            ArrayCoefficientExpansion1D, data, firstExpansionNumber
        )
        self.assertEqual(len(se1d), len(data))

    def test___init__(self):
        """Test the __init__ method."""
        ace1d = ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(ace1d[i - firstExpansionNumber],
                                   data[i - firstExpansionNumber])
        self.assertEqual(ace1d.firstExpansionNumber, firstExpansionNumber)
        self.assertEqual(ace1d.lastExpansionNumber, lastExpansionNumber)

    def test_invert(self):
        """Test the inverse method."""
        ace1d = ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        inverse = ace1d.invert()
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(inverse.getCoefficient(i),
                                   1/data[i - firstExpansionNumber])

    def test_negate(self):
        """Test the negate method."""
        ace1d = ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        negation = ace1d.negate()
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(negation.getCoefficient(i),
                                   -data[i - firstExpansionNumber])

    def test_getCoefficient(self):
        """Test the getCoefficient method."""
        ace1d = ArrayCoefficientExpansion1D(data, firstExpansionNumber)
        for i in range(firstExpansionNumber, lastExpansionNumber + 1):
            self.assertAlmostEqual(ace1d.getCoefficient(i),
                                   data[i - firstExpansionNumber])


if __name__ == "__main__":
    unittest.main()
