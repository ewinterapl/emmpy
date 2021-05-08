"""emmpy.crucible.crust.surfaces.surfaceintersectioncomputer

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class SurfaceIntersectionComputer:

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTANTIATE
        """
        raise Exception

    def intersects(self, source, ray):
        """Check if a ray intersects the surface

        INTERFACE - DO NOT INVOKE
        """
        raise Exception

    def compute(self, source, ray, buffer):
        """Compute the intersection of a ray with the surface

        INTERFACE - DO NOT INVOKE

        throws NoIntersectionException if ray emanating from source fails to
        intersect the surface
        """
        raise Exception
