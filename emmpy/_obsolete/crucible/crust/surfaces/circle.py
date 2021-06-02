"""emmpy.crucible.crust.surfaces.circle"""


from math import sqrt

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.cruciblemath import signum
from emmpy.crucible.core.math.vectorspace.vectorij import VectorIJ
from emmpy.crucible.crust.surfaces.nointersectionexception import (
    NoIntersectionException
)


class Circle:

    def __init__(self, radius):
        """Constructor"""
        self.rr = radius*radius

    def isSimple(self):
        return True

    def isClosed(self):
        return True

    def isJordan(self):
        return self.isSimple() and self.isClosed()

    def computeIntersectionsLineSegment(self, point1, point2):
        """Computes the first intersection of the r"""
        points = self.computeIntersectionsLine(point1, point2)
        minX = min(point1.getI(), point2.getI())
        maxX = max(point1.getI(), point2.getI())
        minY = min(point1.getJ(), point2.getJ())
        maxY = max(point1.getJ(), point2.getJ())
        result = []
        for point in points:
            x = point.getI()
            y = point.getJ()
            if x >= minX and x <= maxX and y >= minY and y <= maxY:
                result.append(point)
        return result

    def computeIntersectionsRay(self, *args):
        """Computes the first intersection of the r"""
        if len(args) == 2:
            (source, rayFromSource) = args
            points = self.computeIntersectionsLine(
                source, VectorIJ.add(source, rayFromSource)
            )
            result = []
            for point in points:
                pointRay = VectorIJ.subtract(point, source)
                if pointRay.getDot(rayFromSource) > 0:
                    result.append(point)
            return result
        elif len(args) == 3:
            (source, rayFromSource, buffer) = args
            points = self.computeIntersectionsRay(source, rayFromSource)
            if len(points) == 0:
                raise NoIntersectionException

            def my_compare(o1, o2):
                dx1 = o1.getI() - source.getI()
                dy1 = o1.getJ() - source.getJ()
                d1 = sqrt(dx1*dx1 + dy1*dy1)
                dx2 = o2.getI() - source.getI()
                dy2 = o2.getJ() - source.getJ()
                d2 = sqrt(dx2*dx2 + dy2*dy2)
                if d1 < d2:
                    return -1
                elif d1 < d2:
                    return 1
                else:
                    return 0
            points.sort(key=my_compare)
            return buffer.setTo(points[0])
        else:
            raise Exception

    def computeIntersectionsLine(self, point1, point2):
        """Computes all the intersections along an (infinite) line defined by
        two points and the curve.

        param point1 the first point defining the line
        param point2 the second point defining the line
        return a List of all the intersections.
        """
        Preconditions.checkArgument(
            not point1.equals(point2),
            "Both points are the same, cannot form a line from one point"
        )
        vects = []
        x1 = point1.getI()
        y1 = point1.getJ()
        x2 = point2.getI()
        y2 = point2.getJ()
        dx = x2 - x1
        dy = y2 - y1
        dr = sqrt(dx*dx + dy*dy)
        drdr = dr*dr
        det = x1*y2 - x2*y1
        delta = rr*drdr - det*det
        if delta < 0:
            pass
        elif delta == 0:
            # TODO should there be some tolerance on this, it is unlikely to
            # ever be exactly zero
            xi1 = (
                (det*dy + Circle.signumStar(dy)*dx *
                 sqrt(self.rr*drdr - det*det))/drdr
            )
            yi1 = (-det*dx + abs(dy)*sqrt(self.rr*drdr - det*det))/drdr
            vects.append(VectorIJ(xi1, yi1))
        else:
            rad = sqrt(self.rr*drdr - det*det)
            xi1 = (det*dy + signumStar(dy)*dx*rad)/drdr
            yi1 = (-det*dx + abs(dy)*sqrt(rr*drdr - det*det))/drdr
            xi2 = (det*dy - signumStar(dy)*dx*rad)/drdr
            yi2 = (-det*dx - abs(dy)*rad)/drdr
            vects.append(VectorIJ(xi1, yi1))
            vects.append(VectorIJ(xi2, yi2))
        return vects

    def computeGradient(self, surfacePoint, buffer):
        return buffer.setTo(2*surfacePoint.getI(), 2*surfacePoint.getJ())

    @staticmethod
    def signumStar(value):
        if value == 0:
            return 1.0
        return signum(value)
