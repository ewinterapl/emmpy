"""Tests for the cylindricaltocartesianjacobian module."""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.cylindricaltocartesianjacobian import (
    CylindricalToCartesianJacobian
)
from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.math.coordinates.cylindricalvector import CylindricalVector


# Test grids.
n = 25
rhos = np.linspace(0, 10, n)
phis = np.linspace(0, 2*pi, n)
zs = np.linspace(-10, 10, n)


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricaltocartesianjacobian module."""

    def test___init__(self):
        """Test the __init__ method."""
        c2cj = CylindricalToCartesianJacobian()
        self.assertIsInstance(c2cj, CylindricalToCartesianJacobian)

    def test_getTransformation(self):
        """Test the getTransformation method."""
        c2cj = CylindricalToCartesianJacobian()
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    cylindrical = CylindricalVector(rho, phi, z)
                    buffer = MatrixIJK()
                    jac = c2cj.getTransformation(cylindrical, buffer)
                    self.assertIs(jac, buffer)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    jac_ref = np.array([[cos_phi, -rho*sin_phi, 0],
                                        [sin_phi, rho*cos_phi, 0],
                                        [0, 0, 1]])
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac[row][col],
                                                   jac_ref[row][col])

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        c2cj = CylindricalToCartesianJacobian()
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    cylindrical = CylindricalVector(rho, phi, z)
                    buffer = MatrixIJK()
                    if rho == 0:
                        with self.assertRaises(PointOnAxisException):
                            jac = c2cj.getInverseTransformation(
                                cylindrical, buffer)
                        continue
                    jac = c2cj.getInverseTransformation(
                        cylindrical, buffer)
                    self.assertIs(jac, buffer)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    jac_ref = np.array([[cos_phi, -rho*sin_phi, 0],
                                        [sin_phi, rho*cos_phi, 0],
                                        [0, 0, 1]])
                    jac_ref = np.linalg.inv(jac_ref)
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac[row][col],
                                                   jac_ref[row][col])

    def test_mxv(self):
        """Test the mxv method."""
        c2cj = CylindricalToCartesianJacobian()
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    # Transform a cylindrical vector to Cartesian,
                    # then back to cylindrical.
                    cyl = CylindricalVector(rho, phi, z)
                    buffer = MatrixIJK()
                    jac = c2cj.getTransformation(cyl, buffer)
                    cart = c2cj.mxv(jac, cyl)
                    cart_ref = [row.dot(cyl) for row in jac]
                    for i in range(3):
                        self.assertAlmostEqual(cart[i], cart_ref[i])
                    if rho == 0:
                        with self.assertRaises(PointOnAxisException):
                            jac = c2cj.getInverseTransformation(
                                cyl, buffer)
                        continue
                    jac_inv = np.linalg.inv(jac)
                    new_cyl = c2cj.mxv(jac_inv, cart)
                    for i in range(3):
                        self.assertAlmostEqual(new_cyl[i], cyl[i])


if __name__ == '__main__':
    unittest.main()
