"""emmpy.crucible.crust.surfaces.ellipsoid"""


# import static com.google.common.base.Preconditions.checkArgument;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;
from emmpy.com.google.common.base.preconditions import Preconditions
from emmpy.crucible.crust.surfaces.surface import Surface


class Ellipsoid(Surface):
    """Methods that still require implementation from SPICE:

    Nearest point on the ellipsoid to a location (NEARPT) Nearest point on an
    ellipse to a location (NPELPT) Nearest point on an ellipsoid to a line
    (NPEDLN)
    """

    # private final double a;
    # private final double b;
    # private final double c;
    # private final double minRadius;
    # private final double maxRadius;
    # private final EllipsoidalSurfaceNormalComputer normalComputer;
    # private final EllipsoidalIntersectionComputer intersectionComputer;
    # private final EllipsoidalPlaneIntersectionComputer planeIntersectionComputer;
    # private final EllipsoidalLimbComputer limbComputer;

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

    #     this.normalComputer = new EllipsoidalSurfaceNormalComputer(a, b, c, minRadius);
    #     this.intersectionComputer = new EllipsoidalIntersectionComputer(a, b, c);
    #     this.planeIntersectionComputer = new EllipsoidalPlaneIntersectionComputer(a, b, c);
    #     this.limbComputer = new EllipsoidalLimbComputer(a, b, c);
    #   }

    #   @Override
    #   public VectorIJK computeOutwardNormal(UnwritableVectorIJK surfacePoint, VectorIJK buffer) {
    #     return normalComputer.computeOutwardNormal(surfacePoint, buffer);
    #   }

    #   @Override
    #   public boolean intersects(UnwritableVectorIJK source, UnwritableVectorIJK ray) {
    #     return intersectionComputer.intersects(source, ray);
    #   }

    #   @Override
    #   public VectorIJK compute(UnwritableVectorIJK source, UnwritableVectorIJK ray, VectorIJK buffer) {
    #     return intersectionComputer.compute(source, ray, buffer);
    #   }

    #   public boolean intersects(UnwritablePlane plane) {
    #     return planeIntersectionComputer.intersects(plane);
    #   }

    #   public Ellipse intersect(UnwritablePlane plane, Ellipse buffer) {
    #     return planeIntersectionComputer.intersect(plane, buffer);
    #   }

    #   public Ellipse computeLimb(UnwritableVectorIJK viewPoint, Ellipse buffer) {
    #     return limbComputer.computeLimb(viewPoint, buffer);
    #   }

    #   /**
    #    * Determines if the supplied location is interior to the surface
    #    * 
    #    * @param location the supplied location
    #    * @return true if location is interior
    #    */
    #   public boolean isInterior(UnwritableVectorIJK location) {
    #     double x = location.getI();
    #     double y = location.getJ();
    #     double z = location.getK();

    #     double value = x * x / (a * a) + y * y / (b * b) + z * z / (c * c);

    #     return value < 1;
    #   }

    #   public VectorIJK getRadii(VectorIJK buffer) {
    #     return buffer.setTo(a, b, c);
    #   }

    #   public double getA() {
    #     return a;
    #   }

    #   public double getB() {
    #     return b;
    #   }

    #   public double getC() {
    #     return c;
    #   }

    #   public double getMinRadius() {
    #     return minRadius;
    #   }

    #   public double getMaxRadius() {
    #     return maxRadius;
    #   }

    # }
