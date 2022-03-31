"""Tests for the quadraticapproximationdifferentiablevectorfield module."""


import unittest

from emmpy.math.vectorfields.quadraticapproximationdifferentiablevectorfield import (
    QuadraticApproximationDifferentiableVectorField
)


class TestBuilder(unittest.TestCase):
    """Tests for the quadraticapproximationdifferentiablevectorfield module."""

    def test___init__(self):
        """Test the __init__ method."""
        qadvf = QuadraticApproximationDifferentiableVectorField()
        self.assertIsInstance(qadvf, QuadraticApproximationDifferentiableVectorField)


if __name__ == "__main__":
    unittest.main()
