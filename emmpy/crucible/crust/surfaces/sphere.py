"""emmpy.crucible.crust.surfaces.sphere"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.crust.surfaces.ellipsoid import Ellipsoid
from emmpy.crucible.crust.surfaces.sphericalsurfacenormalcomputer import (
    SphericalSurfaceNormalComputer
)


class Sphere(Ellipsoid):

    def __init__(self, radius):
        """Constructor"""
        Ellipsoid.__init__(self, radius, radius, radius)
        Preconditions.checkArgument(
            radius > 0,
            "A sphere's radius must be strictly greater than zero."
        )
        self.normalComputer = SphericalSurfaceNormalComputer()

    def getRadius(self):
        return self.getA()

    def computeOutwardNormal(self, surfacePoint, buffer):
        return self.normalComputer.computeOutwardNormal(surfacePoint, buffer)
