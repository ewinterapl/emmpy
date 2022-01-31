"""Expansions for a thin current sheet.

Expansions for a thin current sheet.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.math.coordinates.vectorijk import VectorIJK


class TailSheetExpansions:
    """Expansions for a thin current sheet.

    A container for the Basis functions expansion of a thin current sheet,
    i.e. it represents the individual basis functions.

    Attributes
    ----------
    tailSheetSymmetricValues : Expansion1D
        tailSheetSymmetricValues
    tailSheetOddValues : Expansion2D
        tailSheetOddValues
    tailSheetEvenValues : Expansion2D
        tailSheetEvenValues
    numAzimuthalExpansions : int
        Number of azimuthal expansions.
    numRadialExpansions : int
        Number of radial expansions.
    """

    def __init__(self, tailSheetSymmetricValues, tailSheetOddValues,
                 tailSheetEvenValues):
        """Initialize a new TailSheetExpansions object.

        Initialize a new TailSheetExpansions object.

        Parameters
        ----------
        tailSheetSymmetricValues : Expansion1D
            tailSheetSymmetricValues
        tailSheetOddValues : Expansion2D
            tailSheetOddValues
        tailSheetEvenValues : Expansion2D
            tailSheetEvenValues
        """
        self.tailSheetSymmetricValues = tailSheetSymmetricValues
        self.tailSheetOddValues = tailSheetOddValues
        self.tailSheetEvenValues = tailSheetEvenValues
        self.numAzimuthalExpansions = len(tailSheetOddValues)
        self.numRadialExpansions = len(tailSheetOddValues[0])

    def getExpansionsAsList(self):
        """Return the basis functions in a list.

        Return the basis functions in a list.

        Parameters
        ----------
        None

        Returns
        -------
        basisFunctions : list of function
            List of basis functions for expansion.
        """
        basisFunctions = []

        # n is the radial expansion number.
        for n in range(self.numRadialExpansions):
            basisFunctions.append(
                self.tailSheetSymmetricValues[n]
            )

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(self.numRadialExpansions):
            for m in range(self.numAzimuthalExpansions):
                basisFunctions.append(self.tailSheetOddValues[m][n])

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(self.numRadialExpansions):
            for m in range(self.numAzimuthalExpansions):
                basisFunctions.append(self.tailSheetEvenValues[m][n])

        return basisFunctions

    def sum(self):
        """Compute the sum of the expansion.
        
        Compute the sum of the expansion.

        Parameters
        ----------
        None

        Returns
        -------
        result : VectorIJK
            Vector sum of expansion.
        """
        bxSum = 0.0
        bySum = 0.0
        bzSum = 0.0

        # n is the radial expansion number.
        for n in range(self.numRadialExpansions):
            basisFunction = self.tailSheetSymmetricValues[n]
            bxSum += basisFunction.x
            bySum += basisFunction.y
            bzSum += basisFunction.z

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(self.numRadialExpansions):
            for m in range(self.numAzimuthalExpansions):
                basisFunction = self.tailSheetOddValues[m][n]
                bxSum += basisFunction.i
                bySum += basisFunction.j
                bzSum += basisFunction.k

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(self.numRadialExpansions):
            for m in range(self.numAzimuthalExpansions):
                basisFunction = self.tailSheetEvenValues[m][n]
                bxSum += basisFunction.i
                bySum += basisFunction.j
                bzSum += basisFunction.k

        return VectorIJK(bxSum, bySum, bzSum)
