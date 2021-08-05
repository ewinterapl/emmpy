"""emmpy.geomagmodel.ts07.modeling.fieldaligned.scaledfield"""


# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class ScaledField(VectorField):
    """Scales a VectorField by scaling both the position and the output vector
    by a scalar value.

    where B' is the resulting scaled field
    B and r are the original unscaled
    and a is the scale factor

    author G.K.Stephens
    """

    def __init__(self, unscaledField, kappaScale):
        """Constructor
        
        Constructs a scaled VectorField by scaling both the position and the
        output vector by a scalar value.

        B'(r) = a B(a r)

        where B' is the resulting scaled field
        B and r are the original unscaled and a is the scale factor

        param VectorField unscaledField
        param double kappaScale
        """
        # VectorField unscaledField
        self.unscaledField = unscaledField
        # double kappaScale
        self.kappaScale = kappaScale

    def evaluate(self, location, buffer):
        """evaluate

        param UnwritableVectorIJK location
        param VectorIJK buffer
        return VectorIJK
        """

        # perform spatial scaling, eq. (25)
        scaledLocation = location*self.kappaScale
        self.unscaledField.evaluate(scaledLocation, buffer)

        # Apply the kappa scaling factor eq. (25)
        buffer *= self.kappaScale
        return buffer
