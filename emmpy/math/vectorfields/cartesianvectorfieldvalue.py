"""Vector field in a 3-D Cartesian space.

A Cartesian vector field value contains a position in the vector field,
and a value for the vector field, both in Cartesian coordinates.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from .vectorfieldvalue import VectorFieldValue


class CartesianVectorFieldValue(VectorFieldValue):
    """Vector field in a 3-D Cartesian space.

    A Cartesian vector field value contains a position in the vector
    field, and a value for the vector field, both in Cartesian
    coordinates.
    """
