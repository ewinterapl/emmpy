"""Represenation of a latitudinal vector."""


from emmpy.crucible.core.math.coords.abstractvector import AbstractVector


class LatitudinalVector(AbstractVector):
    """A class representing a vector in the latitudinal coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, *args):
        """Build a new object."""
        (radius, latInRadians, longInRadians) = args
        AbstractVector.__init__(self, radius, latInRadians, longInRadians)

    def getRadius(self):
        """Return the radius."""
        return AbstractVector.getI(self)

    def getLatitude(self):
        """Return the latitude."""
        return AbstractVector.getJ(self)

    def getLongitude(self):
        """Return the longitude."""
        return AbstractVector.getK(self)


# The ZERO vector.
ZERO = LatitudinalVector(0, 0, 0)
