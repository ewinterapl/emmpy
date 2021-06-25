"""Represenation of a vector in cylindrical coordinates."""


from emmpy.crucible.core.math.coords.abstractvector import AbstractVector


class CylindricalVector(AbstractVector):
    """A class representing a vector in the cylindrical coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, cylindricalRadius, longInRadians, height):
        """Build a new object."""
        AbstractVector.__init__(self, cylindricalRadius, longInRadians, height)

    def getCylindricalRadius(self):
        """Return the cylindrical radius (often denoted as r)."""
        return AbstractVector.getI(self)

    def getLongitude(self):
        """Return the longitude."""
        return AbstractVector.getJ(self)

    def getHeight(self):
        """Return the height (often denoted as z)."""
        return AbstractVector.getK(self)


# The ZERO vector.
ZERO = CylindricalVector(0, 0, 0)
