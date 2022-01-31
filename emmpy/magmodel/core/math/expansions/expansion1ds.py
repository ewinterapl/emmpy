"""Utility functions for 1-D expansions.

Utility functions for 1-D expansions.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.arrayexpansion1d import (
    ArrayExpansion1D
)
from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D
from emmpy.math.coordinates.cartesianvector import CartesianVector
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.utilities.nones import nones


class Expansion1Ds:
    """Utility functions for 1-D expansions.
    
    Utility functions for 1-D expansions.
    """

    @staticmethod
    def createFromArray(array):
        """Create an expansion from an array.

        Create an expansion from an array.

        Parameters
        ----------
        array : list of float
            List of values for expansion.
        
        Returns
        -------
        result : ArrayExpansion1D
            New expansion object.
        """
        return ArrayExpansion1D(array)

    class Vectors:
        """Internal class for vectors.

        Internal class for vectors.
        """

        @staticmethod
        def add(a, b):
            """Add 2 1-D expansions.

            Add 2 1-D expansions.

            Parameters
            ----------
            a, b : Expansion1D
                Expansions to add.

            Returns
            -------
            ae1d : ArrayExpansion1D
                An expansion that is the sum of a and b.
            """
            array = []
            for i in range(len(a.array)):
                array.append(CartesianVector(a.array[i] + b.array[i]))
            ae1d = ArrayExpansion1D(array)

            return ae1d
