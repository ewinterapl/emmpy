"""Reflect a field about the XY plane."""


# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class XYPlaneReflectedField(VectorField):
    """Reflect a field about the XY plane.

    From T02: "The contribution from the southern currents (symmetric to the
    northern ones for TILT = 0) can be readily represented by rotating the
    northern (N) part by 180deg around the X-axis and changing the polarity
    of the current."

    author G.K.Stephens
    """

    def __init__(self, delgate):
        """Build a new object.

        param VectorField delgate
        """
        # VectorField delgate
        self.delgate = delgate

    def evaluate(self, location, buffer):
        """Evaluate the field.

        param UnwritableVectorIJK location
        param VectorIJK buffer
        return VectorIJK
        """
        # UnwritableVectorIJK reflectedLocation
        reflectedLocation = VectorIJK(
            location.i, location.j, -location.k
        )
        self.delgate.evaluate(reflectedLocation, buffer)
        # double bz
        bz = buffer.k
        buffer.k = -bz
        return buffer
