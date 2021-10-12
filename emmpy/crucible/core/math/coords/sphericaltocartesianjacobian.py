"""Jacobian to convert vectors from spherical to Cartesian coordinates.

Jacobian to convert vectors from spherical to Cartesian coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


# from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException
)
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.math.coordinates.sphericalvector import SphericalVector
from emmpy.math.coordinates.vectorijk import VectorIJK


class SphericalToCartesianJacobian(Transformation):
    """Jacobian to convert vectors from spherical to Cartesian coordinates.

    Jacobian to convert vectors from spherical to Cartesian coordinates.
    """

    def __init__(self):
        """Initialize a new SphericalToCartesianJacobian object.

        Initialize a new SphericalToCartesianJacobian object.

        Parameters
        ----------
        None
        """

    def getTransformation(self, coordPosition, buffer):
        """Return the spherical-to-Cartesian Jacobian.

        Return the spherical-to-Cartesian Jacobian at the specified
        position.

        Parameters
        ----------
        coordPosition : SphericalVector
            Position in spherical coordinates.
        buffer : MatrixIJK
            Buffer to hold the spherical-to-Cartesian Jacobian.

        Returns
        -------
        buffer : MatrixIJK
            The spherical-to-Cartesian Jacobian.
        """
        r = coordPosition.r
        theta = coordPosition.theta
        phi = coordPosition.phi
        cos_theta = cos(theta)
        sin_theta = sin(theta)
        cos_phi = cos(phi)
        sin_phi = sin(phi)
        xByR = cos_phi*sin_theta
        yByR = sin_phi*sin_theta
        zByR = cos_theta
        xByTheta = r*cos_phi*cos_theta
        yByTheta = r*sin_phi*cos_theta
        zByTheta = -r*sin_theta
        xByPhi = -r*sin_phi*sin_theta
        yByPhi = r*cos_phi*sin_theta
        zByPhi = 0
        buffer[:, :] = [[xByR, xByTheta, xByPhi],
                        [yByR, yByTheta, yByPhi],
                        [zByR, zByTheta, zByPhi]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the Cartesian-to-spherical Jacobian.

        Return the Cartesian-to-spherical Jacobian at the specified
        position.

        Parameters
        ----------
        coordPosition : SphericalVector
            Position in spherical coordinates.
        buffer : MatrixIJK
            Buffer to hold the Cartesian-to-spherical Jacobian.

        Returns
        -------
        buffer : MatrixIJK
            The Cartesian-to-spherical Jacobian.
        """
        try:
            self.getTransformation(coordPosition, buffer)
            buffer[:, :] = np.linalg.inv(buffer)
            return buffer
        except np.linalg.LinAlgError as e:
            raise PointOnAxisException(e)

    def mxv(self, jacobian, vector):
        """Transform a vector between spherical and Cartesian coordinates.

        Transform a vector between spherical and Cartesian coordinates.
        The transformation can go in either direction, and is computed
        based on the input vector type.

        Parameters
        ----------
        jacobian : MatrixIJK
            Jacobian matrix for conversion.
        vector : SphericalVector or VectorIJK
            Vector in original coordinates.

        Returns
        -------
        converted_vector : VectorIJK or SphericalVector
            Vector in converted coordinates.
        """
        v = jacobian.dot(vector)
        converted_vector = None
        if isinstance(vector, SphericalVector):
            converted_vector = VectorIJK(v)
        else:
            converted_vector = SphericalVector(v)
        return converted_vector
