"""Vector field in a 3-D spherical space.

A spherical vector field value contains a position in the vector field,
and a value for the vector field, both in spherical coordinates.

Authors
-------
Grant Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from .vectorfieldvalue import VectorFieldValue


class SphericalVectorFieldValue(VectorFieldValue):
    """Vector field in a 3-D spherical space.

    A spherical vector field value contains a position in the vector field,
    and a value for the vector field, both in spherical coordinates.
    """
