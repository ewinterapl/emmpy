"""emmpy.crucible.core.math.coords.latitudinalvector"""


from emmpy.crucible.core.math.coords.abstractvector import AbstractVector


class LatitudinalVector(AbstractVector):
    """A class representing a vector in the latitudinal coordinate system.

    @author G.K.Stephens
    """
    # public final class LatitudinalVector extends AbstractVector {

    # The ZERO vector.
    # ZERO = LatitudinalVector(0, 0, 0)

    def __init__(self, *args):
        """Constructor"""
        (radius, latInRadians, longInRadians) = args
        AbstractVector.__init__(self, radius, latInRadians, longInRadians)

    def getRadius(self):
        """@return the radius"""
        return AbstractVector.getI(self)

    def getLatitude(self):
        """@return the latitude"""
        return AbstractVector.getJ(self)

    def getLongitude(self):
        """@return the longitude"""
        return AbstractVector.getK(self)

    def toString(self):
        return (
            "LatitudinalVector [radius: %s, latitude: %s, longitude: %s]" %
            (self.getRadius(), self.getLatitude(), self.getLongitude())
        )
