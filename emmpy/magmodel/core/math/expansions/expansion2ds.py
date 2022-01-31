"""Utility methods for 2-D expansions.

Utility methods for 2-D expansions.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.arrayexpansion2d import (
    ArrayExpansion2D
)
from emmpy.magmodel.core.math.expansions.expansion2d import Expansion2D
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.utilities.nones import nones


class Expansion2Ds:
    """Utility methods for 2-D expansions.

    Utility methods for 2-D expansions.
    """

    @staticmethod
    def createFromArray(data):
        """Create an expansion from a 2-D array.
        
        Create an expansion from a 2-D array.
        
        Parameters
        ----------
        data : 2-D list of VectorIJK
            Values to use for expansion.
        
        Returns
        -------
        result : ArrayExpansion2D
            Expansion for the specified inputs.
        """
        return ArrayExpansion2D(data)

    class Vectors:
        """Internal helper class."""
