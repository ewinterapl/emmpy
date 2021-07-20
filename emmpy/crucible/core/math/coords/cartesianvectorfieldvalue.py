"""Class to represent a Cartesian vector field value."""


from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)
from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


class CartesianVectorFieldValue(AbstractVectorFieldValue):
    """A Cartesian coordinate and vector field value at that coordinate.

    author G.K.Stephens
    """

    def __init__(self, position, value):
        """Build a new object.

        @param position a Cartesian coordinate
        @param value a Cartesian vector field value at that coordinate
        """
        AbstractVectorFieldValue.__init__(
            self, VectorIJK.copyOf(position), VectorIJK.copyOf(value)
        )
