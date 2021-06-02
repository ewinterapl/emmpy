"""emmpy.crucible.crust.surfaces.ellipsoidalsurfacenormalcomputer"""


from emmpy.crucible.crust.surfaces.surfacenormalcomputer import (
    SurfaceNormalComputer
)


class EllipsoidalSurfaceNormalComputer(SurfaceNormalComputer):

    def __init__(self, a, b, c, minRadius):
        self.a1 = minRadius/a
        self.b1 = minRadius/b
        self.c1 = minRadius/c

    def computeOutwardNormal(self, surfacePoint, buffer):
        """Compute (surfacePoint.getI()/a/a, surfacePoint.getJ()/b/b,
        surfacePoint.getK()/c/c).

        This could be numerically unwise due to overflow. Use minRadius as a
        scaling.
        """
        buffer.setTo(surfacePoint.getI()*self.a1*self.a1,
                     surfacePoint.getJ()*self.b1*self.b1,
                     surfacePoint.getK()*self.c1*self.c1)
        return buffer
