"""Base class for vector field values.

This class represents a generic vector field value in an arbitrary
coordinate system.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class VectorFieldValue:
    """Base class for vector field values.

    This class represents a generic vector field value in an arbitrary
    coordinate system. A vector field value is defined as a position
    vector and a value vector.

    The position and value are assumed to have the same dimensionality.

    Attributes
    ----------
    position : Vector
        Position in the vector field, coordinate system undefined.
    value : Vector
        Value of the vector field at the position, coordinate system
        undefined. Assumed to have the same dimensionality as position.
    """

    def __init__(self, position, value):
        """Initialize a new VectorFieldValue object.

        Initialize a new VectorFieldValue object.

        Parameters
        ----------
        position : Vector
            Position in the vector field, coordinate system undefined.
        value : Vector
            Value of the vector field at the position, coordinate system
            undefined.
        """
        self.position = position
        self.value = value
