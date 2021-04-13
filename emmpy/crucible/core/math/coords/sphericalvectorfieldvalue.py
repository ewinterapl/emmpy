"""emmpy.crucible.core.math.coords.sphericalvectorfieldvalue

A container class for a spherical coordinate and vector field value at that
coordinate.

@author G.K.Stephens
"""


from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)


class SphericalVectorFieldValue(AbstractVectorFieldValue):
    """SphericalVectorFieldValue"""

    def __init__(self, position, value):
        """Constructor

        @param position a spherical coordinate
        @param value a spherical vector field value at coordinate
        """
        AbstractVectorFieldValue.__init__(self, position, value)
