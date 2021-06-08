"""Polar vectors."""


from emmpy.crucible.core.math.coords.abstractvectorij import AbstractVectorIJ


class PolarVector(AbstractVectorIJ):
    """A class representing a vector in the polar coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, radius, angle):
        """Polar vectors."""
        AbstractVectorIJ.__init__(self, radius, angle)

    def getRadius(self):
        """Return the radius."""
        return AbstractVectorIJ.getI(self)

    def getAngle(self):
        """Return the angle."""
        return AbstractVectorIJ.getJ(self)

    # def toString(self):
    #     """Convert the object to a string."""
    #     return (
    #         "PolarVector [radius: %s, angle: %s]" %
    #         (self.getRadius(), self.getAngle())
    #     )


ZERO = PolarVector(0, 0)
