"""emmpy.package crucible.core.math.coords.radecvector"""


from emmpy.crucible.core.math.coords.abstractvector import AbstractVector


class RaDecVector(AbstractVector):
    """A class representing a vector in the Celestial Coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, radius, raRadians, decRadians):
        """Constructor"""
        AbstractVector.__init__(self, radius, raRadians, decRadians)

    def getRadius(self):
        """@return the radius"""
        return AbstractVector.getI(self)

    def getRightAscension(self):
        """@return the right ascension"""
        return AbstractVector.getJ(self)

    def getDeclination(self):
        """@return the declination"""
        return AbstractVector.getK(self)

    def toString(self):
        return (
            "RaDecVector [radius: %s, rightAscension: %s, declination: %s]" %
            (self.getRadius(), self.getRightAscension(), self.getDeclination())
        )


# The ZERO vector.
ZERO = RaDecVector(0, 0, 0)
