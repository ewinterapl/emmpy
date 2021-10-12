"""Utility functions for 1-D expansions.

Utility functions for 1-D expansions.

Authors
-------
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.magmodel.core.math.expansions.arrayexpansion1d import (
    ArrayExpansion1D
)
from emmpy.magmodel.core.math.expansions.coefficientexpansion1d import (
    CoefficientExpansion1D
)
from emmpy.magmodel.core.math.expansions.expansion1d import Expansion1D
from emmpy.magmodel.core.math.expansions.listexpansion1d import ListExpansion1D
from emmpy.math.coordinates.vectorijk import VectorIJK
from emmpy.utilities.nones import nones


class Expansion1Ds:
    """Utility functions for 1-D expansions.
    
    Utility functions for 1-D expansions.
    """

    @staticmethod
    def createFromList(aList, firstRadialExpansionNumber):
        """Create an expansion from a list.

        Create an expansion from a list.

        Parameters
        ----------
        aList : list of float
            List of values for expansion.
        firstRadialExpansionNumber : int
            Index of first expansion.
        
        Returns
        -------
        result : ListExpansion1D
            New expansion object.
        """
        return ListExpansion1D(list, firstRadialExpansionNumber)

    @staticmethod
    def createFromArray(array, firstRadialExpansionNumber):
        """Create an expansion from an array.

        Create an expansion from an array.

        Parameters
        ----------
        array : list of float
            List of values for expansion.
        firstRadialExpansionNumber : int
            Index of first expansion.
        
        Returns
        -------
        result : ArrayExpansion1D
            New expansion object.
        """
        return ArrayExpansion1D(array, firstRadialExpansionNumber)

    class Vectors:
        """Internal class for vectors.

        Internal class for vectors.
        """

        @staticmethod
        def createConstant(firstRadialExpansionNumber, lastRadialExpansionNumber,
                           constant):
            """Create an array of constant vectors.

            Parameters
            ----------
            firstRadialExpansionNumber : int
                Lowest index of expansion.
            lastRadialExpansionNumber : int
                Highest index of expansion.
            constant : VectorIJK
                Constant vector to use for expansion.

            Returns
            -------
            e1d : Expansion1D
                New expansion object.
            """
            constantCopy = VectorIJK.copyOf(constant)

            # Create a custom wrapper object for this expansion.
            e1d = Expansion1D()
            e1d.getUpperBoundIndex = lambda: lastRadialExpansionNumber
            e1d.getLowerBoundIndex = lambda: firstRadialExpansionNumber
            e1d.getExpansion = lambda radialExpansion: constantCopy
            return e1d

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
            e1d : Expansion1D
                Wrapper object for expansion sum.
            """
            firstExpansion = a.firstRadialExpansionNumber
            lastExpansion = a.lastRadialExpansionNumber
            array = nones((lastExpansion - firstExpansion + 1,))
            e1d = Expansion1D()
            e1d.getLowerBoundIndex = lambda: firstExpansion
            e1d.getUpperBoundIndex = lambda: lastExpansion

            def my_getExpansion(radialExpansion):
                value = array[radialExpansion - firstExpansion]
                if value is None:
                    value = (a.getExpansion(radialExpansion) +
                             b.getExpansion(radialExpansion))
                    array[radialExpansion - firstExpansion] = value
                    return value
                return value
            e1d.getExpansion = my_getExpansion
            return e1d
