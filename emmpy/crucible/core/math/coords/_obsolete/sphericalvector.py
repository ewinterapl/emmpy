"""A spherical vector."""


from emmpy.crucible.core.math.coords.abstractvector import AbstractVector


class SphericalVector(AbstractVector):
    """A class representing a vector in the spherical coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, radius, colatInRadians, longInRadians):
        """Build a new object."""
        AbstractVector.__init__(self, radius, colatInRadians, longInRadians)

    def getRadius(self):
        """Return the radius."""
        return AbstractVector.getI(self)

    def getColatitude(self):
        """Return the colatitude."""
        return AbstractVector.getJ(self)

    def getLongitude(self):
        """Return the longitude."""
        return AbstractVector.getK(self)


# The ZERO vector.
ZERO = SphericalVector(0, 0, 0)
