"""A container class for a cylindrical coordinate and vector field value."""


from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)


class CylindricalVectorFieldValue(AbstractVectorFieldValue):
    """A container class for a cylindrical coordinate and vector field value.

    @author G.K.Stephens
    """

    def __init__(self, position, value):
        """Build a new object.

        @param position a cylindrical coordinate
        @param value a cylindrical vector field value at that coordinate
        """
        AbstractVectorFieldValue.__init__(self, position, value)
