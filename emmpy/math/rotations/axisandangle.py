"""A rotation axis and angle.

This class represents a rotation angle around an axis.

Authors
-------
F.S. Turner
Eric Winter (eric.winter@jhuapl.edu)
"""


# from math import atan2, pi

from emmpy.math.vectorspace.rotationmatrixijk import (
    IDENTITY
)
from emmpy.math.rotations.privilegedrotationmatrixijk import (
    PrivilegedRotationMatrixIJK
)
from emmpy.math.rotations.rotation import Rotation
from emmpy.math.coordinates.vectorijk import  (
    I, J, K, VectorIJK, rotate
)

class AxisAndAngle(Rotation):
    """A rotation axis and angle.

    Implementation of a rotation axis and angle and the corresponding
    arithmetic algorithms.

    This class can be thought of as capturing the NAIF routines RAXISA and
    AXISAR, with a few small differences.

    TODO: Add a description of the mathematical action of this class, and
    the non-symmetric nature of the inverse methods.

    Attributes
    ----------
    axis : VectorIJK, optional, default z-axis
        Axis about which the rotation is performed.
    angle : float, default 0
        Rotation angle in radians.
    """

    def __init__(self, *args):
        """Initialize a new AxisAndAngle object.

        Initialize a new AxisAndAngle object.

        Parameters
        ----------
        axis : VectorIJK
            Axis for rotation, not necessarily unit-length.
        angle : float
            Angle of rotation, in radians.

        Raises
        ------
        TypeError
            If incorrect parameters are provided.
        """
        if len(args) == 0:
            # Default rotation of 0 around z-axis.
            self.axis = VectorIJK(K)
            self.angle = 0.0
        elif len(args) == 2:
            (axis, angle) = args
            # Create an axis and angle rotation from the specified
            # rotation axis and angle.
            self.axis = VectorIJK(axis)
            self.angle = angle
        else:
            raise TypeError

    def getRotation(self, buffer):
        """Get the rotation matrix for this axis and angle.

        Put the rotation matrix for this axis and angle into the buffer.

        Parameters
        ----------
        buffer : PrivilegedRotationMatrixIJK
            Buffer to hold the rotation matrix.

        Returns
        -------
        buffer : RotationMatrixIJK
            Buffer holding the rotation matrix.
        """
        if self.angle == 0.0:
            buffer[...] = IDENTITY
        else:
            matrix = PrivilegedRotationMatrixIJK()
            vi = rotate(I, self.axis, self.angle)
            vj = rotate(J, self.axis, self.angle)
            vk = rotate(K, self.axis, self.angle)
            matrix.setToWithoutCheck(vi, vj, vk)
            buffer[:, :] = matrix
        return buffer
