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
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.math.coordinates.cylindricalvector import CylindricalVector


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

        Parameters
        ----------
        None
        """

    def getTransformation(self, cylindrical, buffer):
        """Return the cylindrical-to-Cartesian basis transformation matrix.

        Return the cylindrical-to-Cartesian basis transformation matrix at
        the specified position.

        Parameters
        ----------
        cylindrical : CylindricalVector
            Position in cylindrical coordinates.
        buffer : MatrixIJK
            Buffer to hold the cylindrical-to-Cartesian basis
            transformation matrix.

        Returns
        -------
        buffer : MatrixIJK
            The cylindrical-to-Cartesian basis transformation matrix.
        """
        phi = cylindrical.phi
        cos_phi = cos(phi)
        sin_phi = sin(phi)
        buffer[:, :] = [[cos_phi, -sin_phi, 0],
                        [sin_phi, cos_phi, 0],
                        [0, 0, 1]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the Cartesian-to-cylindrical basis transformation matrix.

        Return the Cartesian-to-cylindrical basis transformation matrix at
        the specified position.

        The Cartesian-to-cylindrical basis transformation matrix is the
        inverse of the cylindrical-to-Cartesian transformation matrix.

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
        self.getTransformation(coordPosition, buffer)
        buffer[:, :] = np.linalg.inv(buffer)
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
