"""emmpy.crucible.crust.surfaces.unwritableplane"""


from math import sqrt

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.java.lang.double import Double
from emmpy.java.lang.illegalargumentexception import IllegalArgumentException


class UnwritablePlane:
    """A weakly immutable 3-dimensional plane designed to properly support a
    writable subclass.

    This class captures a canonical representation of a plane in 3-dimensions.
    It supports a variety of representations:

    * Normal vector and constant: < x, normal > = constant
    * Normal vector and point: < x - point, normal > = 0
    * Point and spanning vectors: point + s*u + t*v

    @author F.S.Turner
    """

    PLANE_CONTAINMENT_TOLERANCE = 5e-14
    INVERSE_PROJECTION_BOUND = 10.0

    def __init__(self, *args):
        """Constructor

        A plane can be defined by the expression:
           < x, normal > = constant
        where <,> denotes the inner product, and x an arbitrary point
        in the plane.

        OR

        point + s * u + t * v

        where s and t are real numbers, u and v are the linearly independent
        spanning vectors, and point is an arbitrary point in the plane of
        interest.
        """
        if len(args) == 0:
            # Private constructor that builds a default plane.
            # This is only to be utilized within the constructors that exist on
            # this class.
            # The unit normal that points from the origin to the point closest
            # in the plane.
            self.theNormal = VectorIJK(VectorIJK.K)
            # Package private accessible read-only view of the actual normal
            # vector.
            self.normal = self.theNormal
            # The plane constant. In the canonical form this is always non-
            # negative and captures the minimum distance to the plane from
            # the origin.
            self.constant = 0
        elif len(args) == 1:
            # Copy constructor.
            # param plane creates a new plane, copying the contents of the
            # supplied plane.
            (plane,) = args
            self.__init__()
            self.setTo(plane)
        elif len(args) == 2:
            if isinstance(args[1], float):
                # Constructs a plane from the supplied normal vector and
                # constant.
                # param normal the normal vector
                # param constant the constant
                # throws IllegalArgumentException if normal is zero length.
                (normal, constant) = args
                self.__init__()
                self.setTo(normal, constant)
            elif isinstance(args[1], UnwritableVectorIJK):
                # Constructs a plane from the supplied normal vector and
                # constant.
                # param normal the normal vector
                # param constant the constant
                # throws IllegalArgumentException if normal is zero length.
                (normal, point) = args
                self.__init__()
                self.setTo(normal, point)
            else:
                raise Exception
        elif len(args) == 3:
            # Constructs a plane from the supplied point and two spanning
            # vectors.
            # param point an arbitrary point in the plane
            # param u one of the two linearly independent spanning vectors
            # param v the other of the spanning vectors
            # throws IllegalArgumentException if u and v are parallel
            (point, u, v) = args
            self.__init__()
            self.setTo(point, u, v)
        else:
            raise Exception

    @staticmethod
    def copyOf(plane):
        if isinstance(plane, UnwritablePlane):
            return plane
        return UnwritablePlane(plane)

    def getNormal(self, *args):
        if len(args) == 0:
            # Convenience method that creates a new vector and sets it to the
            # unit normal to the plane.
            # return the newly created unit normal vector
            return self.getNormal(VectorIJK())
        elif len(args) == 1:
            (buffer,) = args
            # Retrieves the unit normal vector.
            # param buffer the buffer to receive the normal.
            # return a reference to buffer for convenience.
            return buffer.setTo(self.theNormal)
        else:
            raise Exception

    def getConstant(self):
        """Retrieves the plane constant.

        return the constant, also the distance of the plane from the origin.
        """
        return self.constant

    def getPoint(self, *args):
        if len(args) == 0:
            # Convenience method that creates a new vector and assigns it to
            # the point in the plane.
            # return the newly created vector capturing the point in the plane
            # closest to the origin
            return self.getPoint(VectorIJK())
        elif len(args) == 1:
            (buffer,) = args
            # Retrieves a point in the plane.
            # param buffer the buffer to receive the point in the plane.
            # return the closest point in the plane to the origin. Point is
            # always a non-negative multiple of normal.
            return buffer.setTo(self.theNormal).scale(self.constant)
        else:
            raise Exception

    def getSpanningVectors(self, uBuffer, vBuffer):
        """Retrieves a pair of vectors that span the plane.

        param uBuffer one of two orthonormal vectors that span the plane
        param vBuffer the other of two orthonormal vectors that span the plane
        """
        a = self.theNormal.getI()*self.theNormal.getI()
        b = self.theNormal.getJ()*self.theNormal.getJ()
        c = self.theNormal.getK()*self.theNormal.getK()

        # This is a bit complicated. Determine the component of the normal that
        # has the smallest magnitude. This component with then arbitrarily be
        # selected to be zero in uBuffer, the first of the two spanning
        # vectors.
        # The other two components of the normal will be put into uBuffer,
        # swapped with the sign of the first changed. From this selection,
        # vBuffer can have only one possible set of values which it obtains
        # from the smallest component of the normal, the non-zero components
        # of uBuffer, and the length of uBuffer.
        f = None
        (s1, s2, s3) = (None, None, None)
        if a <= b and a <= c:
            # The i component of the normal vector is the smallest.
            f = sqrt(b + c)
            s1 = 0
            s2 = 1
            s3 = 2
        elif b <= a and b <= c:
            # The j component of the normal is the smallest.
            f = sqrt(a + c)
            s1 = 1
            s2 = 2
            s3 = 0
        else:
            # The k component of the normal is the smallest.
            f = sqrt(a + b)
            s1 = 2
            s2 = 0
            s3 = 1
        uBuffer.set(s1, 0.0)
        uBuffer.set(s2, -self.theNormal.get(s3)/f)
        uBuffer.set(s3, self.theNormal.get(s2)/f)
        vBuffer.set(s1, f)
        vBuffer.set(s2, -self.theNormal.get(s1)*uBuffer.get(s3))
        vBuffer.set(s3, self.theNormal.get(s1)*uBuffer.get(s2))

    def canonicalizeIfConstantNegative(self):
        """Canonicalize the internal representation such that the constant is
        the distance from the origin to the plane."""
        if self.constant < 0.0:
            self.constant = -self.constant
            self.theNormal.negate()

    def setTo(self, *args):
        if len(args) == 1:
            (plane,) = args
            # Canonical method for copying the contents of one plane into
            # another.
            # param plane the plane to copy
            # return a reference to the instance for convenience
            self.constant = plane.constant
            self.theNormal.setTo(plane.theNormal)
            return self
        elif len(args) == 2:
            if isinstance(args[1], float):
                (normal, constant) = args
                # Canonical method for setting the contents of a plane to a
                # normal vector and a constant.
                # A plane can be defined by the expression:
                #    < x, normal > = constant
                # where <,> denotes the inner product, and x an arbitrary point
                # in the plane.
                # Setters do not typically belong on the unwritable parent
                # classes in the weak immutability pattern Writable. In this
                # particular case, these package private methods allow the
                # convenient consolidation of code.
                # param normal the normal vector in the plane definition above
                # param constant the constant in the plane definition above
                # return a reference to the instance for convenience
                # throws IllegalArgumentException if normal is zero length.
                normalLength = normal.getLength()
                Preconditions.checkArgument(
                    normalLength != 0,
                    "A plane's normal vector must be non-zero."
                )
                self.constant = constant/normalLength
                self.theNormal.setTo(1/normalLength, normal)
                self.canonicalizeIfConstantNegative()
                return self
            elif isinstance(args[1], UnwritableVectorIJK):
                (normal, point) = args
                # Canonical method for setting the contents of a plane to a
                # normal vector and a point.
                # A plane can be defined by the expression:
                #    < x - point, normal > = 0
                # where <,> denotes the inner product, and x an arbitrary point
                # in the plane.
                # Setters do not typically belong on the unwritable parent
                # classes in the weak immutability pattern Writable. In this
                # particular case, these package private methods allow the
                # convenient consolidation of code.
                # param normal the normal vector in the plane definition above
                # param point a point in the plane
                # *return a reference to the instance for convenience
                # throws IllegalArgumentException if normal is zero length
                self.checkArgument(
                    not VectorIJK.ZERO.equals(normal),
                    "A plane's normal must be non-zero."
                )
                self.theNormal.setTo(normal).unitize()
                self.constant = point.getDot(self.theNormal)
                self.canonicalizeIfConstantNegative()
                return self
            else:
                raise Exception
        elif len(args) == 3:
            (point, u, v) = args
            # Canonical method for setting the contents of a plane to a point
            # and a pair of spanning vectors.
            # A plane can be defined by the expression:
            #   point + s * u + t * v
            # where s and t are real numbers, u and v are the linearly
            # independent spanning vectors, and point is an arbitrary point in
            # the plane of interest.
            # Setters do not typically belong on the unwritable parent classes
            # in the weak immutability pattern Writable. In this particular
            # case, these package private methods allow the convenient
            # consolidation of code.
            # param point the arbitrary point in the plane
            # param u one of the two linearly independent spanning vectors
            # param v the other of the two linearly independent spanning
            # ectors
            # return a reference to the instance for convenience
            # throws IllegalArgumentException if u and v are linearly dependent

            # This is a bit convoluted. We are going to allow the normal
            # vector field to be modified in order to verify that u and v are
            # linearly independent. If they are found to be dependent, we'll
            # restore the normal vector before returning. This may be
            # unexpected behavior, but we're going out of our way to preserve
            # the prior state.
            i = self.theNormal.getI()
            j = self.theNormal.getJ()
            k = self.theNormal.getK()
            VectorIJK.uCross(u, v, self.theNormal)
            if VectorIJK.ZERO.equals(self.theNormal):
                self.theNormal.setTo(i, j, k)
                raise IllegalArgumentException(
                    "Spanning vectors are parallel."
                )

            # Determine the constant corresponding to the unit normal vector.
            self.constant = self.theNormal.getDot(point)
            self.canonicalizeIfConstantNegative()
            return self
        else:
            raise Exception

    def projectOnto(self, *args):
        if len(args) == 1:
            (vector,) = args
            return self.projectOnto(vector, VectorIJK())
        elif len(args) == 2:
            (vector, buffer) = args
            return VectorIJK.combine(
                1.0, vector, self.constant - vector.getDot(self.theNormal),
                self.theNormal, buffer
            )
        else:
            raise Exception

    def inverseProjectOnto(self, *args):
        if len(args) == 2:
            pass
            (vector, inversePlane) = args
            self.inverseProjectOnto(vector, inversePlane, VectorIJK())
        elif len(args) == 3:
            (vector, inversePlane, buffer) = args
            # Computes the inverse projection of a vector onto the plane.
            # param vector the vector that lies in the instance plane
            # param inversePlane the plane from which the vector originated
            # under projection
            # param buffer the buffer to receive the inverse image of vector
            # under the projection from inversePlane. The result captured here
            # lies in inversePlane such that inversePlane.projectOnto(buffer)
            # yields vector.
            # return a reference to buffer for convenience
            # throws IllegalArgumentException if the computation can not
            # proceed reliably due to numerical considerations. Typically this
            # happens if the instance and inversePlane are sufficiently close
            # to orthogonal to one another.
            numerator = (
                inversePlane.constant - vector.getDot(inversePlane.normal)
            )
            denominator = self.normal.getDot(inversePlane.normal)
            limit = None
            if abs(numerator) < 1:
                limit = (
                    UnwritablePlane.INVERSE_PROJECTION_BOUND/Double.MAX_VALUE
                )
            else:
                limit = (
                    abs(UnwritablePlane.INVERSE_PROJECTION_BOUND /
                        Double.MAX_VALUE) *
                    numerator
                )
                Preconditions.checkArgument(
                    abs(denominator) > limit,
                    "Unable to compute inverse projection."
                )
                return VectorIJK.combine(
                    1.0, vector, numerator/denominator, self.normal, buffer
                )
        else:
            raise Exception

    def contains(self, *args):
        if len(args) == 1:
            (vector,) = args
            # Determines if the supplied vector is contained in the plane
            # subject to a sufficiently tight tolerance.
            return self.contains(
                vector, UnwritablePlane.PLANE_CONTAINMENT_TOLERANCE
            )
        elif len(args) == 2:
            (vector, tolerance) = args
            # throws IllegalArgumentException if tolerance is not strictly
            # positive
            Preconditions.checkArgument(
                tolerance > 0, "Tolerance must be strictly positive"
            )
            vectorConstant = vector.getDot(self.normal)
            if vectorConstant == self.constant:
                return True
            if self.constant*vectorConstant == 0:
                return abs(self.constant - vectorConstant) < tolerance
            return (
                abs(self.constant - vectorConstant) /
                (abs(vectorConstant) + abs(self.constant))
            ) < tolerance
        else:
            raise Exception

    def directedDistanceTo(self, point):
        """Computes the directed distance from a point to the plane.

        The sign of this value is positive if the point is directed along the
        normal of the plane, and negative if it is directed against the normal.

        The shortest distance from the plane to the plane is the length of the
        vector perpendicular to the plane that passes through the point, thus
        is parallel or anti-parallel to the normal of the plane.

        param point an {@link UnwritableVectorIJK} representing a point
        return the directed distance from the plane to the point, the sign is
        positive if along normal
        """
        i = point.getI()
        j = point.getJ()
        k = point.getK()

        # scale all the components by the 1/maxSize to make all the distances
        # of the same order, so that when the sum is computed, it minimizes
        # rounding errors
        maxSize = max(abs(i), abs(j), abs(k), abs(self.constant))
        if maxSize == 0:
            return 0.0

        # scale the values
        vi = i/maxSize
        vj = j/maxSize
        vk = k/maxSize
        c = self.constant/maxSize

        # undo the scaling
        return (
            (vi*self.normal.getI() + vj*self.normal.getJ() +
             vk*self.normal.getK() - c)*maxSize
        )

    def hashCode(self):
        prime = 31
        result = 1
        temp = Double.doubleToLongBits(self.constant)
        result = prime*result + temp ^ (temp >> 32)
        result = prime*result
        if self.theNormal is not None:
            result += self.theNormal.hashCode()
        return result

    def equals(self, obj):
        if self is obj:
            return True
        if obj is None:
            return False
        if not isinstance(obj, UnwritablePlane):
            return False
        other = obj
        if (Double.doubleToLongBits(self.constant) !=
            Double.doubleToLongBits(other.constant)):
            return False
        if self.theNormal is None:
            if other.theNormal is not None:
                return False
        elif not self.theNormal.equals(other.theNormal):
            return False
        return True

    def toString(self):
        return (
            "UnwritablePlane [constant %s, normal %s]" %
            (self.constant, self.normal.toString())
        )
