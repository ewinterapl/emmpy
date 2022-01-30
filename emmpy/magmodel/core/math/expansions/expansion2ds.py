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
            e2d : Expansion2D
                Wrapper object for expansion sum.
            """
            lastAzimuthalExpansion = a.lastAzimuthalExpansionNumber
            lastRadialExpansion = a.lastRadialExpansionNumber
            array = nones((lastAzimuthalExpansion + 1, lastRadialExpansion + 1))
            e2d = Expansion2D()
            e2d.lastAzimuthalExpansionNumber = lastAzimuthalExpansion
            e2d.lastRadialExpansionNumber = lastRadialExpansion

            def my_getExpansion(azimuthalExpansion, radialExpansion):
                value = array[azimuthalExpansion][radialExpansion]
                if value is None:
                    value = (
                        a.getExpansion(azimuthalExpansion, radialExpansion) +
                        b.getExpansion(azimuthalExpansion, radialExpansion))
                    array[azimuthalExpansion][radialExpansion] = value
                    return value
                return value
            e2d.getExpansion = my_getExpansion
            return e2d
