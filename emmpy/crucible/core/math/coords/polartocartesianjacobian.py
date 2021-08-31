"""Jacobian to convert vectors from polar to Cartesian coordinates.

Jacobian to convert vectors from polar to Cartesian coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.polarvector import PolarVector
from emmpy.crucible.core.math.coords.transformationij import TransformationIJ
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class PolarToCartesianJacobian(TransformationIJ):
    """Jacobian to convert vectors from polar to Cartesian coordinates.

    Jacobian to convert vectors from polar to Cartesian coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new PolarToCartesianJacobian object.

        Initialize a new PolarToCartesianJacobian object.

        Parameters
        ----------
        None
        """

    def getTransformation(self, coordPosition, buffer):
        """Return the polar-to-Cartesian Jacobian.

        Return the polar-to-Cartesian Jacobian at the specified position.

        Parameters
        ----------
        coordPosition : PolarVector
            Position in latipolarudinal coordinates.
        buffer : MatrixIJ
            Buffer to hold the polar-to-Cartesian Jacobian.

        Returns
        -------
        buffer : MatrixIJ
            The polar-to-Cartesian Jacobian.
        """
        r = coordPosition.getRadius()
        angle = coordPosition.getAngle()
        cosAngle = cos(angle)
        sinAngle = sin(angle)
        buffer[:, :] = [[cosAngle, -r*sinAngle], [sinAngle, r*cosAngle]]
        return buffer

    def getInverseTransformation(self, coordPosition, buffer):
        """Return the Cartesian-to-polar Jacobian.

        Return the Cartesian-to-polar Jacobian at the specified position.

        Parameters
        ----------
        coordPosition : PolarVector
            Position in polar coordinates.
        buffer : MatrixIJ
            Buffer to hold the Cartesian-to-polar Jacobian.

        Returns
        -------
        buffer : MatrixIJ
            The Cartesian-to-polar Jacobian.
        """
        self.getTransformation(coordPosition, buffer)
        buffer[:, :] = np.linalg.inv(buffer)
        return buffer

    def mxv(self, jacobian, vector):
        """Transform a vector between polar and Cartesian coordinates.

        Transform a vector between polar and Cartesian coordinates.
        The transformation can go in either direction, and is computed
        based on the input vector type.

        Parameters
        ----------
        jacobian : MatrixIJ
            Jacobian matrix for conversion.
        vector : PolarVector or VectorIJ
            Vector in original coordinates.

        Returns
        -------
        converted_vector : VectorIJ or PolarVector
            Vector in converted coordinates.
        """
        v = jacobian.dot(vector)
        converted_vector = None
        if isinstance(vector, PolarVector):
            # Polar to Cartesian.
            converted_vector = VectorIJ(v[0], v[1])
        else:
            # Cartesian to polar.
            converted_vector = PolarVector(v[0], v[1])
        return converted_vector
