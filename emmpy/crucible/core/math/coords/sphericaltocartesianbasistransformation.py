"""Convert basis vectors between Cartesian and spherical coordinates.

Convert basis vectors between Cartesian and spherical coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.sphericalvector import SphericalVector


class SphericalToCartesianBasisTransformation:
    """Convert basis vectors between Cartesian and spherical coordinates.

    Convert basis vectors between Cartesian and spherical coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new SphericalToCartesianBasisTransformation object.

        Initialize a new SphericalToCartesianBasisTransformation object.

        Parameters
        ----------
        None
        """

    def getTransformation(self, coordPosition, buffer):
        """Return the spherical-to-Cartesian basis transformation matrix.

        Return the spherical-to-Cartesian basis transformation matrix at
        the specified position.

        Parameters
        ----------
        spherical : SphericalVector
            Position in spherical coordinates.
        buffer : MatrixIJK
            Buffer to hold the spherical-to-Cartesian basis
            transformation matrix.

        Returns
        -------
        buffer : MatrixIJK
            The spherical-to-Cartesian basis transformation matrix.
        """
        theta = coordPosition.theta
        phi = coordPosition.phi
        cos_theta = cos(theta)
        sin_theta = sin(theta)
        cos_phi = cos(phi)
        sin_phi = sin(phi)
        xByR = cos_phi*sin_theta
        yByR = sin_phi*sin_theta
        zByR = cos_theta
        xByColat = cos_phi*cos_theta
        yByColat = sin_phi*cos_theta
        zByColat = -sin_theta
        xByLong = -sin_phi
        yByLong = cos_phi
        zByLong = 0
        buffer[:, :] = [[xByR, xByColat, xByLong],
                        [yByR, yByColat, yByLong],
                        [zByR, zByColat, zByLong]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the Cartesian-to-spherical basis transformation matrix.

        Return the Cartesian-to-spherical basis transformation matrix at
        the specified position.

        The Cartesian-to-spherical basis transformation matrix is the
        inverse of the spherical-to-Cartesian transformation matrix.

        Parameters
        ----------
        spherical : SphericalVector
            Position in spherical coordinates.
        buffer : MatrixIJK
            Buffer to hold the Cartesian-to-spherical basis
            transformation matrix.

        Returns
        -------
        buffer : MatrixIJK
            The Cartesian-to-spherical basis transformation matrix.
        """
        self.getTransformation(coordPosition, buffer)
        buffer[:, :] = np.linalg.inv(buffer)
        return buffer

    def mxv(self, jacobian, vector):
        """Transform a basis vector between spherical and Cartesian coordinates.

        Transform a basis vector between spherical and Cartesian
        coordinates. The transformation can go in either direction, and is
        computed based on the input vector type.

        Parameters
        ----------
        jacobian : MatrixIJK
            Jacobian matrix for conversion.
        vector : SphericalVector or CartesianVector
            Vector in original coordinates.

        Returns
        -------
        converted_vector : CartesianVector or SphericalVector
            Vector in converted coordinates.
        """
        v = jacobian.dot(vector)
        converted_vector = None
        if isinstance(vector, SphericalVector):
            converted_vector = CartesianVector(v)
        else:
            converted_vector = SphericalVector(v)
        return converted_vector
