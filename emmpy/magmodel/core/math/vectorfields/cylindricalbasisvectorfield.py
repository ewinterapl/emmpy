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
from emmpy.magmodel.core.math.vectorfields.cylindricalvectorfield import (
    CylindricalVectorField
)


class CylindricalBasisVectorField(CylindricalVectorField):
    """A basis vector field in cylindrical coordinates.

    Represents a VectorField in cylindrical coordinates and provides the
    conversion from a CylindricalVector field to a Cartesian vector field.
    """

    def __init__(self):
        """Initialize a new CylindricalBasisVectorField object.

        Initialize a new CylindricalBasisVectorField object.

        Parameters
        ----------
        None
        """

    def evaluateExpansion(self, location):
        """Evaluate the expansion.

        Evaluate the field expansion at the given position, and returns an
        ImmutableList results of each individual field in the expansion
        in cylindrical coordinates

        Parameters
        ----------
        location : CylindricalVector
            Cylindrical location for field evaluation.

        Returns
        -------
        result : Expansion
            Expansion evaluated at the location.

        Raises
        ------
        AbstractMethodException
            When invoked.
        """
        raise AbstractMethodException
