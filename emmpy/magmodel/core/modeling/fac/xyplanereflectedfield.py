"""emmpy.magmodel.core.modeling.fac.xyplanereflectedfield"""


# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class XYPlaneReflectedField(VectorField):
    """The reflection of the input field about the X-Y plane.

    From T02: "The contribution from the southern currents (symmetric to the
    northern ones for TILT = 0) can be readily represented by rotating the
    northern (N) part by 180deg around the X-axis and changing the polarity
    of the current."

    author G.K.Stephens
    """

    def __init__(self, delgate):
        """Constructor

        param VectorField delgate
        """
        # VectorField delgate
        self.delgate = delgate

    def evaluate(self, location, buffer):
        """evaluate

        param UnwritableVectorIJK location
        param VectorIJK buffer
        return VectorIJK
        """
        # UnwritableVectorIJK reflectedLocation
        reflectedLocation = UnwritableVectorIJK(
            location.getI(), location.getJ(), -location.getK()
        )
        delgate.evaluate(reflectedLocation, buffer)
        # double bz
        bz = buffer.getK()
        buffer.setK(-bz)
        return buffer