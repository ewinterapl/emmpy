"""emmpy.crucible.crust.surfaces.sphere"""


# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.crust.surfaces.ellipsoid import Ellipsoid


class Sphere(Ellipsoid):

    def __init__(self, radius):
        """Constructor"""
        Ellipsoid.__init__(self, radius, radius, radius)
        Preconditions.checkArgument(
            radius > 0,
            "A sphere's radius must be strictly greater than zero."
        )
        self.normalComputer = SphericalSurfaceNormalComputer()

    # public double getRadius() {
    #     return getA();
    # }

    # @Override
    # public VectorIJK computeOutwardNormal(UnwritableVectorIJK surfacePoint, VectorIJK buffer) {
    #     return normalComputer.computeOutwardNormal(surfacePoint, buffer);
    # }

    # }
