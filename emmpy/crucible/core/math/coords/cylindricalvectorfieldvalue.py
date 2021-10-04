"""Vector field in a 3-D cylindrical space.

A cylindrical vector field value contains a position in the vector field,
and a value for the vector field, both in cylindrical coordinates.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)


class CylindricalVectorFieldValue(AbstractVectorFieldValue):
    """Vector field in a 3-D Cartesian space.

    A cylindrical vector field value contains a position in the vector
    field, and a value for the vector field, both in cylindrical
    coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self, position, value):
        """Initialize a new CylindricalVectorFieldValue object.

        Initialize a new CylindricalVectorFieldValue object.

        Parameters
        ----------
        position : CylindricalVector
            Position in the vector field.
        value : CylindricalVector
            Value of the vector field at the position.
        """
        AbstractVectorFieldValue.__init__(self, position, value)
