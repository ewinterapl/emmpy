"""2-D vectors in a polar coordinate system."""


from emmpy.crucible.core.math.coords.abstractvectorij import AbstractVectorIJ


class PolarVector(AbstractVectorIJ):
    """A class representing a 2-D vector in the polar coordinate system.

    author G.K.Stephens
    """

    def __init__(self, radius, angle):
        """2-D vectors in a polar coordinate system."""
        AbstractVectorIJ.__init__(self, radius, angle)

    def getRadius(self):
        """Return the radius."""
        return self.getI()

    def getAngle(self):
        """Return the angle."""
        return self.getJ()


# The null vector in polar coordinates.
ZERO = PolarVector(0, 0)
