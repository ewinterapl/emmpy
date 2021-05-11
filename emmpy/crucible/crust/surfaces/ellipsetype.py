"""emmpy.crucible.crust.surfaces.ellipsetype"""


from math import acos, atan2, cos, hypot, sin

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.core.math.cruciblemath import signum
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
from emmpy.crucible.crust.surfaces.plane import Plane


class EllipseType:
    """Enumeration describing the type of ellipses supported by the Ellipse
    class.

    author F.S.Turner
    """

    # Indicates the ellipse has both semi-axes with zero length.
    POINT = 0

    # Indicates the ellipse has a semi-minor axes with zero length.
    LINE_SEGMENT = 1

    # Indicates the ellipse has a semi-axes with non-zero length.
    ELLIPSE = 2

    @staticmethod
    def isDegenerate(ellipseType):
        if (ellipseType == EllipseType.POINT or
            ellipseType == EllipseType.LINE_SEGMENT):
            return True
        else:
            return False

    @staticmethod
    def isContainedWithin(ellipse, plane):
        """Package private method that determines whether the ellipse of a
        particular type is completely contained within a plane.

        Designed to supportUnwritableEllipse.isContainedWithin(UnwritablePlane)

        param ellipse the ellipse
        param plane the plane
        return true if plane completely contains ellipse, false otherwise
        """
        if ellipse.type == EllipseType.POINT:
            # Also simple, just determine if the point is contained with the
            # plane.
            return plane.contains(ellipse.center)
        elif ellipse.type == EllipseType.LINE_SEGMENT:
            # Determine if the center is contained within the plane.
            if not plane.contains(ellipse.center):
                return False

            # Check that the semi-major axes is orthogonal to the the plane's
            # normal.
            return ellipse.smajor.getDot(plane.normal) == 0

        elif ellipse.type == EllipseType.ELLIPSE:
            # Determine if the center is contained within the plane.
            if not plane.contains(ellipse.center):
                return False

            # Verify that both semi-axes are orthogonal to the plane's normal.
            return (
                ellipse.smajor.getDot(plane.normal) == 0 and
                ellipse.sminor.getDot(plane.normal) == 0
            )

        else:
            raise Exception

    @staticmethod
    def intersects(ellipse, plane):
        """Package private method that determines whether the ellipse of a
        particular type intersects a plane.

        Designed to support UnwritableEllipse.intersects(UnwritablePlane)

        param ellipse the ellipse
        param plane the plane
        return true if ellipse and plane intersect, false otherwise
        """
        if ellipse.type == EllipseType.POINT:
            # This is simple, determine if the point is contained within the
            # plane.
            return plane.contains(ellipse.center)
        elif ellipse.type == EllipseType.LINE_SEGMENT:
            # First get the entire containment case out of the way.
            if EllipseType.isContainedWithin(ellipse, plane):
                return True

            # Compute the plane constant after translating the origin so that
            # it is at the ellipse's center.
            recenteredOrigin = (
                VectorIJK.combine(plane.getConstant(), plane.normal, -1.0,
                                  ellipse.center)
            )
            recenteredConstant = abs(plane.normal.getDot(recenteredOrigin))
            return (
                abs(ellipse.smajor.getDot(plane.normal)) >= recenteredConstant
            )

        elif ellipse.type == EllipseType.ELLIPSE:
            # First get the entire containment case out of the way.
            if EllipseType.isContainedWithin(ellipse, plane):
                return True

            # Compute the plane constant after translating the origin so that
            # it is at the ellipse's center.
            recenteredOrigin = (
                VectorIJK.combine(plane.getConstant(), plane.normal, -1.0,
                                  ellipse.center)
            )
            recenteredConstant = abs(plane.normal.getDot(recenteredOrigin))
            v1 = ellipse.smajor.getDot(plane.normal)
            v2 = ellipse.sminor.getDot(plane.normal)
            return hypot(v1, v2) >= recenteredConstant

        else:
            raise Exception

    @staticmethod
    def intersect(ellipse, plane, bufferOne, bufferTwo):
        """Computes the intersection points of an ellipse of a particular type
        with a plane.

        Designed to support
        UnwritableEllipse#intersect(UnwritablePlane, VectorIJK, VectorIJK)

        param ellipse the ellipse
        param plane the plane
        param bufferOne buffer to capture the an intersection point
        param bufferTwo another, separate buffer, to capture another
        intersection point
        throws IllegalArgumentException if there are no intersections or if the
        ellipse is completely contained within the plane. To guard against this
        use:
        UnwritableEllipse.isContainedWithin(UnwritablePlane)
        and
        UnwritableEllipse.intersects(UnwritablePlane)
        """
        if ellipse.type == EllipseType.POINT:
            Preconditions.checkArgument(
                EllipseType.isContainedWithin(ellipse, plane),
                "Point degenerate ellipse does not intersect plane"
            )
            bufferOne.setTo(ellipse.center)
            bufferTwo.setTo(ellipse.center)
        elif ellipse.type == EllipseType.LINE_SEGMENT:
            # Verify that the line segment is not completely contained within
            # the plane.
            Preconditions.checkArgument(
                not EllipseType.isContainedWithin(ellipse, plane),
                "Line segment degenerate ellipse is entirely contained within "
                "the plane"
            )

            # We will handle the case of no intersection as we go forward.
            # While we could utilize the intersects() method on this type, it
            # would result in redundant execution. Create a new plane that is
            # just the supplied plane recentered to the center of the ellipse.
            newCenter = (
                VectorIJK.combine(plane.getConstant(), plane.normal, -1.0,
                                  ellipse.center)
            )
            newPlane = Plane(plane.normal, newCenter)
            v = ellipse.smajor.getDot(newPlane.normal)
            absV = abs(v)

            # Check to see if there is no intersection. This is two parts,
            # first if the line segment is parallel to the plane (v == 0) or if
            # abs(v) < newPlane.getConstant().
            Preconditions.checkArgument(
                v != 0,
                "Line segment degenerate ellipse is parallel to the candidate "
                "plane for intersection"
            )
            Preconditions.checkArgument(
                absV >= newPlane.getConstant(),
                "Line segment degenerate ellipse does not intersect the "
                "candidate plane."
            )

            # The sign of the scale for the semi-major axis should be the same
            # sign as v.
            VectorIJK.combine(
                1.0, ellipse.center, signum(v)*newPlane.getConstant()/absV,
                ellipse.smajor, bufferOne
            )
            bufferTwo.setTo(bufferOne)
        elif ellipse.type == EllipseType.ELLIPSE:
            # Verify that the line segment is not completely contained within
            # the plane.
            Preconditions.checkArgument(
                not EllipseType.isContainedWithin(ellipse, plane),
                "Ellipse is entirely contained within the plane"
            )

            # We will handle the case of no intersection as we go forward.
            # While we could utilize the intersects() method on this type, it
            # would result in redundant execution. Create a new plane that is
            # just the supplied plane recentered to the center of the ellipse.
            newCenter = (
                VectorIJK.combine(plane.getConstant(), plane.normal, -1.0,
                                  ellipse.center)
            )
            newPlane = Plane(plane.normal, newCenter)
            v1 = ellipse.smajor.getDot(newPlane.normal)
            v2 = ellipse.sminor.getDot(newPlane.normal)
            vnorm = hypot(v1, v2)

            # Check to see if there is no intersection. This is two parts,
            # first if the line segment is parallel to the plane (v == 0) or if
            # Math.abs(v) < newPlane.getConstant.
            Preconditions.checkArgument(
                v1 != 0.0 or v2 != 0.0,
                "Ellipse is parallel to the candidate plane for intersection"
            )
            Preconditions.checkArgument(
                vnorm >= newPlane.getConstant(),
                "Ellipse does not intersect the candidate plane"
            )
            alpha = acos(newPlane.getConstant()/vnorm)
            beta = atan2(v2, v1)
            angle1 = beta - alpha
            angle2 = beta + alpha
            VectorIJK.combine(1.0, ellipse.center, cos(angle1), ellipse.smajor,
                              sin(angle1), ellipse.sminor, bufferOne)
            VectorIJK.combine(1.0, ellipse.center, cos(angle2), ellipse.smajor,
                              sin(angle2), ellipse.sminor, bufferTwo)
        else:
            raise Exception
