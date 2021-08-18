"""Tests for the cylindricaltocartesianbasistransformation module."""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.cylindricaltocartesianbasistransformation import (
    CylindricalToCartesianBasisTransformation
)
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK
from emmpy.math.coordinates.cylindricalvector import CylindricalVector


# Test grids.
n = 25
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rhos = np.linspace(0, 10, n)
phis = np.linspace(0, 2*pi, n)
zs = np.linspace(-10, 10, n)


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricaltocartesianbasistransformation module."""

    def test___init__(self):
        """Test the __init__ method."""
        c2cbt = CylindricalToCartesianBasisTransformation()
        self.assertIsInstance(c2cbt, CylindricalToCartesianBasisTransformation)

    def test_getTransformation(self):
        """Test the getTransformation method."""
        c2cbt = CylindricalToCartesianBasisTransformation()
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    cylindrical = CylindricalVector(rho, phi, z)
                    buffer = MatrixIJK()
                    jac = c2cbt.getTransformation(cylindrical, buffer)
                    self.assertIs(jac, buffer)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    jac_ref = [[cos_phi, -sin_phi, 0],
                               [sin_phi, cos_phi, 0],
                               [0, 0, 1]]
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac[row][col],
                                                   jac_ref[row][col])

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        c2cbt = CylindricalToCartesianBasisTransformation()
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    cylindrical = CylindricalVector(rho, phi, z)
                    buffer = MatrixIJK()
                    jac = c2cbt.getInverseTransformation(
                        cylindrical, buffer)
                    self.assertIs(jac, buffer)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    jac_ref = [[cos_phi, sin_phi, 0],
                               [-sin_phi, cos_phi, 0],
                               [0, 0, 1]]
                    for row in range(3):
                        for col in range(3):
                            self.assertAlmostEqual(jac[row][col],
                                                   jac_ref[row][col])

    def test_mxv(self):
        """Test the mxv method."""
        c2cbt = CylindricalToCartesianBasisTransformation()
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    cyl = CylindricalVector(rho, phi, z)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    jac = np.array([[cos_phi, -sin_phi, 0],
                                    [sin_phi, cos_phi, 0],
                                    [0, 0, 1]])
                    cart = c2cbt.mxv(jac, cyl)
                    cart_ref = [row.dot(cyl) for row in jac]
                    for i in range(3):
                        self.assertAlmostEqual(cart[i], cart_ref[i])
                    jac_inv = np.linalg.inv(jac)
                    new_cyl = c2cbt.mxv(jac_inv, cart)
                    for i in range(3):
                        self.assertAlmostEqual(new_cyl[i], cyl[i])


if __name__ == '__main__':
    unittest.main()
