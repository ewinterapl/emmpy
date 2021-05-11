"""emmpy.crucible.crust.surfaces.unwritableellipse"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.matrixij import MatrixIJ
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.crust.surfaces.ellipsetype import EllipseType
from emmpy.crucible.crust.surfaces.plane import Plane


class UnwritableEllipse:
    """Unmodifiable parent class of the mutable ellipse class.

    This class handles degeneracy, in that it directly supports ellipses that
    are collapsed to a line segment (1D) or point (0D).

    author F.S.Turner
    """

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 0:
            # Creates the default ellipse.
            # This constructor is only to be utilized internally, and is
            # exposed at the package level only to allow the writable sub-class
            # to access it for performance reasons. (The alternate constructor
            # is expensive to invoke.)
            self.theCenter = VectorIJK()
            self.theSmajor = VectorIJK(VectorIJK.I)
            self.theSminor = VectorIJK(VectorIJK.J)
            # Unmodifiable views exposed to the sub-class.
            self.center = self.theCenter
            self.smajor = self.theSmajor
            self.sminor = self.theSminor
            # Field referencing the sub-type of ellipse.
            self.type = EllipseType.ELLIPSE
        elif len(args) == 1:
            (ellipse,) = args
            self.__init__()
            self.setTo(ellipse)
        elif len(args) == 3:
            (center, u, v) = args
            # Creates an unwritable ellipse from the center and two generating
            # vectors.
            # param center the vector to the center of the ellipse
            # param u a generating vector, may be zero.
            # param v another generating vector, v may be parallel to u.
            self.__init__()
            self.setTo(center, u, v)
        else:
            raise Exception

    def copyOf(self, ellipse):
        if isinstance(ellipse, UnwritableEllipse):
            return ellipse
        result = UnwritableEllipse()
        result.setTo(ellipse)
        return result

    def getCenter(self, *args):
        if len(args) == 0:
            # Creates a copy of the center vector.
            # return a newly created vector containing the center of the
            # ellipse
            return self.getCenter(VectorIJK())
        elif len(args) == 1:
            (buffer,) = args
            # Retrieves the center vector.
            # param buffer the buffer to receive the center.
            # return a reference to buffer for convenience.
            return buffer.setTo(self.theCenter)
        else:
            raise Exception

    def getSemiMajorAxis(self, *args):
        if len(args) == 0:
            # Creates a copy of the semi-major axis.
            # return a newly created vector containing the semi-major axis of
            # the ellipse
            return self.getSemiMajorAxis(VectorIJK())
        elif len(args) == 1:
            (buffer,) = args
            # Retrieves the semi-major axis vector.
            # param buffer the buffer to receive the semi-major axis.
            # return a reference to buffer for convenience
            return buffer.setTo(self.theSmajor)
        else:
            raise Exception

    def getSemiMinorAxis(self, *args):
        if len(args) == 0:
            # Creates a copy of the semi-minor axis.
            # return a newly created vector containing the semi-minor axis of
            # the ellipse
            return self.getSemiMinorAxis(VectorIJK())
        elif len(args) == 1:
            (buffer,) = args
            # Retrieves the semi-minor axis vector.
            # param buffer the buffer to receive the semi-minor axis.
            # return a reference to buffer for convenience
            return buffer.setTo(self.theSminor)
        else:
            raise Exception

    def getType(self):
        """Get the type of the ellipse.

        return the associated type enumeration
        """
        return self.type

    def isDegenerate(self):
        """Is the ellipse degenerate, not fully 2D?

        return true if degenerate, false otherwise
        """
        return EllipseType.isDegenerate(self.type)

    def isCircular(self):
        """Is the ellipse precisely a circle?

        return true if the semi-major and semi-minor axis
        """
        if self.type == EllipseType.POINT:
            return True
        return self.smajor.getLength() == self.sminor.getLength()

    def isContainedWithin(self, plane):
        """Is the ellipse contained completely within the plane?

        This method exists to allow for checking if infinite intersections
        between the ellipse and the plane exist. Invoking
        UnwritableEllipse.intersect(UnwritablePlane, VectorIJK, VectorIJK)
        in this case will result in the generation of a runtime exception.

        param plane the plane to test for containment
        return true if ellipse is contained completely within plane, false
        otherwise
        """
        return EllipseType.isContainedWithin(self, plane)

    def intersects(self, plane):
        """Does the ellipse intersect the plane?

        This method exists to allow for checking ahead of time if the ellipse
        intersects the plane. Invoking
        UnwritableEllipse#intersect(UnwritablePlane, VectorIJK, VectorIJK) will
        result in a runtime exception if no exceptions exist.

        param plane the plane to test for intersection
        return true if ellipse intersects plane, false otherwise
        """
        return EllipseType.intersects(self, plane)

    def intersect(self, plane, bufferOne, bufferTwo):
        """Compute the intersection of the ellipse with a plane.

        param plane the plane with which to compute the intersection
        param bufferOne a buffer to capture the first point of intersection
        param bufferTwo another buffer to capture the second point of
        intersection
        throws IllegalArgumentException if not intersection occurs, or if the
        two vector buffers are not sufficient to capture all possible
        intersection points. In general the latter case is triggered if the
        ellipse is anything but a point, and entirely contained within the
        plane.
        """
        EllipseType.intersect(self, plane, bufferOne, bufferTwo)

    def getPlane(self, *args):
        if len(args) == 0:
            return self.getPlane(Plane())
        elif len(args) == 1:
            (buffer,) = args
            Preconditions.checkArgument(
                self.type == EllipseType.ELLIPSE,
                "Only non-degenerate ellipses can be turned into a plane."
            )
            buffer.setTo(self.center, self.smajor, self.sminor)
            return buffer

    def setTo(self, *args):
        if len(args) == 1:
            (ellipse,) = args
            # Package private method to safely configure the instance to
            # that of another ellipse.
            # param ellipse the ellipse to copy
            # return a reference to the instance
            self.theCenter.setTo(ellipse.theCenter)
            self.theSmajor.setTo(ellipse.theSmajor)
            self.theSminor.setTo(ellipse.theSminor)
            self.type = ellipse.type
            return self
        elif len(args) == 3:
            (center, u, v) = args
            # Package private method used to configure the internals of the
            # ellipse to the center and supplied generating vectors.
            # param center the center of the ellipse
            # param u a generating vector (possibly VectorIJK.ZERO)
            # param v another generating vector (possibly VectorIJK.ZERO,
            # or parallel to u)
            # return a reference to the instance
            self.theCenter.setTo(center)
            matrix = MatrixIJ()
            values = VectorIJ()
            tmp = VectorIJK()
            scale = max(u.getLength(), v.getLength())

            # This is an exceptional case representing a single point in
            # space.
            if scale == 0.0:
                self.theSmajor.setTo(VectorIJK.ZERO)
                self.theSminor.setTo(VectorIJK.ZERO)
                self.type = EllipseType.POINT
                return self

            self.theSmajor.setTo(u).scale(1.0/scale)
            self.theSminor.setTo(v).scale(1.0/scale)
            offDiagonals = self.theSmajor.getDot(self.theSminor)
            matrix.setTo(
                self.theSmajor.getDot(self.theSmajor),
                offDiagonals, offDiagonals,
                self.theSminor.getDot(self.theSminor)
            )

            # Diagonalize matrix.
            MatrixIJ.diagonalizeSymmetricMatrix(matrix, values, matrix)

            # Compute the semi-axes.
            (major, minor) = (None, None)
            if abs(values.getI()) >= abs(values.getJ()):
                # The first eigenvector corresponds to the semi-major axes.
                major = 0
                minor = 1
            else:
                # The second eigenvector corresponds to the semi-major
                # axis.
                major = 1
                minor = 0

            VectorIJK.combine(
                matrix.get(0, major), self.theSmajor, matrix.get(1, major),
                self.theSminor, tmp
            )
            VectorIJK.combine(
                matrix.get(0, minor), self.theSmajor, matrix.get(1, minor),
                self.theSminor, self.theSminor
            )
            self.theSmajor.setTo(tmp)

            # Restore the scaling.
            self.theSmajor.scale(scale)
            self.theSminor.scale(scale)
            self.type = self.determineType(self)
            return self
        else:
            raise Exception

    def determineType(self):
        """Simple method that encapsulates the type selection logic by
        interrogating the existing fields on the class.

        return the appropriate instance of type.
        """
        if self.sminor.equals(VectorIJK.ZERO):
            # We have a degenerate case, determine which flavor:
            if self.smajor.equals(VectorIJK.ZERO):
                return EllipseType.POINT
            return EllipseType.LINE_SEGMENT
        return EllipseType.ELLIPSE

    def rotate(self, rotation):
        rotation.mxv(self.theCenter, self.theCenter)
        rotation.mxv(self.theSmajor, self.theSmajor)
        rotation.mxv(self.theSminor, self.theSminor)
        return self

    def offset(self, offset):
        VectorIJK.add(self.theCenter, offset, self.theCenter)
        return self

    def scale(self, scale):
        Preconditions.checkArgument(
            scale >= 0.0,
            "Only positive scalings may be applied to an ellipse."
        )
        self.theCenter.scale(scale)
        self.theSmajor.scale(scale)
        self.theSminor.scale(scale)
        self.type = self.determineType()

    def toString(self):
        return (
            "UnwritableEllipse [center %s, smajor %s, sminor %s]" %
            (self.center, self.smajor.toString(), self.sminor.toString())
        )

    def hashCode(self):
        prime = 31
        result = 1
        result = prime*result
        if self.center is not None:
            result += self.center.hashCode()
        result = prime*result
        if self.smajor is not None:
            result += self.smajor.hashCode()
        result = prime*result
        if self.sminor is not None:
            result += self.sminor.hashCode()
        result = prime*result
        if self.type is not None:
            result += self.type
        return result

    def equals(self, obj):
        if self is obj:
            return True
        if obj is None:
            return False
        if not isinstance(obj, UnwritableEllipse):
            return False
        other = obj
        if self.center is None:
            if other.center is not None:
                return False
        elif not self.center.equals(other.center):
            return False
        if self.smajor is None:
            if other.smajor is not None:
                return False
        elif not self.smajor.equals(other.smajor):
            return False
        if self.sminor is None:
            if other.sminor is not None:
                return False
        elif not self.sminor.equals(other.sminor):
            return False
        if self.type != other.type:
            return False
        return True
