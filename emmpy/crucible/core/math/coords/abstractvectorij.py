"""Abstract base class for 2-D vectors."""


from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ


class AbstractVectorIJ:
    """Abstract class to assist implementors of new 2-D coordinate types.

    The unwritable coordinate should extend this guy. It is also meant
    to help ensure that the outlines for all coordinates are consistent. This
    was also done, since the Jacobian classes require interaction with the
    2-D coordinates as VectorIJs, specifically for calling mxv on a coordinate.
    This makes that possible. There may be further times where a coordinate
    needs to be used as a VectorIJ, as long as this occurs in this package, it
    is possible.

    The fact that a VectorIJ is the true composition class of all coordinate
    systems should not leave this package. We don't want different coordinate
    systems to be VectorIJs as you wont know what coordinate system it is
    supposed to be.

    Also, if any other methods are needed on every coordinate class, they can
    hopefully just be added in here.

    author G.K.Stephens
    """

    def __init__(self, i, j):
        """Construct a coordinate from the two basic components.

        param (float) i
        param (float) j
        """
        self.ijCoordinate = VectorIJ(i, j)

    # These methods should be wrapped in new methods with the appropriate
    # names. The getters in the unwritable and the setters in the writable.
    # These methods should never have there visibility upgraded, but should
    # be wrapped.

    def getI(self):
        """Return the I coordinate."""
        return self.ijCoordinate.i

    def getJ(self):
        """Return the J coordinate."""
        return self.ijCoordinate.getJ()

    def getVectorIJ(self):
        """Return the IJ coordinate."""
        return self.ijCoordinate
