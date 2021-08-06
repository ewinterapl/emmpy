"""Represenation of a vector in cylindrical coordinates."""


from emmpy.math.coordinates.cylindricalvector import CylindricalVector as MyCylindricalVector
from emmpy.math.vectors.vector3d import Vector3D


class CylindricalVector(MyCylindricalVector):
    """A class representing a vector in the cylindrical coordinate system.

    @author G.K.Stephens
    """

    def __init__(self, cylindricalRadius, longInRadians, height):
        """Build a new object."""
        super().__init__(cylindricalRadius, longInRadians, height)

    def getCylindricalRadius(self):
        """Return the cylindrical radius (often denoted as r)."""
        return self.rho

    def getLongitude(self):
        """Return the longitude."""
        return self.phi

    def getHeight(self):
        """Return the height (often denoted as z)."""
        return self.z
