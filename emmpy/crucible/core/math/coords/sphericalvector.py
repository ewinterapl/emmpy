"""A spherical vector."""


from emmpy.math.vectors.vector3d import Vector3D


class SphericalVector(Vector3D):
    """A class representing a vector in the spherical coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, radius, colatInRadians, longInRadians):
        """Build a new object."""
        self[:] = [radius, colatInRadians, longInRadians]

    def getRadius(self):
        """Return the radius."""
        return self[0]

    def getColatitude(self):
        """Return the colatitude."""
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
ZERO = SphericalVector(0, 0, 0)
