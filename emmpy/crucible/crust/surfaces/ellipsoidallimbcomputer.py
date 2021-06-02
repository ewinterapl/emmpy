"""emmpy.crucible.crust.surfaces.ellipsoidallimbcomputer"""


from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.crust.surfaces.ellipsoidalplaneintersectioncomputer import (
    EllipsoidalPlaneIntersectionComputer
)
from emmpy.crucible.crust.surfaces.plane import Plane


class EllipsoidalLimbComputer:

    def __init__(self, a, b, c):
        """Constructor"""
        self.a = a
        self.b = b
        self.c = c
        self.scale = max(abs(a), abs(b), abs(c))
        self.scaledA = self.a/self.scale
        self.scaledB = self.b/self.scale
        self.scaledC = self.c/self.scale
        self.planeComputer = EllipsoidalPlaneIntersectionComputer(
            self.scaledA, self.scaledB, self.scaledC)
        self.scaledASq = self.scaledA*self.scaledA
        self.scaledBSq = self.scaledB*self.scaledB
        self.scaledCSq = self.scaledC*self.scaledC

    def level(self, vector):
        return (
            vector.getI()*vector.getI()/self.scaledASq +
            vector.getJ()*vector.getJ()/self.scaledBSq +
            vector.getK()*vector.getK()/self.scaledCSq
        )

    def computeLimb(self, viewPoint, buffer):
        """Scale the viewpoint."""
        v = VectorIJK(viewPoint)
        v.scale(1.0/self.scale)

        # Determine if the viewing point lies outside the ellipsoid. This
        # amounts to comparing the level of the viewpoint is greater than or
        # equal to 1.0.
        Preconditions.checkArgument(
            self.level(v) >= 1.0, "Viewing point is inside the body."
        )

        # Find a normal vector for the limb plane.
        v.setTo(
            v.getI()/self.scaledASq, v.getJ()/self.scaledBSq,
            v.getK()/self.scaledCSq
        )
        p = Plane(v, 1.0)

        # Find the limb by intersecting the limb plane with the ellipsoid.
        # Note: this will throw an illegal argument exception of the geometry
        # is sufficiently extreme.
        # TODO: Should this exception be wrapped?
        self.planeComputer.intersect(p, buffer)

        # Undo the scaling to each element of the ellipse.
        buffer.scale(self.scale)
        return buffer
