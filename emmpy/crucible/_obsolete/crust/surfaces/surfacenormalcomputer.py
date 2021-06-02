"""emmpy.crucible.crust.surfaces.surfacenormalcomputer

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""

from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class SurfaceNormalComputer:
    """Defines the outward directed normal vector for a surface.

    author F.S.Turner
    """

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTANTIATE
        """
        raise Exception

    def computeOutwardNormal(self, *args):
        """Computes the outward directed normal of a surface at the specified
        point.

        Note: while it may be useful to normalize the resultant vector, there
        is no specific requirement to do so.
        """
        if len(args) == 1:
            (surfacePoint,) = args
            # param surfacePoint the point at which to compute the outward
            # return the normal vector
            return self.computeOutwardNormal(surfacePoint, VectorIJK())
        elif len(args) == 2:
            (surfacePoint, buffer) = args
            # param surfacePoint the point at which to compute the outward
            # param buffer a buffer to capture the normal vector
            # return a reference to buffer for convenience
            # INTERFACE - DO NOT INVOKE
            raise Exception
        else:
            raise Exception
