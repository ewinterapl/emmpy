"""Tests for the cylindricalvector module.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import atan2, cos, pi, sin, sqrt
import unittest

import numpy as np

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.cylindricalvector import (
    CylindricalVector, cylindricalToCartesian, cartesianToCylindrical,
    getCylindricalBasisToCartesianBasisTransformation,
    getCartesianBasisToCylindricalBasisTransformation,
    cylindricalBasisToCartesianBasis, cartesianBasisToCylindricalBasis
)
from emmpy.math.matrices.matrix3d import Matrix3D


# Test grids. Includes the origin and on-axis points.
n = 33
xs = np.linspace(-10, 10, n)
ys = np.linspace(-10, 10, n)
zs = np.linspace(-10, 10, n)
rhos = np.linspace(0, 10, n)
phis = np.linspace(0, 2*pi, n)


class TestBuilder(unittest.TestCase):
    """Tests for the cylindricalvector module."""

    def test___new__(self):
        """Test the __new__ method."""
        # 0-argument form.
        v = CylindricalVector()
        self.assertIsInstance(v, CylindricalVector)
        for i in range(3):
            self.assertTrue(np.isnan(v[i]))
        # 3-argument form.
        (rho, phi, z) = (1.1, 2.2, 3.3)
        v = CylindricalVector(rho, phi, z)
        self.assertIsInstance(v, CylindricalVector)
        self.assertAlmostEqual(v[0], rho)
        self.assertAlmostEqual(v[1], phi)
        self.assertAlmostEqual(v[2], z)

    def test___getattr__(self):
        """Test the __getattr__ method."""
        (rho, phi, z) = (1.1, 2.2, 3.3)
        v = CylindricalVector(rho, phi, z)
        self.assertAlmostEqual(v.rho, rho)
        self.assertAlmostEqual(v.phi, phi)
        self.assertAlmostEqual(v.z, z)
        with self.assertRaises(KeyError):
            v.bad

    def test___setattr__(self):
        """Test the __setattr__ method."""
        v = CylindricalVector(0, 0, 0)
        (rho, phi, z) = (1.1, 2.2, 3.3)
        v.rho = rho
        self.assertAlmostEqual(v.rho, rho)
        v.phi = phi
        self.assertAlmostEqual(v.phi, phi)
        v.z = z
        self.assertAlmostEqual(v.z, z)
        with self.assertRaises(KeyError):
            v.bad = 0

    def test_cylindricalToCartesian(self):
        """Test the cylindricalToCartesian function."""
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    x = rho*cos(phi)
                    y = rho*sin(phi)
                    cylindrical = CylindricalVector(rho, phi, z)
                    cartesian = cylindricalToCartesian(cylindrical)
                    self.assertAlmostEqual(cartesian.x, x)
                    self.assertAlmostEqual(cartesian.y, y)
                    self.assertAlmostEqual(cartesian.z, z)

    def test_cartesianToCylindrical(self):
        """Test the cartesianToCylindrical function."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesian = CartesianVector(x, y, z)
                    rho = sqrt(x**2 + y**2)
                    phi = atan2(y, x)
                    if phi < 0:
                        phi += 2*pi
                    cylindrical = cartesianToCylindrical(cartesian)
                    self.assertAlmostEqual(cylindrical.rho, rho)
                    self.assertAlmostEqual(cylindrical.phi, phi)
                    self.assertAlmostEqual(cylindrical.z, z)

    def test_getCylindricalBasisToCartesianBasisTransformation(self):
        """Test the getCylindricalBasisToCartesianBasisTransformation function."""
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    cylindricalPosition = CylindricalVector(rho, phi, z)
                    m = getCylindricalBasisToCartesianBasisTransformation(
                        cylindricalPosition
                    )
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    m_ref = Matrix3D([[cos_phi, -sin_phi, 0],
                                      [sin_phi, cos_phi, 0],
                                      [0, 0, 1]])
                    for row in range(len(m)):
                        for col in range(len(m[0])):
                            self.assertAlmostEqual(m[row, col],
                                                   m_ref[row, col]
                            )

    def test_getCartesianBasisToCylindricalBasisTransformation(self):
        """Test the getCartesianBasisToCylindricalBasisTransformation function."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesianPosition = CartesianVector(x, y, z)
                    m = getCartesianBasisToCylindricalBasisTransformation(
                        cartesianPosition
                    )
                    phi = atan2(y, x)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    m_ref = Matrix3D([[ cos_phi, sin_phi, 0],
                                      [-sin_phi, cos_phi, 0],
                                      [0, 0, 1]])
                    for row in range(len(m)):
                        for col in range(len(m[0])):
                            self.assertAlmostEqual(m[row, col],
                                                   m_ref[row, col]
                            )

    def test_cylindricalBasisToCartesianBasis(self):
        """Test the cylindricalBasisToCartesianBasis function."""
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    cylindricalPosition = CylindricalVector(rho, phi, z)
                    (a, b, c) = (1.1, 2.2, 3.3)
                    cylindricalValue = CylindricalVector(a, b, c)
                    cartesianValue = cylindricalBasisToCartesianBasis(
                        cylindricalPosition, cylindricalValue
                    )
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    m = Matrix3D([[cos_phi, -sin_phi, 0],
                                  [sin_phi, cos_phi, 0],
                                  [0, 0, 1]])
                    cartesianValue_ref = CartesianVector(
                        m.dot(cylindricalValue)
                    )
                    for row in range(len(cartesianValue)):
                        self.assertAlmostEqual(cartesianValue[row],
                                               cartesianValue_ref[row]
                        )

    def test_cartesianBasisToCylindricalBasis(self):
        """Test the cartesianBasisToCylindricalBasis function."""
        for x in xs:
            for y in ys:
                for z in zs:
                    cartesianPosition = CartesianVector(x, y, z)
                    (a, b, c) = (1.1, 2.2, 3.3)
                    cartesianValue = CartesianVector(a, b, c)
                    cylindricalValue = cartesianBasisToCylindricalBasis(
                        cartesianPosition, cartesianValue
                    )
                    phi = atan2(y, x)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    m = Matrix3D([[ cos_phi, sin_phi, 0],
                                  [-sin_phi, cos_phi, 0],
                                  [0, 0, 1]])
                    cylindricalValue_ref = m.dot(cartesianValue)
                    for row in range(len(cylindricalValue)):
                        self.assertAlmostEqual(cylindricalValue[row],
                                               cylindricalValue_ref[row]
                        )


if __name__ == "__main__":
    unittest.main()
