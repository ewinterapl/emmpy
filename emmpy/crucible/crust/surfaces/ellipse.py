"""emmpy.crucible.crust.surfaces.ellipse"""


from emmpy.crucible.core.designpatterns.writable import Writable
from emmpy.crucible.crust.surfaces.unwritableellipse import UnwritableEllipse


class Ellipse(UnwritableEllipse, Writable):
    """A class capturing an ellipse in a 3D vector space.

    author F.S.Turner
    """

    # Field indicating whether the ellipse type is degenerate.
    # private final boolean degenerate;

    def __init__(self, *args):
        """Constructor"""
        if len(args) == 0:
            # Creates the default ellipse. This is a circle of radius one, with
            # semi-major and semi-minor axes configured to be VectorIJK.I and
            # VectorIJK.J respectively.
            UnwritableEllipse.__init__(self)
        elif len(args) == 1:
            (ellipse,) = args
            UnwritableEllipse.__init__(self)
            UnwritableEllipse.setTo(self, ellipse)
        elif len(args) == 3:
            (center, u, v) = args
            # Creates an ellipse from the center and generating vectors.
            # param center the center vector
            # param u a generating vector, may be VectorIJK.ZERO
            # param v another generating vector, may be VectorIJK.ZERO
            # or parallel/anti-parallel to u.
            UnwritableEllipse.__init__(self, center, u, v)
        else:
            raise Exception

    def setTo(self, *args):
        if len(args) == 1:
            (ellipse,) = args
            UnwritableEllipse.setTo(self, ellipse)
            return self
        elif len(args) == 3:
            (center, u, v) = args
            UnwritableEllipse.setTo(self, center, u, v)
            return self
        else:
            raise Exception

    def rotate(self, rotation):
        UnwritableEllipse.rotate(self, rotation)
        return self

    def offset(self, offset):
        UnwritableEllipse.offset(self, offset)
        return self

    def projectOnto(self, *args):
        if len(args) == 2:
            (ellipse, plane) = args
            # Projects an ellipse onto a plane.
            # param ellipse the ellipse to project
            # param plane the plane onto which to project ellipse
            # return a newly created ellipse containing the requested project
            return self.projectOnto(ellipse, plane, Ellipse())
        elif len(args) == 3:
            (ellipse, plane, buffer) = args
            # Projects an ellipse onto a plane.
            # param ellipse the ellipse to project
            # param plane the plane onto which to project ellipse
            # param buffer an ellipse buffer to receive the result of the
            # projection; buffer may overwrite ellipse
            # return a reference to buffer for convenience

            # Allocate the buffers into which we will be inserting the center
            # and generating vectors. This allows ellipse to overwrite buffer,
            # if they are the same.
            u = VectorIJK()
            v = VectorIJK()
            w = VectorIJK()
            plane.getNormal(w)

            # Project the ellipse semi-major and semi-minor axes onto the
            # plane.
            VectorIJK.planeProject(ellipse.smajor, w, u)
            VectorIJK.planeProject(ellipse.sminor, w, v)

            # Now project the center of ellipse onto plane, this will be the
            # center of the projection.
            plane.projectOnto(ellipse.center, w)

            # Configure the buffer from the new generating vectors and center.
            return buffer.setTo(w, u, v)

        else:
            raise Exception
