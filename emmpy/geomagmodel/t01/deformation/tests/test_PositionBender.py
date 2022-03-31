"""Tests for the positionbender module."""


from math import sin
import unittest

from emmpy.geomagmodel.t01.deformation.positionbender import (
    PositionBender
)


class TestBuilder(unittest.TestCase):
    """Tests for the positionbender module."""

    def test___init__(self):
        """Test the __init__ method."""
        dipoleTilt = 0.2  # radians
        hingeDistance = 6.1  # Arbitrary
        pb = PositionBender(dipoleTilt, hingeDistance)
        self.assertIsInstance(pb, PositionBender)
        self.assertAlmostEqual(pb.sinTilt, sin(dipoleTilt))
        self.assertAlmostEqual(pb.rh0, hingeDistance)

    def test_evaluate(self):
        """Test the evaluate method."""
        pass

    def test_differentiate(self):
        """Test the differentiate method."""
        pass

    def test_deformBasisField(self):
        """Test the deformBasisField method."""
        pass


if __name__ == "__main__":
    unittest.main()
