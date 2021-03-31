"""emmpy.crucible.core.math.coords.cylindricalvector"""


from emmpy.crucible.core.math.coords.abstractvector import AbstractVector


class CylindricalVector(AbstractVector):
    """A class representing a vector in the cylindrical coordinate system.

    @author G.K.Stephens
    """

    # The ZERO vector.
    # ZERO = CylindricalVector(0, 0, 0)

    def __init__(self, cylindricalRadius, longInRadians, height):
        """Constructor"""
        AbstractVector.__init__(self, cylindricalRadius, longInRadians, height)

    def getCylindricalRadius(self):
        """return the cylindrical radius (often denoted as r)"""
        return AbstractVector.getI(self)

    def getLongitude(self):
        """return the longitude"""
        return AbstractVector.getJ(self)

    def getHeight(self):
        """return the height (often denoted as z)"""
        return AbstractVector.getK(self)

    def toString(self):
        return (
            "CylindricalVector [cylindricalRadius: %s, longitude: %s, height: %s]"
            % (self.getCylindricalRadius(), self.getLongitude(), self.getHeight())
        )
