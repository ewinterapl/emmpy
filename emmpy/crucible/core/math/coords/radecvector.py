"""A vector in Ra/Dec coordinates."""


from emmpy.crucible.core.math.coords.abstractvector import AbstractVector


class RaDecVector(AbstractVector):
    """A class representing a vector in the Celestial Coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, radius, raRadians, decRadians):
        """Build a new object."""
        AbstractVector.__init__(self, radius, raRadians, decRadians)

    def getRadius(self):
        """Return the radius."""
        return AbstractVector.getI(self)

    def getRightAscension(self):
        """Return the right ascension."""
        return AbstractVector.getJ(self)

    def getDeclination(self):
        """Return the declination."""
        return AbstractVector.getK(self)


# The ZERO vector.
ZERO = RaDecVector(0, 0, 0)
