"""emmpy.crucible.crust.surfaces.sphericalsurfacenormalcomputer"""


from emmpy.crucible.crust.surfaces.surfacenormalcomputer import (
    SurfaceNormalComputer
)


class SphericalSurfaceNormalComputer(SurfaceNormalComputer):
    """Trivial implementation of the SurfaceNormalComputer interface for a
    spherical target body.

    author F.S.Turner
    """

    def computeOutwardNormal(self, surfacePoint, buffer):
        """There's nothing to do, the surface normal is the surface point
        vector as this is simply a sphere."""
        return buffer.setTo(surfacePoint)
