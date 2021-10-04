"""Tests for the sphericaltocartesianjacobian module."""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.sphericaltocartesianjacobian import (
    SphericalToCartesianJacobian
)
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


# Test grids.
n = 25
rs = np.linspace(0, 10, n)
thetas = np.linspace(0, pi, n)
phis = np.linspace(0, 2*pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the sphericaltocartesianjacobian module."""

    def test___init__(self):
        """Test the __init__ method."""
        s2cj = SphericalToCartesianJacobian()
        self.assertIsInstance(s2cj, SphericalToCartesianJacobian)

    def test_getTransformation(self):
        """Test the getTransformation method."""
        s2cj = SphericalToCartesianJacobian()
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    spherical = SphericalVector(r, theta, phi)
                    cos_theta = cos(theta)
                    sin_theta = sin(theta)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    jac_ref = np.array(
                        [[cos_phi*sin_theta, r*cos_phi*cos_theta,
                          -r*sin_phi*sin_theta],
                         [sin_phi*sin_theta, r*sin_phi*cos_theta,
                          r*cos_phi*sin_theta],
                         [cos_theta, -r*sin_theta, 0]])
                    buffer = MatrixIJK()
                    jac = s2cj.getTransformation(spherical, buffer)
                    self.assertIs(jac, buffer)
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac[row][col],
                                                   jac_ref[row][col])

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        s2cj = SphericalToCartesianJacobian()
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    spherical = SphericalVector(r, theta, phi)
                    buffer = MatrixIJK()
                    cos_theta = cos(theta)
                    sin_theta = sin(theta)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    jac_ref = np.array(
                        [[cos_phi*sin_theta, r*cos_phi*cos_theta,
                          -r*sin_phi*sin_theta],
                         [sin_phi*sin_theta, r*sin_phi*cos_theta,
                          r*cos_phi*sin_theta],
                         [cos_theta, -r*sin_theta, 0]])
                    try:
                        jac_inv_ref = np.linalg.inv(jac_ref)
                    except np.linalg.LinAlgError:
                        with self.assertRaises(PointOnAxisException):
                            jac_inv_ref = s2cj.getInverseTransformation(
                                spherical, buffer)
                        continue
                    jac_inv = s2cj.getInverseTransformation(spherical, buffer)
                    self.assertIs(jac_inv, buffer)
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac_inv[row][col],
                                                   jac_inv_ref[row][col])

    def test_mxv(self):
        """Test the mxv method."""
        s2cj = SphericalToCartesianJacobian()
        for r in rs:
            for theta in thetas:
                for phi in phis:
                    # Transform a spherical gradient into Cartesian, then
                    # back to spherical.
                    spherical = SphericalVector(r, theta, phi)
                    buffer = MatrixIJK()
                    jac = s2cj.getTransformation(spherical, buffer)
                    cart = s2cj.mxv(jac, spherical)
                    cart_ref = [row.dot(spherical) for row in jac]
                    for i in range(3):
                        self.assertAlmostEqual(cart[i], cart_ref[i])
                    try:
                        jac_inv = np.linalg.inv(jac)
                    except np.linalg.LinAlgError:
                        with self.assertRaises(PointOnAxisException):
                            jac_inv = s2cj.getInverseTransformation(spherical,
                                                                    buffer)
                        continue
                    jac_inv = s2cj.getInverseTransformation(spherical, buffer)
                    new_spherical_ref = [row.dot(cart) for row in jac_inv]
                    new_spherical = s2cj.mxv(jac_inv, cart)
                    self.assertAlmostEqual(new_spherical.r,
                                           new_spherical_ref[0])
                    self.assertAlmostEqual(new_spherical.theta,
                                           new_spherical_ref[1])
                    self.assertAlmostEqual(new_spherical.phi,
                                           new_spherical_ref[2])


if __name__ == '__main__':
    unittest.main()
