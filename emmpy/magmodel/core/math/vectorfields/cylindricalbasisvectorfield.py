"""A basis vector field in cylindrical coordinates.

A basis vector field in cylindrical coordinates.

This class is derived from a Java interface, and thus most of the methods
raise an exception when invoked.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.exceptions.abstractmethodexception import AbstractMethodException


class CylindricalBasisVectorField:
    """A basis vector field in cylindrical coordinates.

    Represents a VectorField in cylindrical coordinates and provides the
    conversion from a CylindricalVector field to a Cartesian vector field.
    """
