"""emmpy.crucible.crust.surfaces.ellipsoidalintersectioncomputer"""


from math import sqrt

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.crust.surfaces.nointersectionexception import (
    NoIntersectionException
)
from emmpy.crucible.crust.surfaces.surfaceintersectioncomputer import (
    SurfaceIntersectionComputer
)


class EllipsoidalIntersectionComputer(SurfaceIntersectionComputer):

    def __init__(self, a, b, c):
        """Constructor"""
        self.a = a
        self.b = b
        self.c = c

    def scaleToUnit(self, vector):
        vector.setTo(
            vector.getI()/self.a, vector.getJ()/self.b, vector.getK()/self.c)

    def invertScaleToUnit(self, vector):
        vector.setTo(
            vector.getI()*self.a, vector.getJ()*self.b, vector.getK()*self.c)

    def intersects(self, source, ray):
        Preconditions.checkArgument(
            not ray.equals(VectorIJK.ZERO),
            "Query ray can not be of zero length."
        )
        x = VectorIJK()
        y = VectorIJK()
        ux = VectorIJK()
        p = VectorIJK()
        yproj = VectorIJK()
        x.setTo(ray)
        self.scaleToUnit(x)
        y.setTo(source)
        self.scaleToUnit(y)
        VectorIJK.planeProject(y, x, p)
        VectorIJK.subtract(y, p, yproj)
        ymag = y.getLength()
        pmag = p.getLength()
        ux.setToUnitized(x)

        # There are three cases, the source point lies outside the sphere, the
        # source point lies on the sphere, or it is inside the sphere. Start
        # by handling the outside the sphere case:
        if ymag > 1.0:
            # If p is outside of the unit sphere, or if x points in the same
            # direction as yproj (indicating the ray points away from the
            # sphere), then there can be no intersection.
            if pmag > 1.0 or yproj.getDot(x) > 0.0:
                return False

        # At this point an intersection exists, as we are either inside the
        # sphere or on the sphere itself.
        return True

    def compute(self, source, ray, buffer):
        Preconditions.checkArgument(
            not ray.equals(VectorIJK.ZERO),
            "Query ray can not be of zero length.")
        x = VectorIJK()
        y = VectorIJK()
        ux = VectorIJK()
        p = VectorIJK()
        yproj = VectorIJK()
        x.setTo(ray)
        self.scaleToUnit(x)
        y.setTo(source)
        self.scaleToUnit(y)
        VectorIJK.planeProject(y, x, p)
        VectorIJK.subtract(y, p, yproj)
        ymag = y.getLength()
        pmag = p.getLength()
        ux.setToUnitized(x)

        # There are three cases, the source point lies outside the sphere, the
        # source point lies on the sphere, or it is inside the sphere. Start by
        # handling the outside the sphere case:
        sign = 1.0
        if ymag > 1.0:

            # If p is outside of the unit sphere, or if x points in the same
            # direction as yproj (indicating the ray points away from the
            # sphere), then there can be no intersection.
            if pmag > 1.0 or yproj.getDot(x) > 0.0:
                raise NoIntersectionException("No intersection exists.")

            # If pmag is precisely 1.0, then it is the single unique point of
            # intersection.
            if pmag == 1.0:
                buffer.setTo(p)
                self.invertScaleToUnit(buffer)
                return buffer

            # Set the sign to a negative value, as we have a non-trivial
            # intersection and the component along UX we are adding to P points
            # towards Y.
            sign = -1.0

        if ymag == 1.0:
            # The source lies on the ellipsoid, so it is clearly the first
            # point of intersection.
            buffer.setTo(source)
            return buffer

        # There is a little work left to do at this point. scale is the length
        # of the half chord at p away from the unit sphere's center to either
        # intersection point.
        scale = sqrt(max(0.0, 1 - pmag*pmag))
        VectorIJK.combine(1.0, p, sign*scale, ux, buffer)
        self.invertScaleToUnit(buffer)
        return buffer
