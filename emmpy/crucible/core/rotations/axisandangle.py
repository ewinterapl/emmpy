"""A rotation axis and angle."""


from math import atan2, pi

from emmpy.crucible.core.math.vectorspace.vectorijk import (
    I, J, K, VectorIJK
)
from emmpy.crucible.core.math.vectorspace.rotationmatrixijk import (
    RotationMatrixIJK
)
from emmpy.crucible.core.math.vectorspace.unwritablerotationmatrixijk import (
    UnwritableRotationMatrixIJK
)
from emmpy.crucible.core.rotations.privilegedrotationmatrixijk import (
    PrivilegedRotationMatrixIJK
)
from emmpy.crucible.core.rotations.quaternion import Quaternion
from emmpy.crucible.core.rotations.rotation import Rotation
from emmpy.utilities.doubletolongbits import doubleToLongBits


class AxisAndAngle(Rotation):
    """A rotation axis and angle.

    Implementation of a rotation axis and angle and the corresponding
    arithmetic algorithms.

    This class can be thought of as capturing the NAIF routines RAXISA and
    AXISAR, with a few small differences.

    TODO: Add a description of the mathematical action of this class, and the
    non-symmetric nature of the inverse methods.

    author F.S.Turner
    """

    def __init__(self, *args):
        """Build a new object."""
        if len(args) == 0:
            # Create the default axis and angle rotation representation, a
            # rotation of zero radians about K.

            # Axis of rotation, should always be a unit length vector.
            self.axis = VectorIJK(K)

            # Angle of rotation, specified in radians.
            self.angle = 0.0
        elif len(args) == 1:
            if isinstance(args[0], UnwritableRotationMatrixIJK):
                (matrix,) = args
                # Create an axis and angle rotation from the specified rotation
                # matrix.
                # In the event the identity matrix is supplied, this method
                # will set the axis to K and the angle to zero.
                # param matrix a rotation matrix to convert to axis and angle
                # representation.
                self.setTo(matrix)
            elif isinstance(args[0], AxisAndAngle):
                (axisAndAngle,) = args
                # Create a copy of the supplied axis and angle instance.
                # param axisAndAngle the instance whose contents are to be
                # copied
                self.setTo(axisAndAngle)
            else:
                raise Exception
        elif len(args) == 2:
            (axis, angle) = args
            # Create an axis and angle rotation from the specified rotation
            # axis and angle.
            # param axis any vector whose length is strictly greater than zero.
            # param angle the rotation angle specified in radians.
            # throws UnsupportedOperationException if the length of axis is
            # zero.
            self.__init__()
            self.setTo(axis, angle)
        elif len(args) == 4:
            (axisi, axisj, axisk, angle) = args
            # Create an axis and angle rotation from the supplied vector
            # components and angle.
            # param axisi the ith component of the potentially non-unit
            # rotation axis
            # param axisj the jth component of the potentially non-unit
            # rotation axis
            # param axisk the kth component of the potentially non-unit
            # rotation axis
            # param angle the rotation angle in radians
            # throws UnsupportedOperationException if the axis components are
            # all identically zero.
            self.setTo(axisi, axisj, axisk, angle)
        else:
            raise Exception

    def getAxis(self, *args):
        """Retrieve the rotation axis."""
        if len(args) == 0:
            # There really is no difference between this method and the get
            # method with the buffer argument, except that this method does
            # not perform a copy.
            # return a reference to the internally held rotation axis.
            return self.axis
        elif len(args) == 1:
            (buffer,) = args
            # Retrieve a copy of the unit-length rotation axis.
            # param buffer a buffer to receive the rotation axis.
            # return a reference to buffer for convenience.
            return buffer.setTo(self.axis)
        else:
            raise Exception

    def getAngle(self):
        """Get the rotation angle.

        return the rotation angle expressed in radians
        """
        return self.angle

    def setAxis(self, axis):
        """Set the rotation axis.

        param axis the non-zero length axis of rotation.
        throws UnsupportedOperationException if axis has length zero.
        """
        self.axis.setTo(axis).unitize()

    def setAngle(self, angle):
        """Set the rotation angle.

        param angle the rotation angle specified in radians.
        """
        self.angle = angle

    def setTo(self, *args):
        """Set the axis and angle."""
        if len(args) == 1:
            if isinstance(args[0], AxisAndAngle):
                (axisAndAngle,) = args
                # Copy the contents of the supplied axis and angle into the
                # instance.
                # param axisAndAngle the axis and angle whose contents are to
                # be copied.
                # return a reference to the instance for convenience.
                self.axis.setTo(axisAndAngle.axis)
                self.angle = axisAndAngle.angle
                return self
            elif isinstance(args[0], UnwritableRotationMatrixIJK):
                (matrix,) = args
                # In the event that the identity matrix is supplied to this
                # method, the axis is selected to be VectorIJK.K with a
                # rotation angle of zero by convention. This is done to
                # preserve the integrity of the instance under configuration
                # and to prevent the handling of unnecessary unchecked
                # exceptions.
                q = Quaternion()
                # First convert the supplied matrix to a quaternion.
                q.setTo(matrix)
                q.getVector(self.axis)
                # Handle the identity rotation case. By convention, all
                # rotations that are identity rotations have their axis as
                # VectorIJK.K.
                if self.axis.getLength() == 0.0:
                    self.angle = 0
                    self.axis.setTo(VectorIJK.K)
                    return self
                # Now handle the case when the rotation magnitude is Pi.
                scalar = q.getScalar()
                # There is no need to set the axis, as we already retrieved it
                # with the q.getVector() method above--since the scalar
                # component is 0.0.
                if scalar == 0.0:
                    self.angle = pi
                    return self
                self.angle = 2*atan2(self.axis.getLength(), scalar)
                self.axis.unitize()
                return self
            else:
                raise Exception
        elif len(args) == 2:
            (axis, angle) = args
            # Simultaneously set the axis and angle.
            # param axis the non-zero length rotation axis.
            # param angle a rotation angle specified in radians.
            # return a reference to the instance for convenience.
            # throws UnsupportedOperationException if the supplied axis is of
            # zero length.
            self.axis.setTo(axis).unitize()
            self.angle = angle
            return self
        elif len(args) == 4:
            (axisi, axisj, axisk, angle) = args
            # Set the axis and angle to the supplied axis components and angle.
            # param axisi the ith component of a potentially non-unit length
            # axis
            # param axisj the jth component of a potentially non-unit length
            # axis
            # param axisk the kth component of a potentially non-unit length
            # axis
            # param angle the angle of rotation specified in radians
            # return a reference to the instance for convenience
            # throws UnsupportedOperationException if the supplied axis
            # components are all identially zero.
            self.axis.setTo(axisi, axisj, axisk).unitize()
            self.angle = angle
            return self
        else:
            raise Exception

    def getRotation(self, buffer):
        """Get the rotation matrix."""
        if self.angle == 0.0:
            buffer.setTo(RotationMatrixIJK.IDENTITY)
            return buffer
        assigner = PrivilegedRotationMatrixIJK()
        vi = VectorIJK.rotate(I, self.axis, self.angle)
        vj = VectorIJK.rotate(J, self.axis, self.angle)
        vk = VectorIJK.rotate(K, self.axis, self.angle)
        assigner.setToWithoutCheck(vi, vj, vk)
        buffer.setTo(assigner)
        return buffer
