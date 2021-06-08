"""Magnetic field from 2 conical current sheets."""


# import static crucible.core.math.vectorfields.VectorFields.negate;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorfields.vectorfields import VectorFields
from emmpy.magmodel.core.modeling.fac.xyplanereflectedfield import (
    XYPlaneReflectedField
)


class TwoConicalFields(VectorField):
    """Magnetic field from 2 conical current sheets.

    Represents the magnetic field of two deformed azimuthal harmonic of a
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
        """Build a new object.

        param VectorField field
        """
        # VectorField field
        self.field = VectorFields.add(
            field, XYPlaneReflectedField(VectorFields.negate(field))
        )

    def evaluate(self, location, buffer):
        """Evaluate the field.

        param UnwritableVectorIJK location
        param VectorIJK buffer
        """
        return self.field.evaluate(location, buffer)
