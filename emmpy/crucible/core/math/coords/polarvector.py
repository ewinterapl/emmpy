"""emmpy.crucible.core.math.coords.polarvector"""


from emmpy.crucible.core.math.coords.abstractvectorij import AbstractVectorIJ


class PolarVector(AbstractVectorIJ):
    """A class representing a vector in the polar coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, radius, angle):
        """Constructor"""
        AbstractVectorIJ.__init__(self, radius, angle)

    def getRadius(self):
        """@return the radius"""
        return AbstractVectorIJ.getI(self)

    def getAngle(self):
        """@return the angle"""
        return AbstractVectorIJ.getJ(self)

    def toString(self):
        return (
            "PolarVector [radius: %s, angle: %s]" %
            (self.getRadius(), self.getAngle())
        )


ZERO = PolarVector(0, 0)
