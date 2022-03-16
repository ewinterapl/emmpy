"""Tests for the scalarexpansion1d module."""


import unittest

import numpy as np

from emmpy.math.expansions.scalarexpansion1d import ScalarExpansion1D


# Test data.
data = np.linspace(1, 2, 10)


class TestBuilder(unittest.TestCase):
    """Tests for the scalarexpansion1d module."""

    def test___new__(self):
        """Test the __new__ method."""
        se1d = ScalarExpansion1D.__new__(ScalarExpansion1D, data)
        self.assertEqual(len(se1d), len(data))

    def test___init__(self):
        """Test the __init__ method."""
        se1d = ScalarExpansion1D(data)
        self.assertTrue(np.isclose(se1d, data).all())

    def test_invert(self):
        """Test the invert method."""
        se1d = ScalarExpansion1D(data)
        inverse = se1d.invert()
        self.assertIsInstance(inverse, ScalarExpansion1D)
        self.assertTrue(np.isclose(inverse, 1.0/data).all())

    def test_scale(self):
        """Test the scale method."""
        scaleFactor = 6.6
        se1d = ScalarExpansion1D(data)
        scaled = se1d.scale(scaleFactor)
        self.assertIsInstance(scaled, ScalarExpansion1D)
        self.assertTrue(np.isclose(scaled, scaleFactor*data).all())

    def test_createUnity(self):
        """Test the createUnity method."""
        length = 10
        unity = ScalarExpansion1D.createUnity(length)
        self.assertIsInstance(unity, ScalarExpansion1D)
        self.assertTrue(np.isclose(unity, 1).all())


if __name__ == "__main__":
    unittest.main()
