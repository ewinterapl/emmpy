"""An unwritable 3-D vector.

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

author F.S.Turner
"""


from math import asin, pi

from emmpy.crucible.core.math.vectorspace.internaloperations import (
    computeNorm
)
from emmpy.utilities.doubletolongbits import doubleToLongBits
from emmpy.utilities.isrealnumber import isRealNumber


class UnwritableVectorIJK:
    """UnwritableVectorIJK."""

    def __init__(self, *args):
        """Build a UnwritableVectorIJK."""
        if len(args) == 1:
            if isinstance(args[0], list):
                # Constructs a vector from the first three elements of an
                # array of doubles.
                # param [float] data the array of doubles
                (data,) = args
                self.__init__(data[0], data[1], data[2])
            elif isinstance(args[0], UnwritableVectorIJK):
                # Copy constructor, creates a vector by copying the values of a
                # pre-existing one.
                # param UnwritableVectgorIJK vector the vector whose contents
                # are to be copied
                (vector,) = args
                self.__init__(vector.i, vector.j, vector.k)
            else:
                raise Exception
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], list):
                # Constructs a vector from the three elements of an array of
                # double starting with the offset index.
                # param int offset index into the data array to copy into the
                # ith component.
                # param [float] data the array of doubles
                (offset, data) = args
                self.__init__(data[offset], data[offset + 1], data[offset + 2])
            elif (
                isRealNumber(args[0]) and
                isinstance(args[1], UnwritableVectorIJK)
            ):
                # Scaling constructor, creates a new vector by applying a
                # scalar multiple to the components of a pre-existing vector.
                # param float scale the scale factor to apply
                # param UnwritableVectorIJK vector the vector whose contents
                # are to be scaled
                (scale, vector) = args
                self.__init__(scale*vector.i, scale*vector.j, scale*vector.k)
            else:
                raise Exception
        elif len(args) == 3:
            # Constructs a vector from the three basic components.
            # param float i the ith component
            # param float j the jth component
            # param float k the kth component
            (i, j, k) = args
            self.i = i
            self.j = j
            self.k = k
        else:
            raise Exception

    def createUnitized(self):
        """Create a new, unit length copy of the existing vector.

        This code is just a convenience method that implements:
        new UnwritableVectorIJK(1.0/this.getLength(), this)  in a safe manner.

        return UnwritableVectorIJK a vector of unit length in the direction of
        the instance
        """
        norm = self.getLength()
        if norm > 0.0:
            uvijk = UnwritableVectorIJK(1.0/norm, self)
            return uvijk
        raise Exception("Unable to unitize. Supplied vector has zero length.")

    def createNegated(self):
        """Create a new, negated copy of an the existing vector.

        Convenience method for: new UnwritableVectorIJK(-1.0, this).

        return UnwritableVectorIJK the negated vector, -this.
        """
        return UnwritableVectorIJK(-1, self)

    def createScaled(self, scale):
        """Create a scaled copy of an the vector.

        Convenience method for: new UnwritableVectorIJK(scale, this).

        param float scale the scale factor to apply
        return UnwritableVectorIJK the scaled vector, scale*this.
        """
        return UnwritableVectorIJK(scale, self)

    def getI(self):
        """Get the ith component (float)."""
        return self.i

    def getJ(self):
        """Get the jth component (float)."""
        return self.j

    def getK(self):
        """Get the kth component (float)."""
        return self.k

    def get(self, index):
        """Retrieve the specified component of the vector.

        param int index the index of the component to retrieve.
        0 = ith, 1 = jth, 2 = kth.
        return float the value for the requested component
        throws Exception if an invalid index, outside the range [0,2], is
        specified.
        """
        if index == 0:
            return self.i
        elif index == 1:
            return self.j
        elif index == 2:
            return self.k
        else:
            raise Exception

    def getLength(self):
        """Compute the standard L-2 norm, or length, of the vector.

        return float (i*i + j*j + k*k)^(1/2) without danger of overflow.
        """
        return computeNorm(self.i, self.j, self.k)

    def getDot(self, vector):
        """Compute the dot product of this instance with another vector.

        param UnwritableVectorIJK vector the vector to dot against the
        instance.

        return gloat i*vector.i + j*vector.j + k*vector.k
        """
        return self.i*vector.i + self.j*vector.j + self.k*vector.k

    def getSeparation(self, vector):
        """Compute the angular separation between this and another vector.

        param UnwritableVectorIJK vector
        return float the angular separation between vector and this instance in
        radians.
        throws Exception if either this instance or the supplied vector are
        zero
        """
        thisNorm = self.getLength()
        vectorNorm = vector.getLength()
        if thisNorm == 0.0:
            raise Exception("Unable to compute angular separation. " +
                            "This vector is the zero vector.")
        elif vectorNorm == 0.0:
            raise Exception("Unable to compute angular separation. " +
                            "The argument supplied is the zero vector.")
        dotProduct = self.getDot(vector)
        if dotProduct > 0:
            x = self.i/thisNorm - vector.i/vectorNorm
            y = self.j/thisNorm - vector.j/vectorNorm
            z = self.k/thisNorm - vector.k/vectorNorm
            return 2.0*asin(0.5*computeNorm(x, y, z))
        elif dotProduct < 0:
            x = self.i/thisNorm + vector.i/vectorNorm
            y = self.j/thisNorm + vector.j/vectorNorm
            z = self.k/thisNorm + vector.k/vectorNorm
            return pi - 2.0*asin(0.5*computeNorm(x, y, z))
        return pi/2

    def getSeparationOutOfPlane(self, normal):
        """Compute the angle between this and a plane.

        Note: this really is simply
        FundamentalPhysicalConstants.HALFPI
        UnwritableVectorIJK.getSeparation(UnwritableVectorIJK)
        but is useful as a convenience method.

        param UnwritableVectorIJK normal the normal to the plane
        return float the angular separation of this vector and the plane with
        the specified normal. Positive values lie on the same side as normal,
        negative on the other.
        """
        return pi/2 - self.getSeparation(normal)

    @staticmethod
    def copyOf(vector):
        """Make an unwritable copy of the supplied vector.

        This method makes an unwritable copy only if necessary. It tries to
        avoid making a copy wherever possible.

        param UnwritableVectorIJK vector a vector to copy.

        return UnwritableVectorIJK either a reference to vector (if vector is
        already only an instance of UnwritableVectorIJK, otherwise an
        unwritable copy of vector's contents
        """
        if isinstance(vector, UnwritableVectorIJK):
            return vector
        return UnwritableVectorIJK(vector)
