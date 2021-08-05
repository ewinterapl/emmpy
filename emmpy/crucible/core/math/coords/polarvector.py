"""2-D vectors in a polar coordinate system."""


from emmpy.math.vectors.vector2d import Vector2D


class PolarVector(Vector2D):
    """A class representing a 2-D vector in the polar coordinate system.

    author G.K.Stephens
    """

    def __init__(self, radius, angle):
        """2-D vectors in a polar coordinate system."""
        self[:] = [radius, angle]

    def getRadius(self):
        """Return the radius."""
        return self[0]

    def getAngle(self):
        """Return the angle."""
        return self[1]

    def getVectorIJ(self):
        return self

    def getI(self):
        return self[0]

    def getJ(self):
        return self[1]


# The null vector in polar coordinates.
ZERO = PolarVector(0, 0)
