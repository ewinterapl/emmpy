"""Jacobian to convert vectors from latitudinal to Cartesian coordinates.

Jacobian to convert vectors from latitudinal to Cartesian coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.latitudinalvector import LatitudinalVector
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class LatitudinalToCartesianJacobian(Transformation):
    """Jacobian to convert vectors from latitudinal to Cartesian coordinates.

    Jacobian to convert vectors from latitudinal to Cartesian coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new LatitudinalToCartesianJacobian object.

        Initialize a new LatitudinalToCartesianJacobian object.

        Parameters
        ----------
        None
        """

    def getTransformation(self, coordPosition, buffer):
        """Return the latitudinal-to-Cartesian Jacobian.

        Return the latitudinal-to-Cartesian Jacobian at the specified
        position.

        Parameters
        ----------
        coordPosition : LatitudinalVector
            Position in latitudinal coordinates.
        buffer : MatrixIJK
            Buffer to hold the latitudinal-to-Cartesian Jacobian.

        Returns
        -------
        buffer : MatrixIJK
            The latitudinal-to-Cartesian Jacobian.
        """
        r = coordPosition.getRadius()
        lat = coordPosition.getLatitude()
        lon = coordPosition.getLongitude()
        cos_lat = cos(lat)
        sin_lat = sin(lat)
        cos_lon = cos(lon)
        sin_lon = sin(lon)
        buffer[:, :] = [
            [cos_lon*cos_lat, -r*cos_lon*sin_lat, -r*sin_lon*cos_lat],
            [sin_lon*cos_lat, -r*sin_lon*sin_lat, r*cos_lon*cos_lat],
            [sin_lat, r*cos_lat, 0]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the Cartesian-to-latitudinal Jacobian.

        Return the Cartesian-to-latitudinal Jacobian at the specified
        position.

        Parameters
        ----------
        coordPosition : LatitudinalVector
            Position in latitudinal coordinates.
        buffer : MatrixIJK
            Buffer to hold the Cartesian-to-latitudinal Jacobian.

        Returns
        -------
        buffer : MatrixIJK
            The Cartesian-to-latitudinal Jacobian.
        """
        self.getTransformation(coordPosition, buffer)
        buffer[:, :] = np.linalg.inv(buffer)
        return buffer

    def mxv(self, jacobian, vector):
        """Transform a vector between latitudinal and Cartesian coordinates.

        Transform a vector between latitudinal and Cartesian coordinates.
        The transformation can go in either direction, and is computed
        based on the input vector type.

        Special cases are required when converting Cartesian (0,0,z) to
        latitudinal: latitude will always be +/- pi/2 or 0, longitude will
        always be 0.

        Parameters
        ----------
        jacobian : MatrixIJK
            Jacobian matrix for conversion.
        vector : CylindricalVector or VectorIJK
            Vector in original coordinates.

        Returns
        -------
        converted_vector : VectorIJK or LatitudinalVector
            Vector in converted coordinates.
        """
        v = jacobian.dot(vector)
        converted_vector = None
        if isinstance(vector, LatitudinalVector):
            # Latitudinal to Cartesian.
            converted_vector = VectorIJK(v[0], v[1], v[2])
        else:
            # Cartesian to latitudinal.
            converted_vector = LatitudinalVector(v[0], v[1], v[2])
        return converted_vector
