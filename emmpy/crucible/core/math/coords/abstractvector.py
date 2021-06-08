"""Base class for vectors.

This abstract class is meant to assist implementors of new coordinate types.
"""


from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class AbstractVector:
    """Abstract class to assist implementors of new coordinate types.

    The unwritable coordinate should extend this guy. It is also meant to help
    ensure that the outlines for all coordinates are consistent. This was also
    done, since the Jacobian classes require interaction with the Coordinates
    as VectorIJKs, specifically for calling mxv on a coordinate. This makes
    that possible. There may be further times where a coordinate needs to be
    used as a {@link VectorIJK}, as long as this occurs in this package, it is
    possible.

    The fact that a {@link VectorIJK} is the true composition class of all
    coordinate systems should not leave this package. We don't want different
    coordinate systems to be VectorIJKs as you wont know what coordinate system
    it is supposed to be.

    Also, if any other meabstractcoordinateconverterthods are needed on every
    coordinate class, they can hopefully just be added in here.

    @author G.K.Stephens
    """

    def __init__(self, i: float, j: float, k: float):
        """Construct a coordinate from the three basic components."""
        self.ijkCoordinate = UnwritableVectorIJK(i, j, k)

    # These six methods should be wrapped in new methods with the appropriate
    # names. The getters in the unwritable and the setters in the writable.
    # These six methods should never have there visibility upgraded, but should
    # be wrapped.

    def getI(self) -> float:
        """Get the I coordinate."""
        return self.ijkCoordinate.getI()

    def getJ(self) -> float:
        """Get the J coordinate."""
        return self.ijkCoordinate.getJ()

    def getK(self) -> float:
        """Get the K coordinate."""
        return self.ijkCoordinate.getK()

    def getVectorIJK(self) -> UnwritableVectorIJK:
        """Get the IJK coordinates.

        This method should never have its visibility upgraded.
        """
        return self.ijkCoordinate

    # def hashCode(self) -> int:
    #     """Compute the object hash code.

    #     @see java.lang.Object#hashCode()
    #     """
    #     prime = 31
    #     result = 1
    #     result = prime*result
    #     if self.ijkCoordinate:
    #         result += self.ijkCoordinate.hashCode()
    #     return result

    # def equals(self, obj):
    #     """Check the object for equality with another object.

    #     @see java.lang.Object#equals(java.lang.Object)
    #     """
    #     if self is obj:
    #         return True
    #     if obj is None:
    #         return False
    #     if not isinstance(self, obj.__class__):
    #         return False
    #     other = obj
    #     if self.ijkCoordinate is None:
    #         if other.ijkCoordinate is not None:
    #             return False
    #     elif not self.ijkCoordinate.equals(other.ijkCoordinate):
    #         return False
    #     return True

    # def toString(self):
    #     """Convert the object to a string."""
    #     raise Exception
