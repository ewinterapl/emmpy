"""emmpy.magmodel.core.modeling.equatorial.expansion.tailsheetexpansions"""


from emmpy.crucible.core.math.vectorspace.unwritablevectorijk import (
    UnwritableVectorIJK
)
# from emmpy.magmodel.core.math.expansions.expansion1ds import Expansion1Ds
# from emmpy.magmodel.core.math.expansions.expansion2ds import Expansion2Ds


class TailSheetExpansions:
    """A container for the Basis functions expansion of a thin current sheet,
    i.e. it represents the individual basis functions in the following
    summation:

    author G.K.Stephens
    """

    def __init__(self, tailSheetSymmetricValues, tailSheetOddValues,
                 tailSheetEvenValues):
        self.tailSheetSymmetricValues = tailSheetSymmetricValues
        self.tailSheetOddValues = tailSheetOddValues
        self.tailSheetEvenValues = tailSheetEvenValues
        self.numAzimuthalExpansions = tailSheetOddValues.iSize()
        self.numRadialExpansions = tailSheetOddValues.jSize()

    def getTailSheetSymmetricValues(self):
        return self.tailSheetSymmetricValues

    def getTailSheetOddValues(self):
        return self.tailSheetOddValues

    def getTailSheetEvenValues(self):
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
        bxSum = 0.0
        bySum = 0.0
        bzSum = 0.0

        # n is the radial expansion number
        for n in range(1, self.numRadialExpansions + 1):
            basisFunction = self.tailSheetSymmetricValues.getExpansion(n)
            bxSum += basisFunction.getI()
            bySum += basisFunction.getJ()
            bzSum += basisFunction.getK()

        # n is the radial expansion number
        # m is the azimuthal expansion number
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunction = self.tailSheetOddValues.getExpansion(m, n)
                bxSum += basisFunction.getI()
                bySum += basisFunction.getJ()
                bzSum += basisFunction.getK()

        # n is the radial expansion number
        # m is the azimuthal expansion number
        for n in range(1, self.numRadialExpansions + 1):
            for m in range(1, self.numAzimuthalExpansions + 1):
                basisFunction = self.tailSheetEvenValues.getExpansion(m, n)
                bxSum += basisFunction.getI()
                bySum += basisFunction.getJ()
                bzSum += basisFunction.getK()

        return UnwritableVectorIJK(bxSum, bySum, bzSum)
