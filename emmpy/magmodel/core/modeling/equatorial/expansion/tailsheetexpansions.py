"""Expansions for a thin current sheet."""


from emmpy.crucible.core.math.vectorspace.vectorijk import VectorIJK
# from emmpy.magmodel.core.math.expansions.expansion1ds import Expansion1Ds
# from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds


class TailSheetExpansions:
    """Expansions for a thin current sheet.

    A container for the Basis functions expansion of a thin current sheet,
    i.e. it represents the individual basis functions in the following
    summation:

    author G.K.Stephens
    """

    def __init__(self, tailSheetSymmetricValues, tailSheetOddValues,
                 tailSheetEvenValues):
        """Build a new object."""
        self.tailSheetSymmetricValues = tailSheetSymmetricValues
        self.tailSheetOddValues = tailSheetOddValues
        self.tailSheetEvenValues = tailSheetEvenValues
        self.numAzimuthalExpansions = tailSheetOddValues.iSize()
        self.numRadialExpansions = tailSheetOddValues.jSize()

    def getTailSheetSymmetricValues(self):
        """Return the symmetric expansion values."""
        return self.tailSheetSymmetricValues

    def getTailSheetOddValues(self):
        """Return the odd expansion values."""
        return self.tailSheetOddValues

    def getTailSheetEvenValues(self):
        """Return the even expansion values."""
        return self.tailSheetEvenValues

    # def getAsTailSheetExpansions(
    #     self, expansion, numAzimuthalExpansions, numRadialExpansions
    # ):
    #     """Converts an ImmutableList of UnwritableVectorIJK representing the
    #     results of a BasisVectorField into a TailSheetExpansions

    #     @param expansion
    #     @param numAzimuthalExpansions
    #     @param numRadialExpansions
    #     @return
    #     """
    #     symmetricExpansions = [
    #         UnwritableVectorIJK([0, 0, 0]) for i in range(numRadialExpansions)
    #     ]
    #     oddExpansions = [
    #         [UnwritableVectorIJK([0, 0, 0])
    #          for j in range(numRadialExpansions)]
    #         for i in range(numAzimuthalExpansions)
    #     ]
    #     evenExpansions = [
    #         [UnwritableVectorIJK([0, 0, 0])
    #          for j in range(numRadialExpansions)]
    #         for i in range(numAzimuthalExpansions)
    #     ]

    #     count = 0

    #     # n is the radial expansion number
    #     for n in range(1, numRadialExpansions + 1):
    #         symmetricExpansions[n - 1] = expansion.get(count)
    #         count += 1

    #     for n in range(1, numRadialExpansions + 1):
    #         for m in range(1, numAzimuthalExpansions + 1):
    #             oddExpansions[m - 1][n - 1] = expansion.get(count)
    #             count += 1

    #     # n is the radial expansion number
    #     # m is the azimuthal expansion number
    #     for n in range(1, numRadialExpansions + 1):
    #         for m in range(1, numAzimuthalExpansions + 1):
    #             evenExpansions[m - 1][n - 1] = expansion.get(count)
    #             count += 1

    #     return TailSheetExpansions(
    #         Expansion1Ds.createFromArray(symmetricExpansions, 1),
    #         Expansion2Ds.createFromArray(oddExpansions, 1, 1),
    #         Expansion2Ds.createFromArray(evenExpansions, 1, 1)
    #     )

    def getExpansionsAsList(self):
        """Return the basis functions in a list."""
        basisFunctions = []

        # n is the radial expansion number
        for n in range(1, self.numRadialExpansions + 1):
            basisFunctions.append(
                self.tailSheetSymmetricValues.getExpansion(n)
            )

        # n is the radial expansion number
        # m is the azimuthal expansion number
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunctions.append(
                    self.tailSheetOddValues.getExpansion(m, n)
                )

        # n is the radial expansion number
        # m is the azimuthal expansion number
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunctions.append(
                    self.tailSheetEvenValues.getExpansion(m, n)
                )

        return basisFunctions

    def sum(self):
        """Compute the sum of the expansion."""
        bxSum = 0.0
        bySum = 0.0
        bzSum = 0.0

        # n is the radial expansion number
        for n in range(1, self.numRadialExpansions + 1):
            basisFunction = self.tailSheetSymmetricValues.getExpansion(n)
            bxSum += basisFunction.i
            bySum += basisFunction.j
            bzSum += basisFunction.k

        # n is the radial expansion number
        # m is the azimuthal expansion number
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunction = self.tailSheetOddValues.getExpansion(m, n)
                bxSum += basisFunction.i
                bySum += basisFunction.j
                bzSum += basisFunction.k

        # n is the radial expansion number
        # m is the azimuthal expansion number
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunction = self.tailSheetEvenValues.getExpansion(m, n)
                bxSum += basisFunction.i
                bySum += basisFunction.j
                bzSum += basisFunction.k

        return VectorIJK(bxSum, bySum, bzSum)
