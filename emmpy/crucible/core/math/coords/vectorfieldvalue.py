"""Base class for vector field values.

This class represents a generic vector field in an arbitrary coordinate
system.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class VectorFieldValue:
    """Base class for vector field values.

    This class represents a generic vector field in an arbitrary
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

    def getPosition(self):
        """Return the position in the vector field.

        Return the position in the vector field.

        Parameters
        ----------
        None

        Returns
        -------
        self.position : Vector
            Position in the vector field, coordinate system undefined.
        """
        return self.position

    def getValue(self):
        """Return the value of the vector field.

        Return the value of the vector field.

        Parameters
        ----------
        None

        Returns
        -------
        self.value : Vector
            Value of the vector field, coordinate system undefined.
        """
        return self.value
