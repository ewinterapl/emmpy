"""emmpy.crucible.core.math.vectorspace.unwritablevectorijk

A weakly immutable 3-dimensional vector designed to properly support a writable
subclass.

Note: Subclass implementers, you should only use the protected fields in this
class to store the contents of the vector components, otherwise all of the
methods here and in the operations class may break.

The basic data fields on this class are marked as protected to allow direct
access to them through subclassing. This will get around any performance issues
that one may have in using this vector arithmetic toolkit due to the
enforcement of access to the component values through accessor methods.

Note, the equals and hashcode implementations in this class support proper
comparisons between subclasses of this class and this class. The reason this
works, is because by design the only member variables of this class live in the
parent class. If one subclasses this class and defines additional members then
this will most certainly break the implementation presented here.

@author F.S.Turner
"""

from math import asin, pi

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    computeNorm
)
# from emmpy.java.lang.double import Double
# from emmpy.utilities.isrealnumber import isRealNumber


class UnwritableVectorIJK:

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], list):
                # Constructs a vector from the first three elements of an
                # array of doubles.
                # @aram data the array of doubles
                data = args[0]
                UnwritableVectorIJK.__init__(self, data[0], data[1], data[2])
    #         elif isinstance(args[0], UnwritableVectorIJK):
    #             # Copy constructor, creates a vector by copying the values of a
    #             # pre-existing one.
    #             # @param vector the vector whose contents are to be copied
    #             vector = args[0]
    #             self.__init__(vector.i, vector.j, vector.k)
            else:
                raise Exception
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], list):
                raise Exception
    #             # Constructs a vector from the three elements of an array of
    #             # double starting with the offset index.
    #             # @param offset index into the data array to copy into the ith
    #             # component.
    #             # @param data the array of doubles
    #             (offset, data) = args
    #             self.__init__(data[offset], data[offset + 1], data[offset + 2])
            elif isRealNumber(args[0]) and isinstance(args[1],
                                                      UnwritableVectorIJK):
                # Scaling constructor, creates a new vector by applying a
                # scalar multiple to the components of a pre-existing vector.
                # @param scale the scale factor to apply
                # @param vector the vector whose contents are to be scaled
                (scale, vector) = args
                self.__init__(scale*vector.i, scale*vector.j, scale*vector.k)
            else:
                raise Exception
        elif len(args) == 3:
            # Constructs a vector from the three basic components.
            # param i the ith component
            # param j the jth component
            # param k the kth component
            (i, j, k) = args
            # The ith component of the vector, synonymous with the X-axis
            self.i = i
            # The jth component of the vector, synonymous with the Y-axis
            self.j = j
            # The kth component of the vector, synonymous with the Z-axis
            self.k = k
        else:
            raise Exception

    # def createUnitized(self):
    #     """Creates a new, unit length copy of the existing vector.

    #     This code is just a convenience method that implements:
    #     new UnwritableVectorIJK(1.0/this.getLength(), this)  in a safe manner.

    #     @return a vector of unit length in the direction of the instance
    #     @throws UnsupportedOperationException if the instance vector has zero
    #     length.
    #     """
    #     norm = self.getLength()
    #     if norm > 0.0:
    #         return UnwritableVectorIJK(1.0/norm, self)
    #     raise Exception("Unable to unitize. Supplied vector has zero length.")

    # def createNegated(self):
    #     """Creates a new, negated copy of an the existing vector.

    #     Convenience method for: new UnwritableVectorIJK(-1.0, this).

    #     @return the negated vector, -this.
    #     """
    #     return UnwritableVectorIJK(-1, self)

    def createScaled(self, scale: float):
        """Creates a new, scaled copy of an the existing vector by applying a
        scalar multiple to the components.

        Convenience method for: new UnwritableVectorIJK(scale, this).

        param scale the scale factor to apply
        return the scaled vector, scale*this.
        """
        return UnwritableVectorIJK(scale, self)

    def getI(self):
        """Gets the ith component."""
        return self.i

    def getJ(self):
        """Gets the jth component."""
        return self.j

    def getK(self):
        """Gets the kth component."""
        return self.k

    # def get(self, index: int) -> float:
    #     """Retrieves the specified component of the vector.

    #     @param index the index of the component to retrieve. 0 = ith, 1 = jth,
    #     2 = kth.

    #     @return the value for the requested component

    #     @throws IndexOutOfBoundsException if an invalid index, outside the
    #     range [0,2], is specified.
    #     """
    #     if index == 0:
    #         return self.i
    #     elif index == 1:
    #         return self.j
    #     elif index == 2:
    #         return self.k
    #     else:
    #         raise Exception

    # def getLength(self) -> float:
    #     """Computes the standard L-2 norm, or length, of the vector.

    #     @return (i*i + j*j + k*k)^(1/2) without danger of overflow.
    #     """
    #     return computeNorm(self.i, self.j, self.k)

    # def getDot(self, vector) -> float:
    #     """Compute the dot product of this instance with another vector.

    #     @param vector the vector to dot against the instance.

    #     @return i*vector.i + j*vector.j + k*vector.k
    #     """
    #     return self.i*vector.i + self.j*vector.j + self.k*vector.k

    # def getSeparation(self, vector) -> float:
    #     """Compute the angular separation in radians between this instance and
    #     another vector.

    #     @param vector

    #     @return the angular separation between vector and this instance in
    #     radians.

    #     @throws UnsupportedOperationException if either this instance or the
    #     supplied vector are {@link VectorIJK#ZERO}
    #     """
    #     thisNorm = self.getLength()
    #     vectorNorm = vector.getLength()
    #     if thisNorm == 0.0:
    #         raise Exception("Unable to compute angular separation. " +
    #                         "This vector is the zero vector.")
    #     elif vectorNorm == 0.0:
    #         raise Exception("Unable to compute angular separation. " +
    #                         "The argument supplied is the zero vector.")
    #     dotProduct = self.getDot(vector)
    #     if dotProduct > 0:
    #         x = self.i/thisNorm - vector.i/vectorNorm
    #         y = self.j/thisNorm - vector.j/vectorNorm
    #         z = self.k/thisNorm - vector.k/vectorNorm
    #         return 2.0*asin(0.5*computeNorm(x, y, z))
    #     elif dotProduct < 0:
    #         x = self.i/thisNorm + vector.i/vectorNorm
    #         y = self.j/thisNorm + vector.j/vectorNorm
    #         z = self.k/thisNorm + vector.k/vectorNorm
    #         return pi - 2.0*asin(0.5*computeNorm(x, y, z))
    #     return pi/2

    # def getSeparationOutOfPlane(self, normal) -> float:
    #     """Compute the angle this instance lies out of the plane specified by
    #     normal.

    #     Note: this really is simply
    #     {@link FundamentalPhysicalConstants#HALFPI} -
    #     {@link UnwritableVectorIJK#getSeparation(UnwritableVectorIJK)},
    #     but is useful as a convenience method.

    #     @param normal the normal to the plane

    #     @return the angular separation of this vector and the plane with the
    #     specified normal. Positive values lie on the same side as normal,
    #     negative on the other.
    #     """
    #     return pi/2 - self.getSeparation(normal)

    # # @staticmethod
    # def copyOf(vector):
    #     """Makes an unwritable copy of the supplied vector.

    #     This method makes an unwritable copy only if necessary. It tries to
    #     avoid making a copy wherever possible.

    #     @param vector a vector to copy.

    #     @return either a reference to vector (if vector is already only an
    #     instance of {@link UnwritableVectorIJK}, otherwise an unwritable copy
    #     of vector's contents
    #     """
    #     if isinstance(vector, UnwritableVectorIJK):
    #         return vector
    #     return UnwritableVectorIJK(vector)

    # def hashCode(self) -> int:
    #     """Compute the hash code."""
    #     prime = 31
    #     result = 1
    #     temp = Double.doubleToLongBits(self.i)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.j)
    #     result = prime*result + temp ^ (temp >> 32)
    #     temp = Double.doubleToLongBits(self.k)
    #     result = prime*result + temp ^ (temp >> 32)
    #     return result

    # def equals(self, obj) -> bool:
    #     if self is obj:
    #         return True
    #     if obj is None:
    #         return False
    #     if not isinstance(obj, UnwritableVectorIJK):
    #         return False
    #     if self.i != obj.i:
    #         return False
    #     if self.j != obj.j:
    #         return False
    #     if self.k != obj.k:
    #         return False
    #     return True

    def toString(self):
        return "[%s,%s,%s]" % (self.i, self.j, self.k)
