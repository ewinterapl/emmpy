"""Convert basis vectors between Cartesian and cylindrical coordinates.

Convert basis vectors between Cartesian and cylindrical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.math.coordinates.cylindricalvector import (
    CylindricalVector,
    getCylindricalBasisToCartesianBasisTransformation
)


class CylindricalToCartesianBasisTransformation:
    """Convert basis vectors between Cartesian and cylindrical coordinates.

    Convert basis vectors between Cartesian and cylindrical coordinates.

    Attributes
    ----------
    None
    """

    def getTransformation(self, cylindrical, buffer):
        """Compute the cylindrical-to-Cartesian basis transformation matrix.

        Compute the cylindrical-to-Cartesian basis transformation matrix at
        the specified cylindrical position.

        Parameters
        ----------
        cylindrical : CylindricalVector
            Position in cylindrical coordinates for computing
            the transformation matrix.
        buffer : MatrixIJK
            Buffer to hold the cylindrical-to-Cartesian basis
            transformation matrix.

        Returns
        -------
        buffer : MatrixIJK
            The cylindrical-to-Cartesian basis transformation matrix
            computed at the specified position.
        """
        m = getCylindricalBasisToCartesianBasisTransformation(cylindrical)
        buffer[:] = m[:]
        return buffer

    def getInverseTransformation(self, cylindrical, buffer):
        """Return the Cartesian-to-cylindrical basis transformation matrix.

        Return the Cartesian-to-cylindrical basis transformation matrix at
        the specified *cylindrical* position.

        The Cartesian-to-cylindrical basis transformation matrix is the
        inverse (and transpose) of the cylindrical-to-Cartesian
        transformation matrix. This is computed using the cylindrical
        position, since computing the inverse transformation directly for
        Cartesian positions on the z-axis results in the wrong
        transformation matrix: [[0, 0, 0], [0, 0, 0], [0, 0, 1]]

        Parameters
        ----------
        cylindrical : CylindricalVector
            Position in cylindrical coordinates.
        buffer : MatrixIJK
            Buffer to hold the Cartesian-to-cylindrical basis
            transformation matrix.

        Returns
        -------
        buffer : MatrixIJK
            The Cartesian-to-cylindrical basis transformation matrix.
        """
        m = getCylindricalBasisToCartesianBasisTransformation(cylindrical)
        m = m.T
        buffer[:] = m[:]
        return buffer
