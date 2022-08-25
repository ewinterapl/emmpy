"""Tests for the basisvectorfielddeformation module."""


import unittest

from emmpy.magmodel.math.deformation.basisvectorfielddeformation import (
    BasisVectorFieldDeformation
)


class TestBuilder(unittest.TestCase):
    """Tests for the basisvectorfielddeformation module."""

    def test___init__(self):
        """Test the __init__ method."""
        with self.assertRaises(Exception):
            BasisVectorFieldDeformation()

    def test_evaluateExpansion(self):
        """Test the evaluateExpansion method."""
        pass

    def test_getNumberOfBasisFunctions(self):
        """Test the getNumberOfBasisFunctions method."""
        pass


if __name__ == "__main__":
    unittest.main()
