"""Base class for vector field values.

A vector field value contains a position in the vector field, and a value
for the vector field.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.coords.vectorfieldvalue import VectorFieldValue


class AbstractVectorFieldValue(VectorFieldValue):
    """Base class for vector field values.

    Attributes
    ----------
    position : Vector
        Position in the vector field.
    value : Vector
        Value of the vector field at the position.
    """

    def __init__(self, position, value):
        """Initialize a new AbstractVectorFieldValue object.

        Initialize a new AbstractVectorFieldValue object.

        Parameters
        ----------
        position : Vector
            Position in the vector field.
        value : Vector
            Value of the vector field at the position.
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
        position : Vector
            Position in the vector field.
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
        value : Vector
            Value of the vector field.
        """
        return self.value
