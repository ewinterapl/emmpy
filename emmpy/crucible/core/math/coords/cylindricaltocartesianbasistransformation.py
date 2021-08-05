"""Basis transformations between cartesian and cylindrical coordinates."""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.cylindricalvector import CylindricalVector
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.matrixijk import MatrixIJK


class CylindricalToCartesianBasisTransformation(Transformation):
    """Basis transformations between cartesian and cylindrical coordinates."""

    def __init__(self):
        """Build a new object."""

    def getTransformation(self, coordPosition, buffer):
        """Return the transformation matrix.

        return
              .-                                  -.
              |  cos(long)  -sin(long)      0      |
              |                                    |
              |  sin(long)   cos(long)      0      |
              |                                    |
              |     0           0           1      |
              `-                                  -'
        """
        lon = coordPosition.getLongitude()
        cosLon = cos(lon)
        sinLon = sin(lon)
        j_DX_DR = cosLon
        j_DY_DR = sinLon
        j_DZ_DR = 0.0
        j_DX_DLON = -sinLon
        j_DY_DLON = cosLon
        j_DZ_DLON = 0.0
        j_DX_DZ = 0.0
        j_DY_DZ = 0.0
        j_DZ_DZ = 1.0
        buffer[:, :] = [[j_DX_DR, j_DX_DLON, j_DX_DZ],
                        [j_DY_DR, j_DY_DLON, j_DY_DZ],
                        [j_DZ_DR, j_DZ_DLON, j_DZ_DZ]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the cartesian-to-cylindrical transformation matrix."""
        self.getTransformation(coordPosition, buffer)
        buffer[:] = np.linalg.inv(buffer)
        return buffer

    def mxv(self, *args):
        """Apply this transformation, or inverse, to a cylindrical vector."""
        if isinstance(args[1], CylindricalVector):
            (jacobian, coordValue) = args
            return MatrixIJK.mxv(jacobian, coordValue.getVectorIJK())
        else:
            (inverseTransformation, cartVelocity) = args
            vect = MatrixIJK.mxv(inverseTransformation, cartVelocity)
            return CylindricalVector(vect.i, vect.j, vect.k)
