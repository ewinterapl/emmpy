"""A vector field in cylindrical coordinates.

A vector field in cylindrical coordinates.

N.B. This class was created from a Java interface, and therefore most of
these methods will raise exceptions if invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class CylindricalVectorField(VectorField):
    """A vector field in cylindrical coordinates.

    Represents a VectorField in cylindrical coordinates and provides the
    conversion from a CylindricalVector field to a Cartesian vector
    field.
    """
