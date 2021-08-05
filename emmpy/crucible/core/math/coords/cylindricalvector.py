"""Represenation of a vector in cylindrical coordinates."""


from emmpy.math.vectors.vector3d import Vector3D


class CylindricalVector(Vector3D):
    """A class representing a vector in the cylindrical coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, cylindricalRadius, longInRadians, height):
        """Build a new object."""
        # AbstractVector.__init__(self, cylindricalRadius, longInRadians, height)
        self[:] = [cylindricalRadius, longInRadians, height]

    def getCylindricalRadius(self):
        """Return the cylindrical radius (often denoted as r)."""
        # return AbstractVector.getI(self)
        return self[0]

    def getLongitude(self):
        """Return the longitude."""
        # return AbstractVector.getJ(self)
        return self[1]

    def getHeight(self):
        """Return the height (often denoted as z)."""
        # return AbstractVector.getK(self)
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
ZERO = CylindricalVector(0, 0, 0)
