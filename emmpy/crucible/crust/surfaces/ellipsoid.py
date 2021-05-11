"""emmpy.crucible.crust.surfaces.ellipsoid"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.crust.surfaces.surface import Surface
from emmpy.crucible.crust.surfaces.ellipsoidalintersectioncomputer import (
    EllipsoidalIntersectionComputer
)
from emmpy.crucible.crust.surfaces.ellipsoidallimbcomputer import (
    EllipsoidalLimbComputer
)
from emmpy.crucible.crust.surfaces.ellipsoidalplaneintersectioncomputer import (
    EllipsoidalPlaneIntersectionComputer
)
from emmpy.crucible.crust.surfaces.ellipsoidalsurfacenormalcomputer import (
    EllipsoidalSurfaceNormalComputer
)


class Ellipsoid(Surface):
    """Methods that still require implementation from SPICE:

    Nearest point on the ellipsoid to a location (NEARPT) Nearest point on an
    ellipse to a location (NPELPT) Nearest point on an ellipsoid to a line
    (NPEDLN)
    """

    def __init__(self, a, b, c):
        """Constructor"""
        Preconditions.checkArgument(
            a > 0, "Radius [A] of ellipsoid: %s is not strictly positive." % a)
        Preconditions.checkArgument(
            b > 0, "Radius [B] of ellipsoid: %s is not strictly positive." % b)
        Preconditions.checkArgument(
            c > 0, "Radius [C] of ellipsoid: %s is not strictly positive." % c)
        self.a = a
        self.b = b
        self.c = c
        self.minRadius = min(a, b, c)
        self.maxRadius = max(a, b, c)
        self.normalComputer = (
            EllipsoidalSurfaceNormalComputer(a, b, c, self.minRadius)
        )
        self.intersectionComputer = EllipsoidalIntersectionComputer(a, b, c)
        self.planeIntersectionComputer = (
            EllipsoidalPlaneIntersectionComputer(a, b, c)
        )
        self.limbComputer = EllipsoidalLimbComputer(a, b, c)

    def computeOutwardNormal(self, surfacePoint, buffer):
        return self.normalComputer.computeOutwardNormal(surfacePoint, buffer)

    def intersects(self, *args):
        if len(args) == 1:
            (plane,) = args
            return self.planeIntersectionComputer.intersects(plane)
        elif len(args) == 2:
            (source, ray) = args
            return self.intersectionComputer.intersects(source, ray)
        else:
            raise Exception

    def compute(self, source, ray, buffer):
        return self.intersectionComputer.compute(source, ray, buffer)

    def intersect(self, plane, buffer):
        return self.planeIntersectionComputer.intersect(plane, buffer)

    def computeLimb(self, viewPoint, buffer):
        return self.limbComputer.computeLimb(viewPoint, buffer)

    def isInterior(self, location):
        """Determines if the supplied location is interior to the surface

        param location the supplied location
        return true if location is interior
        """
        x = location.getI()
        y = location.getJ()
        z = location.getK()
        value = x*x/(self.a*self.a) + y*y/(self.b*self.b) + z*z/(self.c*self.c)
        return value < 1

    def getRadii(self, buffer):
        return buffer.setTo(self.a, self.b, self.c)

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def getMinRadius(self):
        return self.minRadius

    def getMaxRadius(self):
        return self.maxRadius
