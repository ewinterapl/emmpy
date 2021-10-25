"""Tests for the cylindricaltocartesianbasistransformation module."""


from math import cos, pi, sin
import unittest

import numpy as np

from emmpy.crucible.core.math.coords.cylindricaltocartesianbasistransformation import (
    CylindricalToCartesianBasisTransformation
)
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.matrices.matrix3d import Matrix3D


# Test grids.
n = 25
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
                    cylindricalPosition = CylindricalVector(rho, phi, z)
                    buffer = Matrix3D()
                    m = c2cbt.getTransformation(cylindricalPosition, buffer)
                    self.assertIs(m, buffer)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    m_ref = Matrix3D(
                        [[cos_phi, -sin_phi, 0],
                         [sin_phi, cos_phi, 0],
                         [0, 0, 1]]
                    )
                    for row in range(len(m)):
                        for col in range(len(m[0])):
                            self.assertAlmostEqual(m[row, col],
                                                   m_ref[row, col]
                            )

    def test_getInverseTransformation(self):
        """Test the getInverseTransformation method."""
        c2cbt = CylindricalToCartesianBasisTransformation()
        for rho in rhos:
            for phi in phis:
                for z in zs:
                    # Note that the inverse transformation is computed
                    # at a cylindrical position, not a Cartesian position.
                    cylindricalPosition = CylindricalVector(rho, phi, z)
                    buffer = Matrix3D()
                    m = c2cbt.getInverseTransformation(cylindricalPosition, buffer)
                    self.assertIs(m, buffer)
                    cos_phi = cos(phi)
                    sin_phi = sin(phi)
                    m_ref = Matrix3D(
                        [[cos_phi, sin_phi, 0],
                         [-sin_phi, cos_phi, 0],
                         [0, 0, 1]]
                    )
                    for row in range(len(m)):
                        for col in range(len(m[0])):
                            self.assertAlmostEqual(m[row, col],
                                                   m_ref[row, col]
                            )


if __name__ == "__main__":
    unittest.main()
