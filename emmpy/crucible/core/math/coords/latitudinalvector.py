"""Represenation of a latitudinal vector."""


from emmpy.math.vectors.vector3d import Vector3D


class LatitudinalVector(Vector3D):
    """A class representing a vector in the latitudinal coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, radius, latInRadians, longInRadians):
        """Build a new object."""
        self[:] = [radius, latInRadians, longInRadians]

    def getRadius(self):
        """Return the radius."""
        return self[0]

    def getLatitude(self):
        """Return the latitude."""
        return self[1]

    def getLongitude(self):
        """Return the longitude."""
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
ZERO = LatitudinalVector(0, 0, 0)
