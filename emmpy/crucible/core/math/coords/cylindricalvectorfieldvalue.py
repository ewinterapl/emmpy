"""Vector field in a 3-D cylindrical space.

A cylindrical vector field value contains a position in the vector field,
and a value for the vector field, both in cylindrical coordinates.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from .vectorfieldvalue import VectorFieldValue

class CylindricalVectorFieldValue(VectorFieldValue):
    """Vector field in a 3-D Cartesian space.

    A cylindrical vector field value contains a position in the vector
    field, and a value for the vector field, both in cylindrical
    coordinates.
    """
