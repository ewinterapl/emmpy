"""Jacobian to convert vectors from cylindrical to Cartesian coordinates.

Jacobian to convert vectors from cylindrical to Cartesian coordinates.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from math import cos, sin

import numpy as np

from emmpy.crucible.core.math.coords.pointonaxisexception import (
    PointOnAxisException)
from emmpy.crucible.core.math.coords.transformation import Transformation
from emmpy.math.coordinates.cylindricalvector import CylindricalVector
from emmpy.math.coordinates.vectorijk import VectorIJK


class CylindricalToCartesianJacobian(Transformation):
    """Jacobian to convert vectors from cylindrical to Cartesian coordinates.

    Jacobian to convert vectors from cylindrical to Cartesian coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self):
        """Initialize a new CylindricalToCartesianJacobian object.

        Initialize a new CylindricalToCartesianJacobian object.

        Parameters
        ----------
        None
        """

    def getTransformation(self, cylindrical, buffer):
        """Return the cylindrical-to-Cartesian Jacobian.

        Return the cylindrical-to-Cartesian Jacobian at the specified
        position.

        Parameters
        ----------
        cylindrical : CylindricalVector
            Position in cylindrical coordinates.
        buffer : MatrixIJK
            Buffer to hold the cylindrical-to-Cartesian Jacobian.

        Returns
        -------
        buffer : MatrixIJK
            The cylindrical-to-Cartesian Jacobian.
        """
        rho = cylindrical.rho
        phi = cylindrical.phi
        cos_phi = cos(phi)
        sin_phi = sin(phi)
        buffer[:, :] = [[cos(phi), -rho*sin_phi, 0],
                        [sin_phi, rho*cos_phi, 0],
                        [0, 0, 1]]
        return buffer

    def getInverseTransformation(self, cylindrical, buffer):
        """Return the Cartesian-to-cylindrical Jacobian.

        Return the Cartesian-to-cylindrical Jacobian at the specified
        position.

        Parameters
        ----------
        cylindrical : CylindricalVector
            Position in cylindrical coordinates.
        buffer : MatrixIJK
            Buffer to hold the Cartesian-to-cylindrical Jacobian.

        Returns
        -------
        buffer : MatrixIJK
            The Cartesian-to-cylindrical Jacobian.
        """
        try:
            self.getTransformation(cylindrical, buffer)
            buffer[:, :] = np.linalg.inv(buffer)
            return buffer
        except np.linalg.LinAlgError as e:
            raise PointOnAxisException

    def mxv(self, jacobian, vector):
        """Transform a vector between cylindrical and Cartesian coordinates.

        Transform a vector between cylindrical and Cartesian coordinates.
        The transformation can go in either direction, and is computed
        based on the input vector type.

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
            converted_vector = CylindricalVector(v)
        return converted_vector
