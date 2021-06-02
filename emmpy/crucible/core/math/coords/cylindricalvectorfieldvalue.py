"""emmpy.crucible.core.math.coords.cylindricalvectorfieldvalue"""


from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)


class CylindricalVectorFieldValue(AbstractVectorFieldValue):
    """A container class for a cylindrical coordinate and vector field value

    @author G.K.Stephens
    """

    def __init__(self, position, value):
        """Constructor

        @param position a cylindrical coordinate
        @param value a cylindrical vector field value at that coordinate
        """
        AbstractVectorFieldValue.__init__(self, position, value)
