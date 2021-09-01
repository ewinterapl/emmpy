"""Vector field in a 3-D spherical space.

A spherical vector field value contains a position in the vector field,
and a value for the vector field, both in spherical coordinates.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.abstractvectorfieldvalue import (
    AbstractVectorFieldValue
)


class SphericalVectorFieldValue(AbstractVectorFieldValue):
    """Vector field in a 3-D spherical space.

    A spherical vector field value contains a position in the vector field,
    and a value for the vector field, both in spherical coordinates.
    """

    def __init__(self, position, value):
        """Initialize a new SphericalVectorFieldValue object.

        Initialize a new SphericalVectorFieldValue object.

        Parameters
        ----------
        position : SpheicalVector
            Position in the vector field.
        value : SphericalVector
            Value of the vector field at the position.
        """
        AbstractVectorFieldValue.__init__(self, position, value)
