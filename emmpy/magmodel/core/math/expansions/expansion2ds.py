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

        @staticmethod
        def add(a, b):
            """Add two expansions using a wrapper object.

            Add two expansions using a wrapper object.

            Parameters
            ----------
            a, b : Expansion2D
                Expansions to add.

            Returns
            -------
            ae2d : ArrayExpansion2D
                Object for expansion sum.
            """
            numAzimuthalExpansions = len(a.data)
            numRadialExpansions = len(a.data[0])
            array = nones((numAzimuthalExpansions, numRadialExpansions))
            for i in range(numAzimuthalExpansions):
                for j in range(numRadialExpansions):
                    array[i][j] = CartesianVector(
                        a.data[i][j] + b.data[i][j]
                    )
            ae2d = ArrayExpansion2D(array)

            return ae2d
