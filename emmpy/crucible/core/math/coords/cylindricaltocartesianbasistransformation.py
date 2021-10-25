"""Convert basis vectors between Cartesian and cylindrical coordinates.

Convert basis vectors between Cartesian and cylindrical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.math.coordinates.cylindricalvector import (
    CylindricalVector, cylindricalToCartesian,
    getCylindricalBasisToCartesianBasisTransformation,
    getCartesianBasisToCylindricalBasisTransformation
)
from emmpy.math.coordinates.cartesianvector3d import CartesianVector3D


class CylindricalToCartesianBasisTransformation(Transformation):
    """Convert basis vectors between Cartesian and cylindrical coordinates.

    Convert basis vectors between Cartesian and cylindrical coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new CylindricalToCartesianBasisTransformation object.

        Initialize a new CylindricalToCartesianBasisTransformation object.

        This dummy __init__ is needed to override the inherited abstract
        __init__, which raises an exception when invoked.

        Parameters
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

    def mxv(self, jacobian, vector):
        """Transform a basis vector between cylindrical and Cartesian coordinates.

        Transform a basis vector between cylindrical and Cartesian
        coordinates. The transformation can go in either direction, and is
        computed based on the input vector type.

        Parameters
        ----------
        jacobian : MatrixIJK
            Jacobian matrix for conversion.
        vector : CylindricalVector or CartesianVector3D
            Vector in original coordinates.

        Returns
        -------
        converted_vector : CartesianVector3D or CylindricalVector
            Vector in converted coordinates.
        """
        v = jacobian.dot(vector)
        converted_vector = None
        if isinstance(vector, CylindricalVector):
            converted_vector = CartesianVector3D(v)
        else:
            converted_vector = CylindricalVector(v)
        return converted_vector
