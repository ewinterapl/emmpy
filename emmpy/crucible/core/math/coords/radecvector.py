"""A vector in Ra/Dec coordinates."""


from emmpy.math.vectors.vector3d import Vector3D


class RaDecVector(Vector3D):
    """A class representing a vector in the Celestial Coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, radius, raRadians, decRadians):
        """Build a new object."""
        self[:] = [radius, raRadians, decRadians]

    def getRadius(self):
        """Return the radius."""
        return self[0]

    def getRightAscension(self):
        """Return the right ascension."""
        return self[1]

    def getDeclination(self):
        """Return the declination."""
        return self[2]

    def getI(self):
        return self[0]

    def getJ(self):
        return self[1]

    def getK(self):
        return self[2]

    def getVectorIJK(self):
        return self


# The ZERO vector.
ZERO = RaDecVector(0, 0, 0)
