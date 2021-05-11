"""emmpy.crucible.crust.surfaces.ellipsoidalplaneintersectioncomputer."""


from math import sqrt

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.crust.surfaces.plane import Plane


class EllipsoidalPlaneIntersectionComputer:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.maxRadius = max(abs(a), abs(b), abs(c))

    def distort(self, v):
        v.setTo(v.getI()/self.a, v.getJ()/self.b, v.getK()/self.c)

    def distortInverse(self, v):
        v.setTo(v.getI()*self.a, v.getJ()*self.b, v.getK()*self.c)

    def intersects(self, plane):
        """Does a plane whose origin is coincident to the ellipsoid intersect
        it?

        param plane the plane
        return true if plane intersects this ellipsoid, false otherwise
        """

        # Start out with the simple check, is the plane constant greater than
        # the maximum radius? If so, then clearly there is no intersection.
        if plane.getConstant() > self.maxRadius:
            return False

        # Distort the input plane into the space where the ellipsoid is a unit
        # sphere.
        u = VectorIJK()
        v = VectorIJK()
        p = VectorIJK()
        plane.getSpanningVectors(u, v)
        plane.getPoint(p)
        self.distort(u)
        self.distort(v)
        self.distort(p)
        distortedPlane = Plane(p, u, v)
        distortedPlane.getPoint(p)

        # The plane intersects the ellipse only if the point lies inside or on
        # the unit sphere in the distorted space.
        return p.getLength() <= 1.0

    def intersect(self, plane, buffer):
        """Determine the ellipse of intersection of a plane with this
        ellipsoid.

        throws IllegalArgumentException if the plane does not intersect the
        ellipse.
        """
        Preconditions.checkArgument(
            plane.getConstant() <= self.maxRadius,
            "Plane does not intersect ellipse."
        )

        # Distort the input plane into the space where the ellipsoid is a unit
        # sphere.
        u = VectorIJK()
        v = VectorIJK()
        p = VectorIJK()
        plane.getSpanningVectors(u, v)
        plane.getPoint(p)
        self.distort(u)
        self.distort(v)
        self.distort(p)
        distortedPlane = Plane(p, u, v)

        # The point and spanning vector retrieval methods on plane always
        # return a point that is closest to the origin in the input plane.
        # This point is the center of the intersection circle. The spanning
        distortedPlane.getPoint(p)
        distortedPlane.getSpanningVectors(u, v)
        dist = p.getLength()
        Preconditions.checkArgument(
            dist <= 1.0, "Plane does not intersect ellipse."
        )
        radius = sqrt(self.clampToUnitLength(1.0 - dist*dist))
        u.scale(radius)
        v.scale(radius)
        self.distortInverse(p)
        self.distortInverse(u)
        self.distortInverse(v)
        buffer.setTo(p, u, v)
        return buffer

    def clampToUnitLength(self, value):
        return max(0.0, min(value, 1.0))
