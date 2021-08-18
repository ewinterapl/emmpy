"""Basis transformations between Cartesian and cylindrical coordinates.

Basis transformations between Cartesian and cylindrical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.coordinates.cylindricalvector import CylindricalVector


class CylindricalToCartesianBasisTransformation(Transformation):
    """Basis transformations between cartesian and cylindrical coordinates."""

    def __init__(self):
        """Build a new object."""

    def getTransformation(self, coordPosition, buffer):
        """Return the cylindrical-to-Cartesian transformation matrix.

        Return the cylindrical-to-Cartesian transformation matrix at the
        specified position.

        Parameters
        ----------
        coordPosition : CylindricalVector
            Position in cylindrical coordinates.
        buffer : MatrixIJK
            Buffer to hold the cylindrical-to-Cartesian transformation
            matrix.

        Returns
        -------
        buffer : MatrixIJK
            Buffer to hold cylindrical-to-Cartesian transformation matrix.
        """
        phi = coordPosition.phi
        cos_phi = cos(phi)
        sin_phi = sin(phi)
        j_DX_DR = cos_phi
        j_DY_DR = sin_phi
        j_DZ_DR = 0
        j_DX_DLON = -sin_phi
        j_DY_DLON = cos_phi
        j_DZ_DLON = 0
        j_DX_DZ = 0
        j_DY_DZ = 0
        j_DZ_DZ = 1
        buffer[:, :] = [[j_DX_DR, j_DX_DLON, j_DX_DZ],
                        [j_DY_DR, j_DY_DLON, j_DY_DZ],
                        [j_DZ_DR, j_DZ_DLON, j_DZ_DZ]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the Cartesian-to-cylindrical transformation matrix.

        Return the Cartesian-to-cylindrical transformation matrix at the
        specified position.

        The Cartesian-to-cylindrical transformation matrix is the inverse
        of the cylindrical-to-Cartesian transformation matrix.

        Parameters
        ----------
        coordPosition : CylindricalVector
            Position in cylindrical coordinates.
        buffer : MatrixIJK
            Buffer to hold the Cartesian-to-cylindrical transformation
            matrix.

        Returns
        -------
        buffer : MatrixIJK
            Buffer to hold the Cartesian-to-cylindrical transformation
            matrix.
        """
        self.getTransformation(coordPosition, buffer)
        buffer[:, :] = np.linalg.inv(buffer)
        return buffer

    def mxv(self, jacobian, vector):
        """Apply a transformation, or inverse, to a vector.

        Apply a transformation, or inverse, to a vector.

        Parameters
        ----------
        jacobian : MatrixIJK
            Jacobian matrix for conversion.
        vector : CylindricalVector or VectorIJK
            Vector in original coordinates.

        Returns
        -------
        converted_vector : VectorIJK or CylindricalVector
            Vector in converted coordinates.
        """
        v = jacobian.dot(vector)
        converted_vector = None
        if isinstance(vector, CylindricalVector):
            converted_vector = VectorIJK(v)
        else:
            converted_vector = VectorIJK(v)
        return converted_vector
