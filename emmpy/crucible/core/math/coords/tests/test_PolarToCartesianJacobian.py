"""Tests for the polartocartesianjacobian package."""


import unittest

from emmpy.crucible.core.math.coords.polartocartesianjacobian import (
    PolarToCartesianJacobian
)
from emmpy.crucible.core.math.coords.polarvector import PolarVector
from emmpy.crucible.core.math.vectorspace.matrixij import MatrixIJ
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class TestBuilder(unittest.TestCase):
    """Tests for the polartocartesianjacobian package."""

    def test___init__(self):
        """Test the __init__ method."""
        p2cj = PolarToCartesianJacobian()
        self.assertIsInstance(p2cj, PolarToCartesianJacobian)

    def test_getTransformation(self):
        """Test the getTransformation method."""
        (r, angle) = (1, 2)
        jac_ref = ((-0.4161468365471424, -0.9092974268256817),
                   (0.9092974268256817, -0.4161468365471424))
        p2cj = PolarToCartesianJacobian()
        polarPosition = PolarVector(r, angle)
        buffer = MatrixIJ()
        jac = p2cj.getTransformation(polarPosition, buffer)
        self.assertIs(jac, buffer)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(jac[row][col], jac_ref[row][col])

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        (r, angle) = (1, 2)
        jac_ref = ((-0.4161468365471424, 0.9092974268256817),
                   (-0.9092974268256817, -0.4161468365471424))
        p2cj = PolarToCartesianJacobian()
        polarPosition = PolarVector(r, angle)
        buffer = MatrixIJ()
        jac = p2cj.getInverseTransformation(polarPosition, buffer)
        self.assertIs(jac, buffer)
        for row in range(2):
            for col in range(2):
                self.assertAlmostEqual(jac[row][col], jac_ref[row][col])

    def test_mxv(self):
        """Test the mxv method."""
        (r, angle) = (1, 2)
        (vr, vangle) = (1, 1)
        (vx, vy) = (1, 1)
        cartesianVelocity_ref = (-1.325444263372824, 0.4931505902785393)
        polarVelocity_ref = (0.4931505902785393, -1.325444263372824)
        p2cj = PolarToCartesianJacobian()
        polarPosition = PolarVector(r, angle)
        buffer = MatrixIJ()
        # Polar to Cartesian.
        jac = p2cj.getTransformation(polarPosition, buffer)
        polarVelocity = PolarVector(vr, vangle)
        cartesianVelocity = p2cj.mxv(jac, polarVelocity)
        for col in range(2):
            self.assertAlmostEqual(cartesianVelocity[col],
                                   cartesianVelocity_ref[col])
        # Cartesian to polar.
        jac = p2cj.getInverseTransformation(polarPosition, buffer)
        cartesianVelocity = VectorIJ(vx, vy)
        polarVelocity = p2cj.mxv(jac, cartesianVelocity)
        for col in range(2):
            self.assertAlmostEqual(polarVelocity[col], polarVelocity_ref[col])


if __name__ == '__main__':
    unittest.main()
