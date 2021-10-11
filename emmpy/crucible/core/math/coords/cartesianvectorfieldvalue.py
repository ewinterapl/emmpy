"""Vector field in a 3-D Cartesian space.

A Cartesian vector field value contains a position in the vector field,
and a value for the vector field, both in Cartesian coordinates.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


class CartesianVectorFieldValue:
    """Vector field in a 3-D Cartesian space.

    A Cartesian vector field value contains a position in the vector
    field, and a value for the vector field, both in Cartesian
    coordinates.

    Attributes
    ----------
    None
    """

    def __init__(self, position, value):
        """Initialize a new CartesianVectorFieldValue object.

        Initialize a new CartesianVectorFieldValue object.

        Parameters
        ----------
        position : VectorIJK
            Position in the vector field.
        value : VectorIJK
            Value of the vector field at the position.
        """
        self.position = position
        self.value = value
