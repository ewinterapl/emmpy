"""emmpy.crucible.core.math.vectorspace.unwritablevectorij"""


from math import asin, pi

from emmpy.crucible.core.exceptions.bugexception import BugException
from emmpy.crucible.core.exceptions.crucibleruntimeexception import (
    CrucibleRuntimeException
)
from emmpy.crucible.core.math.vectorspace.internaloperations import (
    computeNorm
)
from emmpy.utilities.doubletolongbits import doubleToLongBits
from emmpy.java.lang.unsupportedoperationexception import (
    UnsupportedOperationException
)
from emmpy.utilities.isrealnumber import isRealNumber


class UnwritableVectorIJ:
    """A weakly immutable 2-dimensional vector designed to properly support a
    writable subclass.

    Note: Subclass implementers, you should only use the protected fields in
    this class to store the contents of the vector components, otherwise all of
    the methods here and in the operations class may break.

    The basic data fields on this class are marked as protected to allow direct
    access to them through subclassing. This will get around any performance
    issues that one may have in using this vector arithmetic toolkit due to the
    enforcement of access to the component values through accessor methods.

    Note, the equals and hashcode implementations in this class support proper
    comparisons between subclasses of this class and this class. The reason
    this works, is because by design the only member variables of this class
    live in the parent class. If one subclasses this class and defines
    additional members then this will most certainly break the implementation
    presented here.

    This was a simple copy and paste of the UnwritableVectorIJK class.

    author G.K.Stephens copy and extension of F.S.Turner
    """

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], list):
                # Constructs a vector from the first two elements of an array
                # of doubles.
                (data,) = args
                self.__init__(data[0], data[1])
            elif isinstance(args[0], UnwritableVectorIJ):
                # Copy constructor, creates a vector by copying the values of a
                # pre-existing one.
                (vector,) = args
                self.__init__(vector.i, vector.j)
            else:
                raise CrucibleRuntimeException
        elif len(args) == 2:
            if isRealNumber(args[0]) and isRealNumber(args[1]):
                # Basic 2-element constructor
                (i, j) = args
                # The ith component of the vector, synonymous with the X-axis.
                self.i = i
                # The jth component of the vector, synonymous with the Y-axis.
                self.j = j
            elif isinstance(args[0], int) and isinstance(args[1], list):
                # Constructs a vector from the two elements of an array of
                # double starting with the offset index.
                (offset, data) = args
                self.__init__(data[offset], data[offset + 1])
            elif (isRealNumber(args[0]) and
                  isinstance(args[1], UnwritableVectorIJ)):
                # Scaling constructor, creates a new vector by applying a
                # scalar multiple to the components of a pre-existing vector.
                (scale, vector) = args
                self.__init__(scale*vector.i, scale*vector.j)
            else:
                raise CrucibleRuntimeException
        else:
            raise CrucibleRuntimeException

    def createUnitized(self):
        """Creates a new, unit length copy of the existing vector.

        This code is just a convenience method that implements:
        new UnwritableVectorIJK(1.0/this.getLength(), this)
        in a safe manner.

        @return a vector of unit length in the direction of the instance
        @throws UnsupportedOperationException if the instance vector has zero
        length.
        """
        norm = self.getLength()
        if norm > 0.0:
            return UnwritableVectorIJ(1.0/norm, self)
        raise UnsupportedOperationException(
            "Unable to unitize. Supplied vector has zero length.")

    def createNegated(self):
        """Creates a new, negated copy of an the existing vector.

        Convenience method for: new UnwritableVectorIJK(-1.0, this).

        @return the negated vector, -this.
        """
        return UnwritableVectorIJ(-1, self)

    def getI(self) -> float:
        """Gets the ith component.

        @return the ith component.
        """
        return self.i

    def getJ(self) -> float:
        """Gets the jth component.

        @return the jth component.
        """
        return self.j

    def get(self, index: int) -> float:
        """Get the specified component of the vector.

        @param index the index of the component to retrieve. 0 = ith, 1 = jth.
        @return the value from the requested component
        @throws IndexOutOfBoundsException if an invalid index, outside the
        range [0,1], is specified.
        """
        if index == 0:
            return self.i
        elif index == 1:
            return self.j
        else:
            raise BugException

    def getLength(self) -> float:
        """Computes the standard L-2 norm, or length, of the vector.

         @return (i*i + j*j + k*k)^(1/2) without danger of overflow.
         """
        return computeNorm(self.i, self.j)

    def getDot(self, vector) -> float:
        """Compute the dot product of this instance with another vector.

        @param vector the vector to dot against the instance.
        @return i*vector.i + j*vector.j + k*vector.k
        """
        return self.i*vector.i + self.j*vector.j

    def getSeparation(self, vector) -> float:
        """Compute the angular separation in radians between this instance and
        another vector.

        @param vector
        @return the angular separation between vector and this instance in
        radians.
        @throws UnsupportedOperationException if either this instance or the
        supplied vector are {@link VectorIJ#ZERO}
        """
        thisNorm = self.getLength()
        vectorNorm = vector.getLength()
        if thisNorm == 0.0:
            raise UnsupportedOperationException(
                "Unable to compute angular separation. " +
                "This vector is the zero vector.")
        elif (vectorNorm == 0.0):
            raise UnsupportedOperationException(
                "Unable to compute angular separation. " +
                "The argument supplied is the zero vector.")
        dotProduct = self.getDot(vector)
        if dotProduct > 0:
            x = self.i/thisNorm - vector.i/vectorNorm
            y = self.j/thisNorm - vector.j/vectorNorm
            return 2.0*asin(0.5*computeNorm(x, y))
        elif dotProduct < 0:
            x = self.i/thisNorm + vector.i/vectorNorm
            y = self.j/thisNorm + vector.j/vectorNorm
            return pi - 2*asin(0.5*computeNorm(x, y))
        return pi/2

    @staticmethod
    def copyOf(vector):
        """Makes an unwritable copy of the supplied vector.

        This method makes an unwritable copy only if necessary. It tries to
        avoid making a copy wherever possible.

        @param vector a vector to copy.
        @return either a reference to vector (if vector is already only an
        instance of {@link UnwritableVectorIJ}, otherwise an unwritable copy
        of vector's contents
        """
        if isinstance(vector, UnwritableVectorIJ):
            return vector
        return UnwritableVectorIJ(vector)

    def hashCode(self) -> int:
        prime = 31
        result = 1
        temp = doubleToLongBits(self.i)
        result = prime*result + temp ^ (temp >> 32)
        temp = doubleToLongBits(self.j)
        result = prime*result + temp ^ (temp >> 32)
        return result

    def equals(self, obj) -> bool:
        if self is obj:
            return True
        if obj is None:
            return False
        if not isinstance(obj, UnwritableVectorIJ):
            return False
        other = obj
        if doubleToLongBits(self.i) != doubleToLongBits(other.i):
            return False
        if doubleToLongBits(self.j) != doubleToLongBits(other.j):
            return False
        return True

    def toString(self) -> str:
        return "[%s,%s]" % (self.i, self.j)
