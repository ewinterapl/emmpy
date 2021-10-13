"""Tests for the sphericaltocartesianbasistransformation module."""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.sphericaltocartesianbasistransformation import (
    SphericalToCartesianBasisTransformation
)
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.math.matrices.matrixijk import MatrixIJK


# Test grids.
n = 25
rs = np.linspace(0, 10, n)
thetas = np.linspace(0, pi, n)
phis = np.linspace(0, 2*pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the sphericaltocartesianbasistransformation module."""

    def test___init__(self):
        """Test the __init__ method."""
        s2cbt = SphericalToCartesianBasisTransformation()
        self.assertIsInstance(s2cbt, SphericalToCartesianBasisTransformation)

    def test_getTransformation(self):
        """Test the getTransformation method."""
        s2cbt = SphericalToCartesianBasisTransformation()
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    spherical = SphericalVector(r, theta, phi)
                    cos_theta = cos(theta)
                    sin_theta = sin(theta)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    xByR = cos_phi*sin_theta
                    yByR = sin_phi*sin_theta
                    zByR = cos_theta
                    xByColat = cos_phi*cos_theta
                    yByColat = sin_phi*cos_theta
                    zByColat = -sin_theta
                    xByLong = -sin_phi
                    yByLong = cos_phi
                    zByLong = 0
                    jac_ref = [[xByR, xByColat, xByLong],
                               [yByR, yByColat, yByLong],
                               [zByR, zByColat, zByLong]]
                    buffer = MatrixIJK()
                    jac = s2cbt.getTransformation(spherical, buffer)
                    self.assertIs(jac, buffer)
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac[row][col],
                                                   jac_ref[row][col])

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        s2cbt = SphericalToCartesianBasisTransformation()
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    spherical = SphericalVector(r, theta, phi)
                    cos_theta = cos(theta)
                    sin_theta = sin(theta)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    xByR = cos_phi*sin_theta
                    yByR = sin_phi*sin_theta
                    zByR = cos_theta
                    xByColat = cos_phi*cos_theta
                    yByColat = sin_phi*cos_theta
                    zByColat = -sin_theta
                    xByLong = -sin_phi
                    yByLong = cos_phi
                    zByLong = 0
                    jac_ref = np.array([[xByR, xByColat, xByLong],
                                        [yByR, yByColat, yByLong],
                                        [zByR, zByColat, zByLong]])
                    jac_inv_ref = np.linalg.inv(jac_ref)
                    buffer = MatrixIJK()
                    jac_inv = s2cbt.getInverseTransformation(spherical, buffer)
                    self.assertIs(jac_inv, buffer)
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac_inv[row][col],
                                                   jac_inv_ref[row][col])

    def test_mxv(self):
        """Test the mxv method."""
        s2cbt = SphericalToCartesianBasisTransformation()
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    spherical = SphericalVector(r, theta, phi)
                    buffer = MatrixIJK()
                    jac = s2cbt.getTransformation(spherical, buffer)
                    cart_ref = [row.dot(spherical) for row in jac]
                    cart = s2cbt.mxv(jac, spherical)
                    for i in range(3):
                        self.assertAlmostEqual(cart[i], cart_ref[i])


if __name__ == '__main__':
    unittest.main()
