"""Expansions for a thin current sheet.

Expansions for a thin current sheet.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK


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
        self.numAzimuthalExpansions = tailSheetOddValues.iSize()
        self.numRadialExpansions = tailSheetOddValues.jSize()

    def getTailSheetSymmetricValues(self):
        """Return the symmetric expansion values.

        Return the symmetric expansion values.

        Parameters
        ----------
        None

        Returns
        -------
        result : Expansion1D
            tailSheetSymmetricValues
        """
        return self.tailSheetSymmetricValues

    def getTailSheetOddValues(self):
        """Return the odd expansion values.
        
        Return the odd expansion values.

        Parameters
        ----------
        None

        Returns
        -------
        result : Expansion2D
            tailSheetOddValues
        """
        return self.tailSheetOddValues

    def getTailSheetEvenValues(self):
        """Return the even expansion values.
        
        Return the even expansion values.

        Parameters
        ----------
        None

        Returns
        -------
        result : Expansion2D
            tailSheeEvenValues
        """
        return self.tailSheetEvenValues

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
        for n in range(1, self.numRadialExpansions + 1):
            basisFunctions.append(
                self.tailSheetSymmetricValues.getExpansion(n)
            )

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunctions.append(
                    self.tailSheetOddValues.getExpansion(m, n)
                )

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunctions.append(
                    self.tailSheetEvenValues.getExpansion(m, n)
                )

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
        for n in range(1, self.numRadialExpansions + 1):
            basisFunction = self.tailSheetSymmetricValues.getExpansion(n)
            bxSum += basisFunction.i
            bySum += basisFunction.j
            bzSum += basisFunction.k

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunction = self.tailSheetOddValues.getExpansion(m, n)
                bxSum += basisFunction.i
                bySum += basisFunction.j
                bzSum += basisFunction.k

        # n is the radial expansion number.
        # m is the azimuthal expansion number.
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunction = self.tailSheetEvenValues.getExpansion(m, n)
                bxSum += basisFunction.i
                bySum += basisFunction.j
                bzSum += basisFunction.k

        return VectorIJK(bxSum, bySum, bzSum)
