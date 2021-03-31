"""emmpy.crucible.core.math.coords.cartesianvectorfieldvalue"""

# import crucible.core.math.vectorspace.UnwritableVectorIJK;

from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)
from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)


class CartesianVectorFieldValue(AbstractVectorFieldValue):
    """A container class for a Cartesian coordinate and vector field value at
    that coordinate.

    @author G.K.Stephens
    """

    def __init__(self, position, value):
        """Constructor

        @param position a Cartesian coordinate
        @param value a Cartesian vector field value at that coordinate
        """
        AbstractVectorFieldValue.__init__(
            self, UnwritableVectorIJK.copyOf(position),
            UnwritableVectorIJK.copyOf(value)
        )
