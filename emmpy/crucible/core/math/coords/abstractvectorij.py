"""emmpy.crucible.core.math.coords.abstractvectorij"""


from emmpy.crucible.core.math.vectorspace.unwritablevectorij import (
    UnwritableVectorIJ
)


class AbstractVectorIJ:
    """AbstractVectorIJ

    This abstract class is meant to assist implementors of new coordinate
    types. The unwritable coordinate should extend this guy. It is also meant
    to help ensure that the outlines for all coordinates are consistent. This
    was also done, since the Jacobian classes require interaction with the
    Coordinates as VectorIJs, specifically for calling mxv on a coordinate.
    This makes that possible. There may be further times where a coordinate
    needs to be used as a {@link VectorIJ}, as long as this occurs in this
    package, it is possible.

    The fact that a {@link VectorIJ} is the true composition class of all
    coordinate systems should not leave this package. We don't want different
    coordinate systems to be VectorIJs as you wont know what coordinate system
    it is supposed to be.

    Also, if any other methods are needed on every coordinate class, they can
    hopefully just be added in here.

    @author G.K.Stephens
    """

    def __init__(self, i, j):
        """Constructs a coordinate from the three basic components."""
        self.ijCoordinate = UnwritableVectorIJ(i, j)

    # These six methods should be wrapped in new methods with the appropriate
    # names. The getters in the unwritable and the setters in the writable.
    # These six methods should never have there visibility upgraded, but should
    # be wrapped.

    def getI(self):
        """THIS METHOD SHOULD NOT BE PUBLIC"""
        return self.ijCoordinate.getI()

    def getJ(self):
        """THIS METHOD SHOULD NOT BE PUBLIC"""
        return self.ijCoordinate.getJ()

    def getVectorIJ(self):
        """THIS METHOD SHOULD NOT BE PUBLIC

        This method should never have its visibility upgraded.
        """
        return self.ijCoordinate

    def hashCode(self):
        """(non-Javadoc)

        @see java.lang.Object#hashCode()
        """
        prime = 31
        result = 1
        result = prime*result
        if self.ijCoordinate:
            result += self.ijCoordinate.hashCode()
        return result

    def equals(self, obj):
        """(non-Javadoc)

        @see java.lang.Object#equals(java.lang.Object)
        """
        if self is obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.ijCoordinate is None:
            if other.ijCoordinate is not None:
                return False
        elif not self.ijCoordinate.equals(other.ijCoordinate):
            return False
        return True

        def toString(self):
            raise Exception
