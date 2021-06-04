"""Spherical coordinate and vector field value at that coordinate.

@author G.K.Stephens
"""


from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)


class SphericalVectorFieldValue(AbstractVectorFieldValue):
    """Spherical coordinate and vector field value at that coordinate."""

    def __init__(self, position, value):
        """Build a new object.

        @param position a spherical coordinate
        @param value a spherical vector field value at coordinate
        """
        AbstractVectorFieldValue.__init__(self, position, value)
