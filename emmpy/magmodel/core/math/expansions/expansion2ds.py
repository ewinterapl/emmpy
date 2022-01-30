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
    def createFromArray(data, firstAzimuthalExpansionNumber,
                        firstRadialExpansionNumber):
        """Create an expansion from a 2-D array.
        
        Create an expansion from a 2-D array.
        
        Parameters
        ----------
        data : 2-D list of VectorIJK
            Values to use for expansion.
        firstAzimuthalExpansionNumber : int
            First expansion index in 1st dimension.
        firstRadialExpansionNumber : int
            First expansion index in 2nd dimension.
        
        Returns
        -------
        result : ArrayExpansion2D
            Expansion for the specified inputs.
        """
        return ArrayExpansion2D(
            data, firstAzimuthalExpansionNumber, firstRadialExpansionNumber
        )

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
            firstAzimuthalExpansion = a.firstAzimuthalExpansionNumber
            lastAzimuthalExpansion = a.lastAzimuthalExpansionNumber
            firstRadialExpansion = a.firstRadialExpansionNumber
            lastRadialExpansion = a.lastRadialExpansionNumber
            array = nones(
                (lastAzimuthalExpansion - firstAzimuthalExpansion + 1,
                 lastRadialExpansion - firstRadialExpansion + 1))
            e2d = Expansion2D()
            e2d.firstAzimuthalExpansionNumber = firstAzimuthalExpansion
            e2d.lastAzimuthalExpansionNumber = lastAzimuthalExpansion
            e2d.firstRadialExpansionNumber = firstRadialExpansion
            e2d.lastRadialExpansionNumber = lastRadialExpansion

            def my_getExpansion(azimuthalExpansion, radialExpansion):
                value = (
                    array[azimuthalExpansion - firstAzimuthalExpansion]
                         [radialExpansion - firstRadialExpansion]
                )
                if value is None:
                    value = (
                        a.getExpansion(azimuthalExpansion, radialExpansion) +
                        b.getExpansion(azimuthalExpansion, radialExpansion))
                    array[azimuthalExpansion - firstAzimuthalExpansion][radialExpansion - firstRadialExpansion] = value
                    return value
                return value
            e2d.getExpansion = my_getExpansion
            return e2d
