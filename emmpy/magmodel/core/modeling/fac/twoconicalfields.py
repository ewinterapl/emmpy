"""emmpy.magmodel.core.modeling.fac.twoconicalfields"""


# import static crucible.core.math.vectorfields.VectorFields.add;
# import static crucible.core.math.vectorfields.VectorFields.negate;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class TwoConicalFields(VectorField):
    """Represents the magnetic field of two deformed azimuthal harmonic of a
    finite thickness conical current sheet
    
    As described in "A model of the near magnetosphere with a dawn-dusk
    asymmetry 1. Mathematical structure" by N. A. Tsyganenko. See eq. (20).
    The cones' axis is the +/-Z axis.

    see http://onlinelibrary.wiley.com/doi/10.1029/2001JA000219/abstract
    (Tsyganenko, 2002

    author Nicholas Sharp
    author G.K.Stephens
    """

    def __init__(self, field):
        """Constructor

        param VectorField field
        """
        # VectorField field
        self.field = self.add(field, new XYPlaneReflectedField(negate(field)));

    #   @Override
    #   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #     return field.evaluate(location, buffer);
    #   }

    # }
